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
```

配置清单：

```text
interface Tunnel 10
 description SITE-A-SITE-B-IPIP
 tunnel-protocol ipv4-ipv4
 source 192.0.2.1
 destination 198.51.100.2
 ip address 10.10.10.1 255.255.255.252
#
```

CLI 操作：

```text
commit
display interface Tunnel 10
ping 10.10.10.2
```

IPv6 over IPv4示例：

```text
interface Tunnel 11
 ipv6 enable
 tunnel-protocol ipv6-ipv4
 source 192.0.2.1
 destination 198.51.100.2
 ipv6 address 2001:db8:10::1 64
#
```

CLI 操作：

```text
commit
display interface Tunnel 11
ping ipv6 2001:db8:10::2
```

当未显式配置MTU时，系统根据外层IP头自动使用1476字节（GRE over IPv4）、1456字节（GRE over IPv6）、1480字节（IP-in-IP over IPv4）或1460字节（IP-in-IP over IPv6）的有效三层MTU；显式`mtu`始终优先。修改 `tunnel-protocol` 会清除旧协议的源、目的、底层 VPN 和协议专用参数。切换时需重新填写新协议的两端地址，移除不符合新内层地址族的 Tunnel 地址，然后一起提交；提交会重建隧道并短暂中断业务。

## 激活条件

四种 IP-in-IP 均要求接口未 shutdown、封装类型和两端地址完整，外层地址族与所选协议一致。本机须在指定底层 VPN 拥有源地址，该 VPN 须有覆盖远端地址的有效路由。Tunnel 配置相应内层 IP 地址后，才能显示三层 Protocol Up。

接口 Up 不检测远端隧道是否存在，也不保证 ARP/ND、路径过滤或 MTU 已满足。先检查底层路由，再检查两端协议和内层地址，最后测试业务；底层源地址或路由恢复后会自动重新激活。
