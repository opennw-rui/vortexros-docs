# 0.30-dev Debug 8

本页说明本轮变化及相应的操作入口。启用功能前通过 `display version` 核对配套组件，使用整包时按[升级与回退](../installation/07-upgrade-uninstall.md)先查看预检及模拟结果。

## 设备授权

首次修改配置前完成离线授权。试用自首次激活起有 72 小时的配置期，客户正式授权适用于单台设备长期使用，内部授权用于内部测试。用 `display license` 核对授权类型、有效期和配置权限。[设备授权](../installation/license.md)

## 改动涉及的功能

| 功能 | 行为与使用入口 |
| --- | --- |
| MPLS L3VPN | 命名 VPN BGP 地址族默认过滤重分发来源中的缺省路由。每个地址族可用 `default-route imported` 开启，并能独立撤销。核对接收 PE 的 VPN 表和普通前缀。[MPLS L3VPN](../operator/l3vpn.md) |
| EVPN 多归属 | 恢复原 ESI 后，已有客户 MAC 可重新随 Type-2 通告，两台接入 PE 重新进入同一下一跳组。[撤销与恢复 ESI](../examples/evpn/esi.md) |
| EVPN 任播和租户变更 | 新建 VNI 时网关通告随业务配置下发。从已有 L2 VNI 迁移租户后，分别检查旧、新租户的 VNI 和路由。[EVPN 任播网关](../operator/evpn/anycast.md) · [EVPN 生命周期](../operator/evpn/lifecycle.md) |
| IPv4 次地址与 ARP | 撤销同网段次地址后，剩余地址仍覆盖邻居，已学习动态 ARP 保留。撤销整个前缀仍清理其动态邻居。[接口地址与 ARP](../operator/neighbors/configuration.md) |
| OSPF | 支持从接口的显式 area 切换到 network 激活。撤销网络后，仍配置的接口选项可保存并在下次启动时读回。[OSPF 配置案例](../examples/ospf.md) |
| Eth-Trunk 与 uRPF | 接口启用 uRPF 时会阻止不适用的聚合配置，撤销 uRPF 后可按正常接口条件加入聚合。[uRPF](../operator/urpf.md) · [聚合案例](../examples/lacp.md) |
| VRRP | IPv6 VIP 邻居解析使用虚拟 MAC。可从新客户端检查 VIP 和普通地址，切换后核对角色及实际访问。[VRRP 案例](../examples/vrrp.md) |
| NAT | 多条连续 NAT 规则在保存后的配置中保持各自的动作和参数。重新加载后核对规则顺序、命中与实际端点流量。[NAT](../operator/nat.md) |
| MQC 限速 | CAR 的 CIR 与 PIR 可分别显式填写单位，也可为二者使用相同单位。提交后核对策略配置和实际限速。[MQC](../operator/mqc.md) |
| 内核口和 DPDK 口 | 待生效的设备模式在实际切换前保留当前接口归属和已有地址。混合配置下看实际归属，准备启动切换时一并核对管理口。[后端规划](../installation/02-backends.md) · [DPDK 管理](../troubleshooting/dpdk-management.md) |
| 邻居、MAC 限额与大页 | 撤销后按实际默认容量或启动设置核对。保存和冷启动后重新检查接口及大页实际状态。[ARP 与 ND](../operator/neighbors.md) · [VPP 启动](../installation/05-vpp-startup.md) |
| 路由组与服务恢复 | 内容未变化的成功刷新会更新刷新时间。服务恢复后结合活动告警、历史告警和业务流量检查。[路由组](../operator/route-groups.md) · [系统管理](../operator/02-system-services.md) |
| 同版本整包安装 | 版本相同而包内容有变化时选择相应组件，内容一致时直接结束。设备需有与现场已安装内容匹配的旧包才能自动回退。[升级和回退](../installation/07-upgrade-uninstall.md) |

## 检验范围

全量阶段实际执行 852 条规范路径，其中 456 条完整通过、393 条按所测范围通过、3 条部分通过。三条部分通过涉及 ESI 两条路径和同网段次地址撤销，后续已针对修复完成真实 CLI 复验。命名 VPN 缺省路由新增两条路径并作双 PE 双栈复验，当前命令参考为 854 条。全量统计仍保留原执行范围，包含多设备隔离组网和代表性功能组合。

同版本整包复验覆盖旧版跳过、按内容安装、安装中断自动回退和相同内容再次运行。ARP 对照使用实际转发与抓包。ESI 检验包含静默撤销和恢复、Type-2、下一跳成员和双栈转发。MPLS 检验包含默认过滤、开启通告和撤销撤路，普通前缀全程保留。
