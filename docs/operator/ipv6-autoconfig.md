# RA 与 SLAAC

IPv6 路由器发现独立于 DHCPv6。

[命令参考](reference/ipv6-autoconfig.md) · [配置案例](../examples/ipv6-ra.md)

## 配置与撤销

DHCPv6 不会提供IPv6默认网关；默认路由来自Router Advertisement。需要同时从RA生成全局地址并接受RA默认路由时，可使用组合命令：

```text
interface Ethernet 1
 ipv6 address auto global default
commit
display ipv6 interface brief
display ipv6 neighbors
display ipv6 routing-table
```

若只需要其中一项，也可分别使用`ipv6 address auto slaac`或`ipv6 nd ra default-route enable`。使用有状态DHCPv6获取地址、同时从RA获取默认路由时，可以组合`ipv6 address auto dhcp`与`ipv6 nd ra default-route enable`，无需同时启用SLAAC地址生成。

VortexROS只在已配置的接口上开启RA接收。VPP模式下由该接口的LCP host接收RA，Linux内核执行DAD并维护前缀、首选时间、有效时间和Router Lifetime，linux-cp再把有效地址和路由同步到VPP。即使系统开启IPv6转发，该接口仍会使用明确的RA接收策略；其他接口不会被全局放开。接口属于VPN实例时，LCP接口先加入对应Linux VRF，学习结果留在该VPN的路由域内。

组合意图可一次撤销：

```text
interface Ethernet 1
 undo ipv6 address auto global default
commit
```

分别配置的地址自动生成与默认路由也可以用各自的精确`undo`撤销。

撤销全部RA功能后，控制面关闭该接口的RA、自动前缀和默认路由接收，并清理内核中由RA协议安装的路由及可识别的SLAAC地址。DHCPv6地址不属于这套清理范围。
