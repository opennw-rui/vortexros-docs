# IPv6 查询

## 常用查询

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

`display ipv6 nd`读取VPP的IPv6邻居容量、老化时间与回收策略。IPv6 邻居容量默认 102400 条。`ipv6 nd max-number` 与数据面视图中的 IPv6 邻居容量命令使用同一个值，撤销容量命令恢复默认值。`ipv6 nd recycle` 控制 VPP 的动态邻居回收，默认关闭。`display ipv6 pathmtu`读取VPP实际路径MTU数据库，可按VPN实例过滤。`display ipv6 pool`和`display ipv6 prefix`分别显示已提交的DHCPv6地址池和IPv6前缀列表；原有的DHCPv6客户端、中继以及IPv6路由组命令保持不变。

IPv6 邻居查询见 [ARP 与 ND](../neighbors.md)。

[功能目录](../routing-tables.md) · [命令参数](../reference/ip-routing.md)


## 路径 MTU

`display ipv6 pathmtu` 显示数据面已有的 IPv6 路径 MTU 记录。默认路由表显示为 `default`，可按 VPN 实例筛选：

```text
<VortexROS> display ipv6 pathmtu
IPv6 Address     Path MTU  VPN-Instance  Table ID
2001:db8:999::2  1400      default       0
2001:db8:999::3  1280      BLUE          1024

<VortexROS> display ipv6 pathmtu vpn-instance default
IPv6 Address     Path MTU  VPN-Instance  Table ID
2001:db8:999::2  1400      default       0
```

Path MTU 的单位是字节；Table ID 是该 VPN 实例当前使用的数据面表号。IPv4 记录不会出现在此命令中。已有记录删除后，相应行也会消失；只有表头表示当前没有记录，不表示查询失败。

本命令只查询已有记录，不修改接口 MTU，也不主动探测或创建路径 MTU。不要把它的输出等同于所有目的地址均已完成路径 MTU 探测。
