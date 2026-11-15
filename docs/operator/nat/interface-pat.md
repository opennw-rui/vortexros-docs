# 接口 PAT

以出口接口地址作为转换后的源地址，同时分配源端口，使多个内部连接共享一个出口 IPv4 地址。接口地址变化会影响新建映射；不要用它实现固定地址的一对一发布。

## 参数和限制

规则中配置 `action snat pat interface`，接口只能绑定 **outbound**。接口 PAT 缺省端口范围为 10000–65535，可在系统视图配置 `nat-policy interface-pat-range LOW-HIGH`。接口和上游必须有可用路由；NAT 不代替 ACL 或下一跳解析。

## 完整配置与真实结果

[接口 PAT 案例](../../examples/nat-pat.md)给出两端 UDP 端点、地址集、端口集、统计、会话配额及撤销。该案例实际会话节选：

~~~text
host-p1a12/outbound  FIB:0 -> FIB:0  Policy:CLI-UDP(1996602227)/10  Action:SNAT-PAT
198.19.80.1:47100 -> 198.19.80.2:48100  =>  198.19.80.1:52002 -> 198.19.80.2:48100
~~~

这里地址恰好与接口地址相同，源端口仍从 47100 转换到 52002；端点收包与回复证明实际生效。独立内网端点实验还验证了 198.18.11.2 转换为出口 198.19.80.1，见[地址池案例的基础拓扑](../../examples/nat/topology.md)。

撤销必须先 `undo nat-policy POLICY outbound`，再删策略；全局范围用 `undo nat-policy interface-pat-range` 恢复默认。全局分配参数仍有活动会话时可能被后端拒绝；先查会话并安排业务维护，不能忽略 Instance in use。

[会话与统计](sessions.md) · [容量与计时](capacity.md) · [命令参数](../reference/nat.md)
