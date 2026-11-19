# VLAN

使用 VLAN 划分二层广播域，需要三层网关时创建 Vlanif。

[命令参考](reference/vlan.md) · [配置案例](../examples/vlan-gateway.md)

## 工作原理与端口选择

VLAN 按 IEEE 802.1Q 将同一交换网络划分为独立广播域。标签中的 VID 标识业务 VLAN；PVID 用于端口对无标签流量的归属判定，不代表自动允许所有带标签报文。

| 端口模式 | 典型用途 | 需要规划 |
| --- | --- | --- |
| Access | 对接单一业务终端 | 默认 VLAN 与标签准入 |
| Trunk | 交换设备间携带多个 VLAN | 允许列表与 PVID |
| Hybrid | 同端口混合带标签/去标签业务 | 各 VLAN 的出口标签方式 |

通信两端应使用一致的 VLAN 归属和出口标签方式。PVID 与允许 VLAN 列表分开维护；清空允许列表不会自动改变 PVID。跨 VLAN 通信需要三层路由，通常使用相应 Vlanif 网关。

变更可能改变广播域、MAC 学习和网关可达性。先核对端口成员和标签准入，再检查 MAC、网关及终端业务。不要因一个无标签 ping 可通，就认定其他带标签 VLAN 也符合隔离要求。

~~~{toctree}
:maxdepth: 2

vlan/ports
vlan/gateway
vlan/lifecycle
vlan/service-bd
~~~

## 网关激活

Vlanif 未 shutdown、所属 VLAN 至少有一个实际成员端口处于管理 Up 且链路 Up 时，PHY 才能 Up；还需有效网关 IP 地址，三层 Protocol 才能 Up。全部成员不可用时自动 Down，恢复后自动 Up。详见[Vlanif 网关](vlan/gateway.md)。
