# 6PE

## 拓扑、用途与前提

通过IPv4 MPLS承载交换全局IPv6路由，无VPN-instance、RD或RT。两台PE共享AS65000，BGP通过IPv4环回建立IPv6 labeled-unicast邻居。示例为双PE直连的最小6PE，不外推为多P节点或跨AS测试。

~~~text
PE2 Ethernet1 198.19.23.2/24 ── 198.19.23.3/24 Ethernet0 PE3
LoopBack62 10.255.62.2/32          10.255.62.3/32
           2001:db8:620::2/128     2001:db8:620::3/128
~~~

接口已由VPP管理，LCP和FRR可用。LoopBack编号范围0–255，本例用62；IPv6地址中的620不属于接口编号。先用IPv4路由使两端LSR-ID可达，再确认LDP会话Operational。

## PE2

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet1
 ip address 198.19.23.2 255.255.255.0
#
interface LoopBack 62
 ipv6 enable
 ip address 10.255.62.2 255.255.255.255
 ipv6 address 2001:db8:620::2 128
#
ip route-static 10.255.62.3 255.255.255.255 198.19.23.3
mpls lsr-id 10.255.62.2
mpls
#
mpls ldp
interface Ethernet1
 mpls
 mpls ldp
#
~~~

CLI 操作：

~~~text
commit
~~~

配置清单：

~~~text
bgp 65000
 router-id 2.2.2.2
 peer 10.255.62.3 as-number 65000
 peer 10.255.62.3 connect-interface LoopBack 62
 ipv6-family unicast
  peer 10.255.62.3 enable
  peer 10.255.62.3 label-route-capability
  network 2001:db8:620::2 128
#
~~~

CLI 操作：

~~~text
commit
~~~

## PE3

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ip address 198.19.23.3 255.255.255.0
#
interface LoopBack 62
 ipv6 enable
 ip address 10.255.62.3 255.255.255.255
 ipv6 address 2001:db8:620::3 128
#
ip route-static 10.255.62.2 255.255.255.255 198.19.23.2
mpls lsr-id 10.255.62.3
mpls
#
mpls ldp
interface Ethernet0
 mpls
 mpls ldp
#
~~~

CLI 操作：

~~~text
commit
~~~

配置清单：

~~~text
bgp 65000
 router-id 3.3.3.3
 peer 10.255.62.2 as-number 65000
 peer 10.255.62.2 connect-interface LoopBack 62
 ipv6-family unicast
  peer 10.255.62.2 enable
  peer 10.255.62.2 label-route-capability
  network 2001:db8:620::3 128
#
~~~

CLI 操作：

~~~text
commit
~~~

系统视图的mpls会进入MPLS视图，需quit后才能输入全局mpls ldp。接口视图的mpls则只启用该接口转发，不进入同一视图。

## 查询顺序

~~~text
display mpls interface
display mpls ldp interface
display mpls ldp peer
display mpls ldp binding
display bgp ipv6 peer
display ipv6 routing-table 2001:db8:620::3 128 verbose
display ipv6 fib
display mpls forwarding-table
display health
~~~

PE3把目标替换为::2。先确认协议会话和前缀，再发起流量；系统ready不表示BGP邻居已经建立。display bgp ipv6 peer汇总IPv6 unicast与6PE labeled-unicast会话，同一邻居只列一行；使用display bgp ipv6 peer对端IPv4地址 verbose可核对6PE会话和地址族计数。默认display bgp peer仅查询IPv4 unicast，不能用于替代6PE状态查询。

示例输出：

~~~text
Peer ID          Address-Family  Transport Address     State
10.255.62.3      ipv4            10.255.62.3           OPERATIONAL
Total: 1
~~~

## 标签行为

6PE 使用 IPv4 承载 MPLS，业务载荷为 IPv6。设备为本地 IPv6 前缀使用 explicit-null 标签 2，以保留载荷地址族信息；用户不需要额外创建标签策略。查看 IPv6 FIB 和 MPLS 实际路径，不要只以 BGP RIB 中的 Label 字段判断转发。

## 流量与撤销

在路由、标签和会话都就绪后：

~~~text
ping ipv6 -c 3 -a 2001:db8:620::2 2001:db8:620::3
~~~

两端应可达。撤销承载邻居后远端前缀应消失；重新配置邻居与 label-route-capability 后，已有本地 network 前缀应重新发布，无需删除并重加 network。

示例输出：

~~~text
3 packets transmitted, 3 received, 0% packet loss
~~~

线侧抓包辅助确认实际封装：

~~~text
MPLS (label 2, tc 0, [S], ttl 64) IP6 2001:db8:620::2 > 2001:db8:620::3: ICMP6, echo request
MPLS (label 2, tc 0, [S], ttl 63) IP6 2001:db8:620::3 > 2001:db8:620::2: ICMP6, echo reply
~~~

重建数据面后先确认会话、路由与标签恢复，再发起探测。

撤销首先删除本例新增的6PE承载邻居及network，保留共享EVPN邻居：

~~~text
bgp 65000
 undo peer 10.255.62.3
 ipv6-family unicast
  undo network 2001:db8:620::2 128
#
~~~

CLI 操作：

~~~text
commit
display ipv6 routing-table 2001:db8:620::3 128
~~~

PE3反向撤销。两端示例输出均变为Destinations : 0、Routes : 0。再撤销本例独占的MPLS和环回，PE2如下，PE3交换地址：

~~~text
interface Ethernet1
 undo mpls ldp
 undo mpls
#
undo mpls ldp
undo mpls
undo mpls lsr-id
undo interface LoopBack 62
undo ip route-static 10.255.62.3 255.255.255.255 198.19.23.3
~~~

CLI 操作：

~~~text
commit
display mpls ldp peer
display mpls interface
~~~

已有其他 MPLS 业务时不得关闭共享全局功能。完整拆除后，专用 LDP 会话、MPLS 接口和路由应不再存在，健康恢复 ready；核对后 save。

[功能说明](../../operator/6pe.md) · [LDP](../../operator/ldp.md)
