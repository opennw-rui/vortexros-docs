# 路由引入

协议引入可附带策略、metric和外部类型，参数顺序可交换：

```text
ospf 1
 import-route static route-policy REDIST cost 20 type 1
```


需要先按[完整双端案例](../../examples/ospf.md)建立邻接，在对应进程/area视图配置，提交后比较 LSDB、路由与业务；参数撤销后再次查询并保存。不能仅以 FRR 接受配置宣称对端已学到路由。

[OSPF 总览](../ospf.md) · [完整案例](../../examples/ospf.md) · [命令参数](../reference/ospf.md)

## 默认路由

进程视图的命令有两种行为：

```text
ospf 1
 default-route-advertise
#
```

只在本路由实例具有默认路由时发布。若没有默认路由，命令存在也不代表对端一定收到 `0.0.0.0/0`。`default-route-advertise always` 则不要求本地已有默认路由；使用时应确保该设备确实能转发相关业务，不能只验证发布成功。

实际双端验证中，发布端使用 `always` 后，接收端出现 OSPF 外部默认路由，优先级 150，探测发布端业务地址 3 发 3 收。改为不带 `always` 且本地没有默认路由后，默认 LSA 和接收端默认路由消失；在发布端加入真实默认路由后重新发布，撤销该默认路由后停止发布。测试中分别观察到 E2 开销 1 和 10，应以实际 LSDB/路由查询为准，不能把优先级当成开销。

例如以下丢弃默认仅用于明确丢弃不匹配更具体路由的流量，不是通向上游的可用出口：

```text
ip route-static 0.0.0.0 0 NULL 0
commit
```

只有更具体、可达的业务路由仍能正常转发。真实网络应按实际出口配置默认下一跳，并验证出向和回程。

```text
display ospf lsdb ase
display ospf routing
display ip routing-table 0.0.0.0
```

在 VPN 进程中，对应使用 `display ospf vpn-instance 名称 ...` 和该 VPN 的路由查询。

撤销默认发布：

```text
ospf 1
 undo default-route-advertise
#
```

提交后确认默认 LSA 和对端由本进程学习的默认路由消失；不应删除对端其他来源的有效默认路径。若使用了上面的测试丢弃路由，也用 `undo ip route-static 0.0.0.0 0 NULL 0` 撤销。
