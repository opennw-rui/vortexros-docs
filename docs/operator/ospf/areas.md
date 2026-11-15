# Stub、NSSA 与汇总


区域类型和汇总在area视图配置：

```text
ospf 1
 area 0.0.0.1
  nssa no-summary
  abr-summary 10.0.0.0 255.0.0.0 not-advertise
```

`stub`与`nssa`互斥；已经配置一种类型时，必须先执行对应的`undo`，不能用另一条命令隐式覆盖。`no-summary`阻止向该区域发布三类汇总路由，`not-advertise`阻止发布指定区域汇总。撤销命令为`undo stub`、`undo nssa`和`undo abr-summary ADDRESS MASK`。


需要先按[完整双端案例](../../examples/ospf.md)建立邻接，在对应进程/area视图配置，提交后比较 LSDB、路由与业务；参数撤销后再次查询并保存。不能仅以 FRR 接受配置宣称对端已学到路由。

[OSPF 总览](../ospf.md) · [完整案例](../../examples/ospf.md) · [命令参数](../reference/ospf.md)
