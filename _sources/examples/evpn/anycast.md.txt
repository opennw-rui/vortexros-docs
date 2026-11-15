# Anycast 网关

在已有 EVPN 桥域上增加网关。先完成[L2VPN](l2vpn.md)，实验改用 BD450/VNI10450，CE 位于198.18.145.0/24；这里不重复整份二层基础配置。

## 配置

~~~text
system-view
interface Vbdif 450
 mac-address 0200-0000-0450
 ip address 198.18.145.1 255.255.255.0
 vxlan anycast-gateway enable
quit
commit
display interface Vbdif450
display bgp evpn all routing-table
~~~

实际 Linux/VPP MAC 均为02:00:00:00:04:50，FRR VNI 回读为 `Advertise-gw-macip: Yes`，Type-2 路由键含：

~~~text
0:48:0200-0000-0450:32:198.18.145.1
~~~

CE 旧缓存未更新时首轮3发0收；更新后 CE→网关、网关→CE 均3/3，不能省略缓存影响。

## 撤销

~~~text
system-view
interface Vbdif 450
 undo vxlan anycast-gateway enable
quit
commit
~~~

实测变为 `Advertise-gw-macip: No`，网关通告撤销；显式 MAC/IP 保留。需要清理接口时先解除其他引用。只有一个活动网关，未据此证明双活动网关漫游。

[功能与影响](../../operator/evpn/anycast.md)
