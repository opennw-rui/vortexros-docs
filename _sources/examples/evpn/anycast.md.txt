# Anycast 网关

先完整配置 [L2VPN](l2vpn.md) 的 VLAN/BD 101、VNI 5010 及客户接入，再为该桥域增加网关 192.0.2.254/24。两端客户地址为 .1、.3，网关使用不同地址。

## 配置

~~~text
system-view
interface Vbdif 101
 mac-address 0200-0000-0101
 ip address 192.0.2.254 255.255.255.0
 vxlan anycast-gateway enable
quit
commit
display interface Vbdif101
display bgp evpn all routing-table
~~~

网关 MAC 应与配置一致，并通告相应的网关 MAC/IP Type-2。示例路由键：

~~~text
0:48:0200-0000-0101:32:192.0.2.254
~~~

更换网关 MAC 会影响客户端 ARP/ND 缓存，应在邻居更新后检查 CE 到网关及网关到 CE 的可达性。

## 撤销

~~~text
system-view
interface Vbdif 101
 undo vxlan anycast-gateway enable
quit
commit
~~~

开关撤销后，不再通告网关 MAC/IP；显式 MAC 和 IP 保留。需要删除网关接口时先解除引用。

[功能与影响](../../operator/evpn/anycast.md)
