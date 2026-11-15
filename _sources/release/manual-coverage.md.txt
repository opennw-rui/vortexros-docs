# 手册覆盖

## 对照基线

本次文档对照v0.29-dev工作树及统一run1候选包：控制层0.29~dev+run1、VPP26.10.7、FRR1.7-dev、Kea3.0.3修复包。工作树仍有未提交改动，源码身份由完整文件清单记录，不能只用HEAD代表全部源码。最终包的新验收与沿用功能证据分别见[验证记录](cli-validation.md)。

逐条命令参考覆盖 **820条规范路径、953个视图注册形式**，补充 **2227行参数/子命令说明**。这些数字统计实际 CLI Registry，运行时已有对象名称不是固定命令。

## 如何查阅

功能页按使用任务展开，命令参考定义语法、参数位置及可选项，案例给出具体拓扑和真实结果。功能说明与案例相互链接，避免维护两份完整命令定义。NAT 和 EVPN 的详细目录是这种组织方式的示例。

[下载逐条 CLI 对照表](../_static/cli-coverage.tsv)列出每条路径对应页面、视图形式数及已有终端记录。表中“观察到命令输入”不等同于该命令全部参数组合或所有流量路径均通过。

| 功能 | 命令路径 | 参数参考 | 功能说明 |
|---|---:|---|---|
| 本地账号 | 18 | [逐条参数](../operator/reference/aaa.md) | [配置指南](../operator/reference/../aaa.md) |
| ACL | 7 | [逐条参数](../operator/reference/acl.md) | [配置指南](../operator/reference/../acl.md) |
| AmneziaWG | 45 | [逐条参数](../operator/reference/amneziawg.md) | [配置指南](../operator/reference/../amneziawg.md) |
| BFD | 12 | [逐条参数](../operator/reference/bfd.md) | [配置指南](../operator/reference/../bfd.md) |
| BGP | 34 | [逐条参数](../operator/reference/bgp.md) | [配置指南](../operator/reference/../bgp.md) |
| 桥域 | 13 | [逐条参数](../operator/reference/bridge-domains.md) | [配置指南](../operator/reference/../bridge-domains.md) |
| CLI | 12 | [逐条参数](../operator/reference/cli.md) | [配置指南](../operator/reference/../01-cli.md) |
| 数据面 | 29 | [逐条参数](../operator/reference/dataplane.md) | [配置指南](../operator/reference/../dataplane.md) |
| DHCP | 88 | [逐条参数](../operator/reference/dhcp.md) | [配置指南](../operator/reference/../dhcp.md) |
| 路由通用命令 | 38 | [逐条参数](../operator/reference/dynamic-routing.md) | [配置指南](../operator/reference/../01-cli.md) |
| EVPN | 9 | [逐条参数](../operator/reference/evpn.md) | [配置指南](../operator/reference/../11-vxlan-evpn.md) |
| GRE | 2 | [逐条参数](../operator/reference/gre.md) | [配置指南](../operator/reference/../gre.md) |
| Ethernet 与接口 | 33 | [逐条参数](../operator/reference/interfaces.md) | [配置指南](../operator/reference/../ethernet.md) |
| 路由表与 FIB | 7 | [逐条参数](../operator/reference/ip-routing.md) | [配置指南](../operator/reference/../routing-tables.md) |
| RA 与 SLAAC | 6 | [逐条参数](../operator/reference/ipv6-autoconfig.md) | [配置指南](../operator/reference/../ipv6-autoconfig.md) |
| IS-IS | 35 | [逐条参数](../operator/reference/isis.md) | [配置指南](../operator/reference/../isis.md) |
| 链路聚合 | 5 | [逐条参数](../operator/reference/link-aggregation.md) | [配置指南](../operator/reference/../link-aggregation.md) |
| LLDP | 7 | [逐条参数](../operator/reference/lldp.md) | [配置指南](../operator/reference/../lldp.md) |
| MPLS 与 LDP | 14 | [逐条参数](../operator/reference/mpls.md) | [配置指南](../operator/reference/../ldp.md) |
| MQC | 22 | [逐条参数](../operator/reference/mqc.md) | [配置指南](../operator/reference/../mqc.md) |
| TCP MSS | 2 | [逐条参数](../operator/reference/mss.md) | [配置指南](../operator/reference/../mss.md) |
| NAT | 66 | [逐条参数](../operator/reference/nat.md) | [配置指南](../operator/reference/../nat.md) |
| ARP 与 ND | 19 | [逐条参数](../operator/reference/neighbors.md) | [配置指南](../operator/reference/../neighbors.md) |
| 诊断与恢复 | 22 | [逐条参数](../operator/reference/operations.md) | [配置指南](../operator/reference/../09-operations.md) |
| OSPF | 35 | [逐条参数](../operator/reference/ospf.md) | [配置指南](../operator/reference/../ospf.md) |
| OSPFv3 | 22 | [逐条参数](../operator/reference/ospfv3.md) | [配置指南](../operator/reference/../ospfv3.md) |
| 策略通用命令 | 8 | [逐条参数](../operator/reference/policy.md) | [配置指南](../operator/reference/../01-cli.md) |
| 前缀列表 | 7 | [逐条参数](../operator/reference/prefix-lists.md) | [配置指南](../operator/reference/../prefix-lists.md) |
| QoS | 2 | [逐条参数](../operator/reference/qos.md) | [配置指南](../operator/reference/../qos.md) |
| RIP | 10 | [逐条参数](../operator/reference/rip.md) | [配置指南](../operator/reference/../rip.md) |
| RIPng | 7 | [逐条参数](../operator/reference/ripng.md) | [配置指南](../operator/reference/../ripng.md) |
| 静态路由组 | 24 | [逐条参数](../operator/reference/route-groups.md) | [配置指南](../operator/reference/../route-groups.md) |
| 路由策略 | 33 | [逐条参数](../operator/reference/route-policy.md) | [配置指南](../operator/reference/../route-policy.md) |
| SNMP | 27 | [逐条参数](../operator/reference/snmp.md) | [配置指南](../operator/reference/../snmp.md) |
| 静态路由 | 4 | [逐条参数](../operator/reference/static-routing.md) | [配置指南](../operator/reference/../static-routing.md) |
| 系统 | 14 | [逐条参数](../operator/reference/system.md) | [配置指南](../operator/reference/../02-system-services.md) |
| Tunnel 通用命令 | 20 | [逐条参数](../operator/reference/tunnels.md) | [配置指南](../operator/reference/../tunnel-settings.md) |
| uRPF | 6 | [逐条参数](../operator/reference/urpf.md) | [配置指南](../operator/reference/../urpf.md) |
| VLAN | 22 | [逐条参数](../operator/reference/vlan.md) | [配置指南](../operator/reference/../vlan.md) |
| VPN 实例 | 15 | [逐条参数](../operator/reference/vrf.md) | [配置指南](../operator/reference/../vrf.md) |
| VRRP | 6 | [逐条参数](../operator/reference/vrrp.md) | [配置指南](../operator/reference/../vrrp.md) |
| VXLAN | 8 | [逐条参数](../operator/reference/vxlan.md) | [配置指南](../operator/reference/../vxlan.md) |
| WireGuard | 5 | [逐条参数](../operator/reference/wireguard.md) | [配置指南](../operator/reference/../wireguard.md) |

## 实际证据的使用边界

- NAT：接口/池 PAT、NO-PAT、静态、DNAT、Twice NAT、No-NAT、回流均复用真实 CLI 和 HTTP 端点实验；会话、配额和撤销的证据分开写明。
- EVPN：L2VPN 两个 VNI 的相互隔离、双栈 Type-5、ESI 创建/撤销和单网关 Anycast 分别记录。三PE全互联All-Active另外补验了双成员下一跳组、两条接入链路分别故障、恢复、保存冷回放和撤销；四PE RR模板不冒充本轮实测。
- 其他协议、子接口、隧道、MQC、DHCP 等复用对应案例的原始输出。本文不把静态语法覆盖扩展为全部网络组合的验证。
- 0.29-dev 最终统一包的 RIP 端点重建、Zebra 重放、升级和回退另见[验证记录](cli-validation.md)。
- 仅补验缺证据的All-Active、6PE及其发现的问题，并执行ACL改为纯无状态后的定向CLI；没有重新执行全量产品测试、CI、真机升级或已通过且未受影响的流量测试。

## 仍须区分的范围

各页明示的组网模板、单节点增量操作与完整多节点验收不同；单次连通性也不是吞吐、满表容量或无损收敛保证。当前没有把缺少原始输出的高级组合填成“真实输出”。

## 功能树组织规则

复合功能按业务能力分子页：协议激活/发布/查询，SNMP协议/来源/通知，ACL两族/规则/绑定，MQC分类/动作/绑定，隧道Profile/Peer/生命周期等。MSS、uRPF、GRE、IP-in-IP、LLDP等单一功能保留独立末级页面，不为增加层级新建空目录；其参数变化仍在对应功能与逐条命令参考中展开。
