# CAR、标记与重定向

同一 behavior 可同时执行 CAR、remark 和 redirect。redirect vpn-instance 不改变目的地址，在指定 VPN 对应地址族的 FIB 查找；miss 丢弃，不回退原 VPN。table-only、next-hop、interface 三种 redirect 互斥。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/mqc.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
traffic behavior LAB-MARK
 remark dscp 10
quit
commit
~~~

## 查询与实际效果

~~~text
display traffic behavior user-defined LAB-MARK
~~~

[案例的真实 display、报文或路由结果](../../examples/mqc.md)与本节功能相互对应。该功能片段是参数说明，不将这里的演示地址冒充另一组已经执行的输出。对照配置、后端实际状态和业务三者，不能只看commit返回。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
undo traffic behavior LAB-MARK
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/mqc.md) · [功能目录](../mqc.md)
