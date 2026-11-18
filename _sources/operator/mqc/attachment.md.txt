# 策略与接口绑定

policy 关联 classifier 和 behavior，precedence 控制顺序；同一接口方向只能按实际支持绑定策略。解除绑定后再删策略及其引用对象。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/mqc.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
~~~

配置清单：

~~~text
traffic policy LAB-POLICY
 classifier LAB-DST behavior LAB-MARK precedence 10
#
interface Ethernet0
 traffic-policy LAB-POLICY outbound
#
~~~

CLI 操作：

~~~text
commit
~~~

## 查询与实际效果

~~~text
display traffic policy user-defined LAB-POLICY
~~~

[完整配置、检查与撤销](../../examples/mqc.md)；本节说明单项参数，完整组网请按案例的前置条件执行。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo traffic-policy outbound
#
undo traffic policy LAB-POLICY
~~~

CLI 操作：

~~~text
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/mqc.md) · [功能目录](../mqc.md)

撤销命令不带策略名：接口下使用`undo traffic-policy inbound`或`undo traffic-policy outbound`解除一个方向；不写方向会解除该接口两个方向的绑定。随后才可删除不再引用的策略、分类器和行为。
