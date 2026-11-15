# 代理 ARP

代理 ARP 在指定三层接口上，为配置范围内的 IPv4 地址回答 ARP，适用于客户认为目标直连、目标实际位于路由网络另一端的情况。它不执行 NAT，也不代替路由。

## 使用条件

入口应是具有 MAC 的三层接口，如物理口、聚合口、Vlanif 或 Vbdif；二层成员口、LoopBack 和 NVE 不能作为代理入口。接口所属 VPN 决定路由域。设备必须有到目标的路由，目标必须有回程。

## 拓扑

CE1、P1、P2、CE2 均运行 VortexROS：

~~~text
CE1 Ethernet0 ── Ethernet1 P1 Ethernet0 ── Ethernet0 P2 Ethernet1 ── Ethernet0 CE2
198.18.11.100/24  198.18.11.1/24
                            198.19.80.1/30   198.19.80.2/30
                                                    198.19.23.2/24  198.19.23.3/24
                                                    CE2 LoopBack0: 198.18.11.150/32
~~~

CE1 认为 198.18.11.150 与自己同网段，会直接请求它的 MAC；P1 代理应答后，把数据按路由转发到 CE2。

## CE1

~~~text
system-view
interface Ethernet0
 ip address 198.18.11.100 255.255.255.0
quit
commit
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
ip route-static 198.18.11.150 255.255.255.255 198.19.80.2
arp proxy 198.18.11.150 198.18.11.150 interface Ethernet1
commit
~~~

起止相同表示代理单个地址；扩大范围会使更多地址的 ARP 被本设备接收，应与路由规划一致。

## P2

~~~text
system-view
interface Ethernet0
 ip address 198.19.80.2 255.255.255.252
quit
interface Ethernet1
 ip address 198.19.23.2 255.255.255.0
quit
ip route-static 198.18.11.150 255.255.255.255 198.19.23.3
ip route-static 198.18.11.0 255.255.255.0 198.19.80.1
commit
~~~

## CE2

~~~text
system-view
interface Ethernet0
 ip address 198.19.23.3 255.255.255.0
quit
interface LoopBack0
 ip address 198.18.11.150 255.255.255.255
quit
ip route-static 198.18.11.0 255.255.255.0 198.19.23.2
commit
~~~

## 验证

P1 执行 display arp proxy；示例输出：

~~~text
Start Address    End Address      Interface            State
198.18.11.150    198.18.11.150    Ethernet1            active
Total items displayed = 1
~~~

CE1 执行 ping -a 198.18.11.100 -c 3 198.18.11.150，应收到回复。用 display arp 查看目标邻居，其 MAC 应为 P1 接入口的 MAC。P1/P2 用 display ip routing-table 检查目标与回程。

范围外的地址不会自动获得代理应答。若持续不通，应分别检查代理入口、目标主机路由及回程，而不是只检查配置是否存在。

## 撤销

P1 执行：

~~~text
system-view
undo arp proxy 198.18.11.150 198.18.11.150 interface Ethernet1
undo ip route-static 198.18.11.150 255.255.255.255 198.19.80.2
commit
display arp proxy
~~~

代理清单应为空。CE1 的旧 ARP 在老化前可能仍可使用，验证撤销时应考虑缓存。拆除拓扑时在 P2/CE2 撤销本例静态路由、各接口地址以及 CE2 LoopBack0，提交并按需 save。共享的其他业务应保留。

[命令参考](reference/neighbors.md)
