# 接口、区域与发布

## 配置

OSPFv3用于IPv6动态路由。先创建进程和区域，再在三层接口下绑定进程：

```text
ospfv3 1 router-id 10.0.0.1
 maximum load-balancing 6
 bandwidth-reference 100000
 import-route static
 area 0.0.0.0
#
interface Vlanif 12
 ipv6 enable
 ospfv3 1 area 0.0.0.0
 ospfv3 cost 25
 ospfv3 network-type p2p
 ospfv3 dr-priority 0
 ospfv3 timer hello 3
 ospfv3 timer dead 12
 ospfv3 timer retransmit 4
 ospfv3 timer transmit-delay 2
```

接口必须属于与进程相同的VPN实例。进程1对应default；其他进程必须在创建时指定非default VPN，例如`ospfv3 2 router-id 10.0.0.2 vpn-instance BLUE`。同一个VPN只能对应一个后端OSPFv3实例，同一个接口不能同时加入两个OSPFv3进程。

Stub、NSSA和IPv6区域汇总在area视图配置：

```text
ospfv3 1
 area 0.0.0.1
  nssa no-summary
  abr-summary 2001:db8:: 32 not-advertise
```

`stub`与`nssa`互斥。`default-route-advertise`仅在本机已有IPv6默认路由时发布，`default-route-advertise always`则不依赖本机默认路由。`silent-interface INTERFACE`保留该接口的网络发布但停止建立邻居。

```text
display ospfv3 1 brief
display ospfv3 1 peer brief
display ospfv3 1 interface
display ospfv3 1 lsdb
display ospfv3 1 routing
reset ospfv3 1 process
```

`peer brief`中的邻居状态来自FRR OSPFv3运行态，`routing`中的路由数量只统计协议为`ospf6`的IPv6路由。配置提交后，继续确认邻居Full、IPv6路由存在和业务地址可达。

撤销示例：

```text
interface Vlanif 12
 undo ospfv3 1 area 0.0.0.0
#
ospfv3 1
 area 0.0.0.1
  undo abr-summary 2001:db8:: 32
  undo nssa
#
undo ospfv3 1
```

CLI 操作：

```text
commit
```


[功能目录](../ospfv3.md) · [命令参数](../reference/ospfv3.md)


## 网络类型与优先级查询

`display ospfv3 1 interface` 的 Type 是实际运行的网络类型：默认以太网接口显示 `BROADCAST`；配置 `ospfv3 network-type p2p` 并提交后显示 `POINTOPOINT`。撤销该命令后恢复默认类型，邻居会重新建立。

OSPFv3 的进程摘要中，`Backend default preference` 是后端通用缺省值。路由选择应查看 `display ipv6 routing-table protocol ospfv3` 的 Preference；当前内部路由为10，外部路由为150。

两端在同一区域建立邻居后，实际路由查询示例：

```text
<VortexROS> display ipv6 routing-table protocol ospfv3
Destination  : 2001:db8:251::2                         PrefixLength : 128
NextHop      : fe80::fe:54ff:fe56:cc86                 Preference   : 10
Cost         : 11                                      Protocol     : OSPF
```

该前缀同时由 RIPng 发布时，OSPFv3 的优先级10优于 RIPng 的100。撤销远端接口的OSPFv3绑定后，应在路由表确认该前缀切换到RIPng；不能只凭邻居Full判断业务路由存在。


## 接口定时器

接口视图下的 ospfv3 timer hello、dead、retransmit、transmit-delay 分别设置 Hello、邻居失效、LSA 重传和估计传输延迟，单位为秒。两端 Hello/Dead 须一致。例如：

~~~text
interface Ethernet0
 ospfv3 timer hello 2
 ospfv3 timer dead 8
 ospfv3 timer retransmit 3
 ospfv3 timer transmit-delay 2
#
~~~

提交后检查 display ospfv3 1 peer，邻居应为 Full。本例剩余 Dead 时间约 7 秒；通过 OSPFv3 发布远端 LoopBack 后，路由表选中 Preference 10、Cost 11 的 /128，IPv6 探测 2/2。

恢复时在对应接口执行 undo ospfv3 timer hello、undo ospfv3 timer dead、undo ospfv3 timer retransmit 和 undo ospfv3 timer transmit-delay 并提交。默认值分别为 10、40、5、1 秒；修改过程中留意双端参数不匹配造成的邻居变化。


## 自动开销与显式开销

`bandwidth-reference` 的单位为 Mbit/s，用于未设置显式开销的接口。修改进程参考带宽会重新计算这些接口的开销；`ospfv3 cost` 则固定当前接口的开销，不再跟随参考带宽变化。两端应采用相同的参考带宽，以免出现方向不同的路径度量。

例如，参考带宽为 50000、链路带宽为 10000 Mbit/s 时，链路自动开销为 5；远端环回开销为 5，查询到的环回路由 Cost 为 10。本端链路改为显式 37 后，同一路由 Cost 为 42：

```text
ospfv3 1
 bandwidth-reference 50000
#
interface Ethernet0
 ospfv3 cost 37
#
commit
display ospfv3 1 interface
display ipv6 routing-table 2001:db8:244::3
ping ipv6 -a 2001:db8:245::2 -c 1 2001:db8:244::3
```

对应运行结果摘录：

```text
Destination  : 2001:db8:244::3                         PrefixLength : 128
NextHop      : fe80::fe:bff:fede:cd74                  Preference   : 10
Cost         : 42                                      Protocol     : OSPF
1 packets transmitted, 1 received, 0% packet loss, time 0ms
```

`undo ospfv3 cost` 恢复自动计算；进程下的 `undo bandwidth-reference` 恢复后端缺省参考带宽。撤销后应重新查询接口开销和目标路由，不能把撤销前的度量当作当前结果。

## BFD 联动

接口 BFD 用于比 Hello/Dead 更快发现双向转发故障；它不代替 OSPFv3 邻接。先在系统视图启用 BFD，再配置参与 OSPFv3 的接口：

```text
bfd
#
interface Ethernet0
 ospfv3 bfd min-tx-interval 200 min-rx-interval 300 detect-multiplier 4
 ospfv3 bfd enable
#
commit
display bfd session
display ospfv3 1 peer
```

本例本端期望发送间隔 200 ms、最小接收间隔 300 ms、检测倍数 4；实际间隔还受对端协商影响。一组正常运行结果中，链路本地邻居 BFD 为 Up，协商发送 200 ms、接收 300 ms、检测时间 1200 ms，OSPFv3 邻居同时为 Full。只看配置中的 `enable` 不能确认 BFD 已工作。

`undo ospfv3 bfd min-tx-interval min-rx-interval detect-multiplier` 恢复默认计时器；`undo ospfv3 bfd enable` 解除该接口的 OSPFv3/BFD 联动。默认使用 1000 ms 发送、1000 ms 接收、检测 3 次。解除联动后，OSPFv3 仍按自身 Hello/Dead 维持邻接。

同接口同时启用 IS-IS IPv6 与 OSPFv3 时，二者可能共用链路本地 BFD 会话，有效计时器必须相同。修改顺序和故障边界见[协议绑定](../bfd/protocols.md#共享和计时归属)。

## 撤销外部路由发布

在进程视图使用 `import-route direct cost 43 type 1` 可以发布本 VPN 中的直连前缀；`undo import-route direct` 仅取消这项发布，不删除本机直连接口或地址。Type1 外部路由将域内到达发布者的开销计入总 Cost，Type2 则优先比较外部度量。

实际外部前缀 2001:db8:104::3/128 以 E1、Preference150、Cost53 学到；撤销该项发布并提交后，对端相同前缀的路由查询为0。验证时应区分其他协议对相同前缀的替代路由。

~~~text
ospfv3 2 vpn-instance BLUE
 undo import-route direct
#
commit
display ospfv3 2 routing
display ipv6 routing-table vpn-instance BLUE 2001:db8:104::3 128
~~~

进程视图的 `router-id` / `undo router-id` 与自动选择遵循 [Router ID 与重置](../ospf/reset.md) 的规则；OSPFv3 使用自己的 `reset ospfv3 2 process` 命令。
