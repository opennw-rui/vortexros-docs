# 节点与前缀匹配

前缀列表负责匹配路由，路由策略决定允许、拒绝或修改匹配的路由。下面的策略只允许 `10.0.0.0/8` 中掩码长度为16至24的前缀，并把BGP本地优先级设为200：

```text
ip ip-prefix PL-IN index 10 permit 10.0.0.0 8 greater-equal 16 less-equal 24
route-policy RP-IN permit node 10
 if-match ip-prefix PL-IN
 apply local-preference 200
```

配置完成后，输入 `display ip ip-prefix ?`、`display route-policy ?` 或在协议中输入 `route-policy ?`，会同时显示参数说明和已经存在的对象名称。

可用 `display ip ip-prefix <名称> verbose`、`display ip ipv6-prefix <名称> verbose`
查看实际前缀规则与命中计数。用 `display route-policy <名称> verbose` 查看
实际策略节点和调用次数。
在前缀列表名称后使用 `first-match <CIDR>`，可按规则顺序查看第一个匹配项。
IPv4 和 IPv6 分别使用各自的显示命令。

命令关键字不区分大小写；用户定义的对象名按输入原样保存并区分大小写。例如`RP-IN`和`rp-in`是两个不同策略，引用时必须使用定义时的大小写。同一个route-policy节点只能有一个IPv4前缀列表条件和一个IPv6前缀列表条件；再次输入同地址族的`if-match`会替换原条件。需要匹配多个前缀时，应在同一个前缀列表中增加多条规则，或者使用不同的策略节点。

IPv6前缀列表和策略条件使用独立命令：

```text
ip ipv6-prefix V6-IN index 10 permit 2001:db8:: 32 greater-equal 48 less-equal 64
route-policy V6-POLICY permit node 10
 if-match ipv6 address prefix-list V6-IN
```

可使用`display ipv6 prefix V6-IN`验证IPv6列表。IPv4与IPv6列表可以同名，但引用命令明确区分地址族；也可以使用`display ip ipv6-prefix`查看IPv6列表。

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


## 撤销匹配条件的影响

撤销一条匹配条件会保留该节点的许可/拒绝动作、属性设置和其他匹配条件，并不是停用整个策略。例如：

```text
route-policy RP-IN permit node 10
 undo if-match ip-prefix PL-IN
#
route-policy V6-POLICY permit node 10
 undo if-match ipv6 address prefix-list V6-IN
#
```

再执行`commit`生效。若节点已经没有任何匹配条件，该节点就变成无条件许可；
所有到达此节点的路由都可能通过，并执行原来的`apply`动作。这会扩大通告或接收范围。
如果目标是取消策略限制，应先解除协议对策略的引用；如果目标是继续过滤，
应先设置替代匹配条件，不能把删除匹配条件等同于删除节点。

在双栈BGP出口中，前缀列表原本只允许
`198.18.242.3/32`和`2001:db8:242::3/128`，对应许可节点设置MED47和48。
相邻的243前缀未匹配，接收端查询显示0条。
撤销相应IPv4/IPv6匹配条件后，接收端实际出现：

```text
     Network            NextHop             MED     LocPrf Path/Ogn
 *>  198.18.243.3/32    198.19.23.3          47        100 Local i

Total Number of Routes: 1
```

```text
     Network                                      NextHop             MED  LocPrf Path/Ogn
 *>  2001:db8:243::3/128                         2001:db8:23::3       48      100 Local i

Total Number of Routes: 1
```

这两条新增路由均实际探测1发1收。用
`display route-policy <名称> verbose`核对时，`Match clauses`已空，
原来的`metric 47`或`metric 48`仍在；调用计数非零。
该计数反映策略执行情况，不是接口包数，应结合接收端路由和连通性判断结果。

## 删除节点或整个策略

仅删除指定节点：

```text
undo route-policy RP-IN permit node 10
```

删除整个策略：

```text
undo route-policy V6-POLICY
```

先解除协议中的引用，再执行删除并`commit`。
删除前缀列表是另一项操作，使用
`undo ip ip-prefix PL-IN`或`undo ip ipv6-prefix V6-IN`。
在上述双栈配置完整撤销后，策略及两族前缀列表摘要均显示`Total: 0`；
撤销示例BGP网络后，两条243前缀从接收端消失，
IPv4和IPv6探测均明确返回`Network is unreachable`。
不要用一次查询失败来代替已撤销的确认。


[真实 BGP 策略案例](../../examples/bgp-policy.md) · [全部参数](../reference/route-policy.md)
