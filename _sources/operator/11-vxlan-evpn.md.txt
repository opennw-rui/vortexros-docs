# EVPN

本章说明如何使用 BGP EVPN 建立 VXLAN 覆盖网络。当前支持单归属和 All-Active
多归属 L2VNI，以及 L3VNI：BGP 发布和接收 EVPN Type-1 Ethernet A-D、Type-2
MAC/IP、Type-3 Inclusive Multicast、Type-4 Ethernet Segment 与 Type-5 IP Prefix
路由；LCP 把标准 Linux FDB、邻居和 VRF 路由转换为 VPP VXLAN、L2 FIB、ARP/ND
终结表、租户 FIB 和多归属转发状态，VPP 完成业务报文转发。

[命令参考](reference/evpn.md) · [配置案例](../examples/evpn.md)

## 组件职责

| 组件 | 职责 |
|---|---|
| VortexROS | 保存 VLAN、BD、VNI、RD、RT、NVE 和 BGP 配置，配置VPP对象并完成严格读回 |
| switchd | 创建和收敛Linux `switch`、端口VLAN、共享`vxlan0`、服务SVI及多归属控制接口；不承载业务报文 |
| FRR | 建立 BGP EVPN 邻居，选择 Type-2/Type-3/Type-5 路由并通过标准 Linux netlink 发布结果 |
| LCP | 观察switchd创建的Linux对象，在FDB、邻居、VRF路由与VPP VXLAN/L2 FIB/ARP-ND终结表/租户FIB之间转换状态 |
| VPP | 执行 MAC 学习、泛洪、VXLAN 封装以及二层、三层业务报文转发 |

FRR 已有的 EVPN 选路、RD/RT 处理和路由发布不会在 VortexROS 或 LCP 中重复实现；
VPP 已有的 VXLAN、bridge-domain 和 L2 FIB 也不会复制一套数据面。

## 配置前提

- VTEP 源地址之间已经通过 underlay 路由可达；
- 已执行 `enable switch` 和 `evpn-overlay enable`；
- 每个 EVPN VNI 绑定一个存在的 bridge-domain 和 VLAN；
- NVE 源地址是本机稳定的 IPv4 或 IPv6 地址；
- BGP EVPN 对等体已经配置 AS 和源接口。

使用 L3VNI 时还需要：

- 已启用 `vpn-instance`，目标 VPN-instance 已配置 RD、RT 和 `vxlan vni`；
- 对应 BGP VPN-instance IPv4/IPv6 地址族已配置 `advertise l2vpn evpn`；
- 待发布前缀已通过直连、静态或动态路由进入该 VPN-instance。

同一 VNI 不能同时配置静态 head-end peer 和 `protocol bgp`。所有 BGP EVPN VNI 使用
同一个 NVE 源地址及 underlay VPN-instance；每个 VNI 只能由一个 NVE 接口拥有。

## 二层业务实验

从 [VXLAN EVPN 案例](../examples/evpn.md)配置 P1、P2、P3，核对真实 Type-2/Type-3 路由及两个 VNI 的转发和撤销。

## L3VNI 与 Type-5

下面在 P1 的 BLUE 租户中配置 L3VNI 50000，并把直连 IPv4/IPv6 前缀发布为 EVPN
Type-5。P3 使用相同 VNI/RT、不同 RD 和本地地址；其余 underlay 与 EVPN peer 配置
沿用前述拓扑。

```text
ip vpn-instance BLUE
 vxlan vni 50000
 ipv4-family
  route-distinguisher 65000:50001
  vpn-target 65000:50000 both
 quit
quit
interface LoopBack 100
 ip binding vpn-instance BLUE
 ip address 172.16.1.1 255.255.255.255
 ipv6 address 2001:db8:1::1 128
quit
bgp 65000
 ipv4-family vpn-instance BLUE
  import-route direct
  advertise l2vpn evpn
 quit
 ipv6-family vpn-instance BLUE
  import-route direct
  advertise l2vpn evpn
 quit
quit
commit
```

P3 对应地址为 `172.16.3.3/32`、`2001:db8:3::3/128`，RD 为
`65000:50003`。使用以下命令检查 Type-5 和租户路由：

```text
display bgp evpn all routing-table
display ip routing-table vpn-instance BLUE
display ipv6 routing-table vpn-instance BLUE
display health
```

完整双租户、双栈、撤销恢复和 VPP 重启验收入口为：

```text
VORTEXROS_BIN=/path/to/current/vortexros tests/run-p1-p2-p3-evpn-type5.sh
```

## EVPN All-Active 多归属

All-Active 多归属使用同一 ESI 把 CE 同时接入 P1、P2，P3 作为远端 PE，P4 作为
Route Reflector。FRR 负责 Type-1/Type-4、DF 选举和 EVPN 路径选择；switchd 维护
Linux 控制对象；LCP 只负责在 Linux/FRR 与 VPP 之间传递多归属状态；VPP 执行
MAC ECMP、非 DF BUM 过滤、local-bias、split-horizon 和故障切换。

```text
                  P4 (RR)
                 /       \
CE1 == Eth-Trunk1 == P1   P2 == Eth-Trunk1 == CE1
                         \
                          P3 -- CE2
```

P1、P2 的 CE 侧 Eth-Trunk 使用相同 ESI。以下为 P1 示例；P2 使用相同 ESI、VLAN、
VNI 和 RT，但使用自己的 RD、VTEP 地址及物理成员：

```text
system-view
enable switch
evpn-overlay enable
vlan 101
bridge-domain 101
 l2 binding vlan 101
 vxlan vni 5010
 evpn
  route-distinguisher 65000:101
  vpn-target 65000:5010 both
 quit
quit
interface Eth-Trunk 1
 mode manual
 trunkport Ethernet 2
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 101
 port trunk pvid vlan 101
 esi 0000.0000.0000.0000.0001
quit
interface Nve 1
 source 10.255.0.1
 vni 5010 head-end peer-list protocol bgp
quit
bgp 65000
 peer 10.255.0.4 as-number 65000
 peer 10.255.0.4 connect-interface LoopBack 0
 l2vpn-family evpn
  peer 10.255.0.4 enable
 quit
quit
commit
```

Underlay 必须能分别到达 P1、P2、P3 的 VTEP；多归属 VTEP 当前使用 IPv4。P4
按普通 EVPN RR 配置，对 P1、P2、P3 启用 `l2vpn-family evpn` 并配置反射客户端。

使用以下命令确认 Type-1/Type-4、DF、远端 MAC ECMP 和设备健康：

```text
display bgp evpn all routing-table
display mac-address
display interface Eth-Trunk 1
display health
```

链路故障验收必须同时确认：故障成员退出本地 ES、远端 NHG 缩减为单成员、业务仍然
连通；链路恢复后 NHG 恢复双成员。VPP 冷重启验收必须确认本地 ES、远端 NHG 和
业务转发均恢复，不能只以其他 PE 仍能转发作为成功依据。完整入口为：

```text
VORTEXROS_BIN=/path/to/current/vortexros tests/run-p1-p2-p3-p4-evpn-mh.sh
```

## 当前范围

当前支持单归属和 All-Active 多归属 L2VNI、L3VNI、Type-1/Type-2/Type-3/
Type-4/Type-5、IPv4/IPv6 MAC/IP 和租户前缀、ARP/ND 抑制、共享 SVD 多 VNI、
远端 MAC 迁移、MAC ECMP、DF 选举、非 DF BUM 过滤、local-bias、split-horizon，
以及配置撤销、成员故障和 VPP 冷重启后的权威恢复。单归属支持 IPv4/IPv6 VTEP
源地址及 default/命名 underlay VPN-instance；多归属 VTEP 当前限定为 IPv4。

当前 FRR 版本只实现 All-Active EVPN 多归属，因此不提供 Single-Active。按本项目范围，
不实现 PIM、underlay multicast 和 EVPN selective multicast；BUM 使用 ingress
replication。未列出的 EVPN 扩展不能由近似命令静默下发。

实现语义对照：

- VRP VXLAN EVPN 配置模型：`bridge-domain`、`Nve`、`l2vpn-family evpn`；
- FRR BGP EVPN：`advertise-all-vni`、per-VNI/L3VNI RD/RT、Type-1 至 Type-5、
  All-Active ES 与 DF 选举；
- VPP：原生 VXLAN、bridge-domain、L2 FIB、租户 IP FIB，以及 LCP 传入的多归属
  转发状态。
