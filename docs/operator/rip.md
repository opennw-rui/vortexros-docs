# RIP

使用 RIPv2 在 IPv4 网络交换路由。配套 FRR 的缺省优先级为 120，可在进程视图调整。

[命令参考](reference/rip.md) · [配置案例](../examples/rip.md)

## 配置


```text
rip 1
 version 2
 network 10.0.0.0
 default-metric 2
 maximum load-balancing 4
 timers rip 30 180 120
 silent-interface LoopBack 0
```

`network`使用IPv4主类网络地址。提交后匹配接口参加RIP，silent-interface仍发布该接口网络，但不从该接口发送更新。

## 验证与撤销

```text
display rip 1 interface
display rip 1 database
display rip 1 route
```

在系统视图执行 `undo rip 1` 并提交会删除该进程学习和通告的路由。
