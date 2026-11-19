# 收敛与精确撤销

同一次提交可以新增递归解析路由及其依赖路由。确认路由已选中、进入实际FIB且业务连通后再保存；配置提交成功不等于目标已经可达。

下一跳暂时不可达时，配置意图与安装状态不同；恢复后应重建实际路径。相同前缀ECMP撤销一条路径时，仍可用的其他路径不应被整组删除。

~~~text
display ip routing-table 203.0.113.0 24 verbose
display ip fib
display ipv6 routing-table
display ipv6 fib
~~~

黑洞路由必须以同一前缀和NULL 0精确撤销；普通静态路由保留原VPN、前缀、下一跳与接口等定位参数加undo。跨表lookup-only路由的Lookup-Table显示实际查表号，普通路径显示-，默认VPP表0与Linux main254各有含义。

[完整配置、示例输出和撤销](../../examples/static-route.md) · [全部参数](../reference/static-routing.md)

## ECMP成员与解析路由

同一前缀可以配置多个等价下一跳。下一跳不可达和撤销下一跳配置是两种操作：

- 保留上层静态路由，只撤销它依赖的解析路由：该路径应退出实际转发，其他有效路径继续使用；解析恢复后，它可重新参与ECMP。
- 对上层静态路由执行精确undo：删除的是配置成员。以后恢复解析路由不应把这个已删除成员重新加入。

递归查询会采用仍然有效的其他路由，包括允许参与解析的默认路由。因此，撤销一条更具体的解析路由，不一定使下一跳不可达；应以实际RIB和FIB为准。

下面的两个直连网关均须能到达测试目标，并具有回程路由。Ethernet0的IPv4/IPv6地址已经配置且接口Up。

~~~text
ip route-static 203.0.113.23 255.255.255.255 192.0.2.66
ip route-static 203.0.113.24 255.255.255.255 192.0.2.67
ip route-static 198.18.250.1 255.255.255.255 203.0.113.23
ip route-static 198.18.250.1 255.255.255.255 203.0.113.24
ipv6 route-static 2001:db8:113::23 128 2001:db8:304:a::66
ipv6 route-static 2001:db8:113::24 128 2001:db8:304:a::67
ipv6 route-static 2001:db8:250::1 128 2001:db8:113::23
ipv6 route-static 2001:db8:250::1 128 2001:db8:113::24
~~~

提交后核对两个地址族的选中路径、实际FIB和连通性：

~~~text
display ip routing-table 198.18.250.1 32
display ipv6 routing-table 2001:db8:250::1 128
display ip fib
display ipv6 fib
ping -c 3 198.18.250.1
ping ipv6 -c 3 2001:db8:250::1
~~~

如果决定永久移除第一条业务路径，使用原前缀和下一跳精确撤销：

~~~text
undo ip route-static 198.18.250.1 255.255.255.255 203.0.113.23
undo ipv6 route-static 2001:db8:250::1 128 2001:db8:113::23
~~~

commit后应只剩第二条业务路径；即使第一条解析路由恢复，也不能再次出现已删除的成员。确认后save。
示例中保留的业务路径经192.0.2.67及2001:db8:304:a::67转发。

本版一次IPv4成员撤销后的实际查询结果如下。203.0.113.23已不在业务路由中：

~~~text
Route Flags: R - relay, D - download to fib, T - nexthop VPN instance, B - black hole route
-----------------------------------------------------------------------------------------------
Routing Table : default
         Destinations : 1         Routes : 1

Destination/Mask   Proto   Pre  Cost    Flags   NextHop         Interface       VPN-Instance

 198.18.250.1/32   Static  60   0         D    203.0.113.24     Ethernet0       default
~~~

上述保留路径的IPv4和IPv6探测均为3 sent、3 received、0% packet loss。
两条解析路径恢复后，未撤销配置的ECMP成员可以重新参与转发；已撤销配置的成员保持删除。

接口重新Up后，还需要等待路由和ARP/ND邻居恢复。先确认路由及邻居可用，再验证业务；
不要把接口Up等同于业务已经恢复，也不要把此例当作无损或亚秒切换承诺。
