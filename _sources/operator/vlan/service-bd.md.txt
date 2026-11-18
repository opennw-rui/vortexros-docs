# VLAN 与业务桥域

使用业务桥域关联VLAN及可选的VNI，Vbdif提供该桥域的三层网关。例如将VLAN666绑定到桥域666：

~~~text
system-view
~~~

配置清单：

~~~text
enable switch
vlan 666
#
bridge-domain 666
 l2 binding vlan 666
#
~~~

CLI 操作：

~~~text
display this
~~~

CLI 操作：

~~~text
commit
display bridge-domain 666
~~~

撤销绑定时，进入同一桥域执行无参数的`undo l2 binding vlan`：

~~~text
bridge-domain 666
 undo l2 binding vlan
#
~~~

CLI 操作：

~~~text
commit
~~~

撤销绑定不会自动删除桥域。仍有Vbdif、VNI或其他引用时，应先按业务依赖解除；不再使用后再删除桥域和VLAN。

[桥域配置](../bridge-domains.md) · [二层子接口案例](../../examples/subinterfaces/l2.md)
