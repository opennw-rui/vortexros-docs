# Debug 6

Debug 6 更新 VortexROS 控制层和配套 VPP。统一安装包包含 FRR 1.10-dev 与 Kea 3.0.3-1+vortexros1。

- 对数据面接管失败后的恢复进行修正。具备一条仍可用的 IPv6 ECMP 路径时，恢复过程补回缺失的路径并保留权重。配置已保存而数据面尚未恢复时，操作结果分别报告这两个状态。
- Linux 数据面允许按全部受管接口、接口、IPv4 地址或接口与地址的组合清除动态 ARP 表项。预配置接口同名重建后重新应用其受管属性。
- 含引号或反斜杠的主机名可以保存并回放。删除 VPN 仅清理由此次删除变空的相关 QoS 或 NAT 策略。
- 对 Kea 的状态、租约和配置控制请求遵循操作期限。
- SNMP 恢复公开接口对应的 LCP 诊断行。采样过期时接口表和接口数量同时不可用。
- VPP 的 LCP 遇到 Netlink 通知订阅失败时，重新建立订阅并同步内核状态。

升级时采用[统一安装包](../installation/07-upgrade-uninstall.md)。本版更新 VPP，升级期间数据面会重启。升级后可用 `display version` 查看组件版本，使用 `display service verbose` 核对服务状态。
