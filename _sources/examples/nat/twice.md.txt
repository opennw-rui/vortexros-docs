# Twice NAT

在一次动作中同时改变源、目的地址，可处理服务发布中需要强制回程经网关的场景。本例源地址改为 LAN 网关，目标改为 P3 服务。

## 前提与参数

显式端口转换只支持 TCP/UDP（或对应协议号6/17），不能把 SCTP 会话查询能力等同于 SCTP 端口转换。

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。source/destination 后的 port 分别指定源/目的转换端口，不写则保留对应端口。会话记录原始和转换后的两组地址；应用服务端将看到转换后的源地址。

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
  action twice-nat source 198.18.11.1 destination 198.18.11.2 port 8081
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
display nat-policy sessions action twice-nat
~~~

已有隔离实验真实输出节选：

~~~text
host-p1a12/inbound  FIB:0 -> FIB:0  Policy:LAB-DNAT(2572252004)/10  Action:TWICE-NAT
198.19.80.2:46738 -> 198.19.80.1:18080  =>  198.18.11.1:46738 -> 198.18.11.2:8081
~~~

P2 访问发布地址实际 HTTP 200，P3 日志看到 198.18.11.1。实验首次未接入 LAN 回程状态处理时失败；绑定 LAB-LAN-PASS 后成功，不能省略该回程条件。 该记录证明本例路径，不是地址池耗尽、满表容量或吞吐测试。运行 ID、端口和时间会随连接变化。

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

[功能说明](../../operator/nat/twice.md) · [命令参数](../../operator/reference/nat.md)
