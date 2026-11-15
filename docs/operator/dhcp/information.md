# IPv6 信息请求

## 只获取 IPv6 信息

接口下的 `dhcpv6 client information-request` 只请求 DNS 等非地址信息，不应期待 IA_NA 地址或委派前缀。`display dhcpv6 client` 显示运行状态而地址列为 `-`，不等于请求失败。可在接口下执行 `dhcpv6 client renew`，结合 DHCPv6 抓包确认 Reply；系统 DNS 仍由 Linux 管理，不自动改写。

开发拓扑中，P1 的 `host-p1r12` 属于 CLI-UNDER，仅有链路本地 IPv6 地址；对端 P2 的 `host-p2r12` 属于本机 DHCP-EMPTY，服务地址为 `2001:db8:150::1/64`。在已启用 DHCP 服务的 P2 配置：

```text
dhcpv6 pool CLI6-U
 vpn-instance DHCP-EMPTY
 address prefix 2001:db8:150::/64 life-time 3600 1800
 dns-server 2001:db8::53
 dns-domain-name cli.example
 information-refresh 600
 quit
dhcpv6 duid llt
interface host-p2r12
 dhcpv6 server CLI6-U
 quit
commit
```

P1：

```text
interface host-p1r12
 dhcpv6 client information-request
 quit
commit
interface host-p1r12
 dhcpv6 client renew
 quit
```

真实报文节选，同一事务号配对：

```text
fe80::c0a6:56ff:fe77:567c.546 > ff02::1:2.547:
  dhcp6 inf-req (xid=74ec4e) (option-request DNS-server DNS-search-list)
fe80::24a2:e1ff:fefc:8ec.547 > fe80::c0a6:56ff:fe77:567c.546:
  dhcp6 reply (xid=74ec4e)
  server-ID hwaddr/time
  DNS-server 2001:db8::53
  DNS-search-list cli.example.
```

DUID LLT 已通过服务端报文验证；恢复默认 LL 后，Reply 使用 hwaddr 形式。`information-refresh 600` 已核对 Kea 实际配置；该客户端未请求对应选项，因此不将上述报文作为该选项返回值的证据。

VPP 数据面中，只有链路本地地址的接口也必须在当前 VPN 实例的组播表上接收邻居发现。本次验收发现并修复了启用 IPv6 后切换接口表时，原生 VPP 未迁移这一成员关系的问题；否则 Kea 可接收请求并成功发出 Reply，但回程邻居发现会失败。这里不需要修改 Kea，也不需要放宽组播入口校验。

撤销时，P1 执行 `undo dhcpv6 client information-request`；P2 先在接口下 `undo dhcpv6 server`，再删除不再使用的池，必要时 `undo dhcpv6 duid` 恢复默认。提交后，客户端及服务器进程均已实际停止，成功的服务和池查询均为空。地址、接口、VPN 实例属于独立配置，按各自依赖处理。若要持久保留撤销结果，再执行 `save`。

[DHCP 功能与开关](../dhcp.md) · [逐条命令参数](../reference/dhcp.md)
