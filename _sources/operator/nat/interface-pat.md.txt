# 接口 PAT

以出口接口地址作为转换后的源地址，同时分配源端口，使多个内部连接共享一个出口 IPv4 地址。接口地址变化会影响新建映射；不要用它实现固定地址的一对一发布。

## 参数和限制

规则中配置 `action snat pat interface`，接口只能绑定 **outbound**。接口 PAT 缺省端口范围为 10000–65535，可在系统视图配置 `nat-policy interface-pat-range LOW-HIGH`。接口和上游必须有可用路由；NAT 不代替 ACL 或下一跳解析。

## 配置、检查与撤销

[完整案例](../../examples/nat-pat.md)给出三台 VortexROS 的配置、策略、查询及撤销顺序。使用出口接口地址，有状态流量同时分配转换标识；仅支持相应出方向绑定。

提交后查询 display nat-policy name、interfaces、statistics 和 sessions。先确认策略绑定及命中，再检查原始与转换后的地址；TCP/UDP 还需核对端口，ICMP 则核对标识符。旧会话可能保留原映射，修改策略后用新连接检查。

撤销先解除接口绑定，再删除策略及不再引用的对象，commit 后确认绑定和目标规则消失；需要持久保留时 save。其他策略、共享地址和路由应保留。

[对象与规则](objects.md) · [会话与统计](sessions.md) · [命令参考](../reference/nat.md)
