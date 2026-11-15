# AS 与路由属性


VortexROS只开放能够用VRP语义完整映射到当前FRR 10.7.1后端、并可保存和撤销的命令，不直接暴露FRR的`neighbor`语法。外部邻居可以使用伪本地AS：

```text
bgp 64512
 peer 192.0.2.2 as-number 64513
 peer 192.0.2.2 fake-as 64514 dual-as
 ipv4-family unicast
  peer 192.0.2.2 substitute-as
  peer 192.0.2.2 preferred-value 200
  peer 192.0.2.2 keep-all-routes
```

这些命令也可配置在外部邻居组上，成员继承组值。`fake-as`只适用于EBGP邻居；伪AS不能等于全局AS。`dual-as`允许对端使用全局AS或伪AS建立会话；`prepend-global-as`在发出的AS_PATH中同时保留全局AS。FRR 10.7.1不能精确表达`dual-as`和`prepend-global-as`同时启用的VRP行为，因此该组合会在提交前明确拒绝，不会静默改变含义。

地址族命令的含义如下：

- `substitute-as`把发往EBGP邻居的路径中与对端AS相同的AS替换为本地AS；后端使用`as-override`。
- `preferred-value`设置本机选择从该邻居收到的路由时使用的优先值；后端使用本地`weight`，不会向其他设备传播。
- `keep-all-routes`保留被入方向策略拒绝的原始更新，供策略变更后重新计算；后端使用入方向软重配置。

精确撤销示例：

```text
bgp 64512
 undo peer 192.0.2.2 fake-as
 ipv4-family unicast
  undo peer 192.0.2.2 substitute-as
  undo peer 192.0.2.2 preferred-value
  undo peer 192.0.2.2 keep-all-routes
```

可用语法见[命令参考](../reference/bgp.md)。请通过VortexROS CLI配置BGP属性，不直接修改FRR配置。


[会话与路由查询、精确撤销](queries.md) · [完整双端案例](../../examples/bgp.md) · [策略实际结果](../../examples/bgp-policy.md)
