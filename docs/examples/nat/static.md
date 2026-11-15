# 静态 NAT

为匹配的源前缀建立固定转换。本例使用 /32 到 /32 一对一映射，不分配 PAT 端口。外网必须有到映射地址的返回路由。

## 前提与参数

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。必须使用单一直接 source 前缀，不能用 source address-set；内外前缀长度必须相等，不允许端口匹配，协议必须为 any；不要把一个大网段全部压成一个 /32 来实现端口复用，该需求使用 PAT。未匹配流量不因此自动转换。

## 配置

P1 从用户视图开始；接口与基础路由由前置拓扑提供：

~~~text
system-view
nat-policy name LAB-SNAT
 statistic enable
 rule 10
  source address 198.18.11.2/32
  action static-nat 198.19.81.2/32
 quit
quit
interface host-p1a12
 nat-policy LAB-SNAT outbound
quit
commit
~~~

## 验证与真实结果

在 P3 访问 http://198.19.80.2:8080/。随后在 P1 查询：

~~~text
display nat-policy name LAB-SNAT
display nat-policy statistics name LAB-SNAT
display nat-policy sessions
~~~

已有隔离实验真实输出节选：

~~~text
Scope: active stateful NAT translations; no-NAT and static NAT are stateless and are not listed
~~~

真实 HTTP 返回 200，服务端看到 198.19.81.2；这项动作是无状态转换，不会生成 sessions 中的条目。上面摘录的是真实会话查询的范围提示，不是静态映射表。 该记录证明本例路径，不是地址池耗尽、满表容量或吞吐测试。运行 ID、端口和时间会随连接变化。

## 撤销与保存

P1 系统视图：

~~~text
system-view
interface host-p1a12
 undo nat-policy LAB-SNAT outbound
quit
undo nat-policy name LAB-SNAT
commit
display nat-policy runtime
display nat-policy interfaces
~~~

解除绑定后再发起新连接，确认不再采用该策略。基础拓扑的普通路由仍在，撤销 NAT 不一定使业务断开，应比较转换结果而非只看 ping。需要重启保留配置时，在提交并验证后执行 `save`；撤销后也再次保存。

[功能说明](../../operator/nat/static.md) · [命令参数](../../operator/reference/nat.md)
