# IPv6 邻居查询

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

[功能目录](../neighbors.md) · [命令参数](../reference/neighbors.md)
