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

display ip routing-table 和 display ipv6 routing-table 显示路由选择结果；verbose 或 inactive 可查询详细路径及备选路由。display ip fib 和 display ipv6 fib 显示实际转发表，用于确认路径已经安装。未指定 vpn-instance 时查询 default 表，VPN 名称区分大小写。Lookup-Table 仅对显式继续查表路径显示目标表号，包括 default 的 0；普通转发路径显示 -。IPv6 FIB 按路径分块显示目的前缀、下一跳、Preference、权重、路径类型、出接口及可用标志，ECMP 的每条有效路径各占一个块。

两条 FIB 命令支持单个 `| include`、`| exclude` 和 `| begin` 逐行过滤。IPv4 的
`include` 保留匹配表项的表头，计数仍表示所选 FIB 的总量。过滤按显示行匹配，
IPv6 输出中未匹配的路径字段可以省略。


[功能目录](../routing-tables.md) · [命令参数](../reference/ip-routing.md)
