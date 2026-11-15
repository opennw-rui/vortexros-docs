# IPv6 前缀

IPv6 列表与 IPv4 地址族分开。允许同名列表，但引用命令明确区分地址族，不能把IPv4列表挂到IPv6邻居策略。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/bgp-policy.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
ip ipv6-prefix V6-IN index 10 permit 2001:db8:: 32 greater-equal 48 less-equal 64
commit
~~~

## 查询与实际效果

~~~text
display ipv6 prefix V6-IN
display ip ipv6-prefix V6-IN verbose
~~~

[完整配置、检查与撤销](../../examples/bgp-policy.md)；本节说明单项参数，完整组网请按案例的前置条件执行。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
undo ip ipv6-prefix V6-IN
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/prefix-lists.md) · [功能目录](../prefix-lists.md)
