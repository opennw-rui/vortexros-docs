# 路由组

**目标**：让两个目的前缀共用一个网关，后续增删成员时无需重复写下一跳。

**前提**：示例设备能直接到达 192.0.2.1，且目标前缀没有与本例冲突的同路径配置。

## 配置

~~~text
system-view
route-static group name LAB
 route 198.51.100.0/25
 route 203.0.113.0/25
 quit
ip route-static-group LAB 192.0.2.1 preference 60
commit
~~~

组定义管理成员；绑定决定下一跳。未绑定的组不会单独安装路由。参见[静态路由组](../operator/route-groups.md)。

## 验证

用 `display route-static group name LAB verbose` 检查成员，用 `display ip routing-table-group name LAB verbose` 检查应用结果。再查询目标前缀和下一跳，并从示例网发起探测。

## 撤销

先用 `undo ip route-static-group LAB 192.0.2.1` 去掉该绑定，再用 `undo route-static group name LAB` 删除已无引用的组，最后提交。确认仅该组路径被撤销。

## 双栈外部列表与撤销

两台 VortexROS 的 Ethernet0 直连，分别配置 198.19.80.1/30、.2/30 与 2001:db8:80::1/64、::2/64。P2 LoopBack199 配置 198.18.199.2/32、2001:db8:199::2/128。外部列表由独立的列表发布服务提供，分别包含这两个前缀；发布服务是数据来源，不是路由设备或本机手工启动的网络服务。

```text
route-static group name CLI-FINAL4
 source url https://lists.example.net/routes/v4.txt
 auto-refresh interval 5
 auto-refresh enable
 quit
ipv6 route-static group name CLI-FINAL6
 source url https://lists.example.net/routes/v6.txt
 auto-refresh interval 5
 auto-refresh enable
 quit
ip route-static-group CLI-FINAL4 198.19.80.2
ipv6 route-static-group CLI-FINAL6 2001:db8:80::2
commit
```

将 URL 替换为实际可访问的列表地址，证书应有效。下载完成后，两组 verbose 应各有一个 external 成员，刷新周期为 5 分钟，应用状态为 applied；检查两族路由和到 LoopBack199 的探测。

将来源改为手工维护时，在各组中撤销自动刷新和 URL，再加入同一前缀并提交：

```text
route-static group name CLI-FINAL4
 undo auto-refresh enable
 undo auto-refresh interval
 undo source url
 route 198.18.199.2/32
 quit
commit
```

IPv6 使用对应 IPv6 组及前缀。实际两组均变为 `manual 1 external 0 effective 1`，来源 URL 和刷新计划不再显示。之后 `undo route` 删除最后一个成员，提交后 IPv4/IPv6 的精确路由查询都成功返回0条。最后撤销两条绑定并删除两组，成功的两族组清单均为空。删除单个成员、删除绑定和删除组是不同操作，不能用一次查询错误代替这些结果。
