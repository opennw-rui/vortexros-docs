# 支持矩阵

VortexROS 0.28 开发版 Debug 9 的单文件安装器适用于 **Ubuntu 26.04 amd64**。默认从 Linux 数据面启动。配套 VPP、FRR 版本见[软件组成](02-backends.md)，CPU、网卡和虚拟机路径见[支持的硬件](hardware.md)。

| 使用目标 | Linux 数据面 | VPP 数据面 |
| --- | --- | --- |
| 本地 AAA、管理 SSH 与 sudo | OpenSSH 认证，VortexROS 受管账号与角色投影到 Linux | 同样按 AAA 角色授权，管理口归属另行规划 |
| 系统时间、主机 DNS | 由 Ubuntu 管理 | 由 Ubuntu 管理 |
| 三层接口、IPv4／IPv6 静态路由、VPN 实例 | 使用 Linux 接口及路由表 | VPP 转发，按功能与 Linux 同步 |
| BGP、OSPF、OSPFv3、IS‑IS、RIP／RIPng | FRR 提供控制面，实际路由从 Linux 核对 | FRR 提供控制面，还需核对 VPP FIB |
| DHCPv4／v6、SNMP | Linux 主机服务，按接口和功能配置 | 仍由 Linux 服务提供，业务口需有相应的 Linux/LCP 路径。SNMP 系统对象和 VPP 接口计数来源不同 |
| 接口 ACL、MQC、NAT Policy | 此处列出的 VortexROS 转发策略使用 VPP | 使用配套 VPP 插件，按功能页确认接口类型和方向 |
| WireGuard、AmneziaWG、静态 VXLAN、VXLAN EVPN、MPLS L3VPN | 本手册的实现和案例使用 VPP | 使用配套 VPP，EVPN／MPLS L3VPN 另需 FRR 控制面 |

VPP 数据面是否可用与某张物理网卡是否能由 DPDK 接管分别核对。案例中的 AF_PACKET/veth、memif 证明对应实验路径；实际 PCI 网卡还需核对驱动、端口链路、MTU 和硬件卸载。具体功能的拓扑和实测结果见[配置案例](../examples/index.md)。

Debian、Arm64 和其他虚拟化平台的 VortexROS 安装包验收目前没有收录。现场新增硬件可沿用[硬件验收](08-hardware-acceptance.md)的检查顺序。
