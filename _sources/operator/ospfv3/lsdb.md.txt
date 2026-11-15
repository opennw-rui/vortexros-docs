# LSDB 与撤销核对

## LSDB 的作用域

`display ospfv3 ... lsdb` 按 Area、Area + Interface 和 AS External Database 分区。相同 Link State ID 可以合法地出现在不同作用域，不能全局去重。后端为同一个 LSA 的多个前缀生成多条摘要记录时，CLI 将同一作用域中的同一 LSA 显示一次；`Total LSAs` 统计 LSA，不统计它包含的前缀数。本轮多区域实际 CLI 为 29，与原生 JSON 中按作用域统计的 29 个身份一致。

LSA Age 达到 3600 的记录可能正在冲刷，显示它不等于该外部前缀仍在转发表中。撤销验收同时查询协议路由和系统路由表。区域汇总、NSSA 在线切换及实际结果见[多区域案例](../../examples/ospfv3.md#多区域汇总与nssa)。

[功能目录](../ospfv3.md) · [命令参数](../reference/ospfv3.md)
