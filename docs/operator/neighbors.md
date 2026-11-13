# ARP 与 ND

检查和管理 IPv4 ARP 与 IPv6 ND 邻居。

[命令参考](reference/neighbors.md)

## 配置与验证

IPv4 ARP和IPv6 ND邻居老化是VPP进程级参数，不依赖VLAN或bridge-domain。纯三层接口同样使用这些参数。默认值均为1200秒，并在VPP每次启动或重新连接后优先恢复，再下发接口、地址和业务配置。

```text
arp timeout 900
ipv6 nd stale-timeout 1800
ipv6 nd max-number 65536
ipv6 nd recycle enable
commit
```

恢复默认值：

```text
undo arp timeout
undo ipv6 nd stale-timeout
undo ipv6 nd max-number
undo ipv6 nd recycle
commit
```

`max-number`限制VPP IPv6邻居表容量；`recycle enable`在容量已满时回收最老的动态条目，静态邻居不参与动态回收。回收策略必须显式配置，`undo`恢复VPP启动时的默认策略。容量同步到 Linux ND 回收阈值。老化时间和回收开关作用于 VPP 邻居表。默认值不显示在配置中，非默认值通过 `display current-configuration` 和 `display ipv6 nd` 回读验证。

静态 IPv6 邻居绑定在三层数据面接口上。MAC 支持三段式和冒号分隔形式，保存时统一为冒号分隔形式。

```text
ipv6 neighbor 2001:db8:10::2 0211-2233-4455 interface Vlanif10
commit
display ipv6 neighbors static
undo ipv6 neighbor 2001:db8:10::2 02:11:22:33:44:55 interface Vlanif10
commit
```

多播、未指定IPv6地址，多播或全零MAC，以及二层或控制型接口都会在提交前被拒绝。提交后的静态项由Linux后端写入对应LCP接口，再由LCP同步至VPP；接口重建时按同一路径恢复，不再由VPP后端重复写入。动态邻居只属于运行态，不会写入配置。

静态ARP只接受可用IPv4单播地址和六字节单播MAC；全零、组播或广播映射会在提交前拒绝。

## IPv6 邻居查询

IPv6邻居表直接读取VPP实际ND条目，可按接口、VPN实例或动态/静态类型过滤：

```text
display ipv6 neighbors
display ipv6 neighbors Vlanif 10
display ipv6 neighbors interface Ethernet 1
display ipv6 neighbors vpn-instance BLUE
display ipv6 neighbors dynamic
display ipv6 neighbors static
```

静态邻居使用`ipv6 neighbor IPV6 MAC interface IF`配置并随Candidate、commit和save持久化；删除时使用对应的完整`undo ipv6 neighbor ...`命令。`undo`中的接口、IPv6地址和MAC必须与Candidate中的条目完全匹配，避免输错MAC时误删另一条配置。承载接口被删除并重建后，即使静态邻居配置本身未变化，控制面也会重新下发该条目。commit会以VPP静态邻居表为权威读回，不能把动态学习条目误认为已配置静态条目。

每个邻居使用独立的信息块，`IPv6 Address`独占一行；其余字段固定按`Link-layer/State`、`Interface/Age`、`VLAN/CEVLAN`、`VPN name/Is Router`两列显示，`Secure FLAG`单列显示。动态和静态类型只在汇总中计数，不增加无后端字段的明细行。VLAN信息只来自已提交模型，不根据接口名称猜测：Vlanif使用其VLAN，子接口使用外层/内层VLAN，Vbdif只有在业务桥域明确绑定VLAN时才显示该VLAN；桥域ID不会冒充VLAN ID。当前VPP Binary API不提供完整ND状态、Router标志和SEND安全状态，这些字段显示`-`，不会伪造为REACH、Router或安全邻居。命令也不会根据接口地址伪造本机邻居项。
