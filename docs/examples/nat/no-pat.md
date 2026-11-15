# NO-PAT

只改变源地址，保留源端口或 ICMP identifier。适用于不允许改变源端口、且映射不会冲突的业务；不是多主机共享端口空间的 PAT 替代品。

## 前提与参数

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。接口来源和池来源二选一。修改现有 action 后，用新连接验证；旧会话仍保留原有映射。

## 配置

P1 从用户视图开始；接口与基础路由由前置拓扑提供：

~~~text
system-view
nat-policy address-pool name LAB-PUBLIC
 address 198.19.81.1/32
quit
nat-policy name LAB-SNAT
 statistic enable
 rule 10
  source address 198.18.11.2/32
  action snat no-pat address-pool LAB-PUBLIC
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
display nat-policy sessions action snat-no-pat name LAB-SNAT
~~~

已有隔离实验真实输出节选：

~~~text
host-p1a12/outbound  FIB:0 -> FIB:0  Policy:LAB-SNAT(4124874345)/10  Action:SNAT-NO-PAT
198.18.11.2:43092 -> 198.19.80.2:8080  =>  198.19.81.1:43092 -> 198.19.80.2:8080
~~~

HTTP 返回 200，源端口 43092 保持不变。随后仅把 action 改成 snat no-pat interface，真实会话中源地址变为 198.19.80.1、端口 51388 仍保持 51388；接口形式同样只能出方向绑定。 该记录证明本例路径，不是地址池耗尽、满表容量或吞吐测试。运行 ID、端口和时间会随连接变化。

## 撤销与保存

P1 系统视图：

~~~text
system-view
interface host-p1a12
 undo nat-policy LAB-SNAT outbound
quit
undo nat-policy name LAB-SNAT
undo nat-policy address-pool name LAB-PUBLIC
commit
display nat-policy runtime
display nat-policy interfaces
~~~

解除绑定后再发起新连接，确认不再采用该策略。基础拓扑的普通路由仍在，撤销 NAT 不一定使业务断开，应比较转换结果而非只看 ping。需要重启保留配置时，在提交并验证后执行 `save`；撤销后也再次保存。

[功能说明](../../operator/nat/no-pat.md) · [命令参数](../../operator/reference/nat.md)
