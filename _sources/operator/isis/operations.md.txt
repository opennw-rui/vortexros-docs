# 查询、撤销与迁移

```text
display isis 10 brief
display isis 10 peer
display isis 10 interface
display isis 10 lsdb
display isis 10 route
display isis 10 spf-delay
```

撤销示例：

```text
interface Vlanif 100
 undo isis ipv6-enable 10
 undo isis enable
#
undo isis 10
```

CLI 操作：

```text
commit
```

如果需要把进程迁移到另一个VPN，应先删除进程，再使用新VPN重新创建。当前配套FRR 对 Level-1、Level-2 均使用缺省路由优先级 15。这对应路由表的 `Pre`，不是协议内部的 Level 选路顺序。切换 Level 会重新建立对应级别的链路状态并计算路由；应同时检查邻居、LSDB、路由表和连通性，不能仅以邻居 Up 判断恢复。

[双端配置和路由查询](../../examples/isis.md) · [全部参数](../reference/isis.md)


## 双栈撤销与过载位

IPv4 与 IPv6 的接口绑定可以分别撤销。一次双端配置中，两族前缀均显示 ISIS、Preference 15、Cost 20；仅重新启用 IPv4 时，IPv4 路由恢复，IPv6 前缀仍无路由，随后启用 IPv6 才恢复该族。删除专用环回接口后，两族对应前缀均撤销。

set-overload-bit 设置本机 LSP 的过载位；对端 LSDB 的 ATT/P/OL 从 0/0/0 变为 0/0/1，undo set-overload-bit 后恢复。过载位主要影响其他设备是否将本机作为中转，不能据仍可访问本机所连网段判断它无效。


## DIS 和邻居优先级

`display isis 进程号 interface` 的 DIS 列显示本机当选 DIS 的级别：`L1`、`L2` 或 `L1/L2`；LAN 上未当选时显示 `No`，点到点链路没有 DIS 选举，显示 `--`。`display isis 进程号 peer` 的 PRI 列显示对端通告的 LAN 优先级，点到点邻居显示 `-`。

例如，两端的 LAN 优先级分别设置为 127 与 1，在 Level-1 邻接 Up 后，优先级 127 的设备显示 DIS `L1`，其邻居 PRI 为 `1`；另一端显示 DIS `No`，其邻居 PRI 为 `127`。路由表仍使用 IS-IS 缺省 Preference 15；DIS 优先级不会变成 IP 路由优先级。

## 重启 IS-IS 服务

需要重启协议服务时，在用户视图执行：

```text
reset service isis
```

确认提示输入 `Y` 后，设备重启 IS-IS 进程，按当前 Running 重新下发并回读配置。该操作会短暂中断 IS-IS 邻接与相关路由，不会保存尚未保存的配置，也不会重启其他路由协议或数据面。恢复后检查邻居、目标路由和实际业务：

```text
display health
display isis 1 peer
display ip routing-table 198.18.246.3
ping -a 198.19.23.2 -c 1 198.18.246.3
```

一次正常恢复结果为邻居 Up、目标路由 ISIS/Preference 15/Cost 20，探测 1/1；健康状态为 ready。仅收到“服务已重启”消息不足以证明远端路由和流量已经恢复。


## TE 运行状态查询

```text
display isis 2 traffic-eng router
display isis 2 traffic-eng interface
display isis 2 traffic-eng database
```

查询按所选 IS-IS 进程显示数据，也可以使用 `vpn-instance` 选择实例。接口查询只显示该进程对应的接口参数，不混入其他 VPN 实例。实际有数据的查询可显示 `MPLS-TE IPv4 Router-Address : 1.1.1.1`、`Traffic Engineering Metric : 123`，数据库汇总为 `2 Vertices, 2 Edges, 6 Subnets`；另一个 VPN 内的接口参数可独立显示 Metric `234`。

这些命令读取已有 TE 状态，不启用 TE、Segment Routing 或 MPLS 转发，也不创建隧道。当前版本未提供 IS-IS TE 发布配置入口。未启用时没有 TE 参数或显示禁用状态，不应据此判断普通 IS-IS 邻接和路由故障；普通路由仍通过 `peer`、`lsdb` 和 `route` 查询。
