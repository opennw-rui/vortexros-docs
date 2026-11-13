# OSPF

在 IPv4 路由域内建立链路状态邻接并交换前缀。

[命令参考](reference/ospf.md) · [配置案例](../examples/ospf.md)

## 配置

### 使用area下的network激活

```text
ospf 1 router-id 10.0.0.1
 opaque-capability enable
 area 0.0.0.0
  network 10.0.12.1 0.0.0.0 description P1-P2
```

`network`只能在area视图中输入。提交后，地址匹配的接口开始发送Hello报文；只有两端area、网络类型、认证和计时等条件兼容时才会建立邻居。

### 使用接口命令激活

```text
ospf 1 router-id 10.0.0.1
interface Vlanif 12
 ospf enable 1 area 0.0.0.0
 ospf network-type p2p
 ospf cost 10
 ospf dr-priority 100
 ospf timer hello 3
 ospf timer dead 12
 ospf timer retransmit 4
 ospf timer transmit-delay 2
```

同一进程只能选择 `network` 或接口 `ospf enable` 一种激活方式；混用会在命令进入待提交配置前报错。广播网络上的DR优先级范围为0至255，0表示不参与DR/BDR选举。

协议引入可附带策略、metric和外部类型，参数顺序可交换：

```text
ospf 1
 import-route static route-policy REDIST cost 20 type 1
```

### Stub、NSSA与区域汇总

区域类型和汇总在area视图配置：

```text
ospf 1
 area 0.0.0.1
  nssa no-summary
  abr-summary 10.0.0.0 255.0.0.0 not-advertise
```

`stub`与`nssa`互斥；已经配置一种类型时，必须先执行对应的`undo`，不能用另一条命令隐式覆盖。`no-summary`阻止向该区域发布三类汇总路由，`not-advertise`阻止发布指定区域汇总。撤销命令为`undo stub`、`undo nssa`和`undo abr-summary ADDRESS MASK`。

### 验证与撤销

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

修改或撤销已有进程Router-ID时，配置可以先被接受，但FRR活动Router-ID需要进程reset才能切换。未显式配置时，控制层依据设备配置中的真实接口类型，在同一VPN实例中优先选择数值最大的LoopBack IPv4地址；不存在LoopBack IPv4时，才从该VPN的静态IPv4和受管Linux/LCP接口上的DHCP等可信运行IPv4中选择最大值，并把这个有效值投射给FRR。DHCP运行地址不会写回静态CFG；Linux/LCP侧接口类型也不会改变LoopBack优先的产品语义。Router-ID投入运行后不会仅因原地址Down、被删除、DHCP续租或出现更大地址而自动重启进程；需要切换时执行`reset ospf ... process`。reset会在允许重选的边界更新受管Router-ID、清理目标进程，再读取活动Router-ID及完整FRR权威状态，不会重启整个FRR。由于当前FRR后端不能保证多OSPFv2实例的单实例清理，配置多个OSPFv2进程时该操作会明确拒绝；单OSPFv2进程和OSPFv3使用受支持的目标范围。

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
