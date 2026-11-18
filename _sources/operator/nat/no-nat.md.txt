# No-NAT

匹配指定流量而不修改地址和端口。可用作比转换规则更优先的豁免；它不是丢弃动作，也不能替代路由或 ACL。

## 行为与限制

No-NAT 是无状态动作，因此没有会话条目是正常现象。豁免放在较小 priority 的规则中，先于覆盖同一流量的转换规则；未显式 priority 时取规则 ID。

此功能需要 VPP。配置写入 Candidate，`commit` 后参与下发，`save` 保存已提交配置；重启后从启动 CFG 恢复。缺省不创建 NAT 策略或接口绑定。

## 配置、检查与撤销

[完整案例](../../examples/nat/no-nat.md)给出三台 VortexROS 的配置、策略、查询及撤销顺序。匹配后不转换，不是拒绝动作。仍需正确的双向路由；通常放在更早命中的规则中作为豁免。

提交后查询 display nat-policy name、interfaces、statistics 和 sessions。先确认策略绑定及命中，再检查原始与转换后的地址；TCP/UDP 还需核对端口，ICMP 则核对标识符。旧会话可能保留原映射，修改策略后用新连接检查。

撤销先解除接口绑定，再删除策略及不再引用的对象，commit 后确认绑定和目标规则消失；需要持久保留时 save。其他策略、共享地址和路由应保留。

[对象与规则](objects.md) · [会话与统计](sessions.md) · [命令参考](../reference/nat.md)
