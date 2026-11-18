# BGP IPv6 策略

## 目标与前提

在[IPv4策略案例](bgp-policy.md)的P1/P2直连链路上增加IPv6，两端AS均为65000。使用IPv6邻居接收IPv6路由，并通过前缀列表及Local Preference选择路径。

| 设备 | Ethernet0 | LoopBack253 |
|---|---|---|
| P1 | 2001:db8:80::1/64 | 无 |
| P2 | 2001:db8:80::2/64 | 2001:db8:253::2/128 |

接口先执行`ipv6 enable`。IPv4/IPv6前缀列表和策略条件分别配置，不能用IPv4列表筛选IPv6前缀。

## P2增量配置

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ipv6 enable
 ipv6 address 2001:db8:80::2 64
#
interface LoopBack 253
 ipv6 enable
 ipv6 address 2001:db8:253::2 128
#
bgp 65000
 peer 2001:db8:80::1 as-number 65000
 ipv6-family unicast
  peer 2001:db8:80::1 enable
  peer 198.19.80.1 enable
  network 2001:db8:253::2 128
#
```

CLI 操作：

```text
commit
```

## P1增量配置

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ipv6 enable
 ipv6 address 2001:db8:80::1 64
#
ip ipv6-prefix D1-BGP6 index 10 permit 2001:db8:253::2 128
route-policy D1-BGP6 permit node 10
 if-match ipv6 address prefix-list D1-BGP6
 apply local-preference 230
 apply cost 38
 apply ipv6 next-hop 2001:db8:80::2
#
bgp 65000
 peer 2001:db8:80::2 as-number 65000
 ipv6-family unicast
  peer 2001:db8:80::2 enable
  peer 2001:db8:80::2 route-policy D1-BGP6 import
  peer 198.19.80.2 enable
#
```

CLI 操作：

```text
commit
```

本例同时启用原IPv4传输邻居的IPv6地址族，作为独立路径对照。只有IPv6邻居挂载了策略，因此其Local Preference230高于另一条路径的100。不需要该对照时，可以不配置IPv4邻居的IPv6启用行。

IPv6邻居不会因此自动承载IPv4路由。IPv4邻居承载IPv6地址族的启用命令与IPv6邻居自身的属性配置是两个入口；当前不能在IPv6地址族用IPv4地址修改邻居的route-policy属性。

## 查询与实际结果

```text
display bgp ipv6 peer
display bgp ipv6 peer 2001:db8:80::2 verbose
display bgp ipv6 routing-table
display ip ipv6-prefix D1-BGP6 verbose
display ip ipv6-prefix D1-BGP6 first-match 2001:db8:253::2/128
display route-policy D1-BGP6 verbose
display ipv6 routing-table 2001:db8:253::2
ping ipv6 -c 3 2001:db8:253::2
```

示例路径节选：

```text
Network                    NextHop            MED   LocPrf
2001:db8:253::2/128         2001:db8:80::2      38    230
2001:db8:253::2/128         2001:db8:80::2       0    100
```

实测230路径胜出，策略及前缀列表有实际调用/命中记录，IPv6探测3发3收。路由表中的协议优先级为254，与Local Preference不同。实际转发可使用同一邻居的链路本地下一跳，这是IPv6下一跳解析结果，不表示配置的全局下一跳被忽略。

## 拒绝、撤销与保存

把IPv6前缀项改为deny并提交后，IPv6邻居接收该前缀的计数降为0；对照的IPv4传输路径仍保留，选中Local Preference100。恢复permit后，230路径重新胜出。

```text
ip ipv6-prefix D1-BGP6 index 10 deny 2001:db8:253::2 128
commit
display bgp ipv6 routing-table
ip ipv6-prefix D1-BGP6 index 10 permit 2001:db8:253::2 128
commit
```

完全撤销时先解除策略引用：

```text
bgp 65000
 ipv6-family unicast
  undo peer 2001:db8:80::2 route-policy D1-BGP6 import
#
undo route-policy D1-BGP6 permit node 10
undo ip ipv6-prefix D1-BGP6
```

CLI 操作：

```text
commit
```

实测策略及列表从配置和后端移除。只撤销apply动作时，两条路径恢复MED0、Local Preference100。需要停止业务发布时，在P2撤销IPv6的network；需要删除专用邻居时，在双方BGP视图执行`undo peer IPv6地址`并提交。仍需IPv6服务时保留接口地址。确认预期状态后执行`save`。
