# RIP 与 BFD 多路径

本例在两台 VortexROS 间建立两条独立三层链路，在 VPN 实例 BLUE 中通过 RIP 学习 LoopBack 前缀。BFD 默认以 1000ms 发送、1000ms 接收、检测3次；一条邻居失效后，另一路径继续转发。两端以 Ethernet0、Ethernet1 组成三层 Eth-Trunk12，另以独立 Ethernet2 连接第二条三层链路。成员口不能配置独立地址。

## 拓扑

~~~text
P1 Ethernet0/1 === Eth-Trunk12 === Ethernet0/1 P2
       198.19.198.1/24 ---- 198.19.198.2/24
P1 Ethernet2 198.19.197.1/24 ---- 198.19.197.2/24 Ethernet2 P2
P1 LoopBack246 172.30.0.1/16      172.31.0.2/16 LoopBack247 P2
~~~

## P1 配置

~~~text
bfd
ip vpn-instance BLUE
 ipv4-family
#
interface Ethernet 2
 ip binding vpn-instance BLUE
 ip address 198.19.197.1 24
 rip bfd enable
#
interface Eth-Trunk 12
 mode lacp-static
 trunkport Ethernet 0 to Ethernet 1
 ip binding vpn-instance BLUE
 ip address 198.19.198.1 24
 rip bfd enable
#
interface LoopBack 246
 ip binding vpn-instance BLUE
 ip address 172.30.0.1 16
#
rip 96 vpn-instance BLUE
 version 1
 network 198.19.197.0
 network 198.19.198.0
 network 172.30.0.0
 maximum load-balancing 2
#
commit
save
~~~

## P2 配置

~~~text
bfd
ip vpn-instance BLUE
 ipv4-family
#
interface Ethernet 2
 ip binding vpn-instance BLUE
 ip address 198.19.197.2 24
 rip bfd enable
#
interface Eth-Trunk 12
 mode lacp-static
 trunkport Ethernet 0 to Ethernet 1
 ip binding vpn-instance BLUE
 ip address 198.19.198.2 24
 rip bfd enable
#
interface LoopBack 247
 ip binding vpn-instance BLUE
 ip address 172.31.0.2 16
#
rip 96 vpn-instance BLUE
 version 1
 network 198.19.197.0
 network 198.19.198.0
 network 172.31.0.0
 maximum load-balancing 2
#
commit
save
~~~

本例使用 RIPv1 有类网络以便同时演示版本1互通；新部署若不需要兼容 RIPv1，可在两端使用版本2。不要把上述 /16 换为有类网络内不连续的子网后仍照用版本1。

## 正常状态



~~~text
display bfd session all
display bfd statistics
display rip 96 route
display ip routing-table vpn-instance BLUE protocol rip
ping -vpn-instance BLUE -a 172.30.0.1 -c 3 172.31.0.2
~~~

实测两个邻居都为 Up，路由表为1个目的、2条路径，优先级100、Cost2；下一跳分别为198.19.197.2和198.19.198.2。

## 单链路协议故障

在 P1 的198.19.198.0/24链路入口暂时拒绝 BFD 和 RIP，普通 IP 数据仍允许。下面的规则只用于演示检测与撤路，测试结束必须撤销。

~~~text
acl name BFD-TEST advance
 rule 5 deny udp destination-port eq 3784
 rule 6 deny udp destination-port eq 520
 rule 100 permit ip
#
interface Eth-Trunk 12
 traffic-filter inbound acl BFD-TEST
#
commit
~~~

检测超时后，实测故障邻居路径被撤销，另一邻居仍为 Up：

~~~text
Routing Table : BLUE
         Destinations : 1        Routes : 1

Destination/Mask   Proto   Pre  Cost    NextHop
172.31.0.0/16       Rip     100  2       198.19.197.2
~~~

故障期间从 P1 的 LoopBack 发往 P2 LoopBack，实际3发3收。若业务只剩一条路径，再使该邻居失效，活跃 IP 路由表应没有该 RIP 前缀；RIP 协议表可暂时保留 Cost16 的不可达记录，等待正常回收，这不代表仍可转发。

解除测试限制：

~~~text
interface Eth-Trunk 12
 undo traffic-filter inbound
#
commit
~~~

重新收到通告、建立 BFD 会话后，实测路由恢复为2条。接口保持 Up 不能替代上述路由和连通性检查。

## 恢复默认与撤销

以下操作在两端分别执行。撤销 BFD 绑定只删除本例引用，不会停止其他协议仍使用的会话：

~~~text
interface Ethernet 2
 undo rip bfd enable
#
interface Eth-Trunk 12
 undo rip bfd enable
#
rip 96 vpn-instance BLUE
 undo maximum load-balancing
#
commit
display bfd session all
display ip routing-table vpn-instance BLUE protocol rip
~~~

实测本例两个动态会话消失，其他协议会话仍保留；恢复缺省 ECMP 后，同一目的仅保留1条 RIP 路径。

完全撤销专用案例时，先移除本例 ACL 和 RIP 进程，再撤销接口地址、VPN 绑定及 LoopBack，最后删除专用 VPN 实例。不要删除其他业务仍在使用的全局 BFD 或 VPN 实例。

[协议绑定](../operator/bfd/protocols.md) · [RIPv1](rip-v1.md)
