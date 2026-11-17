# 静态路径与查表

为指定前缀配置固定路径、黑洞路径或跨表查询。

[命令参考](../reference/static-routing.md) · [配置案例](../../examples/static-route.md)

## 配置

```text
ip route-static 203.0.113.0 255.255.255.0 192.0.2.1 preference 60 tag 100 description TO-WAN
ip route-static 198.51.100.0 255.255.255.0 NULL 0 preference 80 tag 900 description DISCARD
ip route-static vpn-instance BLUE 10.0.0.0 8 vpn-instance default 192.0.2.1 Tunnel 1
ip route-static vpn-instance BLUE 198.51.100.0 24 vpn-instance default
ipv6 route-static 2001:db8:100:: 64 2001:db8::1
ipv6 route-static vpn-instance BLUE 2001:db8:200:: 64 vpn-instance default
ipv6 route-static 2001:db8:dead:: 48 NULL 0 preference 80 tag 900 description DISCARD-V6
```

`NULL 0`明确创建黑洞路由，可同时携带`preference`、`tag`和`description`，但不能再指定下一跳、出接口或下一跳VPN。撤销时使用同一目的前缀和`NULL 0`，只删除该黑洞路径，不影响同前缀的普通静态路径。运行路由表中的接口名称仍显示为`NULL0`。

多条静态路由在配置中连续显示，不用无意义的`#`逐条分隔。跨VPN下一跳要同时显示目标VPN和下一跳VPN。

不指定下一跳和出接口、只指定另一 VPN 实例时，表示到目标表中继续查表。该路径可供 BGP network、静态路由引入和路由策略使用。相同目的 VPN 和前缀不能同时配置继续查表路径与普通下一跳路径，也不能配置多个查表目标。用 display ip fib 或 display ipv6 fib 核对实际安装及 Lookup-Table，再检查目标 VPN 的后续路由和双向业务。

[查询 RIB 与 FIB](../routing-tables.md)。

## 检查路由

| 场景 | 配置 | 数据面效果 | 验证 |
|---|---|---|---|
| 直连下一跳 | 普通静态路由 | 安装到目标VRF | ping和routing-table |
| 递归下一跳 | 先建递归可达路由 | 解析成功后安装 | verbose中的NextHop/Interface |
| ECMP | 同前缀不同下一跳 | 多路径进入RIB/FIB | route verbose和流量 |
| 跨VPN | 目标VPN+下一跳VPN | 在目标表安装、去指定表解析下一跳 | 两个VPN路由表 |
| 默认路由 | `/0` | 无更长匹配时使用 | 特定目的ping/tracert |
| 精确undo | 完整路径参数 | 只删除一个所有者/路径 | 其他所有者仍保留 |


## 指定出接口

出接口可以使用分离式名称，例如 `Ethernet 1`，也可以使用完整名称 `Ethernet1`。
系统会按实际接口身份保存和显示，不会因为使用了缩写而创建另一条接口路径。
IPv6 路由使用的三层接口须先配置 `ipv6 enable`。

以下两种参数顺序表达同一条路径，不需要同时配置：

```text
ip route-static 198.19.201.0 24 Ethernet 1 198.18.31.2 preference 75 tag 201 description TO-UPLINK
ip route-static 198.19.201.0 24 198.18.31.2 Ethernet 1 preference 75 tag 201 description TO-UPLINK
```

仅指定接口、不指定下一跳时，设备直接在该接口上解析目的地址的 ARP 或 ND。
以太网上的远端网段通常应同时指定下一跳；只有接口或配置存在，不能证明远端已经可达。

```text
ip route-static 198.18.31.2 32 Ethernet 1 preference 80 tag 220
display ip routing-table 198.18.31.2 32 verbose
display ip fib | include 198.18.31.2
```

检查详细路由中的 `State: Active Adv Relied`、`Interface: Ethernet1`，
再检查来自其他接口的业务能否到达目的端。设备自身发起的 Ping 不代替转发业务检查。

精确撤销时保留路径定位参数。同一前缀还存在其他下一跳或其他接口路径时，
它们继续参与选路；省略路径参数则撤销该目的表中该前缀的所有静态路径：

```text
undo ip route-static 198.19.201.0 24 Ethernet 1 198.18.31.2
commit
display ip routing-table 198.19.201.0 24 verbose
```

## 继续查表与跨表下一跳

两者的使用目的不同：

| 配置方式 | 含义 | FIB 的 Lookup-Table |
|---|---|---|
| 只指定下一跳 VPN，不指定下一跳和接口 | 报文到另一张表继续查找目的地址 | 显示目标表号 |
| 指定下一跳 VPN 和下一跳地址，可带接口 | 在指定 VPN 解析下一跳，再使用实际出口 | 已解析为普通出口时显示 `-` |

例如默认表到 SHOW201 的继续查表路径：

```text
ip route-static 198.19.203.0 24 vpn-instance SHOW201
ipv6 route-static 2001:db8:213:: 64 vpn-instance SHOW201
commit
display ip fib | include 198.19.203
display ipv6 fib | begin 2001:db8:213
```

当 SHOW201 的实际表号为 1024 时，这两条路径显示 `Lookup-Table: 1024`。
表号以本机运行结果为准，不应硬编码到配置中。目标表还须具备后续可用路由和回程路径。
撤销继续查表路径时使用同一目标 VPN；成功查询后相应前缀应消失：

```text
undo ip route-static 198.19.203.0 24 vpn-instance SHOW201
undo ipv6 route-static 2001:db8:213:: 64 vpn-instance SHOW201
commit
display ip fib | include 198.19.203
display ipv6 fib | include 2001:db8:213
```
