# 路由策略、OSPF、BGP、IS-IS、RIP、BFD 与 VRRP

本章从设备使用者的角度说明如何建立邻居、发布路由、检查结果和撤销配置。示例中的接口、地址、AS号和计时值仅用于说明，部署时应替换为实际规划。

## 查询输出与大路由表

BGP、OSPF、OSPFv3、IS-IS、RIP、RIPng、LDP和MPLS控制面查询都直接读取对应
FRR daemon的VTY流，并在一次解析过程中生成VRP风格输出。路由表不会先完整读入内存，
也不会为排版再次请求后端。`display mpls forwarding-table`例外：它直接读取VPP实际
LFIB，用于确认数据面而不是重复显示FRR控制面。

常用大表入口如下：

```text
display bgp routing-table
display ospf 1 routing
display ospfv3 1 routing
display isis 1 route
display rip 1 route
display ripng 1 route
display mpls ldp binding
display mpls lsp
```

开发服务器使用十万条记录、输出到`io.Discard`的格式化基准结果如下。该测试只衡量
解析和排版，不包含FRR生成数据、终端传输或分页时间：

| 协议 | 十万条排版时间 |
|---|---:|
| BGP | 721.7 ms |
| OSPF | 669.6 ms |
| OSPFv3 | 382.3 ms |
| IS-IS | 220.6 ms |
| RIP | 215.7 ms |
| RIPng | 171.7 ms |
| LDP binding | 619.0 ms |
| MPLS LSP | 876.9 ms |

这些数字用于防止实现退回到“全量反序列化后再排版”的路径，不是设备转发性能承诺。

## IP前缀列表与路由策略

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

## OSPF

### 使用area下的network激活

```text
ospf 1 router-id 10.0.0.1
 opaque-capability enable
 area 0.0.0.0
  network 10.0.12.1 0.0.0.0 description P1-P2
```

`network`只能在area视图中输入。提交后，地址匹配的接口开始发送Hello报文；只有两端area、网络类型、认证和计时等条件兼容时才会建立邻居。

### 使用接口命令激活

```text
ospf 1 router-id 10.0.0.1
interface Vlanif 12
 ospf enable 1 area 0.0.0.0
 ospf network-type p2p
 ospf cost 10
 ospf dr-priority 100
 ospf timer hello 3
 ospf timer dead 12
 ospf timer retransmit 4
 ospf timer transmit-delay 2
```

同一进程只能选择 `network` 或接口 `ospf enable` 一种激活方式；混用会在命令进入待提交配置前报错。广播网络上的DR优先级范围为0至255，0表示不参与DR/BDR选举。

协议引入可附带策略、metric和外部类型，参数顺序可交换：

```text
ospf 1
 import-route static route-policy REDIST cost 20 type 1
```

### Stub、NSSA与区域汇总

区域类型和汇总在area视图配置：

```text
ospf 1
 area 0.0.0.1
  nssa no-summary
  abr-summary 10.0.0.0 255.0.0.0 not-advertise
```

`stub`与`nssa`互斥；已经配置一种类型时，必须先执行对应的`undo`，不能用另一条命令隐式覆盖。`no-summary`阻止向该区域发布三类汇总路由，`not-advertise`阻止发布指定区域汇总。撤销命令为`undo stub`、`undo nssa`和`undo abr-summary ADDRESS MASK`。

### 验证与撤销

```text
display ospf 1 brief
display ospf 1 peer brief
display ospf 1 peer 10.0.0.2
display ospf 1 interface
display ospf 1 lsdb
display ospf 1 lsdb router
display ospf 1 lsdb router 10.0.0.1
display ospf 1 lsdb ase 192.0.2.0
display ospf vpn-instance BLUE lsdb
display ospf vpn-instance BLUE lsdb ase 192.0.2.0
display ospf 1 lsdb originate-router 10.0.0.2
display ospf 1 lsdb router self-originate
display ospf 1 lsdb age min-value 300 max-value 1800
display ospf 1 lsdb | include Router
display ospf 1 routing
reset ospf 1 process
```

无类型的`display ospf 1 lsdb`按Area显示Router、Network、Summary和ASBR Summary等LSA摘要，并将AS External和Opaque数据库分段显示。摘要的`Len`为LSA实际长度，具有单一度量值的LSA在`Metric`列显示实际值。Router和Network等无单一度量值的LSA显示`-`。AS External明细的`E type`显示1或2。指定`router`、`network`、`summary`、`asbr`、`ase`、`nssa`或`opaque-*`后逐条显示该类LSA的详细字段；类型后可继续指定Link State ID。`originate-router`按Advertising Router过滤，`self-originate`只显示本机产生的LSA，`age`按0至3600秒的LSA年龄范围过滤。显示管道继续支持`include`、`exclude`、`begin`和`section`，过滤后的表格保留所属标题和表头。

修改或撤销已有进程Router-ID时，配置可以先被接受，但FRR活动Router-ID需要进程reset才能切换。未显式配置时，控制层依据设备配置中的真实接口类型，在同一VPN实例中优先选择数值最大的LoopBack IPv4地址；不存在LoopBack IPv4时，才从该VPN的静态IPv4和受管Linux/LCP接口上的DHCP等可信运行IPv4中选择最大值，并把这个有效值投射给FRR。DHCP运行地址不会写回静态CFG；Linux/LCP侧接口类型也不会改变LoopBack优先的产品语义。Router-ID投入运行后不会仅因原地址Down、被删除、DHCP续租或出现更大地址而自动重启进程；需要切换时执行`reset ospf ... process`。reset会在允许重选的边界更新受管Router-ID、清理目标进程，再读取活动Router-ID及完整FRR权威状态，不会重启整个FRR。由于当前FRR后端不能保证多OSPFv2实例的单实例清理，配置多个OSPFv2进程时该操作会明确拒绝；单OSPFv2进程和OSPFv3使用受支持的目标范围。

`display ospf peer brief`按以下顺序显示，Interface位于Neighbor id左侧：

```text
Area Id    Pri  Up Time   Dead Time  Interface   Neighbor id  State
0.0.0.0      1  00:12:31  00:00:38   Vlanif12    10.0.0.2     Full
```

修改与删除示例：

```text
interface Vlanif 12
 undo ospf dr-priority
 undo ospf network-type
 undo ospf enable 1
undo ospf 1
commit
```

撤销接口激活只影响该接口；删除进程会撤销该进程的全部邻居和路由。

## OSPFv3

OSPFv3用于IPv6动态路由。先创建进程和区域，再在三层接口下绑定进程：

```text
ospfv3 1 router-id 10.0.0.1
 maximum load-balancing 6
 bandwidth-reference 100000
 import-route static
 area 0.0.0.0
interface Vlanif 12
 ospfv3 1 area 0.0.0.0
 ospfv3 cost 25
 ospfv3 network-type p2p
 ospfv3 dr-priority 0
 ospfv3 timer hello 3
 ospfv3 timer dead 12
 ospfv3 timer retransmit 4
 ospfv3 timer transmit-delay 2
```

接口必须属于与进程相同的VPN实例。进程1对应default；其他进程必须在创建时指定非default VPN，例如`ospfv3 2 router-id 10.0.0.2 vpn-instance BLUE`。同一个VPN只能对应一个后端OSPFv3实例，同一个接口不能同时加入两个OSPFv3进程。

Stub、NSSA和IPv6区域汇总在area视图配置：

```text
ospfv3 1
 area 0.0.0.1
  nssa no-summary
  abr-summary 2001:db8:: 32 not-advertise
```

`stub`与`nssa`互斥。`default-route-advertise`仅在本机已有IPv6默认路由时发布，`default-route-advertise always`则不依赖本机默认路由。`silent-interface INTERFACE`保留该接口的网络发布但停止建立邻居。

```text
display ospfv3 1 brief
display ospfv3 1 peer brief
display ospfv3 1 interface
display ospfv3 1 lsdb
display ospfv3 1 routing
reset ospfv3 1 process
```

`peer brief`中的邻居状态来自FRR OSPFv3运行态，`routing`中的路由数量只统计协议为`ospf6`的IPv6路由。配置已提交但尚未形成邻接时不会伪造Full状态；验收时应同时确认邻居Full、IPv6路由存在和业务地址可达。

撤销示例：

```text
interface Vlanif 12
 undo ospfv3 1 area 0.0.0.0
ospfv3 1
 area 0.0.0.1
  undo abr-summary 2001:db8:: 32
  undo nssa
undo ospfv3 1
commit
```

## BGP

全系统只允许一个主BGP AS。再次输入相同AS会进入现有视图；输入不同AS会报错且不会修改配置。AS 65535不可使用。

### 建立IPv4邻居

```text
bgp 64512
 router-id 10.0.0.1
 peer 10.0.0.2 as-number 64513
 peer 10.0.0.2 description EBGP-P2
 peer 10.0.0.2 connect-interface LoopBack 0
 peer 10.0.0.2 route-policy RP-IN import
 ipv4-family unicast
  network 10.10.0.0 255.255.0.0
```

常用会话、GTSM、GR、RR和多路径控制均进入Canonical配置，而不是直接透传FRR：

```text
bgp 64512
 timer keepalive 10 hold 30
 graceful-restart enable
 graceful-restart timer restart 90
 graceful-restart timer wait-for-rib 300
 reflector cluster-id 10.0.0.1
 load-balancing as-path-ignore
 peer 192.0.2.2 valid-ttl-hops 2
 peer 192.0.2.2 timer keepalive 5 hold 15
 peer 192.0.2.2 timer connect-retry 10
 peer 192.0.2.2 graceful-restart helper-only
 ipv4-family unicast
  maximum load-balancing ebgp 8
  maximum load-balancing ibgp 4
  import-route static route-policy REDIST cost 100
```

`valid-ttl-hops`与`ebgp-max-hop`互斥，系统在进入Candidate前拒绝同时配置。全局和邻居keepalive/hold必须成对配置；除显式`0/0`外，hold不能小于keepalive的三倍。显式`0/0`和`graceful-restart timer restart 0`会原样保存并下发，与`undo`恢复默认值的语义不同。scoped GR、RR和ECMP命令都支持精确`undo`和保存恢复。

提交后，设备使用指定源接口连接邻居，对收到的路由应用 `RP-IN`，并在本地路由表存在相同前缀时发布network。输入 `lo0` 等合法缩写时，配置会显示为设备中的规范接口名。

### 邻居组与TCP MD5认证

具有相同属性的邻居可以加入同一个邻居组。内部组继承本地AS；外部组必须先指定对端AS，再加入成员：

```text
bgp 64512
 group IBGP-RR internal
 peer IBGP-RR password simple Lab-Password-01
 peer IBGP-RR connect-interface LoopBack 0
 peer 10.0.0.2 group IBGP-RR
 peer 10.0.0.3 group IBGP-RR
 group TRANSIT external
 peer TRANSIT as-number 64513
 peer TRANSIT password simple Transit-Password-01
 peer 192.0.2.2 group TRANSIT
 ipv4-family unicast
  peer IBGP-RR reflect-client
  peer TRANSIT route-policy RP-IN import
```

命令关键字不区分大小写，邻居组名称按输入原样保存并区分大小写；`TRANSIT`与`transit`是两个不同对象。成员继承组的AS、认证、源接口及地址族策略。邻居可以用`peer ADDRESS password simple PASSWORD`设置自己的认证密码，以覆盖组密码。已经加入邻居组的成员不能再单独配置AS；需要改变归属时，应先执行`undo peer ADDRESS`，再重新创建。

BFD按字段继承。组上启用BFD并配置计时器后，成员默认继承；成员只配置一个计时字段时，仅该字段覆盖组值，其余字段继续继承。`peer ADDRESS bfd disable`用于明确关闭该成员从组继承的BFD，`undo peer ADDRESS bfd disable`恢复继承；`undo peer ADDRESS bfd enable`同样删除成员级开关。存在显式关闭的成员时，系统会把组的有效BFD配置逐一投影到其余成员，避免后端重新继承组BFD而使关闭失效。运行态、BFD会话归属和FRR profile使用同一套有效值。

密码认证使用BGP TCP MD5。当前只提供`simple`形式，密码以明文进入配置并按明文下发到FRR，`display current-configuration`也会显示原值；应限制配置文件、命令输出和运维会话的访问权限。密码长度为1至80个不含空格的可打印字符，不支持`cipher`输入形式。

邻居组不能在仍有成员引用时删除。可按以下顺序撤销：

```text
bgp 64512
 undo peer 192.0.2.2
 undo peer TRANSIT password
 undo group TRANSIT
commit
```

`display bgp group`用于查看后端邻居组状态；`display current-configuration configuration bgp`用于核对设备配置。密码只应通过配置查看，不会作为普通BGP会话状态字段输出。

### VRP邻居AS与入站路由属性

VortexROS只开放能够用VRP语义完整映射到当前FRR 10.7.1后端、并可保存和撤销的命令，不直接暴露FRR的`neighbor`语法。外部邻居可以使用伪本地AS：

```text
bgp 64512
 peer 192.0.2.2 as-number 64513
 peer 192.0.2.2 fake-as 64514 dual-as
 ipv4-family unicast
  peer 192.0.2.2 substitute-as
  peer 192.0.2.2 preferred-value 200
  peer 192.0.2.2 keep-all-routes
```

这些命令也可配置在外部邻居组上，成员继承组值。`fake-as`只适用于EBGP邻居；伪AS不能等于全局AS。`dual-as`允许对端使用全局AS或伪AS建立会话；`prepend-global-as`在发出的AS_PATH中同时保留全局AS。FRR 10.7.1不能精确表达`dual-as`和`prepend-global-as`同时启用的VRP行为，因此该组合会在提交前明确拒绝，不会静默改变含义。

地址族命令的含义如下：

- `substitute-as`把发往EBGP邻居的路径中与对端AS相同的AS替换为本地AS；后端使用`as-override`。
- `preferred-value`设置本机选择从该邻居收到的路由时使用的优先值；后端使用本地`weight`，不会向其他设备传播。
- `keep-all-routes`保留被入方向策略拒绝的原始更新，供策略变更后重新计算；后端使用入方向软重配置。

精确撤销示例：

```text
bgp 64512
 undo peer 192.0.2.2 fake-as
 ipv4-family unicast
  undo peer 192.0.2.2 substitute-as
  undo peer 192.0.2.2 preferred-value
  undo peer 192.0.2.2 keep-all-routes
```

本次命令覆盖审计见[《BGP命令覆盖与后端映射》](reference/commands.md)。FRR支持但VRP没有等价公开语义、或者尚未具备Candidate、撤销、持久化与权威回读闭环的命令不会仅因后端存在而自动开放。

### VPN与IPv6地址族

```text
bgp 64512
 ipv4-family vpn-instance BLUE
  import-route direct
 ipv6-family vpn-instance BLUE
```

VPN地址族使用VPN实例下配置的RD和全部RT。进入VPN-instance地址族后，设备按缺省语义向FRR下发自动导出标签，不在公开配置中显示后端的`label vpn export auto`。`undo default ipv4-unicast`用于取消自动启用新IPv4邻居；此后需要在IPv4 unicast地址族中显式启用邻居。

全局VPNv4/VPNv6传输地址族缺省启用VPN-Target过滤，缺省配置不显示。RR或Inter-AS Option B需要保留所有VPN路由时使用：

```text
bgp 64512
 ipv4-family vpnv4
  undo policy vpn-target
 ipv6-family vpnv6
  undo policy vpn-target
```

`policy vpn-target`恢复缺省过滤行为。FRR后端分别使用`no bgp retain route-target all`和`bgp retain route-target all`表达这两个状态。

6PE使用IPv4邻居承载全局IPv6标签路由：

```text
bgp 64512
 peer 10.0.0.2 as-number 64512
 peer 10.0.0.2 connect-interface LoopBack0
 ipv6-family unicast
  peer 10.0.0.2 enable
  peer 10.0.0.2 label-route-capability
```

设备使用FRR原生IPv6 labeled-unicast地址族，路由仍经Zebra、Linux netlink和LCP进入VPP。

VortexROS对外只有一个BGP进程。VPN地址族未单独配置`router-id`时继承BGP视图的全局Router-ID；只有在对应VPN地址族中显式配置时才覆盖该值。全局Router-ID修改会同步更新后端VPN实例，并在同一事务恢复IPv4/IPv6的RD/RT投影，防止后端自动身份刷新改变已配置的VPN目标。

IPv4与IPv6邻居只能在对应的unicast地址族视图下修改。引用了IPv4 `ip ip-prefix`的route-policy不能挂载到IPv6邻居、IPv6 network或IPv6 `import-route`；IPv6地址族应使用`ip ipv6-prefix`和`if-match ipv6 address prefix-list`。IPv6地址族使用`import-route ospfv3`，由系统映射到后端OSPFv3路由类型。

地址族中可以生成聚合路由：

```text
bgp 64512
 ipv4-family unicast
  aggregate 10.0.0.0 255.0.0.0 detail-suppressed
 ipv6-family unicast
  aggregate 2001:db8:: 32 as-set detail-suppressed
```

`detail-suppressed`只发布聚合路由；`as-set`保留组成路由的AS信息。显式使用`as-set`时，系统会同步调整该BGP实例的后端AS_SET接收模式，使配置不会被FRR静默忽略。两项均未配置时，聚合路由与组成路由同时发布。

### 验证与撤销

```text
display bgp peer
display bgp peer 10.0.0.2 verbose
display bgp vpnv4 vpn-instance BLUE peer 10.0.0.2 verbose
display bgp vpnv4 vpn-instance BLUE peer 10.0.0.2 log-info
display bgp vpnv6 all peer verbose
display bgp routing-table
display bgp routing-table peer 10.0.0.2 received-routes
display bgp vpnv4 vpn-instance BLUE routing-table
display bgp vpnv4 vpn-instance BLUE routing-table statistics
display bgp tcp-protection verbose
```

动态路由的 `display` 输出由 VortexROS 统一排版，不透出 FRR 的原始标题、内部实例号或内存地址。BGP 全表、VPN 路由表、邻居收发路由及 AS Path 列表，OSPF/OSPFv3 路由与 LSDB，以及 IS-IS 路由与 LSDB，均直接读取对应协议 daemon 的 VTY 数据并逐项输出，首批记录不需要等待完整表进入内存；总数位于表尾。BGP 路由表的 `Path/Ogn` 与 AS Path 列表统一使用十进制 AS 号。`routing-table statistics` 显示后端统计的前缀、通告和重分发数量。BGP 邻居明细和 `log-info` 从对应地址族的 FRR 会话查询逐个解码邻居，`all` 查询按 VPN 实例标出结果。`log-info` 显示当前会话状态、可用的建立时间及 FRR 保留的最近重置和 Notification 原因。邻居摘要、接口和其他有界状态读取一次后端快照并按固定字段排版。

默认TCP保护只接受已经配置的BGP邻居源地址。需要关闭时：

```text
bgp 64512
 undo default tcp-protected
```

精确删除邻居或单项参数：

```text
bgp 64512
 undo peer 10.0.0.2 route-policy RP-IN import
 undo peer 10.0.0.2 description
 undo peer 10.0.0.2
undo bgp 64512
commit
```

## IS-IS

进程号在设备内全局唯一。一个进程只能绑定一个VPN，一个VPN最多配置一个IS-IS进程；接口所属VPN必须与进程VPN一致。

```text
isis 10 vpn-instance BLUE
 network-entity 49.0001.0100.0000.0001.00
 is-level level-2
 cost-style wide
 log-adjacency-changes
interface Vlanif 100
 isis enable 10
 isis ipv6-enable 10
 isis circuit-type p2p
 isis circuit-level level-2
 isis cost 20
```

提交后，IPv4和IPv6在同一进程中运行。接口VPN不一致、同一接口引用另一个进程或同一VPN已存在其他进程时，命令会被拒绝。

`import-route`用于导入IPv4路由，`ipv6 import-route`用于导入IPv6路由：

```text
isis 10
 import-route static
 ipv6 import-route static
 ipv6 import-route ospfv3
```

系统根据进程的IS-IS level生成FRR要求的`level-1`或`level-2`重分发命令；默认level-1-2会同时下发两级，避免后端接受命令时因缺少level而拒绝配置。

```text
display isis 10 brief
display isis 10 peer
display isis 10 interface
display isis 10 lsdb
display isis 10 route
display isis 10 spf-delay
```

在 IS-IS 进程视图用 `spf-delay-ietf init-delay 50 short-delay 200 long-delay 1000 holddown 5000 time-to-learn 500`
设置 SPF 退避参数，单位为毫秒。提交后查看 `display isis 10 spf-delay`，使用
`undo spf-delay-ietf` 并提交可关闭这组定时器。

撤销示例：

```text
interface Vlanif 100
 undo isis ipv6-enable 10
 undo isis enable
undo isis 10
commit
```

如果需要把进程迁移到另一个VPN，应先删除进程，再使用新VPN重新创建。配套 FRR 的 IS-IS 路由缺省优先级为 115。

查看 OSPF 接口报文计数可用 `display ospf <进程号> interface traffic [接口]`。
`display bgp update-peer-group statistics` 显示 BGP 更新组计数。
在单播地址族视图配置 `peer <邻居或组> add-path send 2` 后，除最佳路径外最多再通告两条路径。
对端需要协商 Add-Path 接收能力。用 `undo peer <邻居或组> add-path` 恢复默认通告。撤销或修改已有的通告条数时，受影响的邻居或组成员会重新建立会话。
变更能力可能触发会话重新协商。

## RIP与RIPng

RIP 和 RIPng 路由的缺省优先级均为 120。IPv4 RIP 可用 `preference <值>` 覆盖，
`undo preference` 恢复 120。RIPng 使用后端缺省值。

### RIP IPv4

```text
rip 1
 version 2
 network 10.0.0.0
 default-metric 2
 maximum load-balancing 4
 timers rip 30 180 120
 silent-interface LoopBack 0
```

`network`使用IPv4主类网络地址。提交后匹配接口参加RIP，silent-interface仍发布该接口网络，但不从该接口发送更新。

### RIPng IPv6

```text
ripng 2 vpn-instance BLUE
 network 2001:db8:100::/64
 import-route static
 default-route originate
```

RIPng视图中的`import-route ospf`表示导入OSPFv3路由，系统会映射到后端的IPv6协议名称。

在 RIPng 进程视图用 `aggregate-address 2001:db8:100::/48` 配置汇总。
提交后可在邻居的 `display ripng <进程号> route` 核对收到的前缀。
用 `undo aggregate-address 2001:db8:100::/48` 并提交撤销。

`offset-list <IPv6 ACL> in 4 interface <接口>` 可调整匹配入向路由的度量，
`out` 用于出向，省略接口时应用于该进程。ACL 规则只可用 permit 或 deny 匹配
IPv6 源前缀，该前缀在这里对应路由目的前缀。已引用的 ACL 须保留至少一条规则。用
`undo offset-list in interface <接口>` 撤销，提交后在 RIPng 路由表核对度量。

```text
display rip 1 interface
display rip 1 database
display rip 1 route
display ripng 2 interface
display ripng 2 route
```

RIP/RIPng 的路由数据库按后端到达顺序流式显示；`interface` 与 `statistics` 分别只保留接口状态和路由信息源，不再显示 FRR 的说明性页眉。未配置对应协议进程时命令会明确报告进程不存在。

精确撤销：

```text
rip 1
 undo network 10.0.0.0
 undo timers rip
undo rip 1
undo ripng 2 vpn-instance BLUE
commit
```

## BFD

BFD可建立独立会话，也可由OSPF、IS-IS、RIP和BGP邻居调用。静态和协议会话均默认发送间隔 1000 ms、接收间隔 1000 ms、检测次数 3。默认参数省略于保存配置。BGP 邻居覆盖对等体组的参数时，配置仍会显示有实际影响的覆盖项。

### 独立BFD会话

```text
bfd
bfd TO-P2 bind peer-ip 10.0.12.2 source-ip 10.0.12.1 interface Vlanif 12
 min-tx-interval 300
 min-rx-interval 300
 detect-multiplier 3
 log-session-changes
```

多跳会话需要显式指定 `source-ip`，VPN场景可追加 `vpn-instance BLUE`。

### 路由协议调用BFD

```text
interface Vlanif 12
 ospf bfd enable
```

```text
bgp 64512
 peer 10.0.0.2 bfd enable
```

IS-IS和RIP使用同样的接口形式，将命令前缀替换为 `isis bfd` 或 `rip bfd`。

```text
display bfd configuration
display bfd session all
display bfd statistics
```

BFD 会话摘要显示 Local、Remote 鉴别值、出接口、单跳或多跳和状态。
`display bfd session <名称>` 还显示源地址、配置与运行定时器、检测超时和诊断。
尚未在后端建立的会话显示 Pending。

恢复默认计时或删除会话：

```text
bfd TO-P2 bind peer-ip 10.0.12.2 source-ip 10.0.12.1 interface Vlanif 12
 undo min-tx-interval
 undo min-rx-interval
 undo detect-multiplier
undo bfd TO-P2
commit
```

## VRRP与VRRP6

VRRP用于让两台或多台设备共享一个网关地址。VRRP只能配置在真实的三层Ethernet、Eth-Trunk、子接口、Vlanif或Vbdif上；接口必须处于路由模式。

### IPv4完整示例

假设P1与P2都连接到VLAN 100，客户端使用 `10.100.0.254`作为默认网关。P1优先级120作为Master，P2保持默认优先级100作为Backup。

P1：

```text
interface Vlanif 100
 ip address 10.100.0.1 255.255.255.0
 vrrp vrid 10 version-3 send-packet-mode v3-only
 vrrp vrid 10 virtual-ip 10.100.0.254
 vrrp vrid 10 priority 120
 vrrp vrid 10 timer advertise 1
 vrrp vrid 10 track interface Vlanif 200 reduced 30
```

P2：

```text
interface Vlanif 100
 ip address 10.100.0.2 255.255.255.0
 vrrp vrid 10 version-3 send-packet-mode v3-only
 vrrp vrid 10 virtual-ip 10.100.0.254
 vrrp vrid 10 timer advertise 1
```

IPv4必须先输入 `version-3 send-packet-mode v3-only`，再配置虚拟IP或其他参数。默认优先级为100、通告间隔为1秒、抢占开启。P1的Vlanif200 down后，运行优先级降低30；若低于P2，P2接管虚拟网关。

虚拟IP可以与接口自身地址相同。此时设备是该虚拟地址的地址拥有者，运行优先级自动为255；配置中仍保留用户输入的优先级，状态显示以运行优先级为准。

### IPv6示例

```text
interface Vlanif 100
 ipv6 address 2001:db8:100::1 64
 vrrp6 vrid 20 virtual-ip 2001:db8:100::fe
 vrrp6 vrid 20 priority 120
 vrrp6 vrid 20 timer advertise 1
```

IPv6组使用 `vrrp6`，无需单独输入IPv4的版本命令。

### 查看状态和效果

```text
display vrrp brief
display vrrp interface Vlanif 100
display vrrp 10
display vrrp statistics
display vrrp6 brief
```

brief输出示例：

```text
VRID  State   Interface  Type  Virtual IP      Priority  RunPri  Adv
10    Master  Vlanif100  IPv4  10.100.0.254   120       120     1.00s
```

详细输出会显示状态、版本、地址族、虚拟IP、配置优先级、运行优先级、虚拟MAC、通告间隔和抢占状态。配置已经提交但VRRP组尚未创建时，State显示 `Pending (not created in dataplane)`，应检查接口模式、地址和服务健康状态。

数据面遵循VRRPv3规范：IPv4通告校验和只覆盖VRRP消息，IPv6通告使用IPv6伪首部；Master收到优先级低于或等于本机的通告时会立即发送一次自身通告，并继续保持Master状态。此行为可缩短错误Master出现后的收敛时间，不需要额外CLI配置。

业务验证应包括：客户端持续ping虚拟IP和外部地址；关闭Master的上联或被跟踪接口；确认Backup接管、ARP/ND更新且业务恢复；再恢复接口并观察抢占行为。

### 修改和删除

```text
interface Vlanif 100
 undo vrrp vrid 10 track interface Vlanif 200
 undo vrrp vrid 10 priority
 undo vrrp vrid 10 timer advertise
 undo vrrp vrid 10 virtual-ip 10.100.0.254
 undo vrrp vrid 10
```

`undo priority`恢复100，`undo timer advertise`恢复1秒，`undo preempt-mode`恢复抢占。`undo vrrp vrid 10`删除整个IPv4组；IPv6使用对应的 `undo vrrp6 vrid 20 ...`。

## 配置完成后的通用检查

每次变更后至少执行：

```text
display this
commit
display current-configuration
display ip routing-table
display alarm active
```

随后使用本节对应的邻居、路由、BFD或VRRP命令检查运行状态。确认业务正常后再执行 `save`。删除配置时先解除引用或接口绑定，再删除协议进程和策略对象。
