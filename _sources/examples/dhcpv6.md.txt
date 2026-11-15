# DHCPv6 地址与前缀

## 拓扑

~~~text
P1：客户端                                  P2：服务端
host-p1q12 ─────────────────────────────── host-p2q12
  IA_NA 地址                                2001:db8:14::1/64
  请求 PD14                                 地址池 CLI6
  LoopBack96 使用委派前缀                    委派 /48 中的 /64
~~~

两端使用隔离二层链路、VPP 和 LCP。本例同时验证地址分配、前缀委派、续租和撤销。
接口名称是实验环境的真实名称；设备上请换成实际接口。

DHCPv6 不提供默认网关。本例显式配置到服务端网段的路由，以及服务端到委派前缀的回程路由。
没有配置 RA，也不会自动给下游终端发布 RA。

## 服务端配置

在 P2 上配置服务端地址和地址池，再把接口绑定到池：

~~~text
system-view
enable dhcp server
dhcpv6 pool CLI6
 address prefix 2001:db8:14::/64 life-time 3600 1800
 prefix-delegation 2001:db8:114::/48 64 life-time 3600 1800
 dns-server 2001:db8::53
 dns-domain-name cli6.example
 information-refresh 900
 excluded-address 2001:db8:14::100 2001:db8:14::110
 quit
interface host-p2q12
 ipv6 address 2001:db8:14::1 64
 dhcpv6 server CLI6
 quit
commit
~~~

有效期为 3600 秒，首选期为 1800 秒。排除范围不参与普通地址分配。
委派池将 /48 划成 /64；它与地址池的 /64 是两个独立范围。

## 客户端配置

在 P1 上请求地址和委派前缀，并把前缀用于一个下游三层接口：

~~~text
system-view
interface host-p1q12
 ipv6 address auto dhcp hint 2001:db8:14::14
 dhcpv6 client pd PD14
 quit
interface LoopBack96
 ipv6 address dhcpv6-prefix PD14 ::1/64
 quit
commit
~~~

hint 是请求地址，不保证服务端一定分配该地址。PD14 是本地引用名称，不是固定的委派前缀。
实测获得地址 2001:db8:14::14/128、委派前缀 2001:db8:114:1::/64；
LoopBack96 因而得到 2001:db8:114:1::1/64。

## 地址、租约和连通性

P1 查询客户端及下游接口：

~~~text
display dhcpv6 client interface host-p1q12
display interface LoopBack96
~~~

客户端实际输出节选：

~~~text
Interface   Address-Family  Role    Pool/Servers  VPN-Instance  State    Address                 Delegated-Prefix
host-p1q12  IPv6            client  PD14          default       running  2001:db8:14::14/128      2001:db8:114:1::/64
~~~

P2 查询池及两种租约：

~~~text
display dhcpv6 pool name CLI6 verbose
~~~

实际输出节选；DUID、IAID、剩余时间和实际分配前缀随客户端而变：

~~~text
Pool name  VPN-Instance  Address-prefixes  PD-prefixes  DNS  Used
CLI6       default       1                 1            1    2

Lease 0
  IPv6 address/prefix : 2001:db8:114:1::/64
  Lease type          : IA_PD
  VPN-Instance        : default
  Valid lifetime      : 3600s

Lease 1
  IPv6 address/prefix : 2001:db8:14::14/128
  Lease type          : IA_NA
  VPN-Instance        : default
  Valid lifetime      : 3600s
Total: 2
~~~

先在 P2 的接口详细信息中取得实际链路本地地址。本次为 fe80::f08f:7cff:fe2a:2ab8，
其他设备应替换这个值。P1 配置同链路路由：

~~~text
ipv6 route-static 2001:db8:14:: 64 host-p1q12 fe80::f08f:7cff:fe2a:2ab8
commit
ping ipv6 -a 2001:db8:14::14 -c 3 2001:db8:14::1
~~~

P2 按实际获得的委派前缀配置回程路由：

~~~text
ipv6 route-static 2001:db8:114:1:: 64 host-p2q12 2001:db8:14::14
commit
ping ipv6 -c 3 2001:db8:114:1::1
~~~

两项实际结果均为：

~~~text
3 packets transmitted, 3 received, 0% packet loss
~~~

这验证了客户端地址和下游派生地址的往返连通，不代表已经验证真实终端的 RA 或自动回程发布。
生产环境若委派前缀会变化，应使用适用的路由机制，不能固定套用本例的实验前缀。

## 续租与信息请求

P1 接口视图中执行续租；这是运行命令，不需要 commit：

~~~text
interface host-p1q12
 dhcpv6 client renew
~~~

实测终端返回：

~~~text
Info: DHCPv6 renewal requested on host-p1q12.
~~~

独立抓包确认了 Renew/Reply，并保留同一 IA_NA 和 IA_PD。

只获取 DNS 等选项时，先撤销下游引用和有状态请求，再改成信息请求：

~~~text
quit
interface LoopBack96
 undo ipv6 address dhcpv6-prefix PD14
 quit
interface host-p1q12
 undo dhcpv6 client pd
 undo ipv6 address auto dhcp
 dhcpv6 client information-request
 quit
commit
display dhcpv6 client interface host-p1q12
~~~

实测地址和委派前缀列均为 -，原客户端和下游全局地址已移除。
实际 Information-request/Reply 包含 DNS 2001:db8::53 和搜索域 cli6.example。
信息请求不会生成 IPv6 地址或网关。

## 空池查询

空租约数据库是正常状态。实测空实例返回成功的 Total: 0；
同地址族另一个实例有两条租约时，仍能单独查询到那两条租约。

~~~text
display dhcpv6 pool name CLI6-EMPTY verbose
~~~

~~~text
Pool name   VPN-Instance  Address-prefixes  PD-prefixes  DNS  Used
CLI6-EMPTY  DHCP-EMPTY    1                 0            0    0
Total: 0
~~~

CLI6-EMPTY 是另建于 DHCP-EMPTY VPN 实例的实验池，不是前面配置自动生成的池。
停止客户端并不要求服务端立即删除历史租约；不能仅凭租约仍在判断客户端撤销失败。

## 撤销与保存

P1 撤销信息请求和本例路由：

~~~text
interface host-p1q12
 undo dhcpv6 client information-request
 quit
undo ipv6 route-static 2001:db8:14:: 64 host-p1q12 fe80::f08f:7cff:fe2a:2ab8
commit
display dhcpv6 client interface host-p1q12
~~~

若尚未切换到信息请求，应先执行上一节撤销 IA_NA、PD 和下游引用的命令。
实测撤销后客户端查询只剩表头，进程停止，两个接口不再保留本例的全局地址。

P2 撤销接口绑定、地址、回程路由和池：

~~~text
interface host-p2q12
 undo dhcpv6 server
 undo ipv6 address 2001:db8:14::1 64
 quit
undo ipv6 route-static 2001:db8:114:1:: 64 host-p2q12 2001:db8:14::14
undo dhcpv6 pool CLI6
commit
display dhcp service verbose
~~~

本轮实际撤销了 IPv6 服务实例，同时保留原有 IPv4 服务实例运行。
全局 DHCP server 开关只在其他池均不再使用时关闭。

需要跨重启保留配置时，两端在 commit 成功后执行 save。Saved 保存请求意图，
动态地址和委派前缀需要客户端重新取得，不能当作固定地址写入启动配置。

[DHCP 配置指南](../operator/dhcp.md) · [RA 与 SLAAC](../operator/ipv6-autoconfig.md)
