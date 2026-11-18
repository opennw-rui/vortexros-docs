# IPv6 服务端

DHCPv6 服务端分配 IA_NA 地址、IA_PD 前缀或提供非地址信息。默认网关来自 RA，不能因为租约成功就假定默认路由已存在。全局启用 `enable dhcp server` 后，在接口绑定已有的 DHCPv6 池。


```text
dhcpv6 pool LAN6
 address prefix 2001:db8:100::/64
 dns-server 2001:4860:4860::8888
#
interface Vlanif 100
 ipv6 enable
 dhcpv6 server LAN6
```

验证和撤销：

```text
display dhcp service verbose
display dhcpv6 pool
```

配置清单：

```text
interface Vlanif 100
 undo dhcpv6 server
```

CLI 操作：

```text
commit
```

DHCPv6客户端和中继在对应接口视图配置；可使用`?`查看地址请求、前缀委派和中继目标的完整参数。接口上不能同时承担相互冲突的客户端、服务器和中继角色；切换角色后检查实际租约及服务状态。

同一DHCPv6地址池内的地址前缀和委派前缀必须使用同一组有效/首选生命周期；显式生命周期最小为
60秒，首选生命周期不得大于有效生命周期。重叠的委派前缀在进入Candidate时即被拒绝，不会留到
Kea启动阶段才失败。


## 配置、验证和撤销

[双端 DHCPv6 案例](../../examples/dhcpv6.md)列出池、接口、客户端、实际 IA_NA/IA_PD 查询与撤销；[中继案例](../../examples/dhcpv6-relay.md)另有三节点配置。正常空库显示零租约，不能当服务故障；服务/Socket 真正失败仍报错。

解除接口的 `dhcpv6 server` 绑定后，再删除不再引用的池。多实例按地址族及 VPN 独立运行；租约显示不应被另一个健康空实例阻断。提交后核对服务、租约和实际客户端状态，再保存。

[租约字段与筛选](leases.md) · [参数参考](../reference/dhcp.md)

## 池参数与服务器标识

| 配置 | 作用与默认值 |
|---|---|
| `address prefix 前缀 [life-time 有效 首选]` | 分配 IA_NA；未指定生命周期时有效 172800 秒、首选 86400 秒 |
| `prefix-delegation 聚合前缀 委派长度 [life-time 有效 首选]` | 从聚合前缀分配 IA_PD；不等同于给客户端接口分配地址 |
| `excluded-address 起始 [结束]` | 保留网关和其他静态地址，禁止动态分配 |
| `dns-server 地址`、`dns-domain-name 域名` | 通告 DNS 和搜索域，不改写服务器自身的 DNS |
| `information-refresh 秒` | 信息刷新选项，默认 86400 秒；客户端是否请求、采用该选项由其实现决定 |
| 池内 `vpn-instance 名称` | 池与服务接口必须属于同一 VPN；缺省为默认实例 |
| 系统视图 `dhcpv6 duid ll` 或 `dhcpv6 duid llt` | 选择服务器标识类型，默认 LL；LLT 还包含时间信息 |

DUID 是客户端识别服务器的依据。修改 DUID 类型可能被客户端视为更换服务器，应安排合适的维护时机。实际请求中，LLT 配置对应回复的 `server-ID hwaddr/time`，`undo dhcpv6 duid` 后恢复 `server-ID hwaddr type 1`。

例如，客户链路使用 `2001:db8:11::/64`，保留前 255 个地址：

```text
dhcpv6 pool LAN6
 address prefix 2001:db8:11::/64 life-time 3600 1800
 excluded-address 2001:db8:11::1 2001:db8:11::ff
 dns-server 2001:db8::53
#
```

实际分配后，查询节选如下（池名按本例表示）：

```text
Pool name  VPN-Instance  Address-prefixes  PD-prefixes  DNS  Used
LAN6       default       1                 0            1    1

IPv6 address/prefix : 2001:db8:11::101/128
Lease type          : IA_NA
DUID                : 00:03:00:01:02:fe:52:79:7d:05
IAID                : 1427819375
State               : used
Valid lifetime      : 3600s
```

`display dhcpv6 pool name LAN6 used` 只列有效租约；`all` 还可能列出过期记录，包括已撤销池的历史记录，不能把这些记录等同于仍在分配地址。裸池摘要中的 `Used -` 表示本次未查询租约，不是查询失败。

撤销某个参数使用相应的 `undo` 命令，例如 `undo excluded-address 起始 结束`、`undo dns-server 地址`、`undo dns-domain-name 域名`、`undo information-refresh`。撤销地址前缀或委派范围前，应先迁移仍使用它的接口和客户端。删除整个池的完整顺序是：解除接口服务器绑定，执行 `undo dhcpv6 pool LAN6`，提交后检查服务和池查询；客户端已获得的地址按其租期和客户端行为处理。
