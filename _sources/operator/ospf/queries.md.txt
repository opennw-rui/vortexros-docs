# 邻居、LSDB 与路由


```text
display ospf 1 brief
display ospf 1 peer brief
display ospf 1 peer 10.0.0.2
display ospf 1 interface
display ospf 1 lsdb
display ospf 1 lsdb router
display ospf 1 lsdb router 10.0.0.1
display ospf 1 lsdb ase 192.0.2.0
display ospf vpn-instance BLUE lsdb
display ospf vpn-instance BLUE lsdb ase 192.0.2.0
display ospf 1 lsdb originate-router 10.0.0.2
display ospf 1 lsdb router self-originate
display ospf 1 lsdb age min-value 300 max-value 1800
display ospf 1 lsdb | include Router
display ospf 1 routing
reset ospf 1 process
```

无类型的`display ospf 1 lsdb`按Area显示Router、Network、Summary和ASBR Summary等LSA摘要，并将AS External和Opaque数据库分段显示。摘要的`Len`为LSA实际长度，具有单一度量值的LSA在`Metric`列显示实际值。Router和Network等无单一度量值的LSA显示`-`。AS External明细的`E type`显示1或2。指定`router`、`network`、`summary`、`asbr`、`ase`、`nssa`或`opaque-*`后逐条显示该类LSA的详细字段；类型后可继续指定Link State ID。`originate-router`按Advertising Router过滤，`self-originate`只显示本机产生的LSA，`age`按0至3600秒的LSA年龄范围过滤。显示管道继续支持`include`、`exclude`、`begin`和`section`，过滤后的表格保留所属标题和表头。

修改或撤销 Router-ID 后，活动进程需要 reset 才能切换。未显式配置时，同一 VPN 内优先选择数值最大的 LoopBack IPv4；没有时，从其他已配置或受管运行 IPv4 地址中选择。投入运行后，不会因地址 Down、被删除、DHCP 续租或出现更大地址而自动重启协议。需要切换时执行 reset ospf ... process，等待目标邻居及路由恢复。当前多个 OSPFv2 进程并存时不支持单进程清理，会明确拒绝；不要改用重启全部 FRR 来代替无影响查询。

`display ospf peer brief`按以下顺序显示，Interface位于Neighbor id左侧：

```text
Area Id    Pri  Up Time   Dead Time  Interface   Neighbor id  State
0.0.0.0      1  00:12:31  00:00:38   Vlanif12    10.0.0.2     Full
```

修改与删除示例：

```text
interface Vlanif 12
 undo ospf dr-priority
 undo ospf network-type
 undo ospf enable 1
undo ospf 1
commit
```

撤销接口激活只影响该接口；删除进程会撤销该进程的全部邻居和路由。


## 报文计数

查看 OSPF 接口报文计数可用 `display ospf <进程号> interface traffic [接口]`。


[OSPF 总览](../ospf.md) · [完整案例](../../examples/ospf.md) · [命令参数](../reference/ospf.md)
