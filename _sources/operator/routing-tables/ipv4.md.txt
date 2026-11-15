# IPv4 查询与过滤

## 查询与输出

```text
display ip routing-table protocol static
display ip routing-table vpn-instance BLUE
display ipv6 routing-table protocol static
display ip fib
display ip fib vpn-instance BLUE
display ipv6 fib
display ipv6 fib vpn-instance BLUE
```

`display ip routing-table`和`display ipv6 routing-table`读取路由控制面的优选结果，并合并已提交的VPP继续查表路由；可通过`verbose`或`inactive`查看详细候选。`display ip fib`和`display ipv6 fib`直接读取VPP Binary API返回的实际转发项，不会用控制面路由冒充已生效FIB。两条FIB命令不带参数时查看default表，指定`vpn-instance`时按大小写敏感的VPP表名查看对应VPN；标题只显示表名，不显示Linux表ID。`Lookup-Table`仅对显式继续查表路径显示目标VPP表ID，包括default表的`0`。普通转发路径显示`-`。IPv6 FIB采用与IPv6路由表一致的逐路径块状布局；每个块只显示VPP能够证明的目的地址、前缀长度、下一跳、Preference、权重、路径类型、出接口、路径标志和递归查表ID。ECMP的每条有效路径各显示一个块。

两条 FIB 命令支持单个 `| include`、`| exclude` 和 `| begin` 逐行过滤。IPv4 的
`include` 保留匹配表项的表头，计数仍表示所选 FIB 的总量。过滤按显示行匹配，
IPv6 输出中未匹配的路径字段可以省略。


[功能目录](../routing-tables.md) · [命令参数](../reference/ip-routing.md)
