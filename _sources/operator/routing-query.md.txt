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
