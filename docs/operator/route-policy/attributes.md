# 属性与继续节点

策略节点还可匹配路由tag、cost和来源协议，并设置tag、origin、IPv4/IPv6下一跳、AS_PATH、标准community和large-community。`continue node`只允许跳到同一策略中已经存在的更大节点号：

```text
route-policy REDIST permit node 10
 if-match protocol static
 if-match tag 100
 apply tag 200
 apply cost 30
 apply origin igp
 apply community 65000:100 no-export additive
 apply large-community 65000:1:100 additive
 continue node 20
quit
route-policy REDIST permit node 20
```

这些动作按实际使用的协议能力解释；例如BGP community只影响BGP属性。配置链在提交前校验引用和地址族，IPv4协议引入不能引用含IPv6 prefix-list条件的策略，反之亦然。`if-match protocol`可用于BGP引入；当前OSPF/OSPFv3后端不能在对应消费者中执行该条件，因此OSPF引入引用这类策略时会在提交前明确拒绝，不能静默退化为无条件许可。

[真实属性变化](../../examples/bgp-policy.md) · [命令参数](../reference/route-policy.md)
