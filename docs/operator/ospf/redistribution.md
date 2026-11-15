# 路由引入

协议引入可附带策略、metric和外部类型，参数顺序可交换：

```text
ospf 1
 import-route static route-policy REDIST cost 20 type 1
```


需要先按[完整双端案例](../../examples/ospf.md)建立邻接，在对应进程/area视图配置，提交后比较 LSDB、路由与业务；参数撤销后再次查询并保存。不能仅以 FRR 接受配置宣称对端已学到路由。

[OSPF 总览](../ospf.md) · [完整案例](../../examples/ospf.md) · [命令参数](../reference/ospf.md)
