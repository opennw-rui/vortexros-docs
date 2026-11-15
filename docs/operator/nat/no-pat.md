# NO-PAT

只改变源地址，保留源端口或 ICMP identifier。适用于不允许改变源端口、且映射不会冲突的业务；不是多主机共享端口空间的 PAT 替代品。

## 行为与限制

接口来源和池来源二选一。修改现有 action 后，用新连接验证；旧会话仍保留原有映射。

此功能需要 VPP。配置写入 Candidate，`commit` 后参与下发，`save` 保存已提交配置；重启后从启动 CFG 恢复。缺省不创建 NAT 策略或接口绑定。

## 配置、显示与撤销

[完整独立案例](../../examples/nat/no-pat.md)包含拓扑、网关和端点前提、完整策略、实际 display 输出、HTTP 往返及撤销。以下是本功能实际验收的转换结果节选：

~~~text
host-p1a12/outbound  FIB:0 -> FIB:0  Policy:LAB-SNAT(4124874345)/10  Action:SNAT-NO-PAT
198.18.11.2:43092 -> 198.19.80.2:8080  =>  198.19.81.1:43092 -> 198.19.80.2:8080
~~~

HTTP 返回 200，源端口 43092 保持不变。随后仅把 action 改成 snat no-pat interface，真实会话中源地址变为 198.19.80.1、端口 51388 仍保持 51388；接口形式同样只能出方向绑定。

[对象与规则](objects.md) · [会话与统计](sessions.md) · [命令参考](../reference/nat.md)
