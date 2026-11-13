# BGP 入站策略

**目标**：只接受实验邻居发布的指定前缀，给匹配路由设置本地优先级。

**前提**：按[直连 eBGP](bgp.md)建立邻接，本端 AS 64512，对端 192.0.2.2。只在实验邻居上应用；既有不匹配路由可能撤销。

## 配置

~~~text
system-view
ip ip-prefix LAB-IN index 10 permit 203.0.113.0 24
route-policy LAB-IN permit node 10
 if-match ip-prefix LAB-IN
 apply local-preference 200
 quit
bgp 64512
 ipv4-family unicast
  peer 192.0.2.2 route-policy LAB-IN import
  quit
 quit
commit
~~~

前缀列表匹配精确 /24；路由策略只许可命中节点的前缀。Local Preference 参与本 AS 选路，不改变外部邻居的 AS。参见[路由策略](../operator/route-policy.md)。

## 验证

让对端分别发布 203.0.113.0/24 与一个不匹配的实验前缀。用 `display route-policy LAB-IN verbose` 查看调用，再查看 `display bgp routing-table` 的前缀和属性，确认只接受预期路由。

## 撤销

在同一 BGP 地址族撤销 `undo peer 192.0.2.2 route-policy LAB-IN import`，再回系统视图撤销策略节点及前缀列表并提交。撤销入站过滤可能重新允许对端前缀，提交前先核对影响。
