# 分类器

通过 operator and/or 组合 if-match 条件；ACL、地址、协议和其他合法匹配以本视图参数表为准。修改已引用 ACL 后本次 commit 更新实际匹配，不必解绑策略。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/mqc.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
traffic classifier LAB-DST operator or
 if-match destination-ip 192.0.2.82/32
quit
commit
~~~

## 查询与实际效果

~~~text
display traffic classifier user-defined LAB-DST
~~~

[案例的真实 display、报文或路由结果](../../examples/mqc.md)与本节功能相互对应。该功能片段是参数说明，不将这里的演示地址冒充另一组已经执行的输出。对照配置、后端实际状态和业务三者，不能只看commit返回。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
undo traffic classifier LAB-DST
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/mqc.md) · [功能目录](../mqc.md)
