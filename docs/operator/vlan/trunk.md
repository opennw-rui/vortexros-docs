# Trunk

Trunk 用于连接交换设备或携带多个 VLAN 的主机。PVID 决定无标签报文所属的 VLAN；允许列表决定哪些 VLAN 可以转发，两者独立。

| 条件 | 入方向 | 出方向 |
|---|---|---|
| VLAN 在允许列表，且等于 PVID | 接收无标签、VID 0 或对应标签的报文 | 去除本 VLAN 的外层标签 |
| VLAN 在允许列表，且不等于 PVID | 接收对应标签的报文 | 携带本 VLAN 的外层标签 |
| VLAN 不在允许列表 | 不接收该 VLAN 业务 | 不转发该 VLAN 业务 |

缺省 PVID 为 1，缺省允许 VLAN 1。`undo port trunk allow-pass vlan all` 清空允许列表，不更改 PVID；之后必须显式允许所需 VLAN。PVID 不在允许列表时，无标签报文也不能通过。

## 配置

两端设备的 Ethernet0 互连，VLAN 100 作为无标签业务，VLAN 200 携带标签。两端都执行：

```text
system-view
enable switch
vlan batch 100 200
interface Ethernet 0
 portswitch
 port link-type trunk
 undo port trunk allow-pass vlan all
 port trunk allow-pass vlan 100 200
 port trunk pvid vlan 100
#
commit
```

通过 `display vlan 100` 核对 UT，通过 `display vlan 200` 核对 TG。分别在两端相同 VLAN 中放置终端，验证双向流量；未允许的 VLAN 不应连通。PVID 或允许列表修改会影响正在承载的业务。

## QinQ 与子接口

普通 Trunk 使用外层 VLAN 选择业务，可透明携带其后已有的客户标签。需要独立的 QinQ 服务分类时，使用[显式二层子接口](../qinq.md)；不应让显式子接口与 Trunk 的同一外层 VLAN 重叠。简单 QinQ 的 `dot1q-tunnel` 端口拥有整个客户侧分类空间，不能同时用作普通 Trunk。

## 撤销

```text
system-view
interface Ethernet 0
 undo port trunk allow-pass vlan 200
 undo port trunk pvid vlan
#
commit
```

撤销 PVID 后恢复为 1，但不会自动将 VLAN 1 加回允许列表。完全恢复三层接口时使用 `undo portswitch`。

[交换端口](ports.md) · [命令参考](../reference/vlan.md)
