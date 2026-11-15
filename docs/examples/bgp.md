# 直连 eBGP

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

对端使用本地 AS 64513，并指定对端地址 192.0.2.1 和 AS 64512。network 指定通告范围。接入生产上游前，用[路由策略](../operator/route-policy.md)限制可交换的前缀。

## 验证

用 display bgp peer 查看 Established，再用 display bgp routing-table 和对端路由表核对实际前缀。如果邻居已建立但没有路由，检查本地是否存在精确前缀以及导入和导出策略。

## 撤销

在 BGP 视图执行 undo peer 192.0.2.2 并提交，关闭会话并撤回经它交换的路由。只撤销一条通告时，在 IPv4 单播地址族撤销对应的 network。


## VPN 实例内的 IPv4/IPv6 静态引入

本节使用 [CLI-UNDER 拓扑](ospf.md#vpn-实例的静态引入)。P1/P2 接口地址为 198.18.180.1/.2 与 2001:db8:180::1/::2；P2 在该 VPN 发布 198.18.181.0/24、2001:db8:181::/64，具体响应地址位于 LoopBack80。此处是 VPN 内单播邻居，不需要 VPNv4/VPNv6 传输邻居。

P1：

```text
bgp 65000
 ipv4-family vpn-instance CLI-UNDER
  peer 198.18.180.2 as-number 65000
  peer 198.18.180.2 enable
  quit
 ipv6-family vpn-instance CLI-UNDER
  peer 2001:db8:180::2 as-number 65000
  peer 2001:db8:180::2 enable
  quit
 quit
commit
```

P2：

```text
bgp 65000
 ipv4-family vpn-instance CLI-UNDER
  peer 198.18.180.1 as-number 65000
  peer 198.18.180.1 enable
  import-route static
  quit
 ipv6-family vpn-instance CLI-UNDER
  peer 2001:db8:180::1 as-number 65000
  peer 2001:db8:180::1 enable
  import-route static
  quit
 quit
commit
```

本节不让 OSPF/OSPFv3 同时发布这些前缀，以免更优 Preference 改变选路。检查 BGP 时应确认选中来源及实际出口：

```text
display bgp vpnv4 vpn-instance CLI-UNDER peer
display bgp vpnv6 vpn-instance CLI-UNDER peer
display ip routing-table vpn-instance CLI-UNDER 198.18.181.2 verbose
display ipv6 routing-table vpn-instance CLI-UNDER 2001:db8:181::2 verbose
ping -vpn-instance CLI-UNDER -c 3 -a 198.18.180.1 198.18.181.2
ping ipv6 -vpn-instance CLI-UNDER -c 3 -a 2001:db8:180::1 2001:db8:181::2
```

邻居应 Established；选中的两族路由来源应为 BGP，下一跳为对端接口。iBGP 默认 Preference 为 254。IPv6 邻居可能同时启用 IPv4 地址族，路径条数不一定等于不同前缀数。

P2 在两个 VPN 地址族下分别 `undo import-route static` 后提交，P1 两次成功查询均为 Summary Count0。恢复引入后执行 `reset service bgp` 并确认 Y，控制层返回 Running configuration re-applied and verified；两族路由恢复，后续一包探测各1/1。该操作会重启整个 BGP 服务并影响既有邻居，应仅在允许的维护窗口使用。
