# 配套 VPP

VPP负责DPDK接口和需要VPP的数据面功能。当前配套版本为26.10.7+vortexros-vpp；五个运行包应来自同一配套版本，统一安装器会完成组件匹配。

## 对用户可见的行为

- 接口、路由、VLAN、隧道和策略由VortexROS CLI统一配置。
- LLDP按选定接口发布邻居信息；接口限速按配置的速率和突发量处理报文。
- 二层MAC同步、EVPN业务及MPLS标签在创建、修改和撤销时与当前配置保持一致。
- Flow Steering仅在满足多worker条件时激活，运行状态可通过CLI查询。
- 硬件卸载能力由网卡和驱动决定，Supported与Active含义不同。

## 变更和恢复

先使用`display dataplane`检查当前数据面归属及状态。CPU、内存、队列等参数的生效要求见[数据面](../operator/dataplane.md)。按提示保存后再执行`reset dataplane`；重建数据面会影响承载业务。

恢复后检查接口、协议邻居、FIB和业务地址。若某个业务仍未恢复，按该功能的[故障排查](../troubleshooting/index.md)定位，避免反复重启设备。

VPP上游资料见[FD.io发布说明](https://raw.githubusercontent.com/FDio/vpp/v26.10/docs/aboutvpp/releasenotes/v26.10.rst)，性能资料见[性能参考](performance.md)。上游软件能力不等于VortexROS已开放的CLI，以本手册为准。
