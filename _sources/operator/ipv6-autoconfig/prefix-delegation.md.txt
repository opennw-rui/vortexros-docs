# 前缀委派

DHCPv6 IA_PD 为下游路由器分配一个前缀；它与为接口分配单个地址的 IA_NA 是不同对象。收到前缀后，需要在下游接口引用它，才会生成该接口的地址和直连路由。DHCPv6 不提供默认网关，访问更远网络还需配置路由或学习 RA 默认路由，并确保上游有返回路由。

## 拓扑与配置

上游路由器 S 的 Ethernet0 连接路由器 R 的 Ethernet0；R 的 Ethernet1 连接下游验证设备 C 的 Ethernet0。三台设备均使用 VortexROS。S 使用 2001:db8:229::1/64，并从 2001:db8:329::/48 委派 /64。

S 的配置清单：

~~~text
enable dhcp server
dhcpv6 pool D1-PD
 address prefix 2001:db8:229::/64 life-time 300 150
 prefix-delegation 2001:db8:329::/48 64 life-time 300 150
#
interface Ethernet0
 ipv6 enable
 ipv6 address 2001:db8:229::1 64
 dhcpv6 server D1-PD
#
~~~

R 同时请求上联地址和委派前缀：

~~~text
interface Ethernet0
 ipv6 enable
 ipv6 address auto dhcp
 dhcpv6 client pd D1-PD-CLIENT
#
interface Ethernet1
 ipv6 enable
 ipv6 address dhcpv6-prefix D1-PD-CLIENT ::1/64
#
~~~

分别 commit。后缀 ::1/64 表示在收到的前缀内生成下联地址，不代表委派值固定不变。先读取 R 的实际委派结果，再为 C 配置同一 /64 内另一个地址。

## 查询与实际结果

R 执行：

~~~text
display dhcpv6 client interface Ethernet0
display dhcpv6 client prefix name D1-PD-CLIENT
display ipv6 interface Ethernet1
~~~

一次实际查询中，命名前缀 D1-PD-CLIENT 为 running，委派结果是 2001:db8:329:3::/64，下联地址为 2001:db8:329:3::1/64。C 配置 2001:db8:329:3::2/64 后，两个方向各探测3/3。

~~~text
interface Ethernet0
 ipv6 enable
 ipv6 address 2001:db8:329:3::2 64
#
~~~

上述 C 地址是该次结果；不要在取得不同前缀时直接照抄。重新申请后实际前缀曾变为 2001:db8:329:5::/64，R 的派生地址随之更新，C 也需要使用当前前缀。该示例验证前缀分配和下游链路，不代替更远网络的路由验收。

## 续租

在 R 的上联接口视图执行：

~~~text
dhcpv6 client renew
~~~

这是即时操作，不需要 commit。查询客户端状态和租期确认续租结果；续租不等于强制获取新前缀。实际验证中客户端保持原运行进程，重新取得地址和前缀租期。

## 撤销

先撤销下游引用，再撤销上联请求：

~~~text
interface Ethernet1
 undo ipv6 address dhcpv6-prefix D1-PD-CLIENT
#
interface Ethernet0
 undo dhcpv6 client pd
#
~~~

commit 后，命名前缀查询为空，下联派生地址和相应直连路由消失。单独撤销 PD 不会删除同接口仍启用的 IA_NA 或 SLAAC 地址。要一并停止地址请求，在上联接口执行 undo ipv6 address auto dhcp。

拆除整个示例时，S 先撤销接口上的 dhcpv6 server，再删除 D1-PD 池；C 删除本例静态地址。共享的其他池和 DHCP 业务保留。

[组合地址获取](combined.md) · [DHCPv6 双端案例](../../examples/dhcpv6.md)
