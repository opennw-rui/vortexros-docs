# EVPN

本章说明如何使用 BGP EVPN 建立 VXLAN 覆盖网络。当前支持单归属和 All-Active
多归属 L2VNI，以及 L3VNI：BGP 发布和接收 EVPN Type-1 Ethernet A-D、Type-2
MAC/IP、Type-3 Inclusive Multicast、Type-4 Ethernet Segment 与 Type-5 IP Prefix
路由，用于发现业务成员、学习远端 MAC/IP、传递租户前缀及协调多归属转发。

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

## 工作原理与业务选择

EVPN 的基本机制见 RFC 7432，VXLAN 承载扩展见 RFC 8365。BGP 负责分发可达性，VXLAN 负责客户报文封装，两者的运行状态分别检查。

| 对象或路由 | 业务用途 |
| --- | --- |
| L2VNI / 桥域 | 延伸客户二层网络及 MAC 学习范围 |
| L3VNI / VPN | 承载租户三层互联 |
| Type-2 | MAC/IP 可达性 |
| Type-3 | 广播、未知单播和组播的业务成员发现 |
| Type-1 / Type-4 | 多归属接入及 Ethernet Segment 信息 |
| Type-5 | 租户 IP 前缀 |

RD 区分路由身份，RT 集合决定导入导出，VNI 标识数据面业务。相同 L3VNI 的 IPv4、IPv6 EVPN 共用一套 RD 及导入/导出 RT 集合，RT 可配置多个；普通 MPLS VPN 的两族配置不因此合并。

多归属还需一致的 ESI、客户侧聚合和 DF 选举条件。看到两条 Type-4 或两个下一跳只证明相关控制信息存在，仍须核对客户 MAC、单播与 BUM 流量、链路故障后的转发和恢复。具体双端配置及撤销见独立案例。

## 业务激活条件

先满足[VXLAN 的激活条件](vxlan.md#激活条件)，再检查 BGP EVPN 邻居、VNI 对应的 RD/RT 及远端路由导入。二层业务还需接入口及 MAC 可达；三层业务需租户 VPN、L3VNI、相应 Type-5 路由和回程路径。NVE Up 或 BGP Established 均不能单独证明所有租户业务可用。Vbdif 网关的状态还取决于其[桥域成员](bridge-domains.md#vbdif-激活条件)。
