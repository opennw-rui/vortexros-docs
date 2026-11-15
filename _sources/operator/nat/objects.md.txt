# 对象与规则

地址集和端口集复用匹配条件；地址池提供转换后的源地址。地址池不是匹配地址集，二者不能互换。名称区分大小写，引用对象必须存在。

## 创建和绑定

在系统视图输入；本例定义内部网段、Web 端口和公网源地址池：

~~~text
system-view
nat-policy address-set name LAB-LAN
 address 198.18.11.0/24
quit
nat-policy port-set name LAB-WEB
 port 80
 port 443
quit
nat-policy address-pool name LAB-PUBLIC
 address 198.19.81.1/32
 pat-port-range 20000-20063
quit
nat-policy name LAB-SNAT
 statistic enable
 rule 10
  source address-set name LAB-LAN
  destination port-set name LAB-WEB
  protocol tcp
  action snat pat address-pool LAB-PUBLIC
 quit
quit
interface host-p1a12
 nat-policy LAB-SNAT outbound
quit
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

旧实验的真实输出节选（地址池尚未缩小 PAT 范围时）：

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
interface host-p1a12
 undo nat-policy LAB-SNAT outbound
quit
undo nat-policy name LAB-SNAT
undo nat-policy address-pool name LAB-PUBLIC
undo nat-policy port-set name LAB-WEB
undo nat-policy address-set name LAB-LAN
commit
display nat-policy runtime
display nat-policy objects
~~~

只移除一个成员时，在相应对象视图执行 `undo address PREFIX` 或 `undo port PORT`；只清除一个匹配条件时，在规则视图执行对应 `undo source/destination ...`。删除仍被引用的对象会被拒绝。

[全部参数](../reference/nat.md) · [保存与恢复](../01-cli.md)
