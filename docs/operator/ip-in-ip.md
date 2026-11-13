# IP-in-IP

用手工点到点 IP 隧道跨接两个三层网络。

[命令参考](reference/tunnels.md) · [配置案例](../examples/ip-in-ip.md)

## 配置与验证

手工IP隧道使用点到点三层接口，支持四种内层与外层地址族组合：

| `tunnel-protocol` | 内层报文 | 外层传输 |
|---|---|---|
| `ipv4-ipv4` | IPv4 | IPv4 |
| `ipv6-ipv4` | IPv6 | IPv4 |
| `ipv4-ipv6` | IPv4 | IPv6 |
| `ipv6-ipv6` | IPv6 | IPv6 |

外层`source`与`destination`必须属于协议指定的同一外层地址族。Tunnel接口地址必须属于协议指定的内层地址族。`destination ... vpn-instance` 选择外层目的地址查路使用的命名 VPN；使用默认路由域时省略该参数。本功能是手工点到点隧道，不提供自动隧道、6to4、ISATAP或隧道发现。

IPv4 over IPv4示例：

```text
system-view
interface Tunnel 10
 description SITE-A-SITE-B-IPIP
 tunnel-protocol ipv4-ipv4
 source 192.0.2.1
 destination 198.51.100.2
 ip address 10.10.10.1 255.255.255.252
quit
commit
display interface Tunnel 10
ping 10.10.10.2
```

IPv6 over IPv4示例：

```text
interface Tunnel 11
 tunnel-protocol ipv6-ipv4
 source 192.0.2.1
 destination 198.51.100.2
 ipv6 address 2001:db8:10::1 64
quit
commit
display interface Tunnel 11
ping 2001:db8:10::2
```

当未显式配置MTU时，系统根据外层IP头自动使用1476字节（GRE over IPv4）、1456字节（GRE over IPv6）、1480字节（IP-in-IP over IPv4）或1460字节（IP-in-IP over IPv6）的有效三层MTU；显式`mtu`始终优先。修改`tunnel-protocol`会清除旧协议的源、目的、underlay及协议专用参数，避免把旧封装参数误用于新协议。
