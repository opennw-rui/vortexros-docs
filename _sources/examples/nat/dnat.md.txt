# DNAT

将外部目的地址和端口改为内网服务。本例把 198.19.80.1:18080 发布到 198.18.11.2:8081，源地址保持外部客户端地址。

## 前提与参数

显式端口转换只支持 TCP/UDP（或对应协议号6/17），不能把 SCTP 会话查询能力等同于 SCTP 端口转换。

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。端口转换使用直接 destination port，不能同时保留 destination port-set。省略 action 的 port 则不改目的端口。该动作不等同于防火墙放行；接口 ACL 也必须允许业务。

## 配置

P1 从用户视图开始；接口与基础路由由前置拓扑提供：

~~~text
system-view
nat-policy name LAB-DNAT
 statistic enable
 rule 10
  protocol tcp
  destination address 198.19.80.1/32
  destination port 18080
  action dnat 198.18.11.2 port 8081
 quit
quit
interface host-p1a12
 nat-policy LAB-DNAT inbound
quit
nat-policy name LAB-LAN-PASS
quit
interface host-p1q13
 nat-policy LAB-LAN-PASS inbound
quit
commit
~~~

## 验证与真实结果

在 P2 访问 http://198.19.80.1:18080/。随后在 P1 查询：

~~~text
display nat-policy sessions action dnat
display nat-policy statistics name LAB-DNAT
~~~

已有隔离实验真实输出节选：

~~~text
host-p1a12/inbound  FIB:0 -> FIB:0  Policy:LAB-DNAT(2572252004)/10  Action:DNAT
198.19.80.2:36924 -> 198.19.80.1:18080  =>  198.19.80.2:36924 -> 198.18.11.2:8081
~~~

从 P2 访问发布地址返回 HTTP 200。P3 回程必须经过 P1；LAN 入方向绑定空策略用于接入 NAT 状态回程处理，没有添加额外转换规则。 该记录证明本例路径，不是地址池耗尽、满表容量或吞吐测试。运行 ID、端口和时间会随连接变化。

## 撤销与保存

P1 系统视图：

~~~text
system-view
interface host-p1a12
 undo nat-policy LAB-DNAT inbound
quit
interface host-p1q13
 undo nat-policy LAB-LAN-PASS inbound
quit
undo nat-policy name LAB-DNAT
undo nat-policy name LAB-LAN-PASS
commit
display nat-policy runtime
display nat-policy interfaces
~~~

解除绑定后再发起新连接，确认不再采用该策略。基础拓扑的普通路由仍在，撤销 NAT 不一定使业务断开，应比较转换结果而非只看 ping。需要重启保留配置时，在提交并验证后执行 `save`；撤销后也再次保存。

[功能说明](../../operator/nat/dnat.md) · [命令参数](../../operator/reference/nat.md)
