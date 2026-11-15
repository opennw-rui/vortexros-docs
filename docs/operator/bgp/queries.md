# 状态与撤销


```text
display bgp peer
display bgp peer 10.0.0.2 verbose
display bgp vpnv4 vpn-instance BLUE peer 10.0.0.2 verbose
display bgp vpnv4 vpn-instance BLUE peer 10.0.0.2 log-info
display bgp vpnv6 all peer verbose
display bgp routing-table
display bgp routing-table peer 10.0.0.2 received-routes
display bgp vpnv4 vpn-instance BLUE routing-table
display bgp vpnv4 vpn-instance BLUE routing-table statistics
display bgp tcp-protection verbose
```

动态路由的 `display` 输出由 VortexROS 统一排版，不透出 FRR 的原始标题、内部实例号或内存地址。BGP 全表、VPN 路由表、邻居收发路由及 AS Path 列表，OSPF/OSPFv3 路由与 LSDB，以及 IS-IS 路由与 LSDB，均直接读取对应协议 daemon 的 VTY 数据并逐项输出，首批记录不需要等待完整表进入内存；总数位于表尾。BGP 路由表的 `Path/Ogn` 与 AS Path 列表统一使用十进制 AS 号。`routing-table statistics` 显示后端统计的前缀、通告和重分发数量。BGP 邻居明细和 `log-info` 从对应地址族的 FRR 会话查询逐个解码邻居，`all` 查询按 VPN 实例标出结果。`log-info` 显示当前会话状态、可用的建立时间及 FRR 保留的最近重置和 Notification 原因。邻居摘要、接口和其他有界状态读取一次后端快照并按固定字段排版。

默认TCP保护只接受已经配置的BGP邻居源地址。需要关闭时：

```text
bgp 64512
 undo default tcp-protected
```

精确删除邻居或单项参数：

```text
bgp 64512
 undo peer 10.0.0.2 route-policy RP-IN import
 undo peer 10.0.0.2 description
 undo peer 10.0.0.2
undo bgp 64512
commit
```
