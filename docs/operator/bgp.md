# BGP

使用邻居和地址族控制前缀交换。

[命令参考](reference/bgp.md) · [配置案例](../examples/bgp.md)

## 配置

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

## 更新组和 Add-Path

`display bgp update-peer-group statistics` 显示 BGP 更新组计数。
在单播地址族视图配置 `peer <邻居或组> add-path send 2` 后，除最佳路径外最多再通告两条路径。
对端需要协商 Add-Path 接收能力。用 `undo peer <邻居或组> add-path` 恢复默认通告。撤销或修改已有的通告条数时，受影响的邻居或组成员会重新建立会话。
变更能力可能触发会话重新协商。
