# SLAAC 地址

Linux在LCP端点执行DAD和有效期维护，LCP再同步地址到VPP。接口属VPN时先进入对应Linux VRF，动态地址不会被写成静态CFG。

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

[案例的真实 display、报文或路由结果](../../examples/ipv6-ra.md)与本节功能相互对应。该功能片段是参数说明，不将这里的演示地址冒充另一组已经执行的输出。对照配置、后端实际状态和业务三者，不能只看commit返回。

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
