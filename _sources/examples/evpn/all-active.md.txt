# All-Active 多归属

## 拓扑与用途

CE1 通过静态 Eth-Trunk 双接入 PE1/P1 与 PE2/P2；PE3/P3 连接 CE2。以下给出各台 VortexROS 设备的配置。PE1、PE2 使用同一个 ESI，PE 间通过 IBGP EVPN 通告以太网段及 MAC。

~~~text
CE1 Ethernet0 ── P1 Ethernet1
CE1 Ethernet1 ── P2 Ethernet2
P1 Ethernet0 ── P2 Ethernet0   198.19.80.0/30
P2 Ethernet1 ── P3 Ethernet0   198.19.23.0/24
P3 Ethernet1 ── CE2 Ethernet0
CE1 Eth-Trunk1: 192.0.2.12/24   CE2: 192.0.2.3/24
VLAN/BD 460; VNI 50460; RT 65000:50460
ESI 0000.1111.2222.1111.1111
~~~

PE 的承载接口应已完成数据面配置，互联 MTU 足以容纳 VXLAN 封装。本例使用 IPv4 VTEP、L2VNI 和 All-Active；不适用于 Single-Active 或 L3VNI 多归属。

## CE1

~~~text
system-view
~~~

配置清单：

~~~text
interface Eth-Trunk 1
 mode manual
 trunkport Ethernet0
 trunkport Ethernet1
 mac-address 0200-0000-1212
 ip address 192.0.2.12 255.255.255.0
#
~~~

CLI 操作：

~~~text
commit
~~~

## CE2

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ip address 192.0.2.3 255.255.255.0
#
~~~

CLI 操作：

~~~text
commit
~~~

CE 接口不带 VLAN 标签，由 PE 接入口的 PVID 460 归入业务。CE1 的两个成员口只加入聚合，不再单独配置 IP。

## P1 完整业务配置

~~~text
system-view
~~~

配置清单：

~~~text
enable switch
evpn-overlay enable
interface Ethernet0
 ip address 198.19.80.1 255.255.255.252
#
ip route-static 198.19.23.0 255.255.255.0 198.19.80.2
vlan 460
bridge-domain 460
 l2 binding vlan 460
 vxlan vni 50460
 evpn
  route-distinguisher 65000:1460
  vpn-target 65000:50460 export-extcommunity
  vpn-target 65000:50460 import-extcommunity
#
interface Eth-Trunk 11
 mode manual
 trunkport Ethernet1
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 460
 port trunk pvid vlan 460
 esi 0000.1111.2222.1111.1111
#
interface Nve1
 source 198.19.80.1
 vni 50460 head-end peer-list protocol bgp
#
bgp 65000
 router-id 1.1.1.1
 peer 198.19.80.2 as-number 65000
 peer 198.19.23.3 as-number 65000
 peer 198.19.23.3 connect-interface Ethernet0
 l2vpn-family evpn
  peer 198.19.80.2 enable
  peer 198.19.23.3 enable
#
~~~

CLI 操作：

~~~text
commit
~~~

## P2 完整业务配置

~~~text
system-view
~~~

配置清单：

~~~text
enable switch
evpn-overlay enable
interface Ethernet0
ip address 198.19.80.2 255.255.255.252
#
interface Ethernet1
ip address 198.19.23.2 255.255.255.0
#
vlan 460
bridge-domain 460
 l2 binding vlan 460
 vxlan vni 50460
 evpn
  route-distinguisher 65000:2460
  vpn-target 65000:50460 export-extcommunity
  vpn-target 65000:50460 import-extcommunity
#
interface Eth-Trunk 11
 mode manual
 trunkport Ethernet2
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 460
 port trunk pvid vlan 460
 esi 0000.1111.2222.1111.1111
#
interface Nve1
 source 198.19.80.2
 vni 50460 head-end peer-list protocol bgp
#
bgp 65000
 router-id 2.2.2.2
 peer 198.19.80.1 as-number 65000
 peer 198.19.23.3 as-number 65000
 peer 198.19.23.3 connect-interface Ethernet0
 l2vpn-family evpn
  peer 198.19.80.1 enable
  peer 198.19.23.3 enable
#
~~~

CLI 操作：

~~~text
commit
~~~

## P3 完整业务配置

~~~text
system-view
~~~

配置清单：

~~~text
enable switch
evpn-overlay enable
interface Ethernet0
 ip address 198.19.23.3 255.255.255.0
#
ip route-static 198.19.80.0 255.255.255.252 198.19.23.2
vlan 460
bridge-domain 460
 l2 binding vlan 460
 vxlan vni 50460
 evpn
  route-distinguisher 65000:3460
  vpn-target 65000:50460 export-extcommunity
  vpn-target 65000:50460 import-extcommunity
#
interface Ethernet1
 portswitch
 port link-type access
 port default vlan 460
#
interface Nve1
 source 198.19.23.3
 vni 50460 head-end peer-list protocol bgp
#
bgp 65000
 router-id 3.3.3.3
 peer 198.19.80.1 as-number 65000
 peer 198.19.80.2 as-number 65000
 l2vpn-family evpn
  peer 198.19.80.1 enable
  peer 198.19.80.2 enable
#
~~~

CLI 操作：

~~~text
commit
~~~

先检查两段underlay与各VTEP互通，再等待EVPN邻居建立。RD各自唯一，ESI/VLAN/VNI/RT在业务两端一致。bridge-domain EVPN视图的RT分别配置import-extcommunity和export-extcommunity，不能使用该视图不支持的both缩写。


## 验证

在三台 PE 执行：

~~~text
display bgp evpn all routing-table
display vxlan tunnel
display mac-address bridge-domain 460
display health
~~~

P1/P2 另执行 display interface Eth-Trunk 11。检查 EVPN 邻居 Established，路由包含 Type-1、Type-4 和客户 MAC/IP 通告。P3 到 CE1 MAC 的出口应为包含两台接入 PE 的 ES 下一跳组。

示例输出（组编号由运行状态决定）：

~~~text
0200-0000-1212    -/-/460    evpn-nhg-50460-536870913    static
~~~

CE1 执行 ping -a 192.0.2.12 -c 3 192.0.2.3；CE2 执行 ping -a 192.0.2.3 -c 3 192.0.2.12。两端应可达；单次 Ping 不用于证明两条成员链路的负载分担比例。

## 单接入链路关闭与恢复

在 P1 的 Ethernet1 和 CE1 的 Ethernet0 分别执行 shutdown、quit、commit，模拟链路两端均 Down。P1 的 Eth-Trunk11 应 Down，P3 的 CE1 MAC 下一跳组应只保留 P2。重复 CE1/CE2 双向 Ping，业务应经剩余接入恢复。

两端执行 undo shutdown 并提交，等待双成员组恢复。对 P2 Ethernet2 和 CE1 Ethernet1 做同样检查，然后恢复。手工关闭一端不一定使另一端立即检测到物理失载，因此本步骤明确同时关闭链路两端。

## 保存与重建

各设备配置完成后执行 save，应答 Y 并等待成功。在维护窗口对一台 PE 执行 reset service vpp；恢复后重新检查 EVPN 邻居、客户 MAC、ES 下一跳组和双向 Ping。数据面重建会中断该 PE 上的转发，其他业务也可能受影响。

## 撤销

P1、P2分别执行以下配置（PE2把端口名换为Ethernet2）：

~~~text
interface Eth-Trunk 11
 undo esi
#
interface Ethernet1
 undo eth-trunk
#
undo interface Eth-Trunk 11
interface Nve 1
 undo vni 50460
#
undo bridge-domain 460
undo vlan 460
~~~

CLI 操作：

~~~text
commit
~~~

P3执行：

~~~text
interface Ethernet1
 undo portswitch
#
interface Nve 1
 undo vni 50460
#
undo bridge-domain 460
undo vlan 460
~~~

CLI 操作：

~~~text
commit
display mac-address bridge-domain 460
display vxlan tunnel
display health
~~~


检查 MAC 中不再有本业务客户项，Nve1 不再承载 VNI 50460。底层和 BGP 邻居仍可保留供其他业务使用。

CE1 解除两条成员口的聚合归属，再删除专用 Eth-Trunk1；CE2 撤销接入地址：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo eth-trunk
#
interface Ethernet1
 undo eth-trunk
#
undo interface Eth-Trunk 1
~~~

CLI 操作：

~~~text
commit
~~~

CE2 进入 Ethernet0 执行 undo ip address 并提交。各节点核对后执行 save。若底层及 BGP 也为本业务独占，再撤销专用邻居、静态路由和接口地址。

[多归属功能](../../operator/evpn/multihoming.md) · [EVPN 参数](../../operator/reference/evpn.md)

## 广播、组播与未知单播

双接入的实测中，远端各发送5帧广播、组播，只有DF一侧向CE交付各5帧，非DF侧为0。关闭原DF接入后，另一侧当选DF，广播仍交付5/5。CE发出的5帧广播在远端收到5帧，未回送原以太网段。当前EVPN业务桥域的未知单播策略为丢弃；不要用未学习目的MAC的任意单播作为广播泛洪验收。

[同一ESI承载多个VNI](all-active-multiple-vni.md)给出新增业务和独立撤销的完整增量配置。EVPN地址族的RR客户端配置尚未提供，本例使用PE全互联。
