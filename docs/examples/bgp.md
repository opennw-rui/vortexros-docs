# 连接直连 eBGP 邻居

**用途**。在不同 AS 之间交换 IPv4 前缀。这里使用 AS 64512 和 64513。

**前提**。本端 192.0.2.1/30 与对端 192.0.2.2/30 直连互通。要发布的 203.0.113.0/24 必须已在本端路由表中精确存在。

## 配置

~~~text
system-view
bgp 64512
 router-id 192.0.2.1
 peer 192.0.2.2 as-number 64513
 ipv4-family unicast
  network 203.0.113.0 255.255.255.0
  quit
 quit
commit
~~~

对端使用本地 AS 64513，并指定对端地址 192.0.2.1 和 AS 64512。network 指定通告范围。接入生产上游前，用[路由策略](../operator/05-dynamic-routing.md)限制可交换的前缀。

## 验证

用 display bgp peer 查看 Established，再用 display bgp routing-table 和对端路由表核对实际前缀。如果邻居已建立但没有路由，检查本地是否存在精确前缀以及导入和导出策略。

## 撤销

在 BGP 视图执行 undo peer 192.0.2.2 并提交，关闭会话并撤回经它交换的路由。只撤销一条通告时，在 IPv4 单播地址族撤销对应的 network。
