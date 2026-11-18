# NO-PAT

只改变源地址，保留源端口或 ICMP identifier。适用于不允许改变源端口、且映射不会冲突的业务；不是多主机共享端口空间的 PAT 替代品。

## 行为与限制

接口来源和池来源二选一。修改现有 action 后，用新连接验证；旧会话仍保留原有映射。

此功能需要 VPP。配置写入 Candidate，`commit` 后参与下发，`save` 保存已提交配置；重启后从启动 CFG 恢复。缺省不创建 NAT 策略或接口绑定。

## 配置、检查与撤销

[完整案例](../../examples/nat/no-pat.md)给出三台 VortexROS 的配置、策略、查询及撤销顺序。只改变地址，保留 TCP/UDP 源端口或 ICMP 标识符；发生映射冲突时不能用它代替 PAT。

提交后查询 display nat-policy name、interfaces、statistics 和 sessions。先确认策略绑定及命中，再检查原始与转换后的地址；TCP/UDP 还需核对端口，ICMP 则核对标识符。旧会话可能保留原映射，修改策略后用新连接检查。

撤销先解除接口绑定，再删除策略及不再引用的对象，commit 后确认绑定和目标规则消失；需要持久保留时 save。其他策略、共享地址和路由应保留。

[对象与规则](objects.md) · [会话与统计](sessions.md) · [命令参考](../reference/nat.md)
