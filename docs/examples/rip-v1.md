# RIPv1 聚合链路


RIPv1 使用有类路由通告，不携带前缀长度。以下独立示例在 VPN 实例中使用不同的 B 类网络，避免把同一有类网络划成无法正确通告的非连续子网。新部署通常选择 RIPv2；仅在互通对端要求 RIPv1 时使用本例。

两台设备以三根 Ethernet 链路组成 Eth-Trunk12。P1 的 LoopBack246 为172.30.0.1/16，P2 的 LoopBack247 为172.31.0.2/16；聚合地址分别为198.19.198.1/24和198.19.198.2/24。

P1：

~~~text
ip vpn-instance D1-V1
 ipv4-family
#
interface Eth-Trunk 12
 mode lacp-static
 trunkport Ethernet0 to Ethernet2
 ip binding vpn-instance D1-V1
 ip address 198.19.198.1 24
#
interface LoopBack 246
 ip binding vpn-instance D1-V1
 ip address 172.30.0.1 16
#
rip 96 vpn-instance D1-V1
 version 1
 network 198.19.198.0
 network 172.30.0.0
#
commit
~~~

P2：

~~~text
ip vpn-instance D1-V1
 ipv4-family
#
interface Eth-Trunk 12
 mode lacp-static
 trunkport Ethernet0 to Ethernet2
 ip binding vpn-instance D1-V1
 ip address 198.19.198.2 24
#
interface LoopBack 247
 ip binding vpn-instance D1-V1
 ip address 172.31.0.2 16
#
rip 96 vpn-instance D1-V1
 version 1
 network 198.19.198.0
 network 172.31.0.0
#
commit
~~~

先确认两端至少有一个 Selected 成员，再查看路由：

~~~text
display eth-trunk 12
display rip 96 interface
display rip 96 route
display ip routing-table vpn-instance D1-V1 protocol rip
ping -vpn-instance D1-V1 -a 172.30.0.1 -c 3 172.31.0.2
~~~

P1 实际路由结果：

~~~text
RIP Process 96, VPN-Instance D1-V1
Interface                Send  Receive Authentication
Eth-Trunk12              1     1       -
LoopBack246              1     1       -

172.31.0.0/16   Rip     100  2         D    198.19.198.2     Eth-Trunk12      D1-V1
~~~

两端使用 LoopBack 作为源地址的双向探测均收到3/3回复。安装默认 ARP 策略使下一跳解析使用聚合接口地址，探测报文本身仍使用指定的 LoopBack 地址。首次建立邻居时可能损失首包；判断稳定连通性应同时检查 ARP 和路由结果。

关闭全部成员后，实际聚合状态为 Down、Selected 数为0，两端活跃 RIP 路由数均为0，探测0/2。恢复一条有效成员后，聚合自动 Up；RIP 重新交换通告后恢复远端/16路由和双向连通性。接口 Up 不表示路由已经收齐，需再检查路由表。

撤销时在两端分别删除本例 RIP 进程、LoopBack、聚合接口及专用 VPN 实例，再提交：

~~~text
undo rip 96 vpn-instance D1-V1
undo interface LoopBack 246
undo interface Eth-Trunk 12
undo ip vpn-instance D1-V1
commit
~~~

P2 将 LoopBack246 换成 LoopBack247。成员恢复独立接口后，才可配置独立 IP 或加入其他聚合。
