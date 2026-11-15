# No-NAT

匹配指定流量而不修改地址和端口。可用作比转换规则更优先的豁免；它不是丢弃动作，也不能替代路由或 ACL。

## 行为与限制

No-NAT 是无状态动作，因此没有会话条目是正常现象。豁免放在较小 priority 的规则中，先于覆盖同一流量的转换规则；未显式 priority 时取规则 ID。

此功能需要 VPP。配置写入 Candidate，`commit` 后参与下发，`save` 保存已提交配置；重启后从启动 CFG 恢复。缺省不创建 NAT 策略或接口绑定。

## 配置、显示与撤销

[完整独立案例](../../examples/nat/no-nat.md)包含拓扑、网关和端点前提、完整策略、实际 display 输出、HTTP 往返及撤销。以下是本功能实际验收的转换结果节选：

~~~text
NAT policy sessions
Total: 0  TCP:0  UDP:0  ICMP:0  SCTP:0  Other:0
Scope: active stateful NAT translations; no-NAT and static NAT are stateless and are not listed
~~~

真实 HTTP 200，P2 看到原始源地址 198.18.11.2。P2 必须保留到内部网段的返回路由；没有转换并不代表不需要回程路由。

[对象与规则](objects.md) · [会话与统计](sessions.md) · [命令参考](../reference/nat.md)
