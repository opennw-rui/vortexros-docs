# NO-PAT

只改变源地址，保留源端口或 ICMP identifier。适用于不允许改变源端口、且映射不会冲突的业务；不是多主机共享端口空间的 PAT 替代品。

## 前提与参数

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。接口来源和池来源二选一。修改现有 action 后，用新连接验证；旧会话仍保留原有映射。

## 配置

P1 从用户视图开始；接口与基础路由由前置拓扑提供：

~~~text
system-view
~~~

配置清单：

~~~text
nat-policy address-pool name D1-NOPAT-P
 address 198.51.100.11/32
#
nat-policy name D1-NOPAT
 statistic enable
 rule 10
  source address 203.0.113.2/32
  action snat no-pat address-pool D1-NOPAT-P
#
interface Ethernet0
 nat-policy D1-NOPAT outbound
#
~~~

CLI 操作：

~~~text
commit
~~~

## 验证

P3 执行 `ping -a 203.0.113.2 -c 3 198.51.100.2`，然后在 P1 查询：

~~~text
display nat-policy name D1-NOPAT
display nat-policy statistics name D1-NOPAT
display nat-policy sessions action snat-no-pat
~~~

应能往返，且源地址取自地址池，ICMP 标识符保持原值。在会话中核对原始和转换后的地址；ICMP 使用标识符而非 TCP/UDP 端口。

Ping 成功只证明往返路径，应同时核对转换结果。查看状态要紧接探测执行，避免会话已老化。地址池耗尽和端口范围需要对应并发业务验证，不能从三次 Ping 推断。

## 撤销与保存

P1 系统视图：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo nat-policy D1-NOPAT outbound
#
undo nat-policy name D1-NOPAT
undo nat-policy address-pool name D1-NOPAT-P
~~~

CLI 操作：

~~~text
commit
display nat-policy runtime
display nat-policy interfaces
~~~

解除绑定后再发起新连接，确认不再采用该策略。基础拓扑的普通路由仍在，撤销 NAT 不一定使业务断开，应比较转换结果而非只看 ping。需要重启保留配置时，在提交并验证后执行 `save`；撤销后也再次保存。

[功能说明](../../operator/nat/no-pat.md) · [命令参数](../../operator/reference/nat.md)

## 实际检查结果

使用 ICMP 标识符 29123 的探测收到 3/3 回复，实际会话源地址转换为 198.51.100.11，标识符仍为 29123。该结果验证地址转换和标识符保留，不代表整个地址池的并发容量。
