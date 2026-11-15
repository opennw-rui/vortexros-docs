# 创建与地址族

RD区分VPN路由身份，RT决定导入导出，两者不代替接口路由表隔离。BGP VPN地址族复用此处RD/RT。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/mpls-l3vpn.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
ip vpn-instance BLUE
 ipv4-family
  route-distinguisher 65000:100
  vpn-target 65000:100 both
 quit
 ipv6-family
 quit
quit
commit
~~~

## 查询与实际效果

~~~text
display ip vpn-instance
~~~

[完整配置、检查与撤销](../../examples/mpls-l3vpn.md)；本节说明单项参数，完整组网请按案例的前置条件执行。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
undo ip vpn-instance BLUE
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/vrf.md) · [功能目录](../vrf.md)
