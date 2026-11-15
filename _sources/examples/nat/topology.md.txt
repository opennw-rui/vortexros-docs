# 基础拓扑

三台设备均运行 VortexROS。P1 是 NAT 网关，P3 是内侧设备，P2 是外侧设备。各案例使用独立策略，同一接口同一方向不要同时绑定多份示例。

~~~text
P3 Ethernet0 ── Ethernet1 P1 Ethernet0 ── Ethernet0 P2
198.18.11.2/24    198.18.11.1/24
                             198.19.80.1/30    198.19.80.2/30
映射地址: 198.19.81.1、198.19.81.2，经 P1 返回
~~~

## P1

~~~text
system-view
interface Ethernet1
 ip address 198.18.11.1 255.255.255.0
quit
interface Ethernet0
 ip address 198.19.80.1 255.255.255.252
quit
commit
~~~

## P2

~~~text
system-view
interface Ethernet0
 ip address 198.19.80.2 255.255.255.252
quit
ip route-static 198.19.81.0 255.255.255.0 198.19.80.1
ip route-static 198.18.11.0 255.255.255.0 198.19.80.1
commit
~~~

## P3

~~~text
system-view
interface Ethernet0
 ip address 198.18.11.2 255.255.255.0
quit
ip route-static 0.0.0.0 0.0.0.0 198.18.11.1
commit
~~~

## 基础验证

在 P3 执行 ping -a 198.18.11.2 -c 3 198.19.80.2，P2 反向 Ping 198.18.11.2。启用 NAT 前先确认普通路由可达，再按案例查询转换后的会话和策略统计。

ICMP 探测用于检查地址转换及往返路径；不能证明 TCP/UDP 端口映射、会话上限或吞吐。需要发布 UDP 服务时，可使用 [WireGuard](../wireguard.md) 中由 VortexROS 承载的 UDP 服务，再按 DNAT 页配置端口映射，无需在网络设备上手工运行服务脚本。

## 拆除基础拓扑

先撤销各案例的接口策略及对象，再在 P2 撤销两条静态路由，在 P3 撤销默认路由，各设备在本例接口执行 undo ip address、commit。保留其他业务共用的地址和路由。需要持久化时在创建及撤销后分别执行 save。
