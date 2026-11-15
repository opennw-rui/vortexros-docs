# SLAAC 地址

启用后自动接收上游自主前缀，执行重复地址检测（DAD）并维护有效期。动态地址属于接口所选 VPN，不写成静态启动配置；重启后重新学习。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/ipv6-ra.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
interface Ethernet 1
 ipv6 address auto slaac
quit
commit
~~~

## 查询与实际效果

~~~text
display ipv6 interface brief
~~~

[完整配置、检查与撤销](../../examples/ipv6-ra.md)；本节说明单项参数，完整组网请按案例的前置条件执行。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
interface Ethernet 1
 undo ipv6 address auto slaac
quit
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/ipv6-autoconfig.md) · [功能目录](../ipv6-autoconfig.md)
