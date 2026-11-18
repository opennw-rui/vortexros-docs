# 路由查询

查询规模较大时，先按 VPN、协议或前缀缩小范围。

## 协议查询

协议查询用于查看邻居及协议学习的路由；系统路由表显示选路结果，FIB显示实际转发路径。`display mpls forwarding-table`查看MPLS数据面转发表。

常用大表入口如下：

```text
display bgp routing-table
display ospf 1 routing
display ospfv3 1 routing
display isis 1 route
display rip 1 route
display ripng 1 route
display mpls ldp binding
display mpls lsp
```

大表查询可按VPN、协议和前缀缩小范围；终端输出较多时使用分页或输出修饰符。控制面协议表与数据面FIB用途不同，排查转发时应同时核对。

## 变更后检查

每次变更后至少执行：

```text
display this
commit
display current-configuration
display ip routing-table
display alarm active
```

随后使用本节对应的邻居、路由、BFD或VRRP命令检查运行状态。确认业务正常后再执行 `save`。删除配置时先解除引用或接口绑定，再删除协议进程和策略对象。

## VPN 内的组合查询

```text
display ip routing-table vpn-instance CLI-UNDER 198.18.181.0 24
display ipv6 routing-table vpn-instance CLI-UNDER 2001:db8:181:: 64
display ip routing-table vpn-instance CLI-UNDER protocol ospf
display ipv6 routing-table vpn-instance CLI-UNDER protocol ospfv3
```

先选择 VPN 实例，再按前缀或协议过滤。核对路由来源、Preference、Cost、下一跳和出口，避免把其他协议的更优路径误认为目标协议已生效。

默认路由精确查询使用 0.0.0.0 0 和 :: 0，第二项为前缀长度。撤销默认路由发布后，应以成功查询返回零条作为撤销结果；查询报错时先排查服务，不能据此判断路由不存在。


## 组合条件与显示上限

IPv4 和 IPv6 路由查询可组合 VPN、协议、目的前缀、`longer-match` 和 `limit`。
以下查询分别只显示 SHOW201 的第一条有效静态路由，以及指定网段内最多两条静态路由：

```text
display ip routing-table vpn-instance SHOW201 protocol static limit 1
display ipv6 routing-table vpn-instance SHOW201 protocol static limit 1
display ip routing-table 198.19.0.0 16 longer-match protocol static limit 2
display ipv6 routing-table 2001:db8:200:: 40 longer-match protocol static limit 2
```

`longer-match` 包含给定前缀及其更具体前缀。只输入目的地址而不指定掩码时，
查询该地址的最长匹配路由。`limit` 限制本次显示的路由条目，不修改路由容量或实际选路。
同一目的前缀存在多条路径时，每条显示路径分别占一个条目；IPv6 的每条路径按一组字段显示。

以下为有实际静态路由时的查询输出节选：

```text
<VortexROS> display ip routing-table 198.19.0.0 16 longer-match protocol static limit 2
Routing Table : default
         Destinations : 2        Routes : 2        Configured Routes : 2

Static routing table status : <Active>
         Destinations : 2        Routes : 2

Destination/Mask   Proto   Pre  Cost    Flags   NextHop         Interface       VPN-Instance
 198.19.201.0/24   Static  90   0         DR   198.18.31.2      Ethernet1       default
 198.19.202.0/24   Static  76   0         DB   NULL0            NULL0           default
```

显示全部 VPN 时，输出分别标明路由所属 VPN 和下一跳所属 VPN，避免混淆跨表路径。
可继续限制详细输出的数量：

```text
display ipv6 routing-table all-vpn-instance protocol static verbose limit 2
display ip routing-table all-routes limit 3
display ipv6 routing-table all-routes limit 3
```

有效路径与未选中路径分别查询。`inactive` 必须跟协议选择使用，不能同时使用 `verbose`：

```text
display ip routing-table vpn-instance SHOW201 protocol static inactive limit 1
display ipv6 routing-table protocol static inactive limit 1
display ip routing-table vpn-instance SHOW201 statistics
display ipv6 routing-table vpn-instance SHOW201 route-number
```

下一跳不可解析时，详细信息中显示 `Invalid Adv`，协议查询的 Inactive 分区列出该路径。
已配置但无效的路径不会因此被当作有效转发项。统计、数量与详细查询均遵守所选 VPN、协议、
目的和显示上限；判断整张表的总量时不要同时添加较小的 `limit`。

FIB 查询支持 `vpn-instance NAME` 选择一张实际转发表；目的或文本筛选通过输出修饰符进行：

```text
display ip fib vpn-instance SHOW201
display ip fib | include 198.19.203
display ipv6 fib vpn-instance SHOW201
display ipv6 fib | begin 2001:db8:213
```

文本筛选按显示行工作，不是对目的地址进行最长匹配。`include` 后只看到某条 IPv6 字段时，
需要完整路径信息可使用 `begin`，或直接查询对应 VPN 的完整 FIB。
