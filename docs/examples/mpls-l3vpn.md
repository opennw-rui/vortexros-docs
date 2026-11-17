# MPLS L3VPN

## 拓扑

~~~text
CE1 ─── P1 (PE) ─── P2 ─── P3 ─── P4 (PE) ─── CE2
        1.1.1.1     2.2.2.2  3.3.3.3  4.4.4.4    ← LoopBack0
~~~

| 链路 | 左端 | 右端 |
| --- | --- | --- |
| CE1—P1 | Ethernet0：192.0.2.2/24 | Ethernet1：192.0.2.1/24 |
| P1—P2 | Ethernet0：10.0.12.1/30 | Ethernet0：10.0.12.2/30 |
| P2—P3 | Ethernet1：10.0.23.1/30 | Ethernet0：10.0.23.2/30 |
| P3—P4 | Ethernet1：10.0.34.1/30 | Ethernet0：10.0.34.2/30 |
| P4—CE2 | Ethernet1：198.51.100.1/24 | Ethernet0：198.51.100.2/24 |

CE1、CE2、P1—P4 均运行 VortexROS。P1/P4 是 PE，将客户接口放入 CUST-A；P2/P3 只运行核心 OSPF 与 LDP，不持有客户路由。两端 RD 不同，RT 均为 65000:100。PE 与核心接口由 VPP 管理。

## 配置核心

按下列命令配置每台设备。先提交 OSPF/LDP，再给 P1/P4 加客户业务。全局 `mpls` 后返回系统视图启用 LDP；接口下分别执行 `mpls` 和 `mpls ldp`。

### P1

~~~text
system-view
~~~

配置清单：

~~~text
mpls lsr-id 1.1.1.1
mpls
#
mpls ldp
interface LoopBack0
 ip address 1.1.1.1 255.255.255.255
#
interface Ethernet0
 ip address 10.0.12.1 255.255.255.252
 mpls
 mpls ldp
#
ospf 1 router-id 1.1.1.1
 area 0.0.0.0
  network 1.1.1.1 0.0.0.0 description LSR-ID
  network 10.0.12.1 0.0.0.0 description Core
#
interface Ethernet0
 ospf network-type p2p
#
~~~

CLI 操作：

~~~text
commit
~~~

### P2

~~~text
system-view
~~~

配置清单：

~~~text
mpls lsr-id 2.2.2.2
mpls
#
mpls ldp
interface LoopBack0
 ip address 2.2.2.2 255.255.255.255
#
interface Ethernet0
 ip address 10.0.12.2 255.255.255.252
 mpls
 mpls ldp
#
interface Ethernet1
 ip address 10.0.23.1 255.255.255.252
 mpls
 mpls ldp
#
ospf 1 router-id 2.2.2.2
 area 0.0.0.0
  network 2.2.2.2 0.0.0.0 description LSR-ID
  network 10.0.12.2 0.0.0.0 description Core
  network 10.0.23.1 0.0.0.0 description Core
#
interface Ethernet0
 ospf network-type p2p
#
interface Ethernet1
 ospf network-type p2p
#
~~~

CLI 操作：

~~~text
commit
~~~

### P3

~~~text
system-view
~~~

配置清单：

~~~text
mpls lsr-id 3.3.3.3
mpls
#
mpls ldp
interface LoopBack0
 ip address 3.3.3.3 255.255.255.255
#
interface Ethernet0
 ip address 10.0.23.2 255.255.255.252
 mpls
 mpls ldp
#
interface Ethernet1
 ip address 10.0.34.1 255.255.255.252
 mpls
 mpls ldp
#
ospf 1 router-id 3.3.3.3
 area 0.0.0.0
  network 3.3.3.3 0.0.0.0 description LSR-ID
  network 10.0.23.2 0.0.0.0 description Core
  network 10.0.34.1 0.0.0.0 description Core
#
interface Ethernet0
 ospf network-type p2p
#
interface Ethernet1
 ospf network-type p2p
#
~~~

CLI 操作：

~~~text
commit
~~~

### P4

~~~text
system-view
~~~

配置清单：

~~~text
mpls lsr-id 4.4.4.4
mpls
#
mpls ldp
interface LoopBack0
 ip address 4.4.4.4 255.255.255.255
#
interface Ethernet0
 ip address 10.0.34.2 255.255.255.252
 mpls
 mpls ldp
#
ospf 1 router-id 4.4.4.4
 area 0.0.0.0
  network 4.4.4.4 0.0.0.0 description LSR-ID
  network 10.0.34.2 0.0.0.0 description Core
#
interface Ethernet0
 ospf network-type p2p
#
~~~

CLI 操作：

~~~text
commit
~~~

在 P1 查询到 4.4.4.4/32 的 OSPF 路由并 Ping 对端 LoopBack；在 P4 做反向检查。P2 应有两个 `OPERATIONAL` 的 LDP 邻居。底层不通时先修复核心，添加 VPN 路由不会替代传输标签。

## 配置客户业务

### P1

~~~text
system-view
~~~

配置清单：

~~~text
ip vpn-instance CUST-A
 ipv4-family
  route-distinguisher 65000:101
  vpn-target 65000:100 both
#
interface Ethernet1
 ip binding vpn-instance CUST-A
 ip address 192.0.2.1 255.255.255.0
#
bgp 65000
 router-id 1.1.1.1
 peer 4.4.4.4 as-number 65000
 peer 4.4.4.4 connect-interface LoopBack0
 peer 4.4.4.4 timer connect-retry 3
 ipv4-family unicast
  undo peer 4.4.4.4 enable
 #
 ipv4-family vpnv4
  peer 4.4.4.4 enable
 #
 ipv4-family vpn-instance CUST-A
  import-route direct
#
~~~

CLI 操作：

~~~text
commit
~~~

### P4

~~~text
system-view
~~~

配置清单：

~~~text
ip vpn-instance CUST-A
 ipv4-family
  route-distinguisher 65000:104
  vpn-target 65000:100 both
#
interface Ethernet1
 ip binding vpn-instance CUST-A
 ip address 198.51.100.1 255.255.255.0
#
bgp 65000
 router-id 4.4.4.4
 peer 1.1.1.1 as-number 65000
 peer 1.1.1.1 connect-interface LoopBack0
 peer 1.1.1.1 timer connect-retry 3
 ipv4-family unicast
  undo peer 1.1.1.1 enable
 #
 ipv4-family vpnv4
  peer 1.1.1.1 enable
 #
 ipv4-family vpn-instance CUST-A
  import-route direct
#
~~~

CLI 操作：

~~~text
commit
~~~

`import-route direct` 将 CUST-A 的直连前缀导出给其他 PE。真实部署若只允许指定子网，应加[路由策略](../operator/route-policy.md)。改接口的 VPN 归属会改变其路由表，不能直接用于现有管理口。

### CE 配置

CE1：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ip address 192.0.2.2 255.255.255.0
#
ip route-static 0.0.0.0 0.0.0.0 192.0.2.1
~~~

CLI 操作：

~~~text
commit
~~~

CE2：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ip address 198.51.100.2 255.255.255.0
#
ip route-static 0.0.0.0 0.0.0.0 198.51.100.1
~~~

CLI 操作：

~~~text
commit
~~~

客户设备只配置接入地址和默认路由，不运行核心 OSPF、LDP 或运营商 MP-BGP。

## 验证

**P1：**

~~~text
display mpls ldp peer
display bgp vpnv4 all routing-table
display ip routing-table vpn-instance CUST-A
display ip fib vpn-instance CUST-A
~~~

示例输出：

~~~text
Peer ID          Address-Family  Transport Address                State         Uptime
2.2.2.2          ipv4            2.2.2.2                          OPERATIONAL   00:00:27

Routing Table : CUST-A
Destination/Mask   Proto   Pre  Cost    Flags   NextHop         Interface       VPN-Instance
 198.51.100.0/24   BGP     254  0         DT   4.4.4.4          Ethernet0       default

Destination/Mask      Type      Pre    Weight    Flags    NextHop      Interface     Lookup-Table
198.51.100.0/24       normal    20     1         -        10.0.12.2    Ethernet0     -
~~~

**P2：** `display mpls forwarding-table`，核对已安装的标签动作和出接口。应有指向 `10.0.23.2 Ethernet1` 的 MPLS 路径。标签值由协议分配，不要求与样例相同。

**CE1：** `ping -c 3 198.51.100.2`；**CE2：** `ping -c 3 192.0.2.2`。两端应各收到 3 个回复。客户不应通过 CUST-A 获得核心网段路由。

## 撤销

在 P4 先只撤销 IPv4 客户路由发布，保留底层作为对照：

~~~text
system-view
~~~

配置清单：

~~~text
bgp 65000
 ipv4-family vpn-instance CUST-A
  undo import-route direct
#
~~~

CLI 操作：

~~~text
commit
~~~

P1 的 CUST-A 路由表应不再包含 198.51.100.0/24。CE1 到 CE2 应不再可达，P1 的 LDP 邻居仍为 `OPERATIONAL`。

拆除整个示例时，两端都撤销客户路由发布，解除客户接口的地址与 VPN 绑定，删除专用 BGP VPN 地址族引用和 CUST-A。若底层也不再使用，先移除接口 LDP/MPLS，再关闭各台全局 LDP/MPLS。只清理本示例创建的对象。

[MPLS L3VPN 指南](../operator/l3vpn.md) · [MPLS 与 LDP 指南](../operator/ldp.md)

在 CE1 撤销 ip route-static 0.0.0.0 0.0.0.0 192.0.2.1，在 CE2 撤销相同命令但下一跳为 198.51.100.1（命令前加 undo）。两端进入 Ethernet0 执行 undo ip address，再 commit。需要保留创建或撤销结果时，在各设备执行 save。
