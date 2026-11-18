# DHCPv6 中继

## 拓扑与前提

三台设备均运行 VortexROS。CE1 是客户端，P1 是中继，P2 使用配套 DHCPv6 服务端。服务器在上行链路，分配的地址属于客户端链路。

~~~text
CE1 Ethernet0 ── Ethernet1 P1 Ethernet0 ── Ethernet0 P2
  DHCPv6        2001:db8:11::1/64
                             2001:db8:12::1/64  2001:db8:12::2/64
客户端地址池: 2001:db8:11::/64
~~~

本例使用上行接口形式，将请求发送到服务器组 ff05::1:3。所有接口应有可用链路本地地址，路径须允许 DHCPv6 和 ICMPv6；不需要手工启动 Kea 或编辑其配置文件。不要把服务器组改为客户端/中继组 ff02::1:2。

## P1：中继

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet1
 ipv6 enable
 ipv6 address 2001:db8:11::1 64
 dhcpv6 relay interface Ethernet0
#
interface Ethernet0
 ipv6 enable
 ipv6 address 2001:db8:12::1 64
#
~~~

CLI 操作：

~~~text
commit
~~~

中继不需要 enable dhcp server。客户口和上行口应属于同一 VPN，且不能是同一个接口。本例服务器上行口只使用 2001:db8:12::2/64；若已有其他 IPv6 地址，先按实际地址规划核对中继到服务器所有可能回复源地址的路由。

## P2：服务器

~~~text
system-view
~~~

配置清单：

~~~text
enable dhcp server
dhcpv6 pool RELAY6
 address prefix 2001:db8:11::/64 life-time 3600 1800
 excluded-address 2001:db8:11::1 2001:db8:11::ff
 dns-server 2001:db8::53
#
interface Ethernet0
 ipv6 enable
 ipv6 address 2001:db8:12::2 64
 dhcpv6 server RELAY6
#
ipv6 route-static 2001:db8:11:: 64 Ethernet0 2001:db8:12::1
~~~

CLI 操作：

~~~text
commit
~~~

地址池前缀必须与中继客户链路一致，不能误用服务器上行口的前缀。排除范围保留中继网关及其他静态地址，避免将 2001:db8:11::1 分配给客户端；服务器不会自动知道远端链路的全部静态地址。到客户链路的静态路由用于分配后的业务回程。

## CE1：客户端

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ipv6 enable
 ipv6 address auto dhcp
#
~~~

CLI 操作：

~~~text
commit
~~~

DHCPv6 不提供默认网关，所获地址通常为 /128。先在 P1 用 display interface Ethernet1 读取当前链路本地地址，再在 CE1 配置到网关及服务器网段的路由。以下以 fe80::fe:5ff:fefe:d57c 为例，必须替换成 P1 当前值，不能使用重建接口前的旧值：

~~~text
ipv6 route-static 2001:db8:11:: 64 Ethernet0 fe80::fe:5ff:fefe:d57c
ipv6 route-static 2001:db8:12:: 64 Ethernet0 fe80::fe:5ff:fefe:d57c
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

客户端和服务器对应租约的示例节选（完整清单可能包含历史租约）：

~~~text
Interface  Address-Family  Role    Pool/Servers  VPN-Instance  State    Address                Delegated-Prefix
Ethernet0  IPv6            client                default       running  2001:db8:11::101/128    -

Index  Pool    IPv6 Address/Prefix   Type   Lease  Status
0      RELAY6  2001:db8:11::101/128   IA_NA  3589s  used
~~~

取得地址并完成 DAD 后，CE1 使用实际地址作为源，分别 Ping 2001:db8:11::1 与 2001:db8:12::2，确认客户链路和跨中继路由。初次探测可能等待邻居解析；持续不通时检查实际链路本地下一跳，而不是重复续租。

~~~text
ping ipv6 -a 2001:db8:11::101 -c 3 2001:db8:12::2
~~~

示例输出：

~~~text
3 packets transmitted, 3 received, 0% packet loss
~~~

在 P2 用源地址 2001:db8:12::2 反向 Ping 客户端当前地址，检查服务器到客户端的路由。不要用中继进程 running 或池内有历史租约代替当前客户端的双向检查。

## 无法取得租约时

1. 确认客户端有 Solicit，中继上行发送到 ff05::1:3，服务器返回 Relay-reply；单播目标的成功不能代替这条组播路径。
2. 服务器接口有多个 IPv6 地址时，组播请求的回复源可能不是示例地址。核对实际回复源，再在中继查询其路由；缺少可达路径时先补齐实际网络规划，不能靠关闭源地址检查处理。
3. 请求已发出但没有租约时，分别检查服务器监听、回复回程和中继接收；短时间内没有抓到报文不能证明服务器没有收到。
4. 地址已取得但无法通信时，检查 /128 客户端路由、当前链路本地下一跳、DAD 及重复地址。排除地址不会自动收回已发放的旧租约，修改后仍须核对客户端当前地址。

组播组含义见 [RFC 9915 第 7.1 节](https://www.rfc-editor.org/rfc/rfc9915.html#section-7.1)。

## 撤销

先在 P1 只撤销中继，保留服务器用于对照：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet1
 undo dhcpv6 relay interface Ethernet0
#
~~~

CLI 操作：

~~~text
commit
display dhcpv6 relay
~~~

此时 CE1 停止并重新申请地址，应不能获得新租约；旧地址或服务器历史租约不代表中继仍在工作。随后在 CE1 Ethernet0 执行 undo ipv6 address auto dhcp，并撤销前述两条静态路由，提交清理。

P2 先解除 Ethernet0 的 dhcpv6 server 绑定，再删除 RELAY6；用相应 undo 命令撤销专用静态路由和接口地址。P1 同样撤销本例地址。提交后检查中继和池均不再存在，各设备按需 save。客户端原地址可能在租期内保留，不能仅凭旧地址仍存在判断中继未撤销。
