# OSPFv3 邻接

## 拓扑

~~~text
LoopBack20 2001:db8:20::1/128          LoopBack20 2001:db8:20::2/128
P1 host-p1e12 2001:db8:12::1/64 ─── 2001:db8:12::2/64 host-p2e12 P2
~~~

两端使用默认 VPN、进程 1、Area 0。链路使用点到点网络类型，两端 Hello/Dead 设置相同。链路地址和测试 LoopBack 先提交，然后启用协议。

## 配置 P1

~~~text
system-view
interface host-p1e12
 ipv6 address 2001:db8:12::1 64
 quit
interface LoopBack 20
 ip address 10.255.20.1 255.255.255.255
 ipv6 address 2001:db8:20::1 128
 quit
commit
ospfv3 1 router-id 10.255.20.1
 area 0.0.0.0
  quit
 quit
interface host-p1e12
 ospfv3 1 area 0.0.0.0
 ospfv3 network-type p2p
 ospfv3 timer hello 3
 ospfv3 timer dead 12
 quit
interface LoopBack 20
 ospfv3 1 area 0.0.0.0
 quit
commit
~~~

## 配置 P2

使用同一命令块，将接口改为 `host-p2e12`，三个本端地址分别改为 `2001:db8:12::2`、`10.255.20.2` 和 `2001:db8:20::2`；Router ID 也改为 `10.255.20.2`。Area、网络类型和计时器不变。

协议通过链路建立邻接，并发布 LoopBack IPv6 前缀。这个配置不引入静态路由或默认路由。

## 验证

**P1：**

~~~text
display ospfv3 1 peer brief
display ospfv3 1 routing
ping ipv6 -n -c 3 -t 1500 2001:db8:20::2
~~~

实际输出节选：

~~~text
Neighbor ID     Pri  State          Dead Time  Interface
10.255.20.2     1    Full/PointToPoint 00:00:10   host-p1e12

2001:db8:20::2/128                          IA           fe80::fe:78ff:fe2a:b801                  host-p1e12

--- 2001:db8:20::2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
~~~

## 撤销

在两端先解除接口绑定，再删专用进程。以下为 P1，P2 替换物理接口名。

~~~text
system-view
interface LoopBack 20
 undo ospfv3 1 area 0.0.0.0
 quit
interface host-p1e12
 undo ospfv3 1 area 0.0.0.0
 quit
undo ospfv3 1
commit
display ipv6 routing-table
~~~

实测 P1 的路由表不再包含对端 LoopBack 前缀，本地接口地址仍可保留。

[OSPFv3 配置指南](../operator/ospfv3.md)


## 静态路由引入与撤销

以下是本轮单独完成的静态路由实测，不把 IS-IS 或 RIPng 选中路由上的成功探测算成 OSPFv3 的结果。

```text
P1 host-p1a12 2001:db8:80::1/64 ─── 2001:db8:80::2/64 host-p2a12 P2
                                               LoopBack98 2001:db8:99::2/128
                                               静态汇总 2001:db8:99::/64
```

P1：

```text
ospfv3 1 router-id 1.1.1.1
 bandwidth-reference 10000
 area 0.0.0.0
  quit
 quit
interface host-p1a12
 ipv6 address 2001:db8:80::1 64
 ospfv3 1 area 0.0.0.0
 ospfv3 network-type p2p
 quit
commit
```

P2：

```text
interface host-p2a12
 ipv6 address 2001:db8:80::2 64
 quit
interface LoopBack 98
 ipv6 address 2001:db8:99::2 128
 quit
ipv6 route-static 2001:db8:99:: 64 NULL 0
ospfv3 1 router-id 2.2.2.2
 bandwidth-reference 10000
 import-route static cost 37 type 2
 area 0.0.0.0
  quit
 quit
interface host-p2a12
 ospfv3 1 area 0.0.0.0
 ospfv3 network-type p2p
 quit
commit
```

静态汇总使用 NULL 0，但本机 LoopBack 的 /128 更具体，发往该本机地址的流量正常交付；汇总中的其他未配置目的地址会被丢弃。不能把 NULL 路由当成到整个 /64 的真实业务出口。

若复用已有多协议拓扑，先检查选中路由。本次暂时从 P2 LoopBack98 撤销 IS-IS IPv6 发布，并从 RIPng 撤销静态引入，使该测试前缀由 OSPFv3 胜出。测试结束后已恢复两项原配置。首次使用本节的新拓扑不需要配置这些无关协议。

P1：

```text
display ipv6 routing-table 2001:db8:99::2
ping ipv6 -c 3 -a 2001:db8:80::1 2001:db8:99::2
```

实际选中路由节选：

```text
Destination  : 2001:db8:99::  PrefixLength : 64
Preference   : 150          Cost         : 37
Protocol     : OSPF         Interface    : host-p1a12

3 packets transmitted, 3 received, 0% packet loss
```

底层 FRR 同时确认该前缀的 protocol 为 ospf6，selected/installed 为 true，distance150、metric37。链路本地下一跳随接口地址而变。E2 的 37 是外部开销；不能错误地以到达发布者的内部开销替代它。

P2 撤销引入：

```text
ospfv3 1
 undo import-route static
 quit
commit
```

P1 的成功查询返回 `Destinations : 0 / Routes : 0`，一次探测没有回包。恢复 `import-route static cost 37 type 2` 后路由重新出现；P2 的 `reset service ospf` 完成 Running 回放及验证后，P1 仍选中同一 OSPFv3 前缀与开销。该结果分别验证了协议发布、实际转发、撤销和受管协议重启。


## VPN 实例中的 IPv6 静态引入

复用 [OSPF 的 CLI-UNDER 拓扑](ospf.md#vpn-实例的静态引入)，在两端 VPN 内启用 `ipv6-family`，b12 地址分别为2001:db8:180::1/64、::2/64。P2 LoopBack80 增加2001:db8:181::2/128。

P1：

```text
ospfv3 80 router-id 10.255.80.1 vpn-instance CLI-UNDER
 quit
interface host-p1b12
 ipv6 address 2001:db8:180::1 64
 ospfv3 80 area 0
 quit
commit
```

P2：

```text
ospfv3 80 router-id 10.255.80.2 vpn-instance CLI-UNDER
 import-route static cost 38 type 2
 quit
interface host-p2b12
 ipv6 address 2001:db8:180::2 64
 ospfv3 80 area 0
 quit
interface LoopBack80
 ipv6 address 2001:db8:181::2 128
 quit
ipv6 route-static vpn-instance CLI-UNDER 2001:db8:181:: 64 NULL 0
commit
```

在首次绑定接口之前创建对应 OSPFv3 进程；已存在本例进程时可直接重新进入。非默认进程重新进入时仍带 `vpn-instance CLI-UNDER`。

P1 实测：

```text
display ospfv3 vpn-instance CLI-UNDER peer
display ipv6 routing-table vpn-instance CLI-UNDER 2001:db8:181::2 verbose
ping ipv6 -vpn-instance CLI-UNDER -c 3 -a 2001:db8:180::1 2001:db8:181::2
```

路由为2001:db8:181::/64、OSPF、Preference150、Cost38，下一跳为对端真实链路本地地址，经host-p1b12；流量3/3。撤销 `import-route static` 后，没有替代发布时成功路由查询 Summary Count 为0。恢复后可执行 `reset ospfv3 80 process`，确认 Y；本轮实际返回 runtime state matches the running configuration。此命令中断目标进程的邻接，不能在业务环境当作无影响查询。

## 多区域汇总与NSSA

复用前面 CLI-UNDER 的 IPv6 骨干链路 b12。在两端增加 q12 区域 1，P2 增加两个区域内 LoopBack。两台设备均为 ABR。

```text
          area 0: 2001:db8:180::/64
P1 b12 ----------------------------- b12 P2
   q12 ----------------------------- q12
          area 1: 2001:db8:182::/64
                              LoopBack81 2001:db8:184::2/128
                              LoopBack82 2001:db8:185::2/128
```

P1：

```text
ospfv3 80 vpn-instance CLI-UNDER
 area 0.0.0.1
  quit
 quit
interface host-p1q12
 ip binding vpn-instance CLI-UNDER
 ipv6 address 2001:db8:182::1 64
 ospfv3 80 area 0.0.0.1
 ospfv3 network-type p2p
 ospfv3 timer hello 1
 ospfv3 timer dead 4
 quit
commit
```

P2 使用相同进程、区域和计时器，接口改为 `host-p2q12`，地址改为 `2001:db8:182::2`，然后增加：

```text
interface LoopBack 81
 ip binding vpn-instance CLI-UNDER
 ipv6 address 2001:db8:184::2 128
 ospfv3 80 area 0.0.0.1
 quit
interface LoopBack 82
 ip binding vpn-instance CLI-UNDER
 ipv6 address 2001:db8:185::2 128
 ospfv3 80 area 0.0.0.1
 quit
ospfv3 80 vpn-instance CLI-UNDER
 area 0.0.0.1
  abr-summary 2001:db8:184:: 47
  quit
 quit
commit
```

在 P1 的 OSPFv3 进程中设置 `silent-interface host-p1q12` 并提交，以隔离骨干上的汇总路径。实测 P1 查询得到 `2001:db8:184::/47`，优先级 10、代价 11，指定源地址的探测为 3/3。P2 将其改为 `abr-summary 2001:db8:184:: 47 not-advertise` 后，成功路由查询返回 0 条，探测为 0/1。恢复汇总，再在 P1 进程中 `undo silent-interface host-p1q12` 恢复区域 1 邻接。

在 P2 撤销该区域汇总；两端按相同顺序在线切换为 NSSA：

```text
ospfv3 80 vpn-instance CLI-UNDER
 area 0.0.0.1
  undo abr-summary 2001:db8:184:: 47
  nssa no-summary
  quit
 quit
commit
display ospfv3 vpn-instance CLI-UNDER peer
display ospfv3 vpn-instance CLI-UNDER lsdb
```

P1 没有这条汇总时不执行对应的撤销命令。保持上一个案例中 P2 已存在的静态前缀和 `import-route static cost 38 type 2` 不变。包含本次必要 OSPFv3 后端修正的版本，在 ABR 从普通区域转为 NSSA 后，会为已有静态外部前缀生成 Type7；不需要撤销再重配引入命令。两端实际 LSDB 均出现来自 `10.255.80.2` 的 Type7，其原生 LSA 载荷为 `2001:db8:181::/64`。普通区域阶段已有 Type5，转换后的 Type7 是此次专门验证的行为。

LSDB 摘要会按区域、接口和 AS 分区；同一 LSA 包含多个前缀不会重复增加 `Total LSAs`。一次真实多区域查询为 29，与原生 JSON 的作用域内唯一 LSA 总数一致。Age 3600 表示冲刷中的记录，撤销是否完成应另外核对路由表。

要改为完全 stub，两端在区域视图执行 `undo nssa`、`stub no-summary` 后提交。本例原生配置与邻居 Full 已验证；双 ABR 拓扑不作为单出口 stub 默认路由的验证证据。恢复普通区域使用 `undo stub`；删除实验 LoopBack 前先解除它们的 `ospfv3 80 area 0.0.0.1` 绑定。保留配置前执行 `save`。
