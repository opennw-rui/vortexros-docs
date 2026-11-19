# 配套 VPP

VPP负责DPDK接口和需要VPP的数据面功能。当前配套版本为26.10.9-debug2+vortexros-vpp；五个运行包应来自同一配套版本，统一安装器会完成组件匹配。

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

## 26.10.8 的主要变化

- 接口 ICMPv4 发送控制作用于本机生成的对应消息，不给普通转发增加 ICMP 策略检查；支持范围及封装限制见 [ICMP 发送控制](../operator/icmp-send.md)。
- Access、Trunk、Hybrid 的 PVID、VLAN 准入和标签转换统一处理；保留业务接口统计以及 QinQ 支持，见 [VLAN](../operator/vlan.md)。
- LLDP 在端口删除后清理邻居发送配置；Linux 接口错误通知不再因等待读取而阻塞数据面恢复。
- IPv6 同接口允许 SLAAC 前缀与 DHCPv6 主机地址共存；接口重建后按配置重新请求通告。
- 完善 Linux 广播路由、本机 EVPN 路由和 Path MTU 对象的创建、删除及恢复。
- 纳入流量分发、MQC、MSS 和 NAT Policy 的已验证批处理与解析优化；不以关闭 VLAN 准入或统计换取性能。
- 新生成的启动文件使用明确的插件加载列表，详见 [插件加载](../operator/dataplane/plugins.md)。

性能数字的条件、波动和适用范围见 [性能参考](performance.md)，不能将单个节点的收益当成整机吞吐提升。

## 26.10.9 的主要变化

- EVPN 已存在的远端下一跳组在数据面启动后恢复，避免 MAC 表指向空组而无法转发。此项不改变普通报文的转发节点。
- 接口自动链路本地 IPv6 地址撤销后，不再因接口状态同步保留额外地址引用；全局 IPv6 地址不受影响。
- 包含上述 26.10.8 的功能和优化，插件加载列表见 [插件加载](../operator/dataplane/plugins.md)。性能数据仍以各表注明的实际测试版本为准。


## 26.10.9 Debug 2

- 支持父接口灵活QinQ的客户VLAN集合，一个端口的同一服务VLAN共用业务对象。
- 回程广播和未知单播遵循对应客户集合的出口准入；接口统计和MAC学习保持可用。
- 修复带PCP/DEI的合法标签报文可能被出口准入错误丢弃的问题。
- 端口业务在服务桥域之间变更、重建和恢复后保留准入和FDB的服务VLAN归属。
- 该版本需要配套控制层，使用统一安装器一起更新，不单独替换旧控制层的VPP包。

配置、限制和完整案例见[灵活QinQ](../operator/qinq-flexible.md)，
性能条件和结果见[性能参考](performance.md)。
