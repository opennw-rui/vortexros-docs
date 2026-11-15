# 6PE

## 拓扑、用途与前提

通过IPv4 MPLS承载交换全局IPv6路由，无VPN-instance、RD或RT。两台PE共享AS65000，BGP通过IPv4环回建立IPv6 labeled-unicast邻居。实验为双PE直连的最小6PE，不外推为多P节点或跨AS测试。

~~~text
PE2 host-p2e23 198.19.23.2/24 ── 198.19.23.3/24 host-p3e23 PE3
LoopBack62 10.255.62.2/32          10.255.62.3/32
           2001:db8:620::2/128     2001:db8:620::3/128
~~~

接口已由VPP管理，LCP和FRR可用。LoopBack编号范围0–255，本例用62；IPv6地址中的620不属于接口编号。先用IPv4路由使两端LSR-ID可达，再确认LDP会话Operational。

## PE2

~~~text
system-view
interface host-p2e23
 ip address 198.19.23.2 255.255.255.0
quit
interface LoopBack 62
 ip address 10.255.62.2 255.255.255.255
 ipv6 address 2001:db8:620::2 128
quit
ip route-static 10.255.62.3 255.255.255.255 198.19.23.3
mpls lsr-id 10.255.62.2
mpls
quit
mpls ldp
interface host-p2e23
 mpls
 mpls ldp
quit
commit
bgp 65000
 router-id 2.2.2.2
 peer 10.255.62.3 as-number 65000
 peer 10.255.62.3 connect-interface LoopBack 62
 ipv6-family unicast
  peer 10.255.62.3 enable
  peer 10.255.62.3 label-route-capability
  network 2001:db8:620::2 128
 quit
quit
commit
~~~

## PE3

~~~text
system-view
interface host-p3e23
 ip address 198.19.23.3 255.255.255.0
quit
interface LoopBack 62
 ip address 10.255.62.3 255.255.255.255
 ipv6 address 2001:db8:620::3 128
quit
ip route-static 10.255.62.2 255.255.255.255 198.19.23.2
mpls lsr-id 10.255.62.3
mpls
quit
mpls ldp
interface host-p3e23
 mpls
 mpls ldp
quit
commit
bgp 65000
 router-id 3.3.3.3
 peer 10.255.62.2 as-number 65000
 peer 10.255.62.2 connect-interface LoopBack 62
 ipv6-family unicast
  peer 10.255.62.2 enable
  peer 10.255.62.2 label-route-capability
  network 2001:db8:620::3 128
 quit
quit
commit
~~~

系统视图的mpls会进入MPLS视图，需quit后才能输入全局mpls ldp。接口视图的mpls则只启用该接口转发，不进入同一视图。

## 查询顺序

~~~text
display mpls interface
display mpls ldp interface
display mpls ldp peer
display mpls ldp binding
display bgp peer
display ipv6 routing-table 2001:db8:620::3 128 verbose
display ipv6 fib
display mpls forwarding-table
display health
~~~

PE3把目标替换为::2。先确认协议会话和前缀，再发起流量；系统ready不表示BGP邻居已经建立。当前display bgp ipv6 peer查看IPv6 unicast地址族，6PE的IPv4承载会话使用display bgp peer；辅助核对LU标签时可由运维读取FRR对应labeled-unicast状态，不能把原生查询冒称产品另有一条CLI。

真实LDP查询节选：

~~~text
Peer ID          Address-Family  Transport Address     State
10.255.62.3      ipv4            10.255.62.3           OPERATIONAL
Total: 1
~~~

## 标签策略与修正依据

FRR缺省为本地前缀通告implicit-null标签3。初次真实实验中LU邻居已建立、IPv6前缀也存在，但IPv4-only承载未保留IPv6载荷标签，两向探测0/3。改用FRR现成的IPv6 explicit-null标签2并重建本地通告后，组件对照恢复连通。

控制层按6PE邻居意图生成该后端策略，不新增用户配置项，不修改FRR/VPP源码；最后一个6PE邻居撤销时恢复。启用时已有IPv6本地通告会在现有增量流程中刷新；冷接管旧implicit-null状态时先撤销相关本地起源再按新策略回放。正常未改变标签模式的编辑不重复刷新。

[FRR官方标签策略](https://docs.frrouting.org/en/latest/bgp.html#labeled-unicast)说明缺省implicit-null和现有显式空标签选项。RIB摘要的Label字段不能替代实际路径标签栈，应结合FIB/MPLS回读和线侧报文。

## 流量与撤销

在路由、标签和会话都就绪后：

~~~text
ping ipv6 -c 3 -a 2001:db8:620::2 2001:db8:620::3
~~~

最终控制层生成后端策略并冷回放，两端真实CLI均为3发3收；在线撤销PE2承载邻居后，PE3对应前缀消失。保留本地network不变，重新通过CLI配置该邻居和label-route-capability，PE3重新学到标签2，PE2探测再次3/3。这验证了已有通告的刷新，而不只验证首次配置。

真实CLI输出节选：

~~~text
3 packets transmitted, 3 received, 0% packet loss
~~~

线侧抓包辅助确认实际封装：

~~~text
MPLS (label 2, tc 0, [S], ttl 64) IP6 2001:db8:620::2 > 2001:db8:620::3: ICMP6, echo request
MPLS (label 2, tc 0, [S], ttl 63) IP6 2001:db8:620::3 > 2001:db8:620::2: ICMP6, echo reply
~~~

初次冷恢复后协议尚未建立时的失败探测保留在原始记录中；上面的成功发生在实际路由和标签就绪后，不用固定延时伪装就绪。

撤销首先删除本例新增的6PE承载邻居及network，保留共享EVPN邻居：

~~~text
bgp 65000
 undo peer 10.255.62.3
 ipv6-family unicast
  undo network 2001:db8:620::2 128
 quit
quit
commit
display ipv6 routing-table 2001:db8:620::3 128
~~~

PE3反向撤销。两端真实查询均变为Destinations : 0、Routes : 0。再撤销本例独占的MPLS和环回，PE2如下，PE3交换地址：

~~~text
interface host-p2e23
 undo mpls ldp
 undo mpls
quit
undo mpls ldp
undo mpls
undo mpls lsr-id
undo interface LoopBack 62
undo ip route-static 10.255.62.3 255.255.255.255 198.19.23.3
commit
display mpls ldp peer
display mpls interface
~~~

已有其他MPLS业务时不得关闭共享全局功能。最终LDP会话和MPLS接口均Total: 0。本轮原撤销触发LCP在最后一条MPLS标签路由消失时调用IP MFIB释放，VPP崩溃于mfib_table_unlock。MPLS表没有IP组播表，修正将这类表的创建/释放限定在IP协议；未改通用MFIB实现。隔离实例加载可追溯的局部修复插件后，重复原CLI撤销成功，健康ready、代号2/2、零告警，VPP PID102391保持不变。旧崩溃日志和修后插件校验保留，修后结果不混同于自动重启恢复。提交并检查后save。

[功能说明](../../operator/6pe.md) · [LDP](../../operator/ldp.md)

## 0.29-dev run1最终包核对

同一最终.run安装后，PE2/PE3均运行包内daemon和VPP26.10.7。真实CLI中LDP Operational，远端标签2、实际路径encap mpls2，两向各3/3。按本页步骤撤销全部6PE对象，目标路由和LDP均0、健康ready、零告警；VPP PID116488/116478不变。最后标签路由撤销已用正式包重新核对，未用自动重启作为通过依据。

已有network不变时在线启用标签策略，以及控制进程冷接管旧策略的定向证据沿用前面的同源验证，没有重复执行。包身份和安装事务见[最终包记录](../../release/cli-validation.md)。
