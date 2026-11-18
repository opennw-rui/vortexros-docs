# 对象与规则

地址集和端口集复用匹配条件；地址池提供转换后的源地址。地址池不是匹配地址集，二者不能互换。名称区分大小写，引用对象必须存在。

## 创建和绑定

在系统视图输入；本例定义内部网段、Web 端口和公网源地址池：

~~~text
system-view
~~~

配置清单：

~~~text
nat-policy address-set name LAB-LAN
 address 198.18.11.0/24
#
nat-policy port-set name LAB-WEB
 port 80
 port 443
#
nat-policy address-pool name LAB-PUBLIC
 address 198.19.81.1/32
 pat-port-range 20000-20063
#
nat-policy name LAB-SNAT
 statistic enable
 rule 10
  source address-set name LAB-LAN
  destination port-set name LAB-WEB
  protocol tcp
  action snat pat address-pool LAB-PUBLIC
#
interface Ethernet0
 nat-policy LAB-SNAT outbound
#
~~~

CLI 操作：

~~~text
commit
~~~

地址接受单个 IPv4、前缀或地址加掩码。端口接受单值或闭区间，例如 `20000-20063`，不能写成两个空格分开的数。规则优先级数值越小越先匹配；未显式设置时由规则 ID 派生。不要把本例的 TCP Web 条件用于需要 UDP/ICMP 的完整出口策略。

## 查询

~~~text
display nat-policy address-set LAB-LAN
display nat-policy port-set LAB-WEB
display nat-policy address-pool LAB-PUBLIC
display nat-policy objects
display nat-policy interfaces
display nat-policy name LAB-SNAT
~~~

旧示例的示例输出（地址池尚未缩小 PAT 范围时）：

~~~text
Name        Address         PAT range
-------------------------------------------------------------------------------
LAB-PUBLIC  198.19.81.1/32  10000-65535
~~~

`objects` 查看运行对象、成员和引用数；`interfaces` 查看实际方向绑定；`name` 查看规则。配置存在不能替代运行对象及业务验证。

## 撤销

先解除绑定，再删除策略，最后删除不再被使用的对象：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo nat-policy LAB-SNAT outbound
#
undo nat-policy name LAB-SNAT
undo nat-policy address-pool name LAB-PUBLIC
undo nat-policy port-set name LAB-WEB
undo nat-policy address-set name LAB-LAN
~~~

CLI 操作：

~~~text
commit
display nat-policy runtime
display nat-policy objects
~~~

只移除一个成员时，在相应对象视图执行 `undo address PREFIX` 或 `undo port PORT`；只清除一个匹配条件时，在规则视图执行对应 `undo source/destination ...`。删除仍被引用的对象会被拒绝。

[全部参数](../reference/nat.md) · [保存与恢复](../01-cli.md)

## 用协议号选择流量

规则内的 `protocol` 支持 any、tcp、udp、icmp 和0–255的IP协议号。
例如 `protocol 17` 与 UDP 对应；它控制这条转换规则的匹配范围，不会禁止其他协议转发。
省略或执行 `undo protocol` 表示匹配任意协议，缺省值不显示在配置中。

以下示例的 Ethernet1 已配置地址198.18.31.15，客户端通过另一接口进入：

~~~text
nat-policy name NUMPROTO
 statistic enable
 rule 10
  source address 198.18.30.99/32
  protocol 17
  action snat no-pat interface
#
interface Ethernet1
 nat-policy NUMPROTO outbound
#
commit
display current-configuration configuration nat-policy NUMPROTO
display nat-policy sessions name NUMPROTO
~~~

实际UDP源198.18.30.99:42035转换为198.18.31.15:42035，出口收到3/3。
同源ICMP不匹配这条UDP规则，仍以原地址发出。规则内执行 `undo protocol` 并提交后，
新的ICMP会话转换为198.18.31.15，标识符保持42030；实际回复成功反向转换并返回客户端。

删除时先在Ethernet1执行 `undo nat-policy NUMPROTO outbound`，
再执行 `undo nat-policy name NUMPROTO` 和 `commit`。
示例撤销后会话归零，新的UDP流量以原地址转发3/3。

## 按 IP 协议号匹配

规则中的 protocol 支持 tcp、udp、icmp、any，也可以直接填写0–255的IP协议号。
例如17为UDP，1为ICMP。undo protocol 恢复为任意协议，默认项不显示在配置中。
不要把IP协议号与TCP/UDP端口号混淆。

以下只转换 Ethernet1 发出的指定客户端UDP流量；其他协议保持原源地址：

~~~text
nat-policy name NUMPROTO
 statistic enable
 rule 10
  source address 198.18.30.99/32
  protocol 17
  action snat no-pat interface
#
interface Ethernet1
 nat-policy NUMPROTO outbound
#
commit
display current-configuration configuration nat-policy NUMPROTO
display nat-policy sessions name NUMPROTO
~~~

在 Ethernet1 地址为198.18.31.15的实例中，实际UDP报文由198.18.30.99:42035
转换为198.18.31.15:42035，出口收到3/3；同一客户端的ICMP报文仍保留原源地址。

~~~text
nat-policy name NUMPROTO
 rule 10
  undo protocol
#
commit
~~~

撤销协议条件后，新ICMP请求也被转换为198.18.31.15，identifier42030保持不变；
实际回复经反向转换返回198.18.30.99。只修改条件不会改写已有会话的映射，使用新流验证。
完全撤销时解除Ethernet1上的绑定，再执行undo nat-policy name NUMPROTO和commit。
此例实际撤销后会话数为0，UDP恢复原源地址，出口收到3/3。
