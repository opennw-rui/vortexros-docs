# 静态项与老化

## 配置与验证

IPv4 ARP和IPv6 ND邻居老化是VPP进程级参数，不依赖VLAN或bridge-domain。纯三层接口同样使用这些参数。默认值均为1200秒，并在VPP每次启动或重新连接后优先恢复，再下发接口、地址和业务配置。

```text
arp timeout 900
ipv6 nd stale-timeout 1800
ipv6 nd max-number 65536
ipv6 nd recycle enable
commit
```

恢复默认值：

```text
undo arp timeout
undo ipv6 nd stale-timeout
undo ipv6 nd max-number
undo ipv6 nd recycle
commit
```

`max-number`限制VPP IPv6邻居表容量；`recycle enable`在容量已满时回收最老的动态条目，静态邻居不参与动态回收。回收策略必须显式配置，`undo`恢复VPP启动时的默认策略。容量同步到 Linux ND 回收阈值。老化时间和回收开关作用于 VPP 邻居表。默认值不显示在配置中，非默认值通过 `display current-configuration` 和 `display ipv6 nd` 回读验证。

静态 IPv6 邻居绑定在三层数据面接口上。MAC 支持三段式和冒号分隔形式，保存时统一为冒号分隔形式。

```text
ipv6 neighbor 2001:db8:10::2 0211-2233-4455 interface Vlanif10
commit
display ipv6 neighbors static
undo ipv6 neighbor 2001:db8:10::2 02:11:22:33:44:55 interface Vlanif10
commit
```

多播、未指定IPv6地址，多播或全零MAC，以及二层或控制型接口都会在提交前被拒绝。静态项在提交后生效，接口重建时按已保存意图恢复。动态邻居只属于运行态，不会写入配置。

静态ARP只接受可用IPv4单播地址和六字节单播MAC；全零、组播或广播映射会在提交前拒绝。


[功能目录](../neighbors.md) · [命令参数](../reference/neighbors.md)


## IPv6 容量和实际查询

全局 ipv6 nd max-number 与 dataplane 下的 neighbor ipv6 limit 共用容量值；更改后提交，Linux 邻居表与 VPP 使用同一生效上限。以下配置的实际内核上限及 Linux 模式查询均为102600；撤销恢复102400：

~~~text
ipv6 nd max-number 102600
#
~~~

~~~text
commit
display ipv6 nd
~~~

~~~text
IPv6 Neighbor Discovery
-------------------------------------------------------------------------------
Active backend    : Linux
Maximum neighbors : 102600
Stale timeout     : - (kernel managed)
Entry recycling   : - (kernel managed)
~~~

Linux 与 VPP 的老化机制不同：Linux 显示不将 VPP stale-timeout 或 recycle 当作内核实际状态。VPP 模式下，stale-timeout150和recycle enable的查询分别显示150秒、enabled，撤销后恢复1200秒和disabled。上限表示容量策略，并非已经验证的满表承载量。

~~~text
undo ipv6 nd max-number
commit
display ipv6 nd
~~~


## Linux 数据面的邻居显示

Linux 数据面直接读取实际 ARP/ND 表，使用与 VPP 模式相同的查询形式：

~~~text
display arp all
display arp dynamic
display arp interface Ethernet0
display ipv6 neighbors
display ipv6 neighbors dynamic
display ipv6 neighbors static
display ipv6 neighbors interface Ethernet0
~~~

一次直接连接配置中，IPv4动态条目198.19.194.1和本地接口地址198.19.194.2均显示在Ethernet0上；动态筛选只保留前者，接口筛选保留两者。IPv6动态条目为2001:db8:194::1，配置对应静态邻居后显示Static1、Dynamic0；撤销静态配置后，静态查询为0条。内核为组播维护的NOARP映射不作为动态邻居显示。

IPv6静态配置与撤销示例，MAC须替换为对端实际地址：

~~~text
ipv6 neighbor 2001:db8:194::1 02fe-0273-0c16 interface Ethernet0
#
~~~

~~~text
commit
display ipv6 neighbors static
~~~

~~~text
undo ipv6 neighbor 2001:db8:194::1 02fe-0273-0c16 interface Ethernet0
commit
display ipv6 neighbors static
~~~

查询不从配置推测邻居是否存在；读取失败会报告错误。Linux不提供此查询所用的条目年龄，Age显示“-”。静态筛选、动态筛选、接口筛选和VPN实例筛选是独立形式，不能任意拼接多个筛选关键字。


## 桥域静态 ARP

桥域静态 ARP 用固定映射回答该桥域内的 ARP 请求。它不创建远端主机，也不创建到该主机的 IP 路由；主机的实际地址、MAC、二层出口和回程仍需正确。

~~~text
arp static 198.19.196.33 02fe-4e89-b4b0 bridge-domain 961
#
~~~

~~~text
commit
display arp static
display bridge-domain 961
~~~

实际查询中静态项为：
~~~text
198.19.196.33   02fe-4e89-b4b0        S/961          Vlanif961        default
Total:1         Dynamic:0        Static:1     Interface:0
~~~

桥域静态映射显示为 `S/桥域编号`，用于 ARP 应答；三层接口学习的动态邻居显示为 `D`。同一 IP 可以分别出现在这两类对象中，不能仅凭静态行就认定三层邻居已经变成永久项。用 `display arp static` 和桥域查询核对前者，用动态筛选及接口查询核对后者。

桥域显示 arp-term:on，并列出该IP/MAC映射。一次对照中，对端端口关闭时，桥域仍回应198.19.196.33的ARP请求，接收端解析为上述MAC；此时IP探测仍为2发0收，因为对端链路尚未恢复。因此，ARP解析成功不能代替端到端连通性检查。

~~~text
undo arp static 198.19.196.33 02fe-4e89-b4b0 bridge-domain 961
commit
display arp static
display bridge-domain 961
~~~

撤销后静态查询为0条。最后一条静态映射撤销后，自动启用的ARP应答关闭；EVPN或其他仍要求ARP应答的功能可继续保持它开启。


## 清除动态 IPv4 邻居

`display arp` 区分接口自身地址、静态配置和动态学习项。只清动态项可执行：

~~~text
reset ip arp interface Vlanif 100 ip 198.18.100.2
reset ip arp 198.18.100.3
reset ip arp
display arp
~~~

分别按接口与地址、仅地址、全局范围选择，按提示确认。静态配置和接口自身地址保留；重新产生业务后，动态项可以再次学习。实际验证覆盖了三种选择方式，清除后的动态项消失，静态项保留，重新学习后探测恢复。
