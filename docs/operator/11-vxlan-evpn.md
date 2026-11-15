# EVPN

本章说明如何使用 BGP EVPN 建立 VXLAN 覆盖网络。当前支持单归属和 All-Active
多归属 L2VNI，以及 L3VNI：BGP 发布和接收 EVPN Type-1 Ethernet A-D、Type-2
MAC/IP、Type-3 Inclusive Multicast、Type-4 Ethernet Segment 与 Type-5 IP Prefix
路由；LCP 把标准 Linux FDB、邻居和 VRF 路由转换为 VPP VXLAN、L2 FIB、ARP/ND
终结表、租户 FIB 和多归属转发状态，VPP 完成业务报文转发。

[命令参考](reference/evpn.md) · [案例目录](../examples/evpn/index.md)


~~~{toctree}
:maxdepth: 2

evpn/l2vpn
evpn/l3vpn
evpn/multihoming
evpn/anycast
evpn/lifecycle
~~~

## 配置前提

- VTEP 源地址之间已经通过 underlay 路由可达；
- 已执行 `enable switch` 和 `evpn-overlay enable`；
- 每个 L2VNI 绑定一个存在的 bridge-domain 和 VLAN；L3VNI 的内部桥域和服务接口由系统管理；
- NVE 源地址是本机稳定的 IPv4 或 IPv6 地址；
- BGP EVPN 对等体已经配置 AS 和源接口。

使用 L3VNI 时还需要：

- 已创建目标 VPN-instance，并配置对应地址族的 RD、RT 和 `vxlan vni`；
- 对应 BGP VPN-instance IPv4/IPv6 地址族已配置 `advertise l2vpn evpn`；
- 待发布前缀已通过直连、静态或动态路由进入该 VPN-instance。

同一 VNI 不能同时配置静态 head-end peer 和 `protocol bgp`。所有 BGP EVPN VNI 使用
同一个 NVE 源地址及 underlay VPN-instance；每个 VNI 只能由一个 NVE 接口拥有。


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
