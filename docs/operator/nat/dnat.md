# DNAT

将外部目的地址和端口改为内网服务。本例把 198.19.80.1:18080 发布到 198.18.11.2:8081，源地址保持外部客户端地址。

## 行为与限制

显式端口转换只支持 TCP/UDP（或对应协议号6/17），不能把 SCTP 会话查询能力等同于 SCTP 端口转换。

端口转换使用直接 destination port，不能同时保留 destination port-set。省略 action 的 port 则不改目的端口。该动作不等同于防火墙放行；接口 ACL 也必须允许业务。

此功能需要 VPP。配置写入 Candidate，`commit` 后参与下发，`save` 保存已提交配置；重启后从启动 CFG 恢复。缺省不创建 NAT 策略或接口绑定。

## 配置、显示与撤销

[完整独立案例](../../examples/nat/dnat.md)包含拓扑、网关和端点前提、完整策略、实际 display 输出、HTTP 往返及撤销。以下是本功能实际验收的转换结果节选：

~~~text
host-p1a12/inbound  FIB:0 -> FIB:0  Policy:LAB-DNAT(2572252004)/10  Action:DNAT
198.19.80.2:36924 -> 198.19.80.1:18080  =>  198.19.80.2:36924 -> 198.18.11.2:8081
~~~

从 P2 访问发布地址返回 HTTP 200。P3 回程必须经过 P1；LAN 入方向绑定空策略用于接入 NAT 状态回程处理，没有添加额外转换规则。

[对象与规则](objects.md) · [会话与统计](sessions.md) · [命令参考](../reference/nat.md)
