# 路由表与 FIB

RIB 用于核对控制面选路；FIB 用于核对数据面实际转发。

[命令参考](reference/ip-routing.md)

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


## IPv6 查询

在`display ipv6 ?`下会列出当前具有实际数据源的命令。未实现的数据采集能力不会显示成可用命令：

```text
fib                  Display IPv6 FIB information
interface            Display IPv6 interface information
nd                   Display IPv6 neighbor discovery information
neighbors            Display IPv6 neighbor information
pathmtu              Display IPv6 path MTU information
pool                 Display IPv6 pool information
prefix               Display IPv6 prefix-list information
routing-table        Display IPv6 routing table
urpf                 Display IPv6 URPF information
```

`display ipv6 nd`读取VPP的IPv6邻居容量、老化时间与回收策略。IPv6 邻居容量默认 102400 条。`ipv6 nd max-number` 与数据面视图中的 IPv6 邻居容量命令使用同一个值，撤销容量命令恢复默认值。`ipv6 nd recycle` 控制 VPP 的动态邻居回收，默认关闭。`display ipv6 pathmtu`读取VPP实际路径MTU数据库，可按VPN实例过滤；数据量较大时CLI按VPP游标连续读取全部分页，不会把正常的继续信号显示成错误。`display ipv6 pool`和`display ipv6 prefix`分别显示已提交的DHCPv6地址池和IPv6前缀列表；原有的DHCPv6客户端、中继以及IPv6路由组命令保持不变。

IPv6 邻居查询见 [ARP 与 ND](neighbors.md)。
