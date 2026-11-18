# IPv6 over IPv4

## 拓扑与影响

两端均需启用 VPP 数据面。

两台 VortexROS 的 Ethernet0 相连。R1/R2 的底层地址分别为 198.19.23.2、198.19.23.3；Tunnel93 分别使用 2001:db8:93::2、2001:db8:93::1。先确保底层 IPv4 双向可达；中间设备须允许 IP 协议号 41。

隧道仅承载指定内层地址族。配置 Tunnel 地址会建立直连路由；其他站点网段仍需单独配置路由。源地址须属于本机选定底层 VPN，目的地址须在该 VPN 内可达。两端须未 shutdown，并配置完整的封装、源和目的地址；Protocol Up 还要求有效的 Tunnel 三层地址。

## R1 配置

进入系统视图后配置：

~~~text
interface Ethernet 0
 ip address 198.19.23.2 255.255.255.0
#
interface Tunnel 93
 tunnel-protocol ipv6-ipv4
 source 198.19.23.2
 destination 198.19.23.3
 ipv6 enable
 ipv6 address 2001:db8:93::2 64
#
~~~

回到系统视图，执行 `commit`。

## R2 配置

进入系统视图后配置：

~~~text
interface Ethernet 0
 ip address 198.19.23.3 255.255.255.0
#
interface Tunnel 93
 tunnel-protocol ipv6-ipv4
 source 198.19.23.3
 destination 198.19.23.2
 ipv6 enable
 ipv6 address 2001:db8:93::1 64
#
~~~

回到系统视图，执行 `commit`。

## 验证

R1：

~~~text
display interface Tunnel 93
ping ipv6 -c 2 -a 2001:db8:93::2 2001:db8:93::1
~~~

R2：

~~~text
ping ipv6 -c 2 -a 2001:db8:93::1 2001:db8:93::2
~~~

验证结果摘要：

~~~text
Tunnel93 current state : UP
Line protocol current state : UP
Tunnel protocol: ipv6-ipv4
Source: 198.19.23.2
Destination: 198.19.23.3

2 packets transmitted, 2 received, 0% packet loss
~~~

反向探测同为 2 发 2 收。接口 Up 只表示本机激活条件满足，仍需用双向业务探测判断远端是否可用。

## 撤销

先解除引用 Tunnel93 的业务路由，再在两端的系统视图执行：

~~~text
undo interface Tunnel 93
commit
display interface brief
~~~

Tunnel93 和对应直连路由消失，底层 Ethernet0 地址保持。若需要跨重启保留修改，再执行 `save` 并确认。

[IP-in-IP 配置指南](../../operator/ip-in-ip.md)
