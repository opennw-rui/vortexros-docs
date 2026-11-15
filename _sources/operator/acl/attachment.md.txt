# 接口绑定与撤销

ACL 仅创建时不丢弃业务。以下将 IPv4 ACL 绑定到接口入方向：

~~~text
system-view
interface Vlanif 100
 traffic-filter inbound acl WEB-IN
quit
commit
display acl name WEB-IN
display interface Vlanif 100
~~~

入/出方向相对于该接口报文路径。二层物理口可能承载广播和 DHCP，Vlanif 则在三层网关路径使用；不能把两处绑定认为作用范围完全相同。普通 stateless permit 不创建返回路径例外，双向 ACL 必须分别满足业务条件。

[完整案例](../../examples/acl.md)提供实际放行、拒绝和撤销对照，不能用单看规则存在替代过滤效果。

~~~text
system-view
interface Vlanif 100
 undo traffic-filter inbound
quit
undo acl name WEB-IN
commit
~~~

仍被 MQC、SSH 源保护等引用时，删除会被拒绝。只解除一个方向不改变另一方向的 ACL。撤销后检查接口绑定及新业务，确认后 save。

[全部参数](../reference/interfaces.md) · [MQC](../mqc.md)
