# 动态路由、策略路由、BFD 与 VRRP


## `abr-summary`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：configure an OSPFv3 area summary；configure an area summary
- 合法语法：

  ```text
  abr-summary X.X.X.X X.X.X.X [not-advertise]
  ```
  ```text
  abr-summary X:X::X:X INTEGER<0-128> [not-advertise]
  ```

## `advertise l2vpn evpn`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：export VPN routes to the EVPN address family
- 合法语法：

  ```text
  advertise l2vpn evpn
  ```

## `aggregate`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：configure a BGP aggregate route
- 合法语法：

  ```text
  aggregate ADDRESS MASK [as-set] [detail-suppressed]
  ```

## `aggregate-address`

- 类别：配置命令
- 视图：`RIPng视图`
- 用途（设备帮助）：advertise a RIPng aggregate
- 合法语法：

  ```text
  aggregate-address X:X::X/M
  ```

## `apply as-path`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：prepend AS numbers to the BGP AS path
- 合法语法：

  ```text
  apply as-path ASNUM [ASNUM ...]
  ```

## `apply community`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set BGP community values
- 合法语法：

  ```text
  apply community VALUE [VALUE ...] [additive]
  ```

## `apply cost`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set route metric
- 合法语法：

  ```text
  apply cost VALUE
  ```

## `apply ip-address next-hop`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set an IPv4 next hop
- 合法语法：

  ```text
  apply ip-address next-hop X.X.X.X
  ```

## `apply ipv6 next-hop`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set an IPv6 next hop
- 合法语法：

  ```text
  apply ipv6 next-hop X:X::X
  ```

## `apply large-community`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set BGP large-community values
- 合法语法：

  ```text
  apply large-community VALUE [VALUE ...] [additive]
  ```

## `apply local-preference`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set local preference
- 合法语法：

  ```text
  apply local-preference VALUE
  ```

## `apply origin`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set the BGP origin attribute
- 合法语法：

  ```text
  apply origin {igp|egp|incomplete}
  ```

## `apply tag`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set route tag
- 合法语法：

  ```text
  apply tag INTEGER<0-4294967295>
  ```

## `area`

- 类别：配置命令
- 视图：`OSPF Area视图`、`OSPF视图`、`ospfv3-area`、`ospfv3`
- 用途（设备帮助）：enter an OSPF area view；enter an OSPFv3 area view
- 合法语法：

  ```text
  area X.X.X.X
  ```

## `auto-cost reference-bandwidth`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：set the OSPF reference bandwidth
- 合法语法：

  ```text
  auto-cost reference-bandwidth INTEGER<1-4294967>
  ```

## `bandwidth-reference`

- 类别：配置命令
- 视图：`ospfv3`
- 用途（设备帮助）：set the OSPFv3 reference bandwidth
- 合法语法：

  ```text
  bandwidth-reference INTEGER<1-4294967>
  ```

## `continue node`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：continue evaluation at a later route-policy node
- 合法语法：

  ```text
  continue node INTEGER<1-65535>
  ```

## `cost-style`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set IS-IS metric style
- 合法语法：

  ```text
  cost-style {narrow|wide|transition}
  ```

## `default ipv4-unicast`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：activate IPv4 unicast by default
- 合法语法：

  ```text
  default ipv4-unicast
  ```

## `default tcp-protected`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：protect the BGP TCP listener with configured peers
- 合法语法：

  ```text
  default tcp-protected
  ```

## `default-metric`

- 类别：配置命令
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`
- 用途（设备帮助）：set default metric；set the default metric for redistributed OSPF routes
- 合法语法：

  ```text
  default-metric INTEGER<1-16777214>
  ```
  ```text
  default-metric INTEGER<1-16>
  ```

## `default-route originate`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：originate a default route
- 合法语法：

  ```text
  default-route originate
  ```

## `default-route-advertise`

- 类别：配置命令
- 视图：`OSPF视图`、`ospfv3`
- 用途（设备帮助）：originate a default route into OSPF；originate an IPv6 default route into OSPFv3
- 合法语法：

  ```text
  default-route-advertise [always]
  ```

## `detect-multiplier`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：Detect multiplier
- 合法语法：

  ```text
  detect-multiplier INTEGER
  ```

## `display bfd`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display BFD information
- 合法语法：

  ```text
  display bfd [configuration|session [all|NAME]|statistics]
  ```

## `display bgp`

peer 查询会话，routing-table 查询前缀，vpnv4 和 vpnv6 切换地址族。见[BGP 案例](../../examples/bgp.md)。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display BGP information
- 合法语法：

  ```text
  display bgp {peer|routing-table|ipv6|vpnv4|vpnv6|...}
  ```

## `display bgp tcp-protection`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display BGP TCP listener source protection
- 合法语法：

  ```text
  display bgp tcp-protection [verbose]
  ```

## `display isis`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IS-IS information
- 合法语法：

  ```text
  display isis [process-id] [brief|peer|lsdb|route|interface|spf-delay|traffic-eng]
  ```

## `display ospf`

peer 查询邻接，routing 查询协议路由，lsdb 查询链路状态数据库。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display OSPF information
- 合法语法：

  ```text
  display ospf [process-id] lsdb [{router|network|summary|asbr|ase|nssa|opaque-*} [link-state-id]] [originate-router router-id|self-originate] [age {min-value|max-value} seconds]
  ```

## `display ospfv3`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display OSPFv3 information
- 合法语法：

  ```text
  display ospfv3 [process-id|vpn-instance NAME] [brief|peer|interface|lsdb|routing]
  ```

## `display rip`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display RIP information
- 合法语法：

  ```text
  display rip [process-id] [database|route|interface|statistics]
  ```

## `display ripng`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display RIPng information
- 合法语法：

  ```text
  display ripng [process-id] [database|route|interface|statistics]
  ```

## `display route-policy`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display route policies
- 合法语法：

  ```text
  display route-policy [NAME [verbose]]
  ```

## `display vrrp`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 VRRPv3 information
- 合法语法：

  ```text
  display vrrp [brief|interface INTERFACE|statistics|protocol-information|VRID]
  ```

## `graceful-restart`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set BGP graceful-restart role
- 合法语法：

  ```text
  graceful-restart {enable|helper-only|disable}
  ```

## `graceful-restart timer restart`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set BGP graceful-restart restart timer
- 合法语法：

  ```text
  graceful-restart timer restart INTEGER<0-4095>
  ```

## `graceful-restart timer wait-for-rib`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set BGP graceful-restart wait-for-rib timer
- 合法语法：

  ```text
  graceful-restart timer wait-for-rib INTEGER<1-4095>
  ```

## `group`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`
- 用途（设备帮助）：create a case-sensitive BGP peer-group
- 合法语法：

  ```text
  group NAME [internal|external]
  ```

## `hostname dynamic`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：enable the IS-IS dynamic hostname
- 合法语法：

  ```text
  hostname dynamic
  ```

## `if-match cost`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set route metric
- 合法语法：

  ```text
  if-match cost INTEGER<0-4294967295>
  ```

## `if-match ip-prefix`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：match an IP prefix list
- 合法语法：

  ```text
  if-match ip-prefix NAME
  ```

## `if-match ipv6 address prefix-list`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：match an IPv6 prefix list
- 合法语法：

  ```text
  if-match ipv6 address prefix-list NAME
  ```

## `if-match protocol`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：match the route source protocol
- 合法语法：

  ```text
  if-match protocol {direct|static|ospf|ospfv3|isis|rip|ripng|bgp}
  ```

## `if-match tag`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set route tag
- 合法语法：

  ```text
  if-match tag INTEGER<0-4294967295>
  ```

## `import-route`

- 类别：配置命令
- 视图：`BGP地址族视图`、`IS-IS视图`、`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：redistribute IPv6 routes into OSPFv3；redistribute routes into BGP；redistribute routes into IS-IS；redistribute routes into OSPF；redistribute routes into RIP
- 合法语法：

  ```text
  import-route PROTOCOL [route-policy NAME] [cost COST]
  ```
  ```text
  import-route PROTOCOL [route-policy NAME] [cost COST] [type {1|2}]
  ```
  ```text
  import-route {direct|static|ospf|bgp|isis}
  ```
  ```text
  import-route {direct|static|ospf|bgp}
  ```

## `ipv4-family unicast`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the IPv4 unicast address family
- 合法语法：

  ```text
  ipv4-family unicast
  ```

## `ipv4-family vpn-instance`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the IPv4 VPN address family
- 合法语法：

  ```text
  ipv4-family vpn-instance VPN
  ```

## `ipv4-family vpnv4`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the VPNv4 address family
- 合法语法：

  ```text
  ipv4-family vpnv4
  ```

## `ipv6 import-route`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：redistribute IPv6 routes into IS-IS
- 合法语法：

  ```text
  ipv6 import-route {direct|static|ospfv3|bgp}
  ```

## `ipv6-family unicast`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the IPv6 unicast address family
- 合法语法：

  ```text
  ipv6-family unicast
  ```

## `ipv6-family vpn-instance`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the IPv6 VPN address family
- 合法语法：

  ```text
  ipv6-family vpn-instance VPN
  ```

## `ipv6-family vpnv6`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the VPNv6 address family
- 合法语法：

  ```text
  ipv6-family vpnv6
  ```

## `is-level`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set IS-IS level
- 合法语法：

  ```text
  is-level {level-1|level-2|level-1-2}
  ```

## `l2vpn-family evpn`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the BGP EVPN address family
- 合法语法：

  ```text
  l2vpn-family evpn
  ```

## `load-balancing as-path-ignore`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：allow equal-length different AS paths in BGP ECMP
- 合法语法：

  ```text
  load-balancing as-path-ignore
  ```

## `log-adjacency-changes`

- 类别：配置命令
- 视图：`IS-IS视图`、`OSPF视图`
- 用途（设备帮助）：log IS-IS adjacency changes；log OSPF adjacency changes
- 合法语法：

  ```text
  log-adjacency-changes
  ```
  ```text
  log-adjacency-changes [detail]
  ```

## `log-session-changes`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：log-session-changes
- 合法语法：

  ```text
  log-session-changes
  ```

## `maximum load-balancing`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：set the maximum OSPFv3 ECMP paths；set the maximum number of BGP equal-cost paths；set the maximum number of RIP equal-cost paths
- 合法语法：

  ```text
  maximum load-balancing INTEGER<1-32>
  ```
  ```text
  maximum load-balancing INTEGER<1-6>
  ```
  ```text
  maximum load-balancing [ebgp|ibgp] INTEGER<1-256>
  ```

## `maximum-paths`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：set the maximum OSPF ECMP paths
- 合法语法：

  ```text
  maximum-paths INTEGER<1-256>
  ```

## `min-rx-interval`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：Minimum receive interval in milliseconds
- 合法语法：

  ```text
  min-rx-interval INTEGER
  ```

## `min-tx-interval`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：Minimum transmit interval in milliseconds
- 合法语法：

  ```text
  min-tx-interval INTEGER
  ```

## `network-entity`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set an IS-IS network entity title
- 合法语法：

  ```text
  network-entity NET
  ```

## `nssa`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：configure a not-so-stubby area；configure an OSPFv3 nssa area
- 合法语法：

  ```text
  nssa [no-summary]
  ```

## `offset-list`

- 类别：配置命令
- 视图：`RIPng视图`
- 用途（设备帮助）：adjust RIPng route metrics selected by an IPv6 ACL
- 合法语法：

  ```text
  offset-list ACL {in|out} INTEGER<0-16> [interface IF]
  ```

## `opaque-capability enable`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：enable OSPF opaque LSA capability
- 合法语法：

  ```text
  opaque-capability enable
  ```

## `passive-interface default`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：make all RIP interfaces passive
- 合法语法：

  ```text
  passive-interface default
  ```

## `passive-mode`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：passive-mode
- 合法语法：

  ```text
  passive-mode
  ```

## `policy vpn-target`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：control VPN route-target filtering
- 合法语法：

  ```text
  policy vpn-target
  ```

## `preference`

- 类别：配置命令
- 视图：`RIP视图`
- 用途（设备帮助）：set RIP route preference
- 合法语法：

  ```text
  preference INTEGER<1-255>
  ```

## `reflect between-clients`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：allow route reflection between clients
- 合法语法：

  ```text
  reflect between-clients
  ```

## `reflector cluster-id`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set the route-reflector cluster ID
- 合法语法：

  ```text
  reflector cluster-id X.X.X.X
  ```

## `router-id`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`OSPF视图`、`ospfv3`
- 用途（设备帮助）：set BGP router ID；set OSPF router ID；set the OSPFv3 router ID
- 合法语法：

  ```text
  router-id X.X.X.X
  ```

## `set-overload-bit`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set the IS-IS overload bit
- 合法语法：

  ```text
  set-overload-bit
  ```

## `silent-interface`

- 类别：配置命令
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：suppress OSPF Hellos on an interface；suppress OSPFv3 Hellos on an interface；suppress RIP updates on an interface
- 合法语法：

  ```text
  silent-interface INTERFACE
  ```

## `spf-delay-ietf`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：configure IETF SPF backoff timers
- 合法语法：

  ```text
  spf-delay-ietf init-delay MS short-delay MS long-delay MS holddown MS time-to-learn MS
  ```

## `stub`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：configure a stub area；configure an OSPFv3 stub area
- 合法语法：

  ```text
  stub [no-summary]
  ```

## `timer keepalive`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set BGP keepalive and hold timers
- 合法语法：

  ```text
  timer keepalive INTEGER<0-21845> hold INTEGER<0-65535>
  ```

## `timers rip`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：set RIP update, timeout and garbage timers
- 合法语法：

  ```text
  timers rip INTEGER<1-32767> INTEGER<1-32767> INTEGER<1-32767>
  ```

## `undo abr-summary`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：delete an area summary；remove an OSPFv3 area summary
- 合法语法：

  ```text
  undo abr-summary X.X.X.X X.X.X.X
  ```
  ```text
  undo abr-summary X:X::X:X INTEGER<0-128>
  ```

## `undo advertise l2vpn evpn`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：export VPN routes to the EVPN address family
- 合法语法：

  ```text
  undo advertise l2vpn evpn
  ```

## `undo aggregate`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：delete a BGP aggregate route
- 合法语法：

  ```text
  undo aggregate ADDRESS MASK
  ```

## `undo aggregate-address`

- 类别：配置命令
- 视图：`RIPng视图`
- 用途（设备帮助）：withdraw a RIPng aggregate
- 合法语法：

  ```text
  undo aggregate-address X:X::X/M
  ```

## `undo apply as-path`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the AS-path prepend action
- 合法语法：

  ```text
  undo apply as-path
  ```

## `undo apply community`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the BGP community action
- 合法语法：

  ```text
  undo apply community
  ```

## `undo apply cost`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：restore default route metric
- 合法语法：

  ```text
  undo apply cost
  ```

## `undo apply ip-address next-hop`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the IPv4 next-hop action
- 合法语法：

  ```text
  undo apply ip-address next-hop
  ```

## `undo apply ipv6 next-hop`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the IPv6 next-hop action
- 合法语法：

  ```text
  undo apply ipv6 next-hop
  ```

## `undo apply large-community`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the BGP large-community action
- 合法语法：

  ```text
  undo apply large-community
  ```

## `undo apply local-preference`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：restore default local preference
- 合法语法：

  ```text
  undo apply local-preference
  ```

## `undo apply origin`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the BGP origin action
- 合法语法：

  ```text
  undo apply origin
  ```

## `undo apply tag`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove route tag
- 合法语法：

  ```text
  undo apply tag
  ```

## `undo auto-cost reference-bandwidth`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：restore the OSPF reference bandwidth
- 合法语法：

  ```text
  undo auto-cost reference-bandwidth
  ```

## `undo bandwidth-reference`

- 类别：配置命令
- 视图：`ospfv3`
- 用途（设备帮助）：restore the OSPFv3 reference bandwidth
- 合法语法：

  ```text
  undo bandwidth-reference
  ```

## `undo bgp`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a BGP instance
- 合法语法：

  ```text
  undo bgp ASNUM
  ```

## `undo continue`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：stop evaluation after this route-policy node
- 合法语法：

  ```text
  undo continue
  ```

## `undo default ipv4-unicast`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`
- 用途（设备帮助）：disable automatic IPv4-unicast peer activation
- 合法语法：

  ```text
  undo default ipv4-unicast
  ```

## `undo default tcp-protected`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：disable BGP TCP listener peer protection
- 合法语法：

  ```text
  undo default tcp-protected
  ```

## `undo default-metric`

- 类别：配置命令
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`
- 用途（设备帮助）：restore default metric；restore the default OSPF redistribution metric
- 合法语法：

  ```text
  undo default-metric
  ```

## `undo default-route originate`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：stop originating a default route
- 合法语法：

  ```text
  undo default-route originate
  ```

## `undo default-route-advertise`

- 类别：配置命令
- 视图：`OSPF视图`、`ospfv3`
- 用途（设备帮助）：remove OSPF default route advertisement；stop originating an IPv6 default route
- 合法语法：

  ```text
  undo default-route-advertise
  ```

## `undo detect-multiplier`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：restore the default Detect multiplier
- 合法语法：

  ```text
  undo detect-multiplier
  ```

## `undo graceful-restart`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore the default BGP graceful-restart helper role
- 合法语法：

  ```text
  undo graceful-restart
  ```

## `undo graceful-restart timer restart`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore BGP graceful-restart restart timer
- 合法语法：

  ```text
  undo graceful-restart timer restart
  ```

## `undo graceful-restart timer wait-for-rib`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore BGP graceful-restart wait-for-rib timer
- 合法语法：

  ```text
  undo graceful-restart timer wait-for-rib
  ```

## `undo group`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`
- 用途（设备帮助）：delete an unused BGP peer-group
- 合法语法：

  ```text
  undo group NAME
  ```

## `undo hostname`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：restore the default IS-IS hostname
- 合法语法：

  ```text
  undo hostname
  ```

## `undo if-match cost`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove route metric
- 合法语法：

  ```text
  undo if-match cost
  ```

## `undo if-match ip-prefix`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove an IP prefix match
- 合法语法：

  ```text
  undo if-match ip-prefix NAME
  ```

## `undo if-match ipv6 address prefix-list`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove an IPv6 prefix match
- 合法语法：

  ```text
  undo if-match ipv6 address prefix-list NAME
  ```

## `undo if-match protocol`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the route source protocol match
- 合法语法：

  ```text
  undo if-match protocol
  ```

## `undo if-match tag`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove route tag
- 合法语法：

  ```text
  undo if-match tag
  ```

## `undo import-route`

- 类别：配置命令
- 视图：`BGP地址族视图`、`IS-IS视图`、`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：stop redistributing routes into BGP；stop redistributing routes into IS-IS；stop redistributing routes into OSPF；stop redistributing routes into OSPFv3；stop redistributing routes into RIP
- 合法语法：

  ```text
  undo import-route PROTOCOL
  ```

## `undo ipv4-family vpn-instance`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove an IPv4 VPN address family
- 合法语法：

  ```text
  undo ipv4-family vpn-instance VPN
  ```

## `undo ipv4-family vpnv4`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove the VPNv4 address family
- 合法语法：

  ```text
  undo ipv4-family vpnv4
  ```

## `undo ipv6 import-route`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：stop redistributing IPv6 routes into IS-IS
- 合法语法：

  ```text
  undo ipv6 import-route PROTOCOL
  ```

## `undo ipv6-family unicast`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove the IPv6 unicast address family
- 合法语法：

  ```text
  undo ipv6-family unicast
  ```

## `undo ipv6-family vpn-instance`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove an IPv6 VPN address family
- 合法语法：

  ```text
  undo ipv6-family vpn-instance VPN
  ```

## `undo ipv6-family vpnv6`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove the VPNv6 address family
- 合法语法：

  ```text
  undo ipv6-family vpnv6
  ```

## `undo is-level`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：restore IS-IS level
- 合法语法：

  ```text
  undo is-level
  ```

## `undo isis`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an IS-IS process
- 合法语法：

  ```text
  undo isis INTEGER<1-65535>
  ```

## `undo l2vpn-family evpn`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove the BGP EVPN address family
- 合法语法：

  ```text
  undo l2vpn-family evpn
  ```

## `undo load-balancing as-path-ignore`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：require identical AS paths for BGP ECMP
- 合法语法：

  ```text
  undo load-balancing as-path-ignore
  ```

## `undo log-adjacency-changes`

- 类别：配置命令
- 视图：`IS-IS视图`、`OSPF视图`
- 用途（设备帮助）：stop logging IS-IS adjacency changes；stop logging OSPF adjacency changes
- 合法语法：

  ```text
  undo log-adjacency-changes
  ```

## `undo log-session-changes`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：undo log-session-changes
- 合法语法：

  ```text
  undo log-session-changes
  ```

## `undo maximum load-balancing`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：restore RIP path default；restore the OSPFv3 ECMP path limit；restore the default BGP equal-cost path count
- 合法语法：

  ```text
  undo maximum load-balancing
  ```
  ```text
  undo maximum load-balancing [ebgp|ibgp]
  ```

## `undo maximum-paths`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：restore the default OSPF ECMP path count
- 合法语法：

  ```text
  undo maximum-paths
  ```

## `undo min-rx-interval`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：restore the default Minimum receive interval in milliseconds
- 合法语法：

  ```text
  undo min-rx-interval
  ```

## `undo min-tx-interval`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：restore the default Minimum transmit interval in milliseconds
- 合法语法：

  ```text
  undo min-tx-interval
  ```

## `undo network-entity`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：remove an IS-IS network entity title
- 合法语法：

  ```text
  undo network-entity NET
  ```

## `undo nssa`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：restore a normal OSPF area；restore a normal OSPFv3 area
- 合法语法：

  ```text
  undo nssa
  ```

## `undo offset-list`

- 类别：配置命令
- 视图：`RIPng视图`
- 用途（设备帮助）：remove a RIPng metric offset
- 合法语法：

  ```text
  undo offset-list {in|out} [interface IF]
  ```

## `undo opaque-capability enable`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：disable OSPF opaque LSA capability
- 合法语法：

  ```text
  undo opaque-capability enable
  ```

## `undo ospf`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an OSPF process
- 合法语法：

  ```text
  undo ospf INTEGER<1-65535>
  ```

## `undo passive-interface default`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：restore passive interface default
- 合法语法：

  ```text
  undo passive-interface default
  ```

## `undo passive-mode`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：undo passive-mode
- 合法语法：

  ```text
  undo passive-mode
  ```

## `undo policy vpn-target`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：control VPN route-target filtering
- 合法语法：

  ```text
  undo policy vpn-target
  ```

## `undo preference`

- 类别：配置命令
- 视图：`RIP视图`
- 用途（设备帮助）：restore RIP route preference
- 合法语法：

  ```text
  undo preference
  ```

## `undo reflect between-clients`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：disable route reflection between clients
- 合法语法：

  ```text
  undo reflect between-clients
  ```

## `undo reflector cluster-id`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore the router ID as the cluster ID
- 合法语法：

  ```text
  undo reflector cluster-id
  ```

## `undo rip`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a RIP process
- 合法语法：

  ```text
  undo rip INTEGER<1-65535> [vpn-instance NAME]
  ```

## `undo ripng`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a RIP process
- 合法语法：

  ```text
  undo ripng INTEGER<1-65535> [vpn-instance NAME]
  ```

## `undo route-policy`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a route policy
- 合法语法：

  ```text
  undo route-policy NAME [permit|deny node INTEGER<1-65535>]
  ```

## `undo router-id`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`OSPF视图`、`ospfv3`
- 用途（设备帮助）：remove BGP router ID；remove OSPF router ID；remove the OSPFv3 router ID
- 合法语法：

  ```text
  undo router-id
  ```

## `undo set-overload-bit`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：clear the IS-IS overload bit
- 合法语法：

  ```text
  undo set-overload-bit
  ```

## `undo silent-interface`

- 类别：配置命令
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：enable RIP updates on an interface；restore OSPF Hellos on an interface；restore OSPFv3 Hellos on an interface
- 合法语法：

  ```text
  undo silent-interface INTERFACE
  ```

## `undo spf-delay-ietf`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：disable IETF SPF backoff timers
- 合法语法：

  ```text
  undo spf-delay-ietf
  ```

## `undo stub`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：restore a normal OSPF area；restore a normal OSPFv3 area
- 合法语法：

  ```text
  undo stub
  ```

## `undo timer keepalive`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore BGP keepalive and hold timers
- 合法语法：

  ```text
  undo timer keepalive
  ```

## `undo timers rip`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：restore RIP timers
- 合法语法：

  ```text
  undo timers rip
  ```

## `version`

- 类别：配置命令
- 视图：`RIP视图`
- 用途（设备帮助）：set RIP version
- 合法语法：

  ```text
  version {1|2}
  ```
