# MPLS L3VPN

## 拓扑

~~~text
CE1 ─── P1 (PE) ─── P2 ─── P3 ─── P4 (PE) ─── CE4
        1.1.1.1     2.2.2.2  3.3.3.3  4.4.4.4    ← LoopBack0
~~~

| 链路 | 左端 | 右端 |
| --- | --- | --- |
| CE1—P1 | ce1p1：192.0.2.2/24 | host-p1ce1：192.0.2.1/24 |
| P1—P2 | host-p1p2：10.0.12.1/30 | host-p2p1：10.0.12.2/30 |
| P2—P3 | host-p2p3：10.0.23.1/30 | host-p3p2：10.0.23.2/30 |
| P3—P4 | host-p3p4：10.0.34.1/30 | host-p4p3：10.0.34.2/30 |
| P4—CE4 | host-p4ce4：198.51.100.1/24 | ce4p4：198.51.100.2/24 |

四台 VortexROS 都启用 VPP，接口名为隔离实验使用的 AF_PACKET 名称。P2/P3 只运行底层 OSPF 与 LDP。P1/P4 将客户接口放入 CUST-A，并通过 MP-BGP 发布 VPNv4 路由。两端 RD 不同，RT 均为 65000:100。下列 IPv4 配置已在独立拓扑逐行提交并验证。

## 配置核心

按下列命令配置每台设备。先提交 OSPF/LDP，再给 P1/P4 加客户业务。全局 `mpls` 后返回系统视图启用 LDP；接口下分别执行 `mpls` 和 `mpls ldp`。

### P1

~~~text
system-view
mpls lsr-id 1.1.1.1
mpls
quit
mpls ldp
interface LoopBack0
 ip address 1.1.1.1 255.255.255.255
 quit
interface host-p1p2
 ip address 10.0.12.1 255.255.255.252
 mpls
 mpls ldp
 quit
ospf 1 router-id 1.1.1.1
 area 0.0.0.0
  network 1.1.1.1 0.0.0.0 description LSR-ID
  network 10.0.12.1 0.0.0.0 description Core
  quit
 quit
interface host-p1p2
 ospf network-type p2p
 quit
commit
~~~

### P2

~~~text
system-view
mpls lsr-id 2.2.2.2
mpls
quit
mpls ldp
interface LoopBack0
 ip address 2.2.2.2 255.255.255.255
 quit
interface host-p2p1
 ip address 10.0.12.2 255.255.255.252
 mpls
 mpls ldp
 quit
interface host-p2p3
 ip address 10.0.23.1 255.255.255.252
 mpls
 mpls ldp
 quit
ospf 1 router-id 2.2.2.2
 area 0.0.0.0
  network 2.2.2.2 0.0.0.0 description LSR-ID
  network 10.0.12.2 0.0.0.0 description Core
  network 10.0.23.1 0.0.0.0 description Core
  quit
 quit
interface host-p2p1
 ospf network-type p2p
 quit
interface host-p2p3
 ospf network-type p2p
 quit
commit
~~~

### P3

~~~text
system-view
mpls lsr-id 3.3.3.3
mpls
quit
mpls ldp
interface LoopBack0
 ip address 3.3.3.3 255.255.255.255
 quit
interface host-p3p2
 ip address 10.0.23.2 255.255.255.252
 mpls
 mpls ldp
 quit
interface host-p3p4
 ip address 10.0.34.1 255.255.255.252
 mpls
 mpls ldp
 quit
ospf 1 router-id 3.3.3.3
 area 0.0.0.0
  network 3.3.3.3 0.0.0.0 description LSR-ID
  network 10.0.23.2 0.0.0.0 description Core
  network 10.0.34.1 0.0.0.0 description Core
  quit
 quit
interface host-p3p2
 ospf network-type p2p
 quit
interface host-p3p4
 ospf network-type p2p
 quit
commit
~~~

### P4

~~~text
system-view
mpls lsr-id 4.4.4.4
mpls
quit
mpls ldp
interface LoopBack0
 ip address 4.4.4.4 255.255.255.255
 quit
interface host-p4p3
 ip address 10.0.34.2 255.255.255.252
 mpls
 mpls ldp
 quit
ospf 1 router-id 4.4.4.4
 area 0.0.0.0
  network 4.4.4.4 0.0.0.0 description LSR-ID
  network 10.0.34.2 0.0.0.0 description Core
  quit
 quit
interface host-p4p3
 ospf network-type p2p
 quit
commit
~~~

在 P1 查询到 4.4.4.4/32 的 OSPF 路由并 Ping 对端 LoopBack；在 P4 做反向检查。P2 应有两个 `OPERATIONAL` 的 LDP 邻居。底层不通时先修复核心，添加 VPN 路由不会替代传输标签。

## 配置客户业务

### P1

~~~text
system-view
ip vpn-instance CUST-A
 ipv4-family
  route-distinguisher 65000:101
  vpn-target 65000:100 both
  quit
 quit
interface host-p1ce1
 ip binding vpn-instance CUST-A
 ip address 192.0.2.1 255.255.255.0
 quit
bgp 65000
 router-id 1.1.1.1
 peer 4.4.4.4 as-number 65000
 peer 4.4.4.4 connect-interface LoopBack0
 peer 4.4.4.4 timer connect-retry 3
 ipv4-family unicast
  undo peer 4.4.4.4 enable
  quit
 ipv4-family vpnv4
  peer 4.4.4.4 enable
  quit
 ipv4-family vpn-instance CUST-A
  import-route direct
  quit
 quit
commit
~~~

### P4

~~~text
system-view
ip vpn-instance CUST-A
 ipv4-family
  route-distinguisher 65000:104
  vpn-target 65000:100 both
  quit
 quit
interface host-p4ce4
 ip binding vpn-instance CUST-A
 ip address 198.51.100.1 255.255.255.0
 quit
bgp 65000
 router-id 4.4.4.4
 peer 1.1.1.1 as-number 65000
 peer 1.1.1.1 connect-interface LoopBack0
 peer 1.1.1.1 timer connect-retry 3
 ipv4-family unicast
  undo peer 1.1.1.1 enable
  quit
 ipv4-family vpnv4
  peer 1.1.1.1 enable
  quit
 ipv4-family vpn-instance CUST-A
  import-route direct
  quit
 quit
commit
~~~

`import-route direct` 将 CUST-A 的直连前缀导出给其他 PE。真实部署若只允许指定子网，应加[路由策略](../operator/route-policy.md)。改接口的 VPN 归属会改变其路由表，不能直接用于现有管理口。

### CE1 和 CE4

在独立的 Linux 实验主机上执行。CE4 把接口改为 `ce4p4`，本地地址为 `198.51.100.2/24`，网关为 `198.51.100.1`。

~~~bash
sudo ip link set ce1p1 up
sudo ip addr add 192.0.2.2/24 dev ce1p1
sudo ip route add default via 192.0.2.1
~~~

## 验证

**P1：**

~~~text
display mpls ldp peer
display bgp vpnv4 all routing-table
display ip routing-table vpn-instance CUST-A
display ip fib vpn-instance CUST-A
~~~

实际输出节选：

~~~text
Peer ID          Address-Family  Transport Address                State         Uptime
2.2.2.2          ipv4            2.2.2.2                          OPERATIONAL   00:00:27

Routing Table : CUST-A
Destination/Mask   Proto   Pre  Cost    Flags   NextHop         Interface       VPN-Instance
 198.51.100.0/24   BGP     254  0         DT   4.4.4.4          host-p1p2       default

Destination/Mask      Type      Pre    Weight    Flags    NextHop      Interface     Lookup-Table
198.51.100.0/24       normal    20     1         -        10.0.12.2    host-p1p2     -
~~~

**P2：** `display mpls forwarding-table`，核对已安装的标签动作和出接口。实验中有指向 `10.0.23.2 host-p2p3` 的 MPLS 路径。标签值由协议分配，不要求与样例相同。

**CE1：** `ping -c 3 198.51.100.2`；**CE4：** `ping -c 3 192.0.2.2`。实测双向各 3 发 3 收；CE1 对核心地址 10.0.23.1 的对照探测不可达。

## 撤销

在 P4 先只撤销 IPv4 客户路由发布，保留底层作为对照：

~~~text
system-view
bgp 65000
 ipv4-family vpn-instance CUST-A
  undo import-route direct
  quit
 quit
commit
~~~

P1 的 CUST-A 路由表实测不再包含 198.51.100.0/24。CE1 到 CE4 变为 3 发 0 收，P1 的 LDP 邻居仍为 `OPERATIONAL`。

拆除整个实验时，两端都撤销客户路由发布，解除客户接口的地址与 VPN 绑定，删除专用 BGP VPN 地址族引用和 CUST-A。若底层也不再使用，先移除接口 LDP/MPLS，再关闭各台全局 LDP/MPLS。只清理本实验创建的对象。

[MPLS L3VPN 指南](../operator/l3vpn.md) · [MPLS 与 LDP 指南](../operator/ldp.md)
