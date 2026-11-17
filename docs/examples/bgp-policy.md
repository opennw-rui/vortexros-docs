# BGP IPv4 策略

## 目标与拓扑

P2发布环回地址，P1只接收指定前缀，并修改本地选路属性。所有网络设备都使用VortexROS；以下接口编号可按设备替换。

```text
P1 Ethernet0 ---------------- Ethernet0 P2
198.19.80.1/30                198.19.80.2/30
AS 65000                     AS 65000
                             LoopBack253: 10.253.29.2/32
```

此例使用私有地址和AS号。策略只挂载到示例邻居的IPv4入方向，不应直接用于正在承载其他前缀的生产邻居。未匹配的路由隐式拒绝。

## P2配置

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ip address 198.19.80.2 30
#
interface LoopBack 253
 ip address 10.253.29.2 32
#
bgp 65000
 router-id 2.2.2.2
 peer 198.19.80.1 as-number 65000
 ipv4-family unicast
  peer 198.19.80.1 enable
  network 10.253.29.2 32
#
```

CLI 操作：

```text
commit
```

`network`要求该精确前缀已经存在于本机路由表。本例由LoopBack253提供直连路由。

## P1配置

先建立继续节点，再引用它。两个节点都匹配同一前缀列表，避免未命中第10节点的路由落入无条件许可的第20节点。

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ip address 198.19.80.1 30
#
ip ip-prefix D1-BGP4 index 10 permit 10.253.29.2 32
route-policy D1-BGP4 permit node 20
 if-match ip-prefix D1-BGP4
 apply tag 253
#
route-policy D1-BGP4 permit node 10
 if-match ip-prefix D1-BGP4
 apply cost 37
 apply local-preference 220
 apply origin egp
 apply ip-address next-hop 198.19.80.2
 apply as-path 65123 65124
 apply community 65000:253 additive
 apply large-community 65000:1:253 additive
 continue node 20
#
bgp 65000
 router-id 1.1.1.1
 peer 198.19.80.2 as-number 65000
 ipv4-family unicast
  peer 198.19.80.2 enable
  peer 198.19.80.2 route-policy D1-BGP4 import
#
```

CLI 操作：

```text
commit
```

## 参数与影响

| 配置 | 作用与影响 |
|---|---|
| 前缀列表的32 | 只匹配该主机路由；不是匹配整个10/8 |
| local-preference 220 | 高于普通接收路径的100，参与本AS内选路 |
| cost 37 | 此BGP消费者中设置MED，不改变接口开销 |
| origin egp | 将Origin改为EGP，表中显示e |
| AS_PATH 65123 65124 | 在接收路径前添加AS序列；错误添加本AS可能触发环路检查 |
| next-hop | 保持为可达的P2；设置成不可达地址会使路径不能用于转发 |
| community / large-community | 给本地路径增加属性；向其他邻居传播还受该邻居的通告设置约束 |
| continue node 20 | 命中第10节点后继续执行第20节点，最终增加Tag253 |

不能只增加一个末尾无条件permit节点来“完成continue”：那也会接受未匹配前置节点的路由。

## 实际验证

```text
display bgp peer
display bgp routing-table 10.253.29.2
display route-policy D1-BGP4
display route-policy D1-BGP4 verbose
display ip ip-prefix D1-BGP4 verbose
display ip ip-prefix D1-BGP4 first-match 10.253.29.2/32
display ip routing-table 10.253.29.2
ping -c 3 10.253.29.2
```

示例输出节选：

```text
     Network            NextHop             MED     LocPrf Path/Ogn
 *>  10.253.29.2/32     198.19.80.2          37        220 65123 65124 e

Total Number of Routes: 1
```

策略明细中的第10、20节点实际均被调用；前缀列表命中计数为2。路径回读同时确认Tag253、Community65000:253及Large Community65000:1:253。实际探测为3发3收。

这是属性与连通性结果，不是吞吐性能保证。BGP的协议优先级仍为254；Local Preference与协议优先级含义不同。

## 拒绝和恢复

把匹配项改为deny并提交：

```text
ip ip-prefix D1-BGP4 index 10 deny 10.253.29.2 32
commit
display bgp routing-table
```

受测邻居没有其他允许路径时，该前缀退出BGP表，实测显示`Total Number of Routes: 0`。如果另一个邻居仍在发布，路由可以正常保留，应按邻居和路径核对，不能把其他路径误认为过滤失效。

恢复permit：

```text
ip ip-prefix D1-BGP4 index 10 permit 10.253.29.2 32
commit
```

实测原MED37、Local Preference220、AS_PATH及Origin恢复。

## 撤销

只撤销属性时，在对应策略节点使用`undo apply ...`及`undo continue`并提交。实测撤销这些动作后，路由仍被允许，恢复MED0、Local Preference100、空AS_PATH和Origin IGP。

完全撤销策略时先解除消费者引用：

```text
bgp 65000
 ipv4-family unicast
  undo peer 198.19.80.2 route-policy D1-BGP4 import
#
undo route-policy D1-BGP4 permit node 10
undo route-policy D1-BGP4 permit node 20
undo ip ip-prefix D1-BGP4
```

CLI 操作：

```text
commit
display route-policy
display ip ip-prefix
```

实测对象从配置和后端均移除，原BGP邻居及network路由保留。仍被引用时直接删除前缀列表会被Candidate拒绝，不会破坏已提交配置。

业务无需继续时，在P2的IPv4地址族撤销`network 10.253.29.2 32`，再移除专用环回接口。验证后按需执行`save`。

[IPv6策略案例](bgp-ipv6-policy.md) · [策略匹配](../operator/route-policy/matching.md) · [命令参数](../operator/reference/route-policy.md)
