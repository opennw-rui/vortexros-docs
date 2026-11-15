# VXLAN EVPN

## 拓扑

~~~text
CE1 ── P1 ── P2 ── P3 ── CE2
      VTEP          VTEP
  10.255.0.1    10.255.0.3
~~~

| 用途 | 左侧 | 右侧 |
| --- | --- | --- |
| P1—P2 | Ethernet0：10.201.12.1/24 | Ethernet0：10.201.12.2/24 |
| P2—P3 | Ethernet1：10.201.23.2/24 | Ethernet0：10.201.23.3/24 |
| VLAN 101，VNI 5010 | CE1：192.0.2.1/24 | CE2：192.0.2.3/24 |
| VLAN 102，VNI 5020 | CE1：198.18.2.1/24 | CE2：198.18.2.3/24 |

所有设备均运行 VortexROS。P1/P3 是 VTEP，P2 只做三层转发；CE1/CE2 接在两端 PE 的客户口。VLAN 101 为不带标签的本征 VLAN，VLAN 102 带 802.1Q 标签。两条业务使用不同 VNI，不提供跨 VLAN 路由。

## 配置 P2

~~~text
system-view
interface Ethernet0
 ip address 10.201.12.2 255.255.255.0
quit
interface Ethernet1
 ip address 10.201.23.2 255.255.255.0
quit
ip route-static 10.255.0.1 255.255.255.255 10.201.12.1
ip route-static 10.255.0.3 255.255.255.255 10.201.23.3
commit
~~~

## 配置 P1

~~~text
system-view
enable switch
evpn-overlay enable
vlan batch 101 102
bridge-domain 101
 l2 binding vlan 101
 vxlan vni 5010
 evpn
  route-distinguisher 65000:101
  vpn-target 65000:5010 export-extcommunity
  vpn-target 65000:5010 import-extcommunity
 quit
quit
bridge-domain 102
 l2 binding vlan 102
 vxlan vni 5020
 evpn
  route-distinguisher 65000:102
  vpn-target 65000:5020 export-extcommunity
  vpn-target 65000:5020 import-extcommunity
 quit
quit
interface Ethernet0
 ip address 10.201.12.1 255.255.255.0
quit
interface Ethernet1
 switchport
 port link-type trunk
 port trunk allow-pass vlan 101 102
 port trunk pvid vlan 101
quit
interface LoopBack0
 ip address 10.255.0.1 255.255.255.255
quit
interface Nve1
 source 10.255.0.1
 vni 5010 head-end peer-list protocol bgp
 vni 5020 head-end peer-list protocol bgp
quit
ip route-static 10.255.0.3 255.255.255.255 10.201.12.2
bgp 65000
 router-id 10.255.0.1
 peer 10.255.0.3 as-number 65000
 peer 10.255.0.3 connect-interface LoopBack0
 l2vpn-family evpn
  peer 10.255.0.3 enable
 quit
quit
commit
~~~

## 配置 P3

~~~text
system-view
enable switch
evpn-overlay enable
vlan batch 101 102
bridge-domain 101
 l2 binding vlan 101
 vxlan vni 5010
 evpn
  route-distinguisher 65000:301
  vpn-target 65000:5010 export-extcommunity
  vpn-target 65000:5010 import-extcommunity
 quit
quit
bridge-domain 102
 l2 binding vlan 102
 vxlan vni 5020
 evpn
  route-distinguisher 65000:302
  vpn-target 65000:5020 export-extcommunity
  vpn-target 65000:5020 import-extcommunity
 quit
quit
interface Ethernet0
 ip address 10.201.23.3 255.255.255.0
quit
interface Ethernet1
 switchport
 port link-type trunk
 port trunk allow-pass vlan 101 102
 port trunk pvid vlan 101
quit
interface LoopBack0
 ip address 10.255.0.3 255.255.255.255
quit
interface Nve1
 source 10.255.0.3
 vni 5010 head-end peer-list protocol bgp
 vni 5020 head-end peer-list protocol bgp
quit
ip route-static 10.255.0.1 255.255.255.255 10.201.23.2
bgp 65000
 router-id 10.255.0.3
 peer 10.255.0.1 as-number 65000
 peer 10.255.0.1 connect-interface LoopBack0
 l2vpn-family evpn
  peer 10.255.0.1 enable
 quit
quit
commit
~~~

同一业务 VNI 的两端 RT 必须相同，RD 应各自唯一。BGP EVPN 发布可达 VTEP 和本地 MAC，P2 不参与 EVPN。CE1/CE2 的二层广播域延伸到对端；VLAN 101 和 102 仍互相隔离。

## 配置 CE1 和 CE2

CE1：

~~~text
system-view
interface Ethernet0
 ip address 192.0.2.1 255.255.255.0
quit
interface Ethernet0.102
 vlan-type dot1q 102
 ip address 198.18.2.1 255.255.255.0
quit
commit
~~~

CE2：

~~~text
system-view
interface Ethernet0
 ip address 192.0.2.3 255.255.255.0
quit
interface Ethernet0.102
 vlan-type dot1q 102
 ip address 198.18.2.3 255.255.255.0
quit
commit
~~~

父接口承载不带标签的 VLAN 101；子接口承载 VLAN 102。CE 不配置 VNI 或 EVPN 邻居。

## 验证

先在 P1 和 P3 用各自的 LoopBack 地址作源地址 Ping 对端 VTEP。若 LoopBack 不通，先检查两条物理链路的下一跳和双向 /32 路由，再等待 BGP 建邻。

**P1：**

~~~text
ping -n -a 10.255.0.1 -c 3 -t 1000 10.255.0.3
display bgp evpn all routing-table mac-route
display bgp evpn all routing-table inclusive-route
display vxlan tunnel
~~~

示例输出；Type-2 的 RD 65000:301 为 P3 的 VLAN 101：

~~~text
Route Distinguisher: 65000:301
 *>i   0:48:42bb-a874-99bf:0:0.0.0.0                                  10.255.0.3

Total Number of MAC Routes: 4
Total Number of Inclusive Routes: 4
Total: 2    Static: 2    L2 dynamic: 0    L3 dynamic: 0
~~~

此版本的 Tunnel 简表使用 `static` 标签显示示例中两条隧道。判断 EVPN 学习请看 BGP Type-2/Type-3 路由及业务流量，不要用该标签判断 peer 是否通过 BGP 学到。

**CE1：**

~~~text
ping -n -a 192.0.2.1 -c 3 -t 1000 192.0.2.3
ping -n -a 198.18.2.1 -c 3 -t 1000 198.18.2.3
~~~

两条业务各 3 发 3 收。CE2 在 VLAN 101 向 CE1 反向探测也是 3 发 3 收。

## 撤销

在 P1 先只撤销一个业务 VNI，保留 P3 和对照 VNI：

~~~text
system-view
interface Nve1
 undo vni 5010 head-end peer-list protocol bgp
 quit
commit
display vxlan tunnel
~~~

示例中 P1 隧道从 2 条减到 1 条。CE1 到 CE2 的 VLAN 101 探测变为 **3 发 0 收**，VLAN 102 仍为 **3 发 3 收**。重新输入原 `vni 5010 ... protocol bgp` 可恢复该业务，随后重查 BGP 和 Ping。

要拆除整个示例，依次撤销两端的 NVE VNI，删除专用 NVE、解除 EVPN 邻居，撤销专用桥域和 VLAN。最后清理示例主机的地址和 VLAN 子接口。共用的 BGP 进程和底层路由按现有业务保留。

[EVPN 配置指南](../../operator/11-vxlan-evpn.md)

CE1/CE2 最后执行以下撤销。

~~~text
system-view
undo interface Ethernet0.102
interface Ethernet0
 undo ip address
quit
commit
~~~
