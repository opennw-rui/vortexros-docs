# 插件加载

适用版本：VortexROS 0.30-dev，配套 VPP 26.10.8。

自动生成的启动配置默认禁止加载未列出的插件，仅启用 VortexROS 支持功能及其依赖。安装包仍包含配套插件；“已安装”不表示“已加载”。

| 插件 | 用途 |
|---|---|
| linux_cp、linux_nl、tap | Linux 接口配对、路由与邻居同步 |
| abf、acl | 无状态 ACL 和按策略选路 |
| af_packet | Linux 以太网接口接入 |
| amneziawg、wireguard、wg_lcp | WireGuard、AmneziaWG 及 Linux 接口联动 |
| crypto_sw_scheduler | WireGuard 和 AmneziaWG 的异步加密调度 |
| gre、ipip | GRE 和 IP-in-IP 隧道 |
| policer | 接口限速 |
| flow_steering | 流量分发 |
| lacp | 链路聚合控制协议 |
| osi、ppp | IS-IS 的 OSI 报文接入及其协议解析依赖 |
| lldp | 链路层邻居发现 |
| memif | 共享内存虚拟接口 |
| mqc、mss_clamp、nat_policy | 流量策略、TCP MSS 调整与 NAT 策略 |
| urpf | 源地址反向路径检查 |
| vrrp | 虚拟路由器冗余协议 |
| vxlan | VXLAN 隧道 |
| dpdk | 仅配置 DPDK 设备时加载，负责 PCI 网卡接管 |

产品功能插件保持可用，以便后续通过 CLI 配置 ACL、隧道或协议时无需为加载插件额外重启。未配置的功能不会因此自动启用。DPDK 则随设备配置加载；没有 DPDK 设备时，不加载该插件，也不生成 DPDK 设备配置段。

接口、路由、桥域、MPLS 和 GSO 等由配套 VPP 的基础能力提供，不需要在插件表中重复添加名称。

使用 `reset dataplane` 重新生成并应用启动配置。已有设备升级后，新的加载列表在下一次按新启动配置启动数据面时生效；升级本身不会擅自改变现有接口模式。勿通过手工修改自动生成文件来保存配置，应使用 CLI 和 `save`。
