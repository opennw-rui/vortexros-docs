# L2 子接口

L2 子接口按 VLAN 标签识别报文，加入 bridge-domain 后转发。它自身不配置 IP，三层网关地址位于该桥域 Vbdif。

## 创建与约束

使用 `interface PARENT.NUMBER mode l2` 创建，`encapsulation dot1q vid VLAN` 指定单标签。子接口编号只表示实例身份，和分类使用的外层 VID、bridge-domain 编号相互独立；父端口必须存在。

显式子接口的实际外层 VID 与全局 `vlan` 对象互斥，适用于 dot1q、dot1ad、QinQ，配置顺序不影响结果。只相同的实例后缀、桥域编号或内层 VID 不构成冲突。不同父接口可复用相同外层 VID，同一父接口的匹配集合不可重叠。系统为 Access、Trunk、Hybrid 派生的内部对象不属于显式子接口，不受这个全局互斥规则限制。

全局 VLAN 通过 `l2 binding vlan` 接入桥域，显式 L2 子接口通过 `bridge-domain` 接入桥域，两种接入可以在同一桥域共存。两者的外层 VID 仍须满足上述互斥规则。

创建后补齐封装并绑定桥域；不能在已有接口上通过重复进入时改写 mode 完成二三层转换。应先解除业务引用、删除接口，再创建目标模式。

## 固定外层、多个内层的 QinQ

固定外层标签下，可以指定一个、多个、一段或任意内层 VID。两端的封装匹配和标签处理必须配套；通过 VXLAN 承载时，还需核对隧道内保留的客户标签，参见[VXLAN 载荷](vxlan.md#qinq-业务的-vxlan-载荷)。

~~~text
interface Ethernet1.17 mode l2
 encapsulation qinq vid 200 ce-vid 10 12 to 15
 rewrite pop single
 bridge-domain 310
~~~

`ce-vid` 可取一个 VID、空格分隔的 VID 列表、`to` 范围，或 `any`。集合会排序、去重并整体替换原集合，不会累加旧配置。多个内层 VID 限 1–4094；旧单值语法保留既有 VID 边界。`qinq` 形式使用外层 TPID 0x8100；`encapsulation dot1ad vid 200 ce-vid ...` 使用 0x88a8。`any` 是 VortexROS 扩展，直接复用原生任意内层分类能力，不展开成数千个子接口。

多内层集合和 `any` 仅支持 L2 子接口。它们必须在提交前明确选择 `rewrite pop single` 或 `rewrite pop none`，否则提交失败；`rewrite pop double` 会被拒绝，因为一个出口固定重写不能恢复多种原始内层 VID。Candidate 允许先编辑封装、随后补齐重写选择。

### 标签处理

| 重写配置 | 入方向处理 | 出方向处理 |
| --- | --- | --- |
| `rewrite pop single` | 移除外层标签，保留原内层标签 | 恢复该子接口固定外层标签 |
| `rewrite pop double` | 移除固定的两个标签，仅适用单内层 VID | 恢复固定外层和内层标签 |
| `rewrite pop none` | 保留标签 | 保留标签 |
| `undo rewrite pop` | 恢复原有默认：单标签 pop1，固定双标签 pop2 | 对应默认的对称恢复 |

`none` 是 VortexROS 扩展。撤销重写不是“保留标签”；多内层或 `any` 撤销后必须重新选择可实现的重写动作才能提交。单值 QinQ 未显式配置重写时仍保留原有 pop2 行为。

`display interface Ethernet1.17` 从数据面读取实际完整内层集合、TPID 和实际重写动作，不只显示集合首值。列表或范围共用一个业务子接口，查询结果应显示完整匹配集合。

`pop single` 保留经过桥接的原始内层客户标签。多内层匹配接口不能作为多个客户 VLAN 共用的 Vbdif 网关接入：本机生成的 ARP 等回应无法按请求自动恢复不同内层标签，可能只携带固定外层标签。需要三层网关时，应将业务拆分为固定双标签子接口和对应的独立桥域。

QinQ 按前两层标签分类，不能将其作为拒绝第三层标签的严格层数过滤器。

修改封装导致子接口重建时，相应动态 MAC 需要重新学习。桥域关闭未知单播洪泛后，目的 MAC 尚未学习的报文会被丢弃；需要允许学习期间的未知单播转发时，在桥域视图配置 `uu-flood`。此项会扩大未知单播的发送范围，应按业务要求选择。

## 激活条件

父接口与子接口均未 shutdown、父接口链路 Up 时，子接口才有可用链路。Protocol Up 还要求封装完整并已加入正确的桥域。L2 子接口不配置 IP，也不以 IP 地址作为 Up 条件。父链路恢复后自动恢复；显式 shutdown 的子接口需执行 undo shutdown。

## 配置、示例输出和撤销

[完整双端案例](../examples/subinterfaces/l2.md)包含 P1 L2 子接口/Vbdif、P2 L3 对端，VLAN701 的真实接口与桥域查询、稳定探测3/3，以及 dot1ad/QinQ 和父端口生命周期。

~~~text
display interface Ethernet0.701
display bridge-domain 701
~~~

撤销先解除依赖，再删除子接口；网关、桥域和父端口是独立对象，只删除不再共用的部分。完整撤销及实际查询结果见案例。确认后保存，不以接口配置存在替代报文分类正确。

[L3 子接口](subinterfaces-l3.md) · [接口参数](reference/interfaces.md)
