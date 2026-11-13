# IPv4/IPv6、VPN、静态路由与路由组

## VPN-instance

VPN-instance 默认可用，直接用 `ip vpn-instance NAME` 创建。已分配的表号继续使用，
新表从 1024 起查找可用值，可以超过 2048。VortexROS 跳过 Linux 和 VPP 已使用的表，
并按受管标记清理自身创建的 Linux VRF。默认实例仍对应 Linux main 表 254 和 VPP 表 0。


```text
ip vpn-instance BLUE
 ipv4-family
  route-distinguisher 65000:100
  vpn-target 65000:100 both
 ipv6-family
```

接口、路由和动态路由协议可以引用VPN实例。仍有配置引用时不能删除VPN。RD/RT只需在VPN实例下配置，在BGP VPN地址族中无需重复输入。

## 普通静态路由

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

不指定下一跳和出接口、只指定不同下一跳VPN实例的形式表示“在目标VPP FIB中继续查表”。VPP仍是
这类路由唯一的数据面所有者，路由不会写入Linux路由表。控制层同时通过route-zapi向Zebra发布一条
不写内核的控制面影子，使BGP `network`、`redistribute static`、路由策略和递归下一跳能够观察该路由；
带下一跳、出接口或`NULL 0`的普通静态路由由统一静态路由后端发布，不再触发协议配置全树提交；
CLI、保存配置及显示语义保持不变。相同目的VPN和前缀不能同时配置继续查表路径与
普通路径，也不能配置多个查表目标。运行显示以精确VPP读回作为安装状态，不重复显示控制面影子，因此
少量此类路由不会触发对大型FIB的全表扫描。

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

## IPv6运行状态命令

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

IPv6邻居表直接读取VPP实际ND条目，可按接口、VPN实例或动态/静态类型过滤：

```text
display ipv6 neighbors
display ipv6 neighbors Vlanif 10
display ipv6 neighbors interface Ethernet 1
display ipv6 neighbors vpn-instance BLUE
display ipv6 neighbors dynamic
display ipv6 neighbors static
```

静态邻居使用`ipv6 neighbor IPV6 MAC interface IF`配置并随Candidate、commit和save持久化；删除时使用对应的完整`undo ipv6 neighbor ...`命令。`undo`中的接口、IPv6地址和MAC必须与Candidate中的条目完全匹配，避免输错MAC时误删另一条配置。承载接口被删除并重建后，即使静态邻居配置本身未变化，控制面也会重新下发该条目。commit会以VPP静态邻居表为权威读回，不能把动态学习条目误认为已配置静态条目。

每个邻居使用独立的信息块，`IPv6 Address`独占一行；其余字段固定按`Link-layer/State`、`Interface/Age`、`VLAN/CEVLAN`、`VPN name/Is Router`两列显示，`Secure FLAG`单列显示。动态和静态类型只在汇总中计数，不增加无后端字段的明细行。VLAN信息只来自已提交模型，不根据接口名称猜测：Vlanif使用其VLAN，子接口使用外层/内层VLAN，Vbdif只有在业务桥域明确绑定VLAN时才显示该VLAN；桥域ID不会冒充VLAN ID。当前VPP Binary API不提供完整ND状态、Router标志和SEND安全状态，这些字段显示`-`，不会伪造为REACH、Router或安全邻居。命令也不会根据接口地址伪造本机邻居项。

## 静态路由组

静态路由组用于让大量前缀共用相同的下一跳、出接口、VPN、Preference和Tag。配置中只保留路由组及其绑定关系，不会把十万条成员展开成同样数量的普通静态路由命令。

```text
route-static group name CDN
 description CDN-PREFIXES
 route 198.18.0.0/24
 route 198.18.1.1
#
ip route-static-group CDN 192.0.2.1 preference 60 tag 100
```

裸IPv4规范为`/32`，裸IPv6规范为`/128`，输入掩码后配置统一显示CIDR。手工成员自动去重。

### 文件成员与URL成员

路由组的外部列表统一存放在：

```text
/VortexROS/route-static-groupd
```

管理员可先把每行一个CIDR的文件放到该目录，再在路由组视图中选择。`?`和Tab只列出目录顶层的普通文件，不接受子目录、符号链接或包含路径分隔符的名称：

```text
route-static group name CDN
 source file cdn-v4.txt
```

首次`commit`会解析、规范化并生成不可变运行快照。之后直接修改原文件不会绕过配置事务改变现网；执行下面的命令才会重新读取、显示进度并增量更新路由：

```text
reset route-static group name CDN
```

URL与本地文件互斥。URL下载后的原始物化结果和元数据也由系统存放在同一目录的受管子目录中：

```text
route-static group name CDN
 source url https://lists.example.net/cdn-v4.txt vpn-instance BLUE
 auto-refresh enable
 auto-refresh interval 4320
```

URL默认必须使用HTTPS。只有明确接受明文传输的受控环境才可配置
`source url http://192.0.2.10/routes.txt insecure`；HTTPS来源不允许经重定向降级为HTTP。

两种来源的内容均为每行一个CIDR，空行和整行`#`注释跳过；任一非法行使新版本整体失效。手工与外部成员取并集。本地文件不支持`auto-refresh`；URL可按配置定时刷新。

首次配置URL后，执行全局 `commit` 会显示连接、下载、检查、应用和完成等进度；只有文件下载并检查成功后配置才会生效。后续普通commit不会重复下载：

```text
reset route-static group name CDN
display route-static group name CDN verbose
display ip routing-table-group name CDN verbose
```

Ctrl+C只停止当前终端的进度显示，不取消设备正在执行的更新，也不关闭SSH。

## 路由组增量修改

- 一个成员变化只影响“该前缀×引用该组的绑定”；
- 一个绑定变化只处理该组成员；
- 普通静态路由和多个路由组产生完全相同的路径和属性时，设备只保留一条有效路由；
- 路径相同但Preference、Tag等不同会报告冲突；
- 增加或删除单个成员时，只更新该成员所影响的路由，不重新加载整个路由组。

## uRPF与路由表

接口可以启用严格或宽松的反向路径检查：

```text
interface Vlanif 100
 ip urpf strict
 ipv6 urpf strict
```

- `strict`：源地址的最佳返回路径必须从收到报文的接口到达；
- `loose`：源地址只需在路由表中可达；
- `disable`或对应的`undo ip urpf`、`undo ipv6 urpf`：关闭该地址族检查。

IPv4和IPv6 uRPF是两个独立配置对象，修改或撤销其中一个不会覆盖另一个。使用 `display urpf` 查看全部地址族，使用`display ipv6 urpf`只查看IPv6接口模式；通过`display ip routing-table ... verbose`或`display ipv6 routing-table ... verbose`检查作为判断依据的路由。

## 功能验证表

| 场景 | 配置 | 数据面效果 | 验证 |
|---|---|---|---|
| 直连下一跳 | 普通静态路由 | 安装到目标VRF | ping和routing-table |
| 递归下一跳 | 先建递归可达路由 | 解析成功后安装 | verbose中的NextHop/Interface |
| ECMP | 同前缀不同下一跳 | 多路径进入RIB/FIB | route verbose和流量 |
| 跨VPN | 目标VPN+下一跳VPN | 在目标表安装、去指定表解析下一跳 | 两个VPN路由表 |
| 默认路由 | `/0` | 无更长匹配时使用 | 特定目的ping/tracert |
| 精确undo | 完整路径参数 | 只删除一个所有者/路径 | 其他所有者仍保留 |

最后验证 `display current-configuration`顺序：路由组定义在普通静态路由上方，`ip route-static-group`绑定位于普通静态路由下方。
