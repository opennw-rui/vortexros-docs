# 启停与保存

## 交换实例的撤销与保存

`enable switch` 创建交换实例及默认 VLAN 1。关闭前需撤销成员口、Vlanif、非默认 VLAN，以及 VLAN 1 上显式配置的描述或 QoS；存在这些依赖时命令会拒绝。`undo enable switch` 同时清除隐式 VLAN 1 和派生桥域，保存后不会留下无法回放的孤立 `vlan batch 1`。

本轮真实终端执行启用、提交、关闭、提交、保存，再执行 `apply config`，回放成功；保存文件不含 `enable switch` 或 `vlan batch`。原问题在同一流程的保存回放阶段实际失败，修后已复测。未撤销显式 VLAN 配置时拒绝关闭的回归也保留。



[功能目录](../vlan.md) · [命令参数](../reference/vlan.md)
