# 交换端口

Ethernet 和 Eth-Trunk 可按业务需要配置为 Access、Trunk 或 Hybrid。端口模式、VLAN 成员和 PVID 决定报文准入与出方向标签，不需要额外配置 Linux 网桥。

~~~{toctree}
:maxdepth: 1

access
trunk
hybrid
~~~

| 模式 | VLAN 成员 | 无标签报文 | 出方向标签 |
|---|---|---|---|
| Access | 一个默认 VLAN | 归入默认 VLAN | 不带该 VLAN 标签 |
| Trunk | 允许列表 | 归入已允许的 PVID | PVID 不带标签，其余 VLAN 带标签 |
| Hybrid | tagged / untagged 列表 | 归入已加入成员列表的 PVID | 按各 VLAN 的 tagged / untagged 设置 |
| dot1q-tunnel | 简单 QinQ 服务 VLAN | 作为客户侧报文承载 | 见[QinQ](../qinq.md) |

所有交换模式都必须先启用交换功能，并创建所需 VLAN。Vlanif、Vbdif 和三层端口不作为普通交换成员。

## 查询

```text
display vlan
display vlan 100
display mac-address vlan 100
display interface brief
```

`display vlan` 中，U/D 表示成员接口 Up/Down，TG/UT 表示带标签/不带标签。MAC 显示使用用户配置的父接口名称，便于定位接入端口。

以下为 VLAN 100 的实际查询输出节选，两端都设置为该 VLAN 的无标签成员：

```text
VID  Type    Status  MAC-LRN  Description      Ports
----------------------------------------------------------------------------
100  common  enable  enable   VLAN 100         UT:Ethernet0(U)  Ethernet1(U)

MAC Address       VLAN/VSI/BD                    Learned-From        Type
-------------------------------------------------------------------------------
0200-00a1-0001    100/-/-                        Ethernet0           dynamic
```

## 网关与 MTU

Vlanif 需要所属 VLAN 至少有一个有效成员端口 Up，且接口没有 shutdown；三层 Protocol Up 还需要有效 IP 地址。成员全部不可用时自动 Down，恢复后自动 Up，见[Vlanif 网关](gateway.md)。

显式二层子接口未配置 MTU 时使用父端口的硬件 MTU 能力，三层子接口缺省为 1500。通过 `display interface` 核对 MTU。物理接口从三层切换为交换端口，会改变现有业务的接口归属，提交前应撤销冲突的三层配置。

[功能目录](../vlan.md) · [命令参考](../reference/vlan.md)


## 切换端口类型

Access、Trunk、Hybrid 之间转换前，须先恢复旧模式的默认 VLAN 状态，
并撤销该端口的灵活 QinQ 规则。系统不会为了切换模式而擅自清空业务 VLAN。
重复输入相同的显式 `port link-type` 不改变已配置的 VLAN。

| 当前模式 | 可以切换时的 VLAN 状态 | 常用清理命令 |
|---|---|---|
| Access | 默认 VLAN 1 | `undo port default vlan` |
| Trunk | PVID 1，允许集合仅 VLAN 1 | 撤销其他允许项、恢复 VLAN 1、`undo port trunk pvid vlan` |
| Hybrid | PVID 1，仅 VLAN 1 为 untagged，无 tagged 业务及 QinQ 规则 | 撤销业务成员和规则、恢复 untagged VLAN 1、`undo port hybrid pvid vlan` |

清空列表不等于恢复默认。特别是 `undo port trunk allow-pass vlan all`
会将 VLAN 1 也撤销，此时仍不能切换模式。应显式重新允许 VLAN 1。
Hybrid 撤销 untagged VLAN 1 后，同样要先恢复它。

例如，将只允许 VLAN 100、PVID 为 100 的 Trunk 改为 Access：

~~~text
system-view
interface Ethernet0
 undo port trunk pvid vlan
 port trunk allow-pass vlan 1
 undo port trunk allow-pass vlan 100
 port link-type access
 port default vlan 100
#
~~~

再执行 `commit`。若允许列表中还有其他非默认 VLAN，也须先撤销。
Hybrid 若将 VLAN 1 配成 tagged，应先撤销该 tagged 成员，再恢复 untagged VLAN 1。
接口描述等与链路模式无关的配置无需删除。

灵活 QinQ 的规则也属于模式相关业务配置，切换前先按
[灵活 QinQ](../qinq-flexible.md)撤销。切换并提交后会重新配置相应的二层接入，
业务可能短暂中断；应在变更后检查成员、实际流量，再保存。

## 与其他功能组合

Ethernet 和 Eth-Trunk 均可使用交换端口配置。聚合成员本身不承担独立三层接口配置；VLAN 配置放在 Eth-Trunk 上，Vlanif 是对应 VLAN 的三层网关。保存后，数据面重置及系统启动会恢复成员、VLAN 和网关配置。

本页对应的报文验证中，Access 的无标签、VID 0、同 PVID 单标签报文均能通过；VID 111 和叠加标签作为拒绝对照未通过。Hybrid 的 VLAN 100 无标签、VLAN 200 带标签业务均完成双向 3/3 转发；将 PVID 配成 tagged 后，优先级标签的 PCP/DEI 能保留到输出标签。移除 VLAN 100 后，该业务停止，VLAN 200 继续转发。独立的 L2/L3 子接口、简单 QinQ、Eth-Trunk 及接口 ACL/MQC 对照均有实际报文验证，不代表任意组合和所有负载已穷举。
