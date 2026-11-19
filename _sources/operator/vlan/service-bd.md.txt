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

## 在同一个 BD 混合接入

全局 VLAN 使用 `l2 binding vlan` 接入 BD，显式二层子接口在接口视图使用 `bridge-domain` 接入。一个 VLAN 和一个 L2 子接口各只能接入一个 BD。两种成员可以共用同一个 BD，并共享广播、洪泛和 MAC 学习范围。需要隔离客户流量时，为各业务分配独立的 BD 和 VNI。

全局 VLAN 与任意显式子接口的外层封装 VID 互斥。子接口实例编号、QinQ 内层 VID 和 BD 编号可以使用相同的数字。[二层子接口的配置规则](../subinterfaces-l2.md)

[桥域配置](../bridge-domains.md) · [二层子接口案例](../../examples/subinterfaces/l2.md)
