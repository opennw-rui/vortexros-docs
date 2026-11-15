# DHCPv6 中继

## 拓扑与前提

三台设备均运行 VortexROS。CE1 是客户端，P1 是中继，P2 使用配套 DHCPv6 服务端。服务器在上行链路，分配的地址属于客户端链路。

~~~text
CE1 Ethernet0 ── Ethernet1 P1 Ethernet0 ── Ethernet0 P2
  DHCPv6        2001:db8:11::1/64
                             2001:db8:12::1/64  2001:db8:12::2/64
客户端地址池: 2001:db8:11::/64
~~~

本例使用指定服务器地址的单播中继。所有接口应有可用链路本地地址，路径须允许 DHCPv6 和 ICMPv6；不需要手工启动 Kea 或编辑其配置文件。

## P1：中继

~~~text
system-view
interface Ethernet1
 ipv6 address 2001:db8:11::1 64
 dhcpv6 relay destination 2001:db8:12::2
quit
interface Ethernet0
 ipv6 address 2001:db8:12::1 64
quit
commit
~~~

中继不需要 enable dhcp server；客户口与上行必须具备正确的 VPN 归属和到服务器的路由。上行直连 2001:db8:12::/64 可提供本例路径。接口形式的服务器组说明见[中继参数](../operator/dhcp/relay.md)。

## P2：服务器

~~~text
system-view
enable dhcp server
dhcpv6 pool RELAY6
 address prefix 2001:db8:11::/64 life-time 3600 1800
 dns-server 2001:db8::53
quit
interface Ethernet0
 ipv6 address 2001:db8:12::2 64
 dhcpv6 server RELAY6
quit
ipv6 route-static 2001:db8:11:: 64 Ethernet0 2001:db8:12::1
commit
~~~

地址池前缀必须与中继客户链路一致，不能误用服务器上行口的前缀。到客户链路的静态路由用于分配后的业务回程。

## CE1：客户端

~~~text
system-view
interface Ethernet0
 ipv6 address auto dhcp
quit
commit
~~~

DHCPv6 不提供默认网关，所获地址通常为 /128。先在 P1 用 display interface Ethernet1 读取当前链路本地地址，再在 CE1 配置到网关及服务器网段的路由。以下以 fe80::fe:72ff:feac:d1ee 为例，必须替换成 P1 当前值，不能使用重建接口前的旧值：

~~~text
ipv6 route-static 2001:db8:11:: 64 Ethernet0 fe80::fe:72ff:feac:d1ee
ipv6 route-static 2001:db8:12:: 64 Ethernet0 fe80::fe:72ff:feac:d1ee
commit
~~~

仅地址分配成功不代表默认路由或其他业务路由已经具备。

## 验证

CE1：

~~~text
display dhcpv6 client interface Ethernet0
display ipv6 interface brief
~~~

P1：

~~~text
display dhcpv6 relay
display dhcp service verbose
~~~

P2：

~~~text
display dhcpv6 pool name RELAY6 used
display dhcpv6 pool name RELAY6 verbose
~~~

应看到中继处于运行状态，客户端取得 2001:db8:11::/64 内的地址，服务器租约中的 DUID、IAID 和地址与客户端相符。正常空池应显示零租约，不是查询失败。

客户端和服务器的对应租约示例：

~~~text
Interface  Address-Family  Role    Pool/Servers  VPN-Instance  State    Address                Delegated-Prefix
Ethernet0  IPv6            client                default       running  2001:db8:11::16/128    -

Index  Pool    IPv6 Address/Prefix   Type   Lease  Status
0      RELAY6  2001:db8:11::16/128   IA_NA  3586s  used
Total: 1
~~~

取得地址并完成 DAD 后，CE1 使用实际地址作为源，分别 Ping 2001:db8:11::1 与 2001:db8:12::2，确认客户链路和跨中继路由。初次探测可能等待邻居解析；持续不通时检查实际链路本地下一跳，而不是重复续租。

~~~text
ping ipv6 -a 2001:db8:11::16 -c 3 2001:db8:12::2
~~~

示例输出：

~~~text
3 packets transmitted, 3 received, 0% packet loss
~~~

## 撤销

先在 CE1 Ethernet0 执行 undo ipv6 address auto dhcp，并撤销上面两条静态路由（命令前加 undo，下一跳使用自己配置的值），提交以停止申请。P1 撤销中继：

~~~text
system-view
interface Ethernet1
 undo dhcpv6 relay destination 2001:db8:12::2
quit
commit
display dhcpv6 relay
~~~

P2 先解除 Ethernet0 的 dhcpv6 server 绑定，再删除 RELAY6；用相应 undo 命令撤销专用静态路由和接口地址。P1 同样撤销本例地址。提交后检查中继和池均不再存在，各设备按需 save。客户端原地址可能在租期内保留，不能仅凭旧地址仍存在判断中继未撤销。
