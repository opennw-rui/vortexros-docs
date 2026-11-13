# 路由策略

允许、拒绝或修改协议接收或发布的路由。

[命令参考](reference/route-policy.md) · [配置案例](../examples/bgp-policy.md)

## 配置与验证

前缀列表负责匹配路由，路由策略决定允许、拒绝或修改匹配的路由。下面的策略只允许 `10.0.0.0/8` 中掩码长度为16至24的前缀，并把BGP本地优先级设为200：

```text
ip ip-prefix PL-IN index 10 permit 10.0.0.0 8 greater-equal 16 less-equal 24
route-policy RP-IN permit node 10
 if-match ip-prefix PL-IN
 apply local-preference 200
```

配置完成后，输入 `display ip ip-prefix ?`、`display route-policy ?` 或在协议中输入 `route-policy ?`，会同时显示参数说明和已经存在的对象名称。

可用 `display ip ip-prefix <名称> verbose`、`display ip ipv6-prefix <名称> verbose`
查看 BGP 后端中的前缀规则与命中计数。用 `display route-policy <名称> verbose` 查看
BGP 后端的策略节点和调用次数。
在前缀列表名称后使用 `first-match <CIDR>`，可按规则顺序查看第一个匹配项。
IPv4 和 IPv6 分别使用各自的显示命令。

命令关键字不区分大小写；用户定义的对象名按输入原样保存并区分大小写。例如`RP-IN`和`rp-in`是两个不同策略，引用时必须使用定义时的大小写。同一个route-policy节点只能有一个IPv4前缀列表条件和一个IPv6前缀列表条件；再次输入同地址族的`if-match`会替换原条件。需要匹配多个前缀时，应在同一个前缀列表中增加多条规则，或者使用不同的策略节点。

IPv6前缀列表和策略条件使用独立命令：

```text
ip ipv6-prefix V6-IN index 10 permit 2001:db8:: 32 greater-equal 48 less-equal 64
route-policy V6-POLICY permit node 10
 if-match ipv6 address prefix-list V6-IN
```

可使用`display ipv6 prefix V6-IN`验证IPv6列表。IPv4与IPv6列表可以同名，但引用命令明确区分地址族；旧入口`display ip ipv6-prefix`仍保留，便于已有运维脚本继续使用。

```text
display ip ip-prefix PL-IN
display route-policy RP-IN
display current-configuration | include PL-IN
```

删除前应先解除协议中的引用：

```text
undo route-policy RP-IN permit node 10
undo ip ip-prefix PL-IN
```

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
