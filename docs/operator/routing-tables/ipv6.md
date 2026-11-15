# IPv6 查询

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

IPv6 邻居查询见 [ARP 与 ND](../neighbors.md)。

[功能目录](../routing-tables.md) · [命令参数](../reference/ip-routing.md)
