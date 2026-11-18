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

每个邻居使用独立信息块显示 IPv6 地址、MAC、接口、所属 VPN 和可用状态。VLAN/CEVLAN 分别表示外层/内层 VLAN；Vlanif 显示所属 VLAN，子接口显示封装标签，Vbdif 仅在桥域绑定 VLAN 时显示相应 VLAN。当前不提供的完整 ND 状态、Router 标志和 SEND 安全状态显示 -；- 表示无法提供该信息，不表示故障。本机接口地址不作为邻居项显示。

[功能目录](../neighbors.md) · [命令参数](../reference/neighbors.md)
