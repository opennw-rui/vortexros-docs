# 进程、Level 与接口

进程号在设备内全局唯一。一个进程只能绑定一个VPN，一个VPN最多配置一个IS-IS进程；接口所属VPN必须与进程VPN一致。

```text
isis 10 vpn-instance BLUE
 network-entity 49.0001.0100.0000.0001.00
 is-level level-2
 log-adjacency-changes
#
interface Vlanif 100
 ipv6 enable
 isis enable 10
 isis ipv6-enable 10
 isis circuit-type p2p
 isis circuit-level level-2
 isis cost 20
```

提交后，IPv4和IPv6在同一进程中运行。接口VPN不一致、同一接口引用另一个进程或同一VPN已存在其他进程时，命令会被拒绝。


[双端配置和路由查询](../../examples/isis.md) · [全部参数](../reference/isis.md)


## NET 与激活条件

接口和进程属于同一 VPN、已配置有效 NET、链路 Up，并且两端存在共同 Level 时，才可能建立邻接。L1 还要求区域地址匹配；System ID 应在路由域中唯一。配置了接口激活命令但没有 NET，不代表进程已经能够交换路由。

撤销最后一个 NET 使用完整值，例如：

~~~text
isis 10 vpn-instance BLUE
 undo network-entity 49.0001.0100.0000.0001.00
#
commit
display isis 10 peer
~~~

该操作保留进程及接口配置，停止该身份对应的协议运行；旧邻接可能保留到 Hold 定时器到期。实际暖撤销中，配置保留空进程，邻居随后变为0；重新加入同一 NET 并提交后，邻居重新 Up，无需重启服务。它不关闭接口，也不删除接口地址。只有要删除整个进程时才使用系统视图的 `undo isis 10`。

## 开销与静默接口

isis cost 调整接口参与路径计算的开销，不是路由优先级。例如两端接口原开销均为 10，远端环回路径为 Cost 20；本端接口改为 37 后，IPv4/IPv6 路径均为 Cost 47，Preference 仍为 15。示例双栈探测各 2/2；undo isis cost 恢复后路径回到 Cost 20。

物理接口执行 isis passive 后停止建立 IS-IS 邻接，接口地址仍可以经其他邻接发布。撤销使用 undo isis passive。LoopBack 自动按静默接口处理，不在环回上建立邻接；无需额外配置 isis passive，撤销显式命令后仍保持环回语义。

动态主机名默认开启。hostname dynamic 恢复该缺省行为，不额外写入配置；undo hostname 同样恢复缺省值。设备名称与 IS-IS System ID 不同，邻接身份以 NET 中的 System ID 为准。


## 电路级别、网络类型与 DIS

`is-level` 设置进程参与的级别；接口 `isis circuit-level` 进一步限定该链路建立哪一级邻接。接口与进程、对端必须存在共同级别。例如，进程使用 `level-1-2`、本接口使用 `level-2` 时，链路运行状态为 L2；改为 `level-1` 后使用 L1。更改级别会重新形成对应邻接并计算路由，切换期间可能出现短暂撤路。

以太网默认使用 LAN 电路。两端只有一台相邻路由器时，可同时配置 `isis circuit-type p2p`；撤销使用 `undo isis circuit-type`，恢复 LAN。两端网络类型必须协调，不能仅配置一端后就以暂时的邻居状态判断正常。

```text
interface Ethernet0
 isis circuit-level level-1
 isis circuit-type p2p
#
commit
display isis 1 peer
display isis 1 interface
display ip routing-table 198.18.246.3
display ipv6 routing-table 2001:db8:246::3
```

一组双栈运行结果中，接口 Type 为 `p2p`、邻居 Type 为 `1` 且 Up，远端 IPv4 /32 和 IPv6 /128 均选中 ISIS、Preference 15、Cost 20，IPv4 探测 1/1。接口改为 L2 时，同一远端前缀仍以 Preference 15、Cost 20 学到；Level 不是路由优先级。

`isis priority` 是 LAN 的 DIS 选举优先级，缺省 64，与 IP 路由表的 Preference 15 无关；点到点电路不选举 DIS。`undo isis priority` 恢复 64。`undo isis circuit-level` 恢复接口的缺省级别范围，实际仍受进程 `is-level` 限制。

接口 BFD 使用 `isis bfd enable`，计时器及共享会话的修改顺序见 [BFD 协议绑定](../bfd/protocols.md)。双栈 IS-IS 可能与同接口 OSPFv3 共用 IPv6 链路本地 BFD；有效参数不一致时，配置会直接被拒绝，不会提交一组含义冲突的后端参数。

## 度量编码

`cost-style narrow` 使用旧式窄度量 TLV，只支持 IPv4 IS-IS 路由。不能同时配置 IS-IS 的 IPv6 接口激活或 `ipv6 import-route`；接口上的其他 IPv6 服务不受此限制影响。需要双栈时使用 `cost-style transition` 或默认的 `wide`，系统不会自动改变编码来替代用户配置。

| 编码 | 发出的 IPv4 可达性信息 | IPv6 IS-IS | 适用场景 |
|---|---|---|---|
| narrow | 旧式 TLV | 不支持 | 与仅支持旧式度量的 IPv4 网络互通 |
| transition | 同时发出旧式与扩展 TLV | 支持 | 从窄度量向宽度量迁移 |
| wide | 扩展 TLV | 支持 | 默认模式，通常采用此项 |

迁移时应协调两端，使用 transition 作为过渡，再恢复 wide。实际 transition 的 LSP 同时包含旧式和 Extended Reachability，双栈外部前缀均学到 ISIS Preference15、Cost10，指定源 IPv6 探测1/1。恢复 wide 后，IPv4 仅发出扩展可达性 TLV。`cost-style wide` 恢复默认，默认项不写入配置；无需额外的 undo cost-style 命令。

[FRR 度量编码说明](https://docs.frrouting.org/en/latest/isisd.html#clicmd-metric-style-narrow-transition-wide)给出各编码的互通范围。
