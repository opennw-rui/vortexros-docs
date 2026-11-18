# IPv6 信息请求

## 只获取 IPv6 信息

接口下的 `dhcpv6 client information-request` 只请求 DNS 等非地址信息，不应期待 IA_NA 地址或委派前缀。`display dhcpv6 client` 显示运行状态而地址列为 `-`，不等于请求失败。可在接口下执行 `dhcpv6 client renew`，结合 DHCPv6 抓包确认 Reply；系统 DNS 仍由 Linux 管理，不自动改写。

## 配置示例

两台 VortexROS 的 Ethernet0 直接相连。客户端启用 IPv6 并使用 SLAAC 获取地址和默认网关，DHCPv6 信息请求独立提供 DNS 等选项；服务器地址为 `2001:db8:229::1/64`。

服务器：

```text
enable dhcp server
dhcpv6 pool INFO6
 address prefix 2001:db8:229::/64 life-time 300 150
 dns-server 2001:4860:4860::8888
 dns-domain-name example.net
 information-refresh 600
#
interface Ethernet0
 ipv6 enable
 ipv6 address 2001:db8:229::1 64
 dhcpv6 server INFO6
#
```

客户端：

```text
interface Ethernet0
 ipv6 enable
 dhcpv6 client information-request
#
```

分别执行 `commit`。若同一接口已配置有状态地址或 PD 请求，先撤销委派前缀的下游引用，再撤销 `ipv6 address auto dhcp` 和 `dhcpv6 client pd`，才能仅发送信息请求。SLAAC 和 RA 默认路由是独立配置，不必为切换信息请求而撤销。

## 验证

```text
display dhcpv6 client
```

实际输出节选（接口名按本例表示）：

```text
Interface  Address-Family  Role    Pool/Servers  VPN-Instance  State    Address  Delegated-Prefix
Ethernet0  IPv6            client                default       running  -        -
```

需要立即重新请求时，在接口视图执行 `dhcpv6 client renew`。实际报文记录中，同一事务号的请求与回复为：

```text
fe80::fe:baff:fea6:b799.546 > ff02::1:2.547:
  dhcp6 inf-req (xid=37cd25)
  option-request DNS-server DNS-search-list
fe80::fe:51ff:fecf:fdf7.547 > fe80::fe:baff:fea6:b799.546:
  dhcp6 reply (xid=37cd25)
  server-ID hwaddr type 1
  DNS-server 2001:4860:4860::8888
  DNS-search-list example.net.
```

本次请求和回复均不包含 IA_NA 或 IA_PD；不会增加 DHCPv6 地址或委派前缀。明确请求信息刷新选项的客户端还收到 `lifetime 600`；是否请求及采用该值由客户端实现决定。

DUID用于服务器识别，修改后客户端可能将其视为不同服务器。`information-refresh`控制服务端信息刷新选项；客户端是否采用该值取决于其请求和实现。

接口绑定VPN后，确认该VPN中的IPv6邻居发现和回程路径正常；只有服务端发出Reply还不足以说明客户端已收到。使用本节查询确认客户端状态和收到的选项。

撤销时，P1 执行 `undo dhcpv6 client information-request`；P2 先在接口下 `undo dhcpv6 server`，再删除不再使用的池，必要时 `undo dhcpv6 duid` 恢复默认。提交后检查客户端、服务和池查询，确认目标绑定不再存在。地址、接口、VPN 实例属于独立配置，按各自依赖处理。若要持久保留撤销结果，再执行 `save`。

[DHCP 功能与开关](../dhcp.md) · [逐条命令参数](../reference/dhcp.md)
