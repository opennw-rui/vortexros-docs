# 默认行为

以下为 Debug 9 空白 Ubuntu 首装时的产品默认行为。已有设备的 Running、启动配置及 Ubuntu 管理策略以当前设备查询为准。

| 项目 | 默认行为 | 核对位置 |
| --- | --- | --- |
| 系统名和配置 | CLI 系统名为 `VortexROS`，出厂配置没有预建业务 VLAN、隧道或动态路由邻居 | `display current-configuration` |
| 网卡归属 | 物理网卡由 Linux 驱动持有。配置为 `mode dpdk` 的设备在数据面重置时接管 | `display dataplane interfaces` |
| 服务 | 安装器启动 VortexROS 管理的服务，屏蔽发行版独立的 `vpp.service` 和 `frr.service`。VPP 是否运行取决于实际数据面配置 | `display service verbose` |
| 远程管理 | 没有预置受管用户和密码。Linux 救援账号使用 `sudo vortexros`；创建的受管账号通过 OpenSSH 直接进入 CLI，按 AAA 角色授权 | [本地账号与 SSH](../operator/aaa.md) |
| 网络服务 | DHCP 服务端、SNMP 按配置启用。DHCP 客户端和中继按接口配置 | [DHCP](../operator/dhcp.md) · [SNMP](../operator/snmp.md) |
| 默认路由域 | 未绑定 VPN 实例的接口和路由使用默认实例。Linux main 表号 254，VPP 默认表号 0 | [VPN 实例](../operator/vrf.md) |
| 邻居和 MAC 容量 | IPv4 邻居、IPv6 邻居和 VPP 全局 MAC 学习上限各为 102400。VPP MAC 启动容量在保存并重置后应用 | `display dataplane tables` |

## 配置何时生效

- 编辑进入本会话的 Candidate。用 `display configuration candidate` 核对内容，`commit` 提交到 Running，并用 `display health` 核对运行状态。
- `save` 将 Running 写入启动 CFG。用 `display configuration storage` 核对保存状态。
- 驱动接管、VPP 启动参数和 MAC 学习启动容量按[数据面配置](../operator/dataplane.md)保存并执行 `reset dataplane`。CPU 隔离等内核启动设置按命令提示安排系统重启。
