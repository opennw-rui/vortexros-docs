# 接口绑定与撤销

ACL 仅创建时不丢弃业务。以下将 IPv4 ACL 绑定到接口入方向：

~~~text
system-view
~~~

配置清单：

~~~text
interface Vlanif 100
 traffic-filter inbound acl WEB-IN
#
~~~

CLI 操作：

~~~text
commit
display acl name WEB-IN
display interface Vlanif 100
~~~

inbound 检查从该接口接收的报文，outbound 检查从该接口发送的报文。二层物理口可承载 DHCP、广播和多个 VLAN；Vlanif 用于相应 VLAN 的三层网关路径，绑定位置会改变过滤范围。ACL 不会自动为回复报文建立例外；需要双向过滤时，应分别允许所需的请求和回复。

[完整案例](../../examples/acl.md)列出了允许和拒绝的业务连接及撤销操作。绑定后先核对接口和规则，再分别测试应通过与应拒绝的连接。

~~~text
system-view
~~~

配置清单：

~~~text
interface Vlanif 100
 undo traffic-filter inbound
#
undo acl name WEB-IN
~~~

CLI 操作：

~~~text
commit
~~~

仍被 MQC、SSH 源保护等引用时，删除会被拒绝。只解除一个方向不改变另一方向的 ACL。撤销后检查接口绑定及新业务，确认后 save。

[全部参数](../reference/interfaces.md) · [MQC](../mqc.md)
