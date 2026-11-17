# QinQ

## 拓扑与作用

CE1、PE1、CE2 均运行 VortexROS。PE1 的客户口为 dot1q-tunnel，核心口为 trunk。客户未打标签的业务增加服务标签 964；客户 VLAN 65 的业务保留原标签，在外面再增加服务标签 964。CE2 分别用单标签和双标签三层子接口终结这两项业务。

~~~text
CE1 Ethernet0 ── Ethernet0 PE1 Ethernet1 ── Ethernet0 CE2
未打标签 .200.2         服务 VLAN 964          Ethernet0.965 .200.3
客户 VLAN65 .199.1                          Ethernet0.964 .199.2
~~~

IPv4 子网分别为 198.19.200.0/24、198.19.199.0/30；IPv6 子网为 2001:db8:200::/64、2001:db8:199::/64。本例端口专用，核心链路应容纳额外 VLAN 标签。此案例证明二层传送和三层终结，不提供两个客户子网之间的额外路由策略。

## CE1

进入系统视图后配置：

~~~text
interface Ethernet0
 mtu 1600
 ip address 198.19.200.2 255.255.255.0
 ipv6 enable
 ipv6 address 2001:db8:200::2 64
#
interface Ethernet0.65
 vlan-type dot1q 65
 ip address 198.19.199.1 255.255.255.252
 ipv6 enable
 ipv6 address 2001:db8:199::1 64
#
~~~

执行 commit。

## PE1

客户口不能保留三层地址或其他 VLAN 子接口。

~~~text
enable switch
vlan 964
#
interface Ethernet0
 mtu 1600
 portswitch
 port link-type dot1q-tunnel
 port default vlan 964
#
interface Ethernet1
 mtu 1600
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 964
#
~~~

执行 commit。客户侧的全部帧进入服务 VLAN 964，不在客户口另建隐藏业务子接口。核心口按外层标签分类，出方向恢复服务标签。

## CE2

子接口编号不是线上 VLAN 标签。编号 965 的子接口终结单层 VLAN 964；编号 964 的子接口终结外标签 964、内标签 65。

~~~text
interface Ethernet0
 mtu 1600
#
interface Ethernet0.965
 vlan-type dot1q 964
 ip address 198.19.200.3 255.255.255.0
 ipv6 enable
 ipv6 address 2001:db8:200::3 64
#
interface Ethernet0.964
 vlan-type dot1q 964 inner 65
 ip address 198.19.199.2 255.255.255.252
 ipv6 enable
 ipv6 address 2001:db8:199::2 64
#
~~~

执行 commit。两种业务可共用外标签；修改或撤销其中一个接口后，仍应检查另一业务的接口、地址和连通性。

## 查询与真实结果

PE1：

~~~text
display vlan 964
display mac-address vlan 964
display current-configuration interface Ethernet0
display current-configuration interface Ethernet1
health check
~~~

实际 VLAN 成员按本例接口名表示为：

~~~text
VID  Type    Status  MAC-LRN  Description  Ports
964  common  enable  enable   VLAN 964     UT:Ethernet0(U)
                                         TG:Ethernet1(U)
~~~

UT 表示客户侧接入，不表示客户帧一定没有内标签。MAC 查询应使用 vlan 964；bridge-domain 选择器用于独立业务桥域。

CE2：

~~~text
display interface Ethernet0.965
display interface Ethernet0.964
display ip routing-table 198.19.199.0 30
~~~

实测显示两个子接口均为 Up，封装分别为：

~~~text
Encapsulation is dot1q, VLAN 964
Encapsulation is QinQ, Outer VLAN 964, Inner VLAN 65
~~~

CE1：

~~~text
ping -c 3 198.19.200.3
ping -a 198.19.199.1 -c 3 198.19.199.2
ping ipv6 -c 3 2001:db8:200::3
ping ipv6 -a 2001:db8:199::1 -c 3 2001:db8:199::2
~~~

实测结果：

| 业务 | IPv4 | IPv6 |
|---|---|---|
| 客户未打标签，核心单层服务标签 | 3 发 3 收 | 3 发 3 收 |
| 客户 VLAN65，核心双层标签，首次邻居解析 | 3 发 2 收 | 3 发 2 收 |
| 客户 VLAN65，父口恢复并完成邻居解析后 | 2 发 2 收 | 2 发 2 收 |

本例物理口设置 MTU 1600，为客户的 1500 字节 IP 报文及 VLAN 标签留出空间；客户子接口仍采用 1500。只用小 Ping 不能检查这项要求。实测 TCP 接收端完整收到 131072 字节，作为大报文传送的功能验证，不代表吞吐性能。

核心链路实际报文包含单层 0x8100/VLAN964，以及双层 0x8100/VLAN964 + 0x8100/VLAN65 的请求和回复。首次地址解析期间的丢包如实保留；持续丢包时应检查客户标签、核心放行、接口地址、邻居及回程。

## 状态转换与独立撤销

客户父口 shutdown 后，其三层子接口自动 Down，地址配置保留；undo shutdown 后恢复。

在 CE2 只删除 Ethernet0.965 并提交后，单标签业务停止，CE1 到 198.19.200.3 的探测为 1 发 0 收；双标签接口 Ethernet0.964 保留地址、恢复 Up，IPv4 和 IPv6 均能收到回复。新增或删除共享外标签的单标签接口时，相关双标签接口可能短暂重建，应在链路和邻居恢复后再检查业务。

不要通过仅执行 undo vlan-type 来删除业务：它会留下不完整子接口，严格提交校验会拒绝。

## 完整撤销

PE1 专用端口：

~~~text
interface Ethernet0
 undo portswitch
#
interface Ethernet1
 undo portswitch
#
undo vlan 964
~~~

CE1：

~~~text
undo interface Ethernet0.65
interface Ethernet0
 undo ip address
 undo ipv6 address 2001:db8:200::2 64
 undo ipv6 enable
#
~~~

CE2：

~~~text
undo interface Ethernet0.964
undo interface Ethernet0.965
~~~

各设备撤销本例额外设置的 mtu 1600（接口视图 undo mtu），再 commit，确认本例子接口、VLAN 成员、直连路由和 MAC 条目消失，再按需 save。共享核心口只撤销本例 VLAN 的放行与引用，不能清空其他业务。

[QinQ 功能](../operator/qinq.md) · [L2 子接口](subinterfaces/l2.md) · [L3 子接口](subinterfaces/l3.md)
