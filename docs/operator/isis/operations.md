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
undo isis 10
commit
```

如果需要把进程迁移到另一个VPN，应先删除进程，再使用新VPN重新创建。当前配套FRR 对 Level-1、Level-2 均使用缺省路由优先级 15。这对应路由表的 `Pre`，不是协议内部的 Level 选路顺序。切换 Level 会重新建立对应级别的链路状态并计算路由；应同时检查邻居、LSDB、路由表和连通性，不能仅以邻居 Up 判断恢复。

[双端配置和真实路由](../../examples/isis.md) · [全部参数](../reference/isis.md)
