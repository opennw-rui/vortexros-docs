# QinQ

## 拓扑与作用

CE1、PE1、PE2、CE2 均运行 VortexROS。客户未打标签的报文及 VLAN 10 报文，通过服务 VLAN 2200 穿过核心；出口移除服务标签，保留客户标签。本例不提供跨子网路由。

~~~text
CE1 Ethernet0 ── Ethernet0 PE1 Ethernet1 ── Ethernet0 PE2 Ethernet1 ── Ethernet0 CE2
未打标签: 198.18.209.2/24                                      198.18.209.3/24
VLAN 10: 198.18.210.2/24                                       198.18.210.3/24
                          核心服务 VLAN 2200
~~~

客户口由 dot1q-tunnel 独占标签分类空间，不应再保留三层地址或独立子接口。核心链路需容纳额外 VLAN 标签，其他 VLAN 业务应与本例分开规划。

## CE1 与 CE2

CE1：

~~~text
system-view
interface Ethernet0
 ip address 198.18.209.2 255.255.255.0
quit
interface Ethernet0.10
 vlan-type dot1q 10
 ip address 198.18.210.2 255.255.255.0
quit
commit
~~~

CE2：

~~~text
system-view
interface Ethernet0
 ip address 198.18.209.3 255.255.255.0
quit
interface Ethernet0.10
 vlan-type dot1q 10
 ip address 198.18.210.3 255.255.255.0
quit
commit
~~~

## PE1

~~~text
system-view
enable switch
vlan 2200
quit
interface Ethernet0
 portswitch
 port link-type dot1q-tunnel
 port default vlan 2200
quit
interface Ethernet1
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 2200
quit
commit
~~~

## PE2

~~~text
system-view
enable switch
vlan 2200
quit
interface Ethernet1
 portswitch
 port link-type dot1q-tunnel
 port default vlan 2200
quit
interface Ethernet0
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 2200
quit
commit
~~~

## 验证

两台 PE 查询 VLAN 和客户口配置：

~~~text
display vlan 2200
display current-configuration interface Ethernet0
display current-configuration interface Ethernet1
display health
~~~

PE1 示例输出：

~~~text
VID   Type    Status  MAC-LRN  Description      Ports
2200  common  enable  enable   VLAN 2200        UT:Ethernet0(U)
                                                TG:Ethernet1(U)
~~~

UT 表示客户侧业务接入，不表示收到的客户帧一定不含 C-Tag。PE2 对应的 UT 是 Ethernet1，TG 是 Ethernet0。

CE1 执行以下命令，CE2 使用本端地址向 .2 反向检查，两条业务均应可达：

~~~text
ping -a 198.18.209.2 -c 3 198.18.209.3
ping -a 198.18.210.2 -c 3 198.18.210.3
~~~

VLAN 10 在核心的帧格式为 S-Tag 2200、C-Tag 10、客户载荷。普通 Ping 只验证可达性；需要确认线上标签时，在核心链路使用独立报文分析设备。

## 撤销

两台 PE 均执行以下命令。本例核心口为专用口；共享核心口应只撤销 VLAN 2200 的放行及引用。

~~~text
system-view
interface Ethernet0
 undo portswitch
quit
interface Ethernet1
 undo portswitch
quit
undo vlan 2200
commit
display vlan 2200
~~~

CE1/CE2 删除 Ethernet0.10，并在 Ethernet0 撤销本例 IP 地址，再提交。客户业务应不再通过该服务 VLAN 互通；各设备按需 save 保存撤销结果。

[QinQ 功能](../operator/qinq.md) · [子接口](subinterfaces/index.md) · [VLAN 参数](../operator/reference/vlan.md)
