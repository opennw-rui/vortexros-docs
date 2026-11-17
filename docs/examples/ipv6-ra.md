# IPv6 自动配置

## 拓扑

客户端和网关均使用 VortexROS，Ethernet0 直连：

~~~text
C1 Ethernet0 ───────── R1 Ethernet0
SLAAC / DHCPv6          2001:db8:193::1/64
RA 默认路由             通告 2001:db8:193::/64
~~~

本例先验证 RA/SLAAC，再说明与 DHCPv6 同时获取地址的效果。RA 的 M/O 标志只是告诉对端可用的获取方式，不会替代对端的客户端配置。

## R1：通告前缀和默认路由

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ipv6 enable
 ipv6 address 2001:db8:193::1 64
 ipv6 nd ra prefix 2001:db8:193:: 64 3600 1800
 undo ipv6 nd ra halt
#
~~~

CLI 操作：

~~~text
commit
~~~

路由器生存期默认1800秒，不进入配置。前缀3600/1800分别是有效寿命和首选寿命，单位秒。

## C1：接收 SLAAC 与默认路由

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ipv6 enable
 ipv6 address auto global default
#
~~~

CLI 操作：

~~~text
commit
~~~

取得地址后检查 DAD 已完成，再使用实际获得的地址探测。自动地址不写成静态配置；保存的是获取方式，重新启动后重新学习。

~~~text
display ipv6 interface Ethernet0
display ipv6 interface brief
display ipv6 routing-table
ping ipv6 -c 3 2001:db8:193::1
~~~

实际验证所用接口的稳定地址后缀为 40aa:6bff:feb8:5155。以下按拓扑统一接口名；地址后缀随MAC变化：

~~~text
Ethernet0 current state : UP
IPv6 protocol current state : UP
  IPv6 configured      : enabled
  VPN instance         : default
  IPv6 addresses (actual):
    2001:db8:193:0:40aa:6bff:feb8:5155/64
    fe80::40aa:6bff:feb8:5155/64
  SLAAC configured     : enabled
  RA default learning  : enabled
  Temporary addresses  : disabled
~~~

对端回读取得 RA 默认路由；独立报文记录确认 IPv6 Hop Limit 255、前缀A/L标志、3600/1800秒寿命及1800秒路由器寿命。默认路由不是DHCPv6分配的。

## 与 DHCPv6 同时使用

按[DHCPv6案例](dhcpv6.md)配置服务器及客户端，可同时存在稳定SLAAC /64和DHCPv6 IA_NA /128。网关可增加：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ipv6 nd autoconfig managed-address-flag
 ipv6 nd autoconfig other-flag
#
~~~

CLI 操作：

~~~text
commit
~~~

实际抓包确认M/O均置位，客户端同时保留稳定SLAAC与DHCPv6地址，没有生成临时隐私地址。需要单一全局地址来源时，见[地址选择](../operator/ipv6-autoconfig/address-selection.md)，不要用固定地址总数代替获取方式配置。

## 分别撤销

C1只保留SLAAC，关闭默认路由学习：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo ipv6 nd ra default-route enable
#
~~~

CLI 操作：

~~~text
commit
~~~

C1切换为只学习默认路由，不再生成SLAAC地址：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo ipv6 address auto global
 ipv6 nd ra default-route enable
#
~~~

CLI 操作：

~~~text
commit
~~~

实际验证中稳定SLAAC地址被移除，独立DHCPv6地址和链路本地地址保留。完全停止RA接收使用：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo ipv6 address auto global default
#
~~~

CLI 操作：

~~~text
commit
~~~

## 通告标志与停止发送

R1通告前缀但不允许SLAAC、不声明on-link，同时不提供默认网关：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ipv6 nd ra prefix 2001:db8:193:: 64 3600 1800 no-autoconfig off-link
 ipv6 nd ra lifetime 0
#
~~~

CLI 操作：

~~~text
commit
~~~

实际RA报文确认：router lifetime0，前缀A/L标志均清除，仍保留3600/1800秒前缀寿命。恢复默认生存期和普通前缀后再查询对端：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo ipv6 nd ra lifetime
 ipv6 nd ra prefix 2001:db8:193:: 64 3600 1800
#
~~~

CLI 操作：

~~~text
commit
~~~

停止发送并清理本例显式参数：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ipv6 nd ra halt
 undo ipv6 nd ra prefix
 undo ipv6 nd autoconfig managed-address-flag
 undo ipv6 nd autoconfig other-flag
#
~~~

CLI 操作：

~~~text
commit
~~~

实际停止发送后，发送RS并观察215秒没有收到RA。远端已有地址仍按此前寿命失效，不能把“停止发送”解释成强制删除远端地址。完成查询后在两端save；删除接口IPv6启用前，先撤销仍使用它的地址和服务依赖。

[接口启用](../operator/ipv6-autoconfig/interface.md) · [RA参数](../operator/ipv6-autoconfig/advertisements.md)


## 启用、关闭与保存恢复

接口仅配置 IPv6 enable、没有静态地址或自动获取方式时，可以保持 IPv6 Protocol Down。只需要链路本地地址时配置：

~~~text
interface Ethernet0
 ipv6 enable
 ipv6 address auto link-local
#
~~~

提交后，实际显示只有 fe80::/64 地址，SLAAC 和 RA 默认路由学习均为 disabled；撤销该获取方式后恢复 unassigned。关闭接口 IPv6 前，应先撤销该接口的 IPv6 地址和依赖服务。

保存双方配置后，网关通过 reset service vpp 重启并恢复了静态地址、RA 前缀和900秒路由器生存期。客户端收到新的 RA，重新学习默认路由；指定稳定全局地址的探测为2发2收。接口重建后的首次探测可能等待邻居解析，本例首次2发1收，邻居完成后2发2收，不保证重启期间零丢包。缓存的旧路由器地址在原通告寿命到期前可能仍可见。

若要独立确认各项控制的效果：

| 配置变化 | 对端实际结果 |
| --- | --- |
| 撤销 auto global，保留默认路由学习 | 无 SLAAC 全局地址，收到 RA 后仍学习默认路由 |
| 开启 SLAAC，关闭默认路由学习 | 生成稳定全局地址和前缀路由，无 RA 默认路由 |
| 前缀使用 no-autoconfig off-link | RA 中 A/L 均为0，不生成该前缀的 SLAAC 地址或链路路由 |
| 路由器生存期改为0 | 默认路由撤销，仍有效的 SLAAC 地址保留 |
| ra halt | 收到路由请求后不再发送 RA；已学习状态按原寿命老化 |
| 撤销 auto global default | 清除对应自动地址和默认路由；没有其他地址来源时显示 unassigned |
