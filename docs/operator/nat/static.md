# 静态 NAT

为匹配的源前缀建立固定转换。本例使用 /32 到 /32 一对一映射，不分配 PAT 端口。外网必须有到映射地址的返回路由。

## 行为与限制

必须使用单一直接 source 前缀，不能用 source address-set；内外前缀长度必须相等，不允许端口匹配，协议必须为 any；不要把一个大网段全部压成一个 /32 来实现端口复用，该需求使用 PAT。未匹配流量不因此自动转换。

此功能需要 VPP。配置写入 Candidate，`commit` 后参与下发，`save` 保存已提交配置；重启后从启动 CFG 恢复。缺省不创建 NAT 策略或接口绑定。

## 配置、显示与撤销

[完整独立案例](../../examples/nat/static.md)包含拓扑、网关和端点前提、完整策略、实际 display 输出、HTTP 往返及撤销。以下是本功能实际验收的转换结果节选：

~~~text
Scope: active stateful NAT translations; no-NAT and static NAT are stateless and are not listed
~~~

真实 HTTP 返回 200，服务端看到 198.19.81.2；这项动作是无状态转换，不会生成 sessions 中的条目。上面摘录的是真实会话查询的范围提示，不是静态映射表。

[对象与规则](objects.md) · [会话与统计](sessions.md) · [命令参考](../reference/nat.md)
