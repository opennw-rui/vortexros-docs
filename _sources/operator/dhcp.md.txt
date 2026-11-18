# DHCP

分别配置 IPv4/IPv6 服务端、客户端和中继。全局 `enable dhcp server` 只控制服务端；客户端、Relay 和 PD 按接口意图运行，不要求启用服务端。

租约中的 DNS 参数不改写 Linux 的系统解析配置。DHCPv6 不提供 IPv6 默认网关，默认路由来自 RA；不要将获取地址与获取网关混为同一步。

~~~{toctree}
:maxdepth: 2

dhcp/server4
dhcp/client4
dhcp/ipv6
dhcp/relay
dhcp/leases
~~~

[DHCPv4 完整案例](../examples/dhcp.md) · [DHCPv6 完整案例](../examples/dhcpv6.md) · [IPv6 RA](ipv6-autoconfig.md) · [命令参数](reference/dhcp.md)
