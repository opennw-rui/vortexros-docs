# IPv4 over IPv4

## 拓扑

| 位置 | P1 | P2 |
| --- | --- | --- |
| 底层端口 | Ethernet0：10.201.12.1/24 | Ethernet0：10.201.12.2/24 |
| Tunnel40 | 10.240.40.1/30 | 10.240.40.2/30 |

两端使用 VPP。先配置底层地址并确认双向可达。本例把 IPv4 封装在 IPv4 中，底层网络需允许 IP 协议号 4。省略底层 VPN 参数时使用默认表。

## P1 配置

~~~text
system-view
~~~

配置清单：

~~~text
interface Tunnel 40
 tunnel-protocol ipv4-ipv4
 source 10.201.12.1
 destination 10.201.12.2
 ip address 10.240.40.1 255.255.255.252
#
~~~

CLI 操作：

~~~text
commit
~~~

## P2 配置

~~~text
system-view
~~~

配置清单：

~~~text
interface Tunnel 40
 tunnel-protocol ipv4-ipv4
 source 10.201.12.2
 destination 10.201.12.1
 ip address 10.240.40.2 255.255.255.252
#
~~~

CLI 操作：

~~~text
commit
~~~

Tunnel40 的直连前缀会走隧道。它不会为站点网络自动添加路由，也不提供加密或对端认证。

## 验证

**P1：**

~~~text
display interface Tunnel 40
ping -n -c 3 -t 1500 10.240.40.2
~~~

**P2：** `ping -n -c 3 -t 1500 10.240.40.1`。

示例输出：

~~~text
Tunnel40 current state : UP
Line protocol current state : UP
Tunnel protocol: ipv4-ipv4
Source: 10.201.12.1
Destination: 10.201.12.2

--- 10.240.40.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms

--- 10.240.40.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
~~~

## 撤销

先解除对 Tunnel40 的业务路由引用，再在两端执行：

~~~text
system-view
~~~

配置清单：

~~~text
undo interface Tunnel 40
~~~

CLI 操作：

~~~text
commit
display interface brief
~~~

示例中两端均不再列出 Tunnel40。P1 对外层地址 10.201.12.2 的探测仍为 3 发 3 收。

[IP-in-IP 配置指南](../../operator/ip-in-ip.md)
