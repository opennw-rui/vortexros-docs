# IPv4 前缀

greater-equal/less-equal 对匹配的掩码长度施加边界；示例匹配10/8内的/16到/24，不是报文源地址 ACL。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/bgp-policy.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
ip ip-prefix PL-IN index 10 permit 10.0.0.0 8 greater-equal 16 less-equal 24
commit
~~~

## 查询与实际效果

~~~text
display ip ip-prefix PL-IN verbose
display ip ip-prefix PL-IN first-match 10.1.0.0/16
~~~

[完整配置、检查与撤销](../../examples/bgp-policy.md)；本节说明单项参数，完整组网请按案例的前置条件执行。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
undo ip ip-prefix PL-IN
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/prefix-lists.md) · [功能目录](../prefix-lists.md)
