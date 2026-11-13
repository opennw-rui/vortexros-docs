# DHCPv6 地址池

## 拓扑

~~~text
P1（Kea 服务端）                         P2（DHCPv6 客户端）
host-p1b12 2001:db8:252:10::1/120 ─── host-p2b12
地址池 LAB-V6                            通过 IA_NA 获取 /128 地址
~~~

两端使用隔离二层链路，VPP 和 LCP 已就绪，没有其他 DHCPv6 服务端。实验只做有状态地址分配，不发布 IPv6 默认路由或委派前缀。

## 配置 P1

先提交接口地址，再绑定池。服务端自身地址从池内排除。

~~~text
system-view
interface host-p1b12
 ipv6 address 2001:db8:252:10::1 120
 quit
commit
enable dhcp server
dhcpv6 pool LAB-V6
 address prefix 2001:db8:252:10::/120 life-time 3600 1800
 excluded-address 2001:db8:252:10::1
 quit
interface host-p1b12
 dhcpv6 server LAB-V6
 quit
commit
~~~

`enable dhcp server` 是全局服务端开关。已有 DHCP 服务的设备应保留原开关状态。租约有效期 3600 秒，首选期 1800 秒。

## 配置 P2

先建立接口配置，再启用客户端。实验拓扑使用 MTU 1496，实际设备使用该链路的既定 MTU。由于没有 RA，显式安装指向链路的 /120 路由，让客户端可以联系同链路服务端；这不是默认路由。

~~~text
system-view
interface host-p2b12
 mtu 1496
 quit
commit
interface host-p2b12
 ipv6 address auto dhcp
 quit
ipv6 route-static 2001:db8:252:10:: 120 host-p2b12
commit
~~~

## 验证

**P1：** `display dhcp service verbose`。实验中 IPv6 服务实例的 `Running` 与 `Ready` 都为 `true`，子网数为 1。

**P2：**

~~~text
display dhcpv6 client interface host-p2b12
ping ipv6 -n -c 3 -t 1000 2001:db8:252:10::1
~~~

实际输出节选：

~~~text
Interface   Address-Family  Role    Pool/Servers  VPN-Instance  State    Address                 Delegated-Prefix
host-p2b12  IPv6            client                default       running  2001:db8:252:10::3/128  -

--- 2001:db8:252:10::1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
~~~

在 P2 的接口视图执行 `dhcpv6 client renew`，再查询客户端，实测地址仍为 `2001:db8:252:10::3/128`。续租是运行命令，不需要提交。

**当前版本限制：** Debug 5 搭配 Kea 3.0.3 时，服务端 `display ipv6 pool name LAB-V6 used` 的查询实测返回以下错误片段。服务端就绪、客户端获得地址和 Ping 成功均已单独验证；服务端租约明细查询没有通过。

~~~text
json: cannot unmarshal string into Go struct field keaLeaseArguments.leases.0.type of type uint8
~~~

## 撤销

**P2：**

~~~text
system-view
undo ipv6 route-static 2001:db8:252:10:: 120 host-p2b12
interface host-p2b12
 undo ipv6 address auto dhcp
 quit
commit
display dhcpv6 client interface host-p2b12
~~~

**P1：**

~~~text
system-view
interface host-p1b12
 undo dhcpv6 server
 undo ipv6 address 2001:db8:252:10::1 120
 quit
undo dhcpv6 pool LAB-V6
commit
~~~

实测撤销后，P2 的客户端查询只剩表头，客户端进程已停止。全局服务端只在确认其他池均不依赖时才用 `undo enable dhcp server` 关闭；若实验前调整过接口 MTU，再恢复原值。

[DHCP 配置指南](../operator/dhcp.md) · [RA 与 SLAAC](../operator/ipv6-autoconfig.md)
