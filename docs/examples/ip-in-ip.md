# IP-in-IP

手工 IP 隧道可让 IPv4 或 IPv6 业务跨越另一种地址族的底层网络。它不提供加密、认证或自动发现。

| 案例 | 内层业务 | 底层网络 |
|---|---|---|
| [IPv4 over IPv4](ip-in-ip/ipv4-in-ipv4.md) | IPv4 | IPv4 |
| [IPv6 over IPv4](ip-in-ip/ipv6-in-ipv4.md) | IPv6 | IPv4 |
| [IPv4 over IPv6](ip-in-ip/ipv4-in-ipv6.md) | IPv4 | IPv6 |
| [IPv6 over IPv6](ip-in-ip/ipv6-in-ipv6.md) | IPv6 | IPv6 |

更改封装类型后，重新配置新协议的源、目的地址，并移除不符合新内层地址族的 Tunnel 地址，再一起提交。提交会重建隧道，业务短暂中断。两端必须使用相反的源、目的地址和相同的封装类型。

~~~{toctree}
:maxdepth: 1

ip-in-ip/ipv4-in-ipv4
ip-in-ip/ipv6-in-ipv4
ip-in-ip/ipv4-in-ipv6
ip-in-ip/ipv6-in-ipv6
~~~

[配置指南](../operator/ip-in-ip.md) · [激活条件](../operator/tunnel-settings/lifecycle.md)
