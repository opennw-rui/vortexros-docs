# 邻居与会话


```text
bgp 64512
 router-id 10.0.0.1
 peer 10.0.0.2 as-number 64513
 peer 10.0.0.2 description EBGP-P2
 peer 10.0.0.2 connect-interface LoopBack 0
 peer 10.0.0.2 route-policy RP-IN import
 ipv4-family unicast
  network 10.10.0.0 255.255.0.0
```

常用会话、GTSM、GR、RR 和多路径参数都先进入候选配置，提交后生效：

```text
bgp 64512
 timer keepalive 10 hold 30
 graceful-restart enable
 graceful-restart timer restart 90
 graceful-restart timer wait-for-rib 300
 reflector cluster-id 10.0.0.1
 load-balancing as-path-ignore
 peer 192.0.2.2 valid-ttl-hops 2
 peer 192.0.2.2 timer keepalive 5 hold 15
 peer 192.0.2.2 timer connect-retry 10
 peer 192.0.2.2 graceful-restart helper-only
 ipv4-family unicast
  maximum load-balancing ebgp 8
  maximum load-balancing ibgp 4
  import-route static route-policy REDIST cost 100
```

`valid-ttl-hops`与`ebgp-max-hop`互斥，系统在进入Candidate前拒绝同时配置。全局和邻居keepalive/hold必须成对配置；除显式`0/0`外，hold不能小于keepalive的三倍。显式`0/0`和`graceful-restart timer restart 0`会原样保存并下发，与`undo`恢复默认值的语义不同。scoped GR、RR和ECMP命令都支持精确`undo`和保存恢复。

提交后，设备使用指定源接口连接邻居，对收到的路由应用 `RP-IN`，并在本地路由表存在相同前缀时发布network。输入 `lo0` 等合法缩写时，配置会显示为设备中的规范接口名。


## Add-Path

`display bgp update-peer-group statistics` 显示 BGP 更新组计数。
在单播地址族视图配置 `peer <邻居或组> add-path send 2` 后，除最佳路径外最多再通告两条路径。
对端需要协商 Add-Path 接收能力。用 `undo peer <邻居或组> add-path` 恢复默认通告。撤销或修改已有的通告条数时，受影响的邻居或组成员会重新建立会话。
变更能力可能触发会话重新协商。


[会话与路由查询、精确撤销](queries.md) · [完整双端案例](../../examples/bgp.md) · [策略实际结果](../../examples/bgp-policy.md)
