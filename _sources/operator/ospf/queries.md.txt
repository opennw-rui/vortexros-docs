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
#
undo ospf 1
```

CLI 操作：

```text
commit
```

撤销接口激活只影响该接口；删除进程会撤销该进程的全部邻居和路由。


## 报文计数

查看 OSPF 接口报文计数可用 `display ospf <进程号> interface traffic [接口]`。


[OSPF 总览](../ospf.md) · [完整案例](../../examples/ospf.md) · [命令参数](../reference/ospf.md)

## E2 外部路由的摘要与明细

导入静态路由时配置 `import-route static cost 37 type 2` 后，接收端使用：

```text
display ospf lsdb
display ospf lsdb ase
display ospf lsdb ase 172.29.200.0
display ip routing-table 172.29.200.0 24
```

实际外部LSA的摘要为 Len36、Metric37；明细显示：

```text
Type      : External
Ls id     : 172.29.200.0
Adv rtr   : 2.2.2.2
Len       : 36
Net mask  : 255.255.255.0
TOS 0  Metric: 37
E type    : 2
```

路由表对应Preference150、Cost37。未显示Metric的Router/Network LSA摘要不能被解读为零开销；不同LSA的metric所在字段不同。按类型、Link State ID及实际路由交叉核对，而不只确认命令能返回表头。若缩写 `as` 同时匹配多个LSA类型，会报歧义；使用完整 `ase`。

## 按接口查看邻居

```text
display ospf 1 peer Ethernet 0 brief
display ospf 1 peer Ethernet 0
```

两种查询都只选择该接口上的邻居。实际摘要能显示区域、优先级、存活/超时时间、接口、Router ID 和 Full 状态；详细输出显示对端地址及剩余 Dead 时间。按 Router ID 查询时使用 display ospf 1 peer 2.2.2.2 brief，接口过滤和 Router ID 过滤的对象含义不同。

VPN 实例查询形式为 display ospf vpn-instance INT lsdb。一个本机 E2 前缀的实际摘要为 External 203.0.113.0，AdvRouter 10.0.0.5，Len 36，Metric 37；display ospf vpn-instance INT lsdb ase 203.0.113.0 的明细显示掩码255.255.255.0、E type 2、Metric37。Router LSA不具有单一全表Metric，摘要中的 - 不代表外部LSA的Metric缺失。

## 辅助查询与范围

```text
display ospf 1 abr-asbr
display ospf 1 asbr-summary
display ospf 1 graceful-restart helper
display ospf 1 mpls-te database
display ospf 1 mpls-te interface
```

`abr-asbr` 显示可达的区域边界或自治系统边界路由器及到达开销。实际区域边界条目可显示 Router ID、Area、Cost 和下一跳接口。`asbr-summary` 查询外部路由聚合状态，不等同于区域内配置的 `abr-summary`；未配置聚合时没有聚合前缀。

当前公开配置命令不提供 OSPF GR Helper 或 MPLS-TE 的启用配置；对应查询用于查看后端状态。`Helper Support: Disabled`、`MPLS-TE database is not enabled` 或接口 TE disabled 表示未启用，不代表已有 GR/TE 会话或隧道。`peer last-nbr-down` 当前后端不支持，会明确说明限制。

LSDB 类型也可用数字1至5表示，依次为 Router、Network、Summary、ASBR Summary、AS External。例如 `display ospf 1 lsdb 5` 与 `display ospf 1 lsdb ase` 查询同类外部 LSA。`detail` 展开各类 LSA；不具备某类 LSA 的区域会显示零条，不应将零条解读为查询失败。

## 进程重置与服务重启

`reset ospf 1 process` 重新建立目标进程的邻接，不修改 Running 配置，也不重启守护进程。重建期间邻居、LSDB 和路由依次恢复；邻居刚显示 Full 时，SPF 和转发表仍可能尚未完成，不保证瞬时无损。实际单进程重置后，邻居恢复 Full，远端主机路由恢复为 OSPF Preference10、Cost20，指定源地址探测2/2。

`reset service ospf` 重启 OSPFv2 和 OSPFv3 服务，随后从 Running 回放并回读确认。此操作会中断两个地址族的 OSPF 邻接；VPP 及 BGP、RIP、IS-IS 等其他协议服务保持运行。实际 VPN 实例内的邻居、路由及指定源地址探测2/2 均恢复。操作前应确认业务可以承受协议收敛时间。

指定的进程不存在，或当前多个 OSPFv2 进程无法隔离重置时，命令会在后端变更前返回错误；此类请求拒绝不会修改 Running 或中断其他正常协议。

## 自动 Router ID 的显示

进程未配置显式 Router ID 时，查询仍显示实际运行的标识，不要求在配置中补写默认值。以下同一进程的查询头部均显示实际 Router ID 203.0.113.104：

~~~text
display ospf 101 peer
display ospf 101 interface Ethernet0
display ospf 101 lsdb router 203.0.113.104
display ospf 101 routing
~~~

本例邻居为 Full，接口为 DR、Cost10；自身 Router LSA 的 Ls id 与 Adv rtr 均为203.0.113.104、长度36。协议路由表包含203.0.113.102/32，开销20。Router ID 是协议标识，不能据此代替业务地址连通性检查；修改和自动恢复的方法见 [进程重置](reset.md)。


## Opaque LSA 和 TE 状态

启用 Opaque 能力后，可以接收对端的扩展 LSA。三种作用域分别查询：

```text
display ospf 1 lsdb opaque-link
display ospf 1 lsdb opaque-area originate-router 2.2.2.2
display ospf 1 lsdb opaque-as
```

Type 9 仅在同一链路传播，Type 10 在区域内传播，Type 11 在自治系统内传播。接收到 Router Information LSA 的实际显示如下：

```text
Type      : Opq-Area
Ls id     : 4.0.0.0
Adv rtr   : 2.2.2.2
Len       : 28
```

AS 作用域的同类记录显示 `Type : Opq-AS`。`4.0.0.0` 是 Opaque 类型与实例组成的标识，不是业务目的地址；应结合通告路由器和作用域判断来源。对端撤销后记录可能先以 MaxAge 3600 显示，随后移除；不能把该过渡状态当作仍然有效的通告。

以下查询只读取已有的 TE 状态，不会启用 MPLS-TE，也不会建立隧道：

```text
display ospf 1 mpls-te router
display ospf 1 mpls-te interface
display ospf 1 mpls-te database
```

有数据时，实际查询可显示 Router-Address `1.1.1.1`、接口 TE Metric `123`，以及 TED 的 `Vertices Count : 5`、`Edges Count : 2`。这与未启用时的状态提示不同，但不表示已经建立 TE 转发路径。本版本不提供 MPLS-TE 发布配置命令；查询仅限默认 VPN 实例。


链路作用域的私用 Opaque LSA 也按其实际字段显示，例如已接收记录为 `Type : Opq-Link`、`Ls id : 255.0.0.41`、`Len : 24`。私用类型的具体载荷含义由通告方定义，不能把收到该类 LSA 解释为设备启用了某个 GR、TE 或 SR 功能。撤销记录先显示 `Ls age : 3600`，确认传播结束后查询恢复零条。
