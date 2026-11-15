# 接口与路由归属

先创建VPN及所需地址族，再把三层接口绑定进去。仍有接口、路由或协议引用时不能删除VPN；改变归属会影响接口路由和邻居。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/mpls-l3vpn.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
interface LoopBack 100
 ip binding vpn-instance BLUE
 ip address 10.100.0.1 255.255.255.255
quit
commit
~~~

## 查询与实际效果

~~~text
display ip interface brief
display ip routing-table vpn-instance BLUE
~~~

[完整配置、检查与撤销](../../examples/mpls-l3vpn.md)；本节说明单项参数，完整组网请按案例的前置条件执行。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
undo interface LoopBack 100
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/vrf.md) · [功能目录](../vrf.md)
