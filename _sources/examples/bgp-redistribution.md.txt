# 静态路由引入BGP

## 目标与拓扑

P2把一条带Tag的静态路由分别引入BGP和OSPF，验证两个消费者的Cost互不覆盖。

```text
P1 Ethernet0 ---------------- Ethernet0 P2
198.19.80.1/30                198.19.80.2/30
BGP AS65000 / OSPF1           BGP AS65000 / OSPF1
                             172.29.200.0/24 -> NULL0
```

NULL0用于明确丢弃目标前缀，不代表可用业务主机。本例检查路由发布、属性和选路，不应对该前缀宣称业务连通。

## P1配置

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ip address 198.19.80.1 30
#
ospf 1 router-id 1.1.1.1
 area 0.0.0.0
  network 198.19.80.1 0.0.0.0
#
bgp 65000
 router-id 1.1.1.1
 peer 198.19.80.2 as-number 65000
 ipv4-family unicast
  peer 198.19.80.2 enable
#
```

CLI 操作：

```text
commit
```

## P2配置

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ip address 198.19.80.2 30
#
ip route-static 172.29.200.0 24 NULL 0 tag 55
route-policy D1-REDIST permit node 10
 if-match protocol static
 if-match tag 55
 if-match cost 0
 apply cost 64
#
ospf 1 router-id 2.2.2.2
 import-route static cost 37 type 2
 area 0.0.0.0
  network 198.19.80.2 0.0.0.0
#
bgp 65000
 router-id 2.2.2.2
 peer 198.19.80.1 as-number 65000
 ipv4-family unicast
  peer 198.19.80.1 enable
  import-route static route-policy D1-REDIST
#
```

CLI 操作：

```text
commit
```

三个if-match条件共同约束来源：static、Tag55、原Cost0。BGP策略设置MED64；OSPF消费者单独设置E2 Cost37。不要将带`if-match protocol`的策略直接用于当前不支持此条件的OSPF引入入口；设备会在提交前拒绝。

## 实际验证

P2：

```text
display route-policy D1-REDIST verbose
display bgp routing-table
display ip routing-table 172.29.200.1
```

实测策略节点被调用，条件包含source-protocol static、tag55及metric0；BGP本地表中该前缀的MED为64，静态路由仍是Pre60、Cost0、NULL0。

P1：

```text
display bgp routing-table
display ospf 1 lsdb ase 172.29.200.0
display ip routing-table 172.29.200.1
```

示例BGP表项：

```text
Network            NextHop             MED     LocPrf Path/Ogn
172.29.200.0/24    198.19.80.2          64        100 ?
```

同一前缀的OSPF明细：

```text
Type      : External
Ls id     : 172.29.200.0
Adv rtr   : 2.2.2.2
Len       : 36
Net mask  : 255.255.255.0
TOS 0  Metric: 37
E type    : 2
Tag       : 55
```

OSPF外部优先级150优于BGP254，所以路由表选中OSPF，而BGP表仍可以存在有效路径。这不是BGP策略失效，协议优先级与MED不是同一个比较层次。

## 修改与撤销

在BGP策略节点撤销匹配条件和`apply cost`后，实测该BGP路由恢复MED0，静态路由本身不变。撤销所有匹配条件会扩大策略许可范围，生产配置应按需保留。

完全撤销BGP引入：

```text
bgp 65000
 ipv4-family unicast
  undo import-route static
#
undo route-policy D1-REDIST permit node 10
```

CLI 操作：

```text
commit
```

实测BGP表不再有该引入前缀，OSPF E2仍为Cost37。若仍需静态路由但不再需要Tag，可重配同一条静态路由而不附加tag：

```text
ip route-static 172.29.200.0 24 NULL 0
commit
display ospf 1 lsdb ase 172.29.200.0
```

实测OSPF中Tag恢复0。业务确实不再需要该静态前缀时，再撤销静态路由；确认其他OSPF静态引入需求后，才考虑`undo import-route static`。最后按需`save`。

[路由优先级](../operator/routing-preference.md) · [策略参数](../operator/reference/route-policy.md)
