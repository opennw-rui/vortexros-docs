# Stub、NSSA 与汇总


区域类型和汇总在area视图配置：

```text
ospf 1
 area 0.0.0.1
  nssa no-summary
  abr-summary 10.0.0.0 255.0.0.0 not-advertise
```

`stub`与`nssa`互斥；已经配置一种类型时，必须先执行对应的`undo`，不能用另一条命令隐式覆盖。`no-summary`阻止向该区域发布三类汇总路由，`not-advertise`阻止发布指定区域汇总。撤销命令为`undo stub`、`undo nssa`和`undo abr-summary ADDRESS MASK`。

在普通区域、Stub 和 NSSA 之间切换会重新建立该区域的邻接并同步链路状态数据库。两端的区域类型必须一致；切换期间可能撤销从该区域学到的路由，收敛时间受网络类型和 OSPF 计时器影响。其他区域的接口不随之重新建立邻接。

仅增加或移除 `no-summary` 不改变区域类型，也不重新建立邻接。在 ABR 上使用 `stub no-summary` 隐藏区域间明细汇总、保留默认路由；改为 `stub` 后恢复这些汇总。NSSA 的 `nssa no-summary` 与 `nssa` 具有相同的区域间汇总控制效果，区内合法的七类外部路由不因 `no-summary` 被隐藏。修改后用 `display ospf vpn-instance NAME peer` 确认邻接状态，再用 `display ospf vpn-instance NAME routing` 与 `display ospf vpn-instance NAME lsdb` 确认所需前缀。


需要先按[完整双端案例](../../examples/ospf.md)建立邻接，在对应进程/area视图配置，提交后比较 LSDB、路由与业务；参数撤销后再次查询并保存。提交后仍需确认对端已学到预期路由，且业务按该路由转发。

[OSPF 总览](../ospf.md) · [完整案例](../../examples/ospf.md) · [命令参数](../reference/ospf.md)

## 区域归属与双栈汇总

同一 OSPF 进程的一条 network 只能属于一个区域。迁移时在原区域撤销该条，再在目标区域添加，统一 commit；不同前缀长度的重叠网络不属于这条重复限制。进程已使用 network 激活时，不要混用接口下的 ospf enable 激活。

已有骨干邻接的边界路由器，将客户 LoopBack 归入区域 0.0.0.1 后，可以汇总 IPv4 和 IPv6：

```text
ospf 1
 area 0.0.0.1
  network 172.29.251.2 0.0.0.0
  abr-summary 172.29.251.0 255.255.255.0
#
ospfv3 1
 area 0.0.0.1
  abr-summary 2001:db8:251:: 64
#
interface LoopBack 251
 ospfv3 1 area 0.0.0.1
#
commit
```

本例 LoopBack 的地址为 172.29.251.2/32 和 2001:db8:251::2/128，IPv6 已启用，骨干邻接按各协议的双端案例建立。IPv4 原有 network 若位于其他区域，必须先撤销。不要在同一次示例中保留到这些地址的其他协议精确路由，否则更具体的路由会优先于汇总，ping 成功不足以确认使用了汇总。

对端实际结果：

| 路由 | 协议 | 优先级 | 开销 | FIB | 业务 |
|---|---|---:|---:|---|---|
| 172.29.251.0/24 | OSPF | 10 | 20 | D | 172.29.251.2，2/2 |
| 2001:db8:251::/64 | OSPFv3 | 10 | 11 | D | 2001:db8:251::2，2/2 |

在对应 abr-summary 后增加 not-advertise 并提交，两族汇总均从对端路由表撤销。撤销过程中 LSDB 可能短暂保留 Age 3600 的冲洗条目；应检查路由/FIB，不能把冲洗条目当作仍在使用的路由。

撤销汇总分别使用 undo abr-summary 172.29.251.0 255.255.255.0 和 undo abr-summary 2001:db8:251:: 64，再提交；对端恢复更具体的 /32、/128 前缀。完全撤销 OSPFv3 接口绑定需带区域：undo ospfv3 1 area 0.0.0.1。只输入 undo ospfv3 1 不完整。

[跨区域外部路由案例](../../examples/ospf-multiarea.md)给出三台设备的完整配置、四类与五类 LSA 的区别、实际路由和双跳流量，以及撤销顺序。
