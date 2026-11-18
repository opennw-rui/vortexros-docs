# L2 子接口

L2 子接口按 VLAN 标签识别报文，加入 bridge-domain 后转发。它自身不配置 IP，三层网关地址位于该桥域 Vbdif。

## 创建与约束

使用 `interface PARENT.NUMBER mode l2` 创建，`encapsulation dot1q vid VLAN` 指定单标签。子接口编号只表示实例身份，和分类使用的外层 VID、bridge-domain 编号相互独立；父端口必须存在。

显式子接口的实际外层 VID 与全局 `vlan` 对象互斥，适用于 dot1q、dot1ad、QinQ，配置顺序不影响结果。只相同的实例后缀、桥域编号或内层 VID 不构成冲突。不同父接口可复用相同外层 VID，同一父接口的匹配集合不可重叠。系统为 Access、Trunk、Hybrid 派生的内部对象不属于显式子接口，不受这个全局互斥规则限制。

全局 VLAN 通过 `l2 binding vlan` 接入桥域，显式 L2 子接口通过 `bridge-domain` 接入桥域，两种接入可以在同一桥域共存。两者的外层 VID 仍须满足上述互斥规则。

创建后补齐封装并绑定桥域；不能在已有接口上通过重复进入时改写 mode 完成二三层转换。应先解除业务引用、删除接口，再创建目标模式。

## 固定外层、多个内层的 QinQ

以下为开发候选的配置语法。本轮已完成固定、多内层及 Any 的部分真实链路、完整回读、重写与撤销对照；已用两端实际抓包验证外层 dot1q、dot1ad 的单层移除与回程恢复，参见[VXLAN 载荷](vxlan.md#qinq-业务的-vxlan-载荷)。具体范围以实验台账和原始记录为准。

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

`display interface Ethernet1.17` 从数据面读取实际完整内层集合、TPID 和实际重写动作，不只显示集合首值。匹配集合仅保存在控制元数据与既有原生分类槽位中；每包不遍历 VLAN 列表。

`pop single` 保留的是经过桥接的原始客户标签。本机 BVI 新生成的回应不一定保留该标签上下文：本轮直接接 BVI 的 ARP 反例中，回应只有固定外层标签。因此，不把“配置了多内层匹配”理解为能为本机新生报文自动选择不同的内层标签；实际业务应核对真实客户端到端报文。

当前独立原生对照中，固定内层和 Any 的 exact 匹配都接收过第三层标签。本候选不承诺严格只允许两层，也没有为此新增逐包扫描。另一个配置边界是未知单播：子接口重建会清除相应学习 MAC，关闭未知单播洪泛时，终端暖邻居产生的首批未知目的 MAC 帧会按桥域策略丢弃。本轮生命周期测试用真实 `bridge-domain 310 uu-flood` 明确开启洪泛，并核对实际 MAC 重学；不要把策略丢弃误当作匹配性能问题。

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
