# IPv6 信息请求

## 只获取 IPv6 信息

接口下的 `dhcpv6 client information-request` 只请求 DNS 等非地址信息，不应期待 IA_NA 地址或委派前缀。`display dhcpv6 client` 显示运行状态而地址列为 `-`，不等于请求失败。可在接口下执行 `dhcpv6 client renew`，结合 DHCPv6 抓包确认 Reply；系统 DNS 仍由 Linux 管理，不自动改写。

本例中，P1 的 `Ethernet0` 属于 CLI-UNDER，仅有链路本地 IPv6 地址；对端 P2 的 `Ethernet0` 属于本机 DHCP-EMPTY，服务地址为 `2001:db8:150::1/64`。在已启用 DHCP 服务的 P2 配置：

```text
dhcpv6 pool CLI6-U
 vpn-instance DHCP-EMPTY
 address prefix 2001:db8:150::/64 life-time 3600 1800
 dns-server 2001:db8::53
 dns-domain-name cli.example
 information-refresh 600
 quit
dhcpv6 duid llt
interface Ethernet0
 dhcpv6 server CLI6-U
 quit
commit
```

P1：

```text
interface Ethernet0
 dhcpv6 client information-request
 quit
commit
interface Ethernet0
 dhcpv6 client renew
 quit
```

示例输出，同一事务号配对：

```text
fe80::c0a6:56ff:fe77:567c.546 > ff02::1:2.547:
  dhcp6 inf-req (xid=74ec4e) (option-request DNS-server DNS-search-list)
fe80::24a2:e1ff:fefc:8ec.547 > fe80::c0a6:56ff:fe77:567c.546:
  dhcp6 reply (xid=74ec4e)
  server-ID hwaddr/time
  DNS-server 2001:db8::53
  DNS-search-list cli.example.
```

DUID用于服务器识别，修改后客户端可能将其视为不同服务器。`information-refresh`控制服务端信息刷新选项；客户端是否采用该值取决于其请求和实现。

接口绑定VPN后，确认该VPN中的IPv6邻居发现和回程路径正常；只有服务端发出Reply还不足以说明客户端已收到。使用本节查询确认客户端状态和收到的选项。

撤销时，P1 执行 `undo dhcpv6 client information-request`；P2 先在接口下 `undo dhcpv6 server`，再删除不再使用的池，必要时 `undo dhcpv6 duid` 恢复默认。提交后检查客户端、服务和池查询，确认目标绑定不再存在。地址、接口、VPN 实例属于独立配置，按各自依赖处理。若要持久保留撤销结果，再执行 `save`。

[DHCP 功能与开关](../dhcp.md) · [逐条命令参数](../reference/dhcp.md)
