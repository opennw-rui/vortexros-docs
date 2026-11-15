# 策略与接口绑定

policy 关联 classifier 和 behavior，precedence 控制顺序；同一接口方向只能按实际支持绑定策略。解除绑定后再删策略及其引用对象。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/mqc.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
traffic policy LAB-POLICY
 classifier LAB-DST behavior LAB-MARK precedence 10
quit
interface host-p1a12
 traffic-policy LAB-POLICY outbound
quit
commit
~~~

## 查询与实际效果

~~~text
display traffic policy user-defined LAB-POLICY
~~~

[案例的真实 display、报文或路由结果](../../examples/mqc.md)与本节功能相互对应。该功能片段是参数说明，不将这里的演示地址冒充另一组已经执行的输出。对照配置、后端实际状态和业务三者，不能只看commit返回。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
interface host-p1a12
 undo traffic-policy LAB-POLICY outbound
quit
undo traffic policy LAB-POLICY
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/mqc.md) · [功能目录](../mqc.md)
