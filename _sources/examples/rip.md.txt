# RIP 路由

## 拓扑

~~~text
P1 Ethernet0 ─── Ethernet0 P2
链路：10.201.12.1/24 → 10.201.12.2/24
LoopBack20：10.255.20.1 → 10.255.20.2
~~~

两端运行独立的 IPv4 路由示例，不应在有同前缀的其他动态协议时评估此例。下列直连重分发只用于隔离示例；生产环境应按需限制发布前缀。

## 配置 P1

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ip address 10.201.12.1 255.255.255.0
#
interface LoopBack 20
 ip address 10.255.20.1 255.255.255.255
#
~~~

CLI 操作：

~~~text
commit
~~~

配置清单：

~~~text
rip 10
 version 2
 network 10.0.0.0
 import-route direct
 timers rip 10 30 20
#
~~~

CLI 操作：

~~~text
commit
~~~

## 配置 P2

使用相同配置，将物理接口改成 `Ethernet0`，接口地址改为 `10.201.12.2`，LoopBack 地址改为 `10.255.20.2`。双方的协议和计时参数相同。

`network` 让示例链路参加协议，`import-route direct` 使本端 LoopBack 前缀可以发布。例中的计时值用于缩短观察时间。

## 验证

~~~text
display rip 10 route
ping -n -c 3 -t 1500 10.255.20.2
~~~

P1 示例输出：

~~~text
10.255.20.2/32                              2     10.201.12.2                              10.201.12.2            0    00:29
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
~~~

收到路由说明协议已交换前缀；探测同时验证了远端前缀的转发。

## 撤销

在两端执行：

~~~text
system-view
undo rip 10
commit
display ip routing-table
~~~

示例中 P1 不再保留对端 LoopBack 路由。保留双方接口地址；若只用于这次示例，再单独清理。不要删除其他链路正在使用的协议进程。

[RIP 配置指南](../operator/rip.md)


## VPN 实例内的双栈发布

R1 Ethernet0 与 R2 Ethernet0 直连，均属于 CLI-UNDER。链路地址分别为198.18.180.1/30、198.18.180.2/30，以及2001:db8:180::1/64、2001:db8:180::2/64。R2 使用 LoopBack222 发布双栈主机地址。VPN 绑定应先于地址配置，重新绑定会清除接口上原有地址。

双方配置：
~~~text
ip vpn-instance CLI-UNDER
 ipv4-family
 ipv6-family
#
~~~

R1：
~~~text
interface Ethernet0
 ip binding vpn-instance CLI-UNDER
 ip address 198.18.180.1 30
 ipv6 enable
 ipv6 address 2001:db8:180::1 64
#
rip 2 vpn-instance CLI-UNDER
 version 2
 network 198.18.180.0
#
ripng 2 vpn-instance CLI-UNDER
 network 2001:db8:180::/64
#
~~~

R2：
~~~text
interface Ethernet0
 ip binding vpn-instance CLI-UNDER
 ip address 198.18.180.2 30
 ipv6 enable
 ipv6 address 2001:db8:180::2 64
#
interface LoopBack222
 ip binding vpn-instance CLI-UNDER
 ip address 198.51.100.222 32
 ipv6 enable
 ipv6 address 2001:db8:222::2 128
#
rip 2 vpn-instance CLI-UNDER
 version 2
 network 198.18.180.0
 network 198.51.100.0
#
ripng 2 vpn-instance CLI-UNDER
 network 2001:db8:180::/64
 network 2001:db8:222::/64
#
~~~

分别 commit 后，在R1查询：
~~~text
display rip 2 vpn-instance CLI-UNDER
display rip 2 vpn-instance CLI-UNDER interface
display rip 2 vpn-instance CLI-UNDER database
display rip 2 vpn-instance CLI-UNDER route
display rip 2 vpn-instance CLI-UNDER statistics
display ripng 2 vpn-instance CLI-UNDER
display ripng 2 vpn-instance CLI-UNDER interface
display ripng 2 vpn-instance CLI-UNDER database
display ripng 2 vpn-instance CLI-UNDER route
display ripng 2 vpn-instance CLI-UNDER statistics
display ip routing-table vpn-instance CLI-UNDER 198.51.100.222
display ipv6 routing-table vpn-instance CLI-UNDER 2001:db8:222::2
ping -vpn-instance CLI-UNDER -c 2 198.51.100.222
ping ipv6 vpn-instance CLI-UNDER -c 2 2001:db8:222::2
~~~

实际两端运行结果：R1分别学到198.51.100.222/32和2001:db8:222::2/128，协议为RIP/RIPng，Preference100、Cost2，路由带D标记；两次探测均2发2收。统计查询能看到更新来源和时间，BadPackets、BadRoutes均为0。IPv4与IPv6路径跟踪均为一跳；每族两次MTR探测均为0%丢包。

撤销时，双方删除本例协议进程：
~~~text
undo rip 2 vpn-instance CLI-UNDER
undo ripng 2 vpn-instance CLI-UNDER
~~~

R2再撤销本例专用LoopBack：
~~~text
undo interface LoopBack222
~~~

双方提交后，R1对上述两个主机前缀的查询均为0条，其他已存在的VPN与路由协议保留。若Ethernet0和CLI-UNDER也仅用于本例，确认没有其他配置依赖后再删除它们；不要删除仍承载其他业务的接口或VPN。

[RIPv1 聚合案例](rip-v1.md)
