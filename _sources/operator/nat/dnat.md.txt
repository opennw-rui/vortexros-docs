# DNAT

将外部目的地址和端口改为内网服务。本例把 198.19.80.1:18080 发布到 198.18.11.2:8081，源地址保持外部客户端地址。

## 行为与限制

显式端口转换只支持 TCP/UDP（或对应协议号6/17），不能把 SCTP 会话查询能力等同于 SCTP 端口转换。

端口转换使用直接 destination port，不能同时保留 destination port-set。省略 action 的 port 则不改目的端口。该动作不等同于防火墙放行；接口 ACL 也必须允许业务。

此功能需要 VPP。配置写入 Candidate，`commit` 后参与下发，`save` 保存已提交配置；重启后从启动 CFG 恢复。缺省不创建 NAT 策略或接口绑定。

## 配置、检查与撤销

[完整案例](../../examples/nat/dnat.md)给出三台 VortexROS 的配置、策略、查询及撤销顺序。发布地址必须路由到网关。内侧回程须经过 NAT 网关，LAN 入方向按完整案例接入状态回程处理；该空策略没有额外地址转换规则。

提交后查询 display nat-policy name、interfaces、statistics 和 sessions。先确认策略绑定及命中，再检查原始与转换后的地址；TCP/UDP 还需核对端口，ICMP 则核对标识符。旧会话可能保留原映射，修改策略后用新连接检查。

撤销先解除接口绑定，再删除策略及不再引用的对象，commit 后确认绑定和目标规则消失；需要持久保留时 save。其他策略、共享地址和路由应保留。

[对象与规则](objects.md) · [会话与统计](sessions.md) · [命令参考](../reference/nat.md)
