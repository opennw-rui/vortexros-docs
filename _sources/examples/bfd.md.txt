# 静态 BFD

独立 BFD 会话提供路径检测状态，本身不增加路由，也不会自动撤销静态路由。需要动态协议撤路时，使用[协议绑定](../operator/bfd/protocols.md)。

## 拓扑与前提

两台设备的三层接口相连，在 VPN 实例 BLUE 中运行 BFD：

~~~text
P1 Ethernet0 198.19.197.1/24 ---- 198.19.197.2/24 Ethernet0 P2
             2001:db8:197::1/64 ---- 2001:db8:197::2/64
~~~

接口必须 Up，源地址已配置，对端地址可达；链路上的过滤策略应允许单跳 BFD UDP3784。以下两端配置分别执行，不要把两端地址同时配置到一台设备。

## P1

~~~text
bfd
ip vpn-instance BLUE
 ipv4-family
 ipv6-family
#
interface Ethernet 0
 ip binding vpn-instance BLUE
 ip address 198.19.197.1 24
 ipv6 enable
 ipv6 address 2001:db8:197::1 64
#
bfd TO-P2 bind peer-ip 198.19.197.2 source-ip 198.19.197.1 interface Ethernet0 vpn-instance BLUE
 min-tx-interval 500
 min-rx-interval 600
 detect-multiplier 4
 log-session-changes
#
bfd TO-P2-V6 bind peer-ipv6 2001:db8:197::2 source-ip 2001:db8:197::1 interface Ethernet0 vpn-instance BLUE
#
commit
save
~~~

## P2

~~~text
bfd
ip vpn-instance BLUE
 ipv4-family
 ipv6-family
#
interface Ethernet 0
 ip binding vpn-instance BLUE
 ip address 198.19.197.2 24
 ipv6 enable
 ipv6 address 2001:db8:197::2 64
#
bfd TO-P1 bind peer-ip 198.19.197.1 source-ip 198.19.197.2 interface Ethernet0 vpn-instance BLUE
 min-tx-interval 600
 min-rx-interval 500
 detect-multiplier 4
 log-session-changes
#
bfd TO-P1-V6 bind peer-ipv6 2001:db8:197::1 source-ip 2001:db8:197::2 interface Ethernet0 vpn-instance BLUE
#
commit
save
~~~

默认间隔为1000ms、检测3次，默认参数不显示在配置中。配置的最小发送与接收间隔需要与对端协商；不能只用本地发送值乘以检测次数来推断最终超时。

## 验证

~~~text
display bfd session all
display bfd session TO-P2
display bfd statistics
display bfd configuration
~~~

实测 IPv4 与 IPv6 单跳会话均为 Up。P1 非默认 IPv4 计时结果：

~~~text
Source IP Address : 198.19.197.1
Configured Tx/Rx/Multiplier : 500/600/4
Effective Tx/Rx/Multiplier : 500/600/4
Detection Timeout (ms)      : 2400
Local/Remote Diagnostic     : ok / ok
~~~

P2 的检测超时为2000ms。实际鉴别值由会话建立时分配，不需手工配置。

## 修改、停止与恢复

用相同绑定重新进入已有会话，不会创建第二条会话：

~~~text
bfd TO-P2 bind peer-ip 198.19.197.2 source-ip 198.19.197.1 interface Ethernet0 vpn-instance BLUE
 passive-mode
 shutdown
#
commit
~~~

实测本端变为 Shutdown，诊断为 administratively down；对端变为 Down。被动模式不主动发起建立，至少需要另一端主动工作。保持对端为主动模式，恢复本端：

~~~text
bfd TO-P2 bind peer-ip 198.19.197.2 source-ip 198.19.197.1 interface Ethernet0 vpn-instance BLUE
 undo shutdown
#
commit
display bfd session TO-P2
~~~

实测会话恢复 Up。恢复缺省参数时，两端分别进入自己的会话执行：

~~~text
undo passive-mode
undo log-session-changes
undo min-tx-interval
undo min-rx-interval
undo detect-multiplier
#
commit
~~~

实测两端有效参数均回到1000/1000/3；配置中省略这些默认项。

## 多跳

多跳会话需指定 source-ip，不绑定 interface。先通过已有静态或动态路由保证两端 LoopBack 互通，并允许 UDP4784。假设 BLUE 中 P1 LoopBack246 为172.30.0.1，P2 LoopBack247 为172.31.0.2：

P1：

~~~text
bfd LOOP-TO-P2 bind peer-ip 172.31.0.2 source-ip 172.30.0.1 vpn-instance BLUE multi-hop
#
commit
~~~

P2：

~~~text
bfd LOOP-TO-P1 bind peer-ip 172.30.0.1 source-ip 172.31.0.2 vpn-instance BLUE multi-hop
#
commit
~~~

实测多跳会话为 Up，默认检测超时3000ms。[RIP 多路径案例](rip-bfd-ecmp.md)提供两端 LoopBack 的路由配置。

## 保存、服务重启与撤销

两端 save 后，P1 执行：

~~~text
reset service bfd
~~~

按提示确认。该操作会重启 BFD 服务，相关协议可能短暂重新检测邻居。实测运行配置自动回放，IPv4 单跳、IPv6 单跳、多跳及原有协议会话全部恢复 Up。

两端分别删除本例的会话，P1 示例：

~~~text
undo bfd TO-P2
undo bfd TO-P2-V6
undo bfd LOOP-TO-P2
commit
display bfd session all
~~~

实测本例会话消失，其他协议仍使用的动态会话保留。不要为撤销本例关闭全局 BFD。接口与 VPN 实例若只供本例使用，再撤销对应地址和绑定后删除；其他业务依赖的对象应保留。
