# IPv6 服务端

DHCPv6 服务端分配 IA_NA 地址、IA_PD 前缀或提供非地址信息。默认网关来自 RA，不能因为租约成功就假定默认路由已存在。全局启用 `enable dhcp server` 后，在接口绑定已有的 DHCPv6 池。



```text
dhcpv6 pool LAN6
 address prefix 2001:db8:100::/64
 dns-server 2001:4860:4860::8888
#
interface Vlanif 100
 dhcpv6 server LAN6
```

验证和撤销：

```text
display dhcp service verbose
display ipv6 pool
interface Vlanif 100
 undo dhcpv6 server
commit
```

DHCPv6客户端和中继在对应接口视图配置；可使用`?`查看地址请求、前缀委派和中继目标的完整参数。DHCPv6客户端同样绑定LCP host接口，因此不会与VPP争用物理接口。

同一DHCPv6地址池内的地址前缀和委派前缀必须使用同一组有效/首选生命周期；显式生命周期最小为
60秒，首选生命周期不得大于有效生命周期。重叠的委派前缀在进入Candidate时即被拒绝，不会留到
Kea启动阶段才失败。


## 配置、验证和撤销

[双端 DHCPv6 案例](../../examples/dhcpv6.md)列出池、接口、客户端、实际 IA_NA/IA_PD 查询与撤销；[中继案例](../../examples/dhcpv6-relay.md)另有三节点配置。正常空库显示零租约，不能当服务故障；服务/Socket 真正失败仍报错。

解除接口的 `dhcpv6 server` 绑定后，再删除不再引用的池。多实例按地址族及 VPN 独立运行；租约显示不应被另一个健康空实例阻断。提交后核对服务、租约和实际客户端状态，再保存。

[租约字段与筛选](leases.md) · [参数参考](../reference/dhcp.md)
