# No-NAT

匹配指定流量而不修改地址和端口。可用作比转换规则更优先的豁免；它不是丢弃动作，也不能替代路由或 ACL。

## 前提与参数

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。No-NAT 是无状态动作，因此没有会话条目是正常现象。豁免放在较小 priority 的规则中，先于覆盖同一流量的转换规则；未显式 priority 时取规则 ID。

## 配置

P1 从用户视图开始；接口与基础路由由前置拓扑提供：

~~~text
system-view
nat-policy name LAB-SNAT
 statistic enable
 rule 10
  source address 198.18.11.2/32
  action no-nat
 quit
quit
interface Ethernet0
 nat-policy LAB-SNAT outbound
quit
commit
~~~

## 验证

P3 执行 `ping -a 198.18.11.2 -c 3 198.19.80.2`，然后在 P1 查询：

~~~text
display nat-policy name LAB-SNAT
display nat-policy statistics name LAB-SNAT
display nat-policy sessions action no-nat
~~~

应能往返，且源地址保持 198.18.11.2，目的地址保持 198.19.80.2。该动作无状态，正常情况下不会创建会话；应结合策略命中统计和对端收到的地址检查。

Ping 成功只证明往返路径，应同时核对转换结果。查看状态要紧接探测执行，避免会话已老化。地址池耗尽和端口范围需要对应并发业务验证，不能从三次 Ping 推断。

## 撤销与保存

P1 系统视图：

~~~text
system-view
interface Ethernet0
 undo nat-policy LAB-SNAT outbound
quit
undo nat-policy name LAB-SNAT
commit
display nat-policy runtime
display nat-policy interfaces
~~~

解除绑定后再发起新连接，确认不再采用该策略。基础拓扑的普通路由仍在，撤销 NAT 不一定使业务断开，应比较转换结果而非只看 ping。需要重启保留配置时，在提交并验证后执行 `save`；撤销后也再次保存。

[功能说明](../../operator/nat/no-nat.md) · [命令参数](../../operator/reference/nat.md)
