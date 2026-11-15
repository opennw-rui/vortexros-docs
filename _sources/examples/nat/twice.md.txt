# Twice NAT

在一次动作中同时改变源、目的地址，可处理服务发布中需要强制回程经网关的场景。本例源地址改为 LAN 网关，目标改为 P3 服务。

## 前提与参数

显式端口转换只支持 TCP/UDP（或对应协议号6/17），不能把 SCTP 会话查询能力等同于 SCTP 端口转换。

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。source/destination 后的 port 分别指定源/目的转换端口，不写则保留对应端口。会话记录原始和转换后的两组地址；应用服务端将看到转换后的源地址。

## 配置

P1 从用户视图开始；接口与基础路由由前置拓扑提供：

~~~text
system-view
nat-policy name LAB-TWICE
 statistic enable
 rule 10
  protocol icmp
  destination address 198.19.81.1/32
  action twice-nat source 198.18.11.1 destination 198.18.11.2
 quit
quit
interface Ethernet0
 nat-policy LAB-TWICE inbound
quit
nat-policy name LAB-LAN-PASS
quit
interface Ethernet1
 nat-policy LAB-LAN-PASS inbound
quit
commit
~~~

## 验证

P2 执行 `ping -a 198.19.80.2 -c 3 198.19.81.1`，然后在 P1 查询：

~~~text
display nat-policy name LAB-TWICE
display nat-policy statistics name LAB-TWICE
display nat-policy sessions action twice-nat
~~~

应能往返，且目的地址变为 198.18.11.2，源地址同时按 action 中的 source 地址转换。在会话中核对原始和转换后的地址；ICMP 使用标识符而非 TCP/UDP 端口。

Ping 成功只证明往返路径，应同时核对转换结果。查看状态要紧接探测执行，避免会话已老化。地址池耗尽和端口范围需要对应并发业务验证，不能从三次 Ping 推断。

## 撤销与保存

P1 系统视图：

~~~text
system-view
interface Ethernet0
 undo nat-policy LAB-TWICE inbound
quit
interface Ethernet1
 undo nat-policy LAB-LAN-PASS inbound
quit
undo nat-policy name LAB-TWICE
undo nat-policy name LAB-LAN-PASS
commit
display nat-policy runtime
display nat-policy interfaces
~~~

解除绑定后再发起新连接，确认不再采用该策略。基础拓扑的普通路由仍在，撤销 NAT 不一定使业务断开，应比较转换结果而非只看 ping。需要重启保留配置时，在提交并验证后执行 `save`；撤销后也再次保存。

[功能说明](../../operator/nat/twice.md) · [命令参数](../../operator/reference/nat.md)
