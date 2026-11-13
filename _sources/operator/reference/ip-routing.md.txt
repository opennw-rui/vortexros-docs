# IP、VPN 与静态路由


## `auto-refresh enable`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：enable automatic remote-list refresh
- 合法语法：

  ```text
  auto-refresh enable
  ```

## `auto-refresh interval`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：set the remote-list refresh interval
- 合法语法：

  ```text
  auto-refresh interval INTEGER<5-10080>
  ```

## `display ip fib`

读取 VPP 中实际安装的 IPv4 转发项。Lookup-Table 的短横线表示普通转发路径。示例 display ip fib vpn-instance BLUE。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the effective VPP IPv4 forwarding table
- 合法语法：

  ```text
  display ip fib [vpn-instance VRF]
  ```

## `display ip interface brief`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 interface brief
- 合法语法：

  ```text
  display ip interface brief
  ```

## `display ip ip-prefix`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IP prefix lists
- 合法语法：

  ```text
  display ip ip-prefix [NAME [verbose|first-match PREFIX]]
  ```

## `display ip ipv6-prefix`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 prefix lists
- 合法语法：

  ```text
  display ip ipv6-prefix [NAME [verbose|first-match PREFIX]]
  ```

## `display ip pool`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display IPv4 address pools and server leases
- 合法语法：

  ```text
  display ip pool [name NAME | interface TYPE N] [all | used] [verbose]
  ```

## `display ip routing-table`

核对控制面选路。protocol static 只查询静态路由，指定目的地址可进一步缩小范围。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the IPv4 routing table
- 合法语法：

  ```text
  display ip routing-table [X.X.X.X [INTEGER<0-32> | X.X.X.X] [longer-match] | vpn-instance NAME | all-vpn-instance | protocol PROTO [inactive | verbose] | statistics | route-number | verbose | all-routes | limit N]
  ```

## `display ip routing-table-group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 static route group applications
- 合法语法：

  ```text
  display ip routing-table-group [name GROUP] [route PREFIX] [verbose]
  ```

## `display ip vpn-instance`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VPN-instance information
- 合法语法：

  ```text
  display ip vpn-instance [NAME | interface | verbose]
  ```

## `display ip vpn-instance interface`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display interfaces bound to VPN instances
- 合法语法：

  ```text
  display ip vpn-instance interface
  ```

## `display ip vpn-instance verbose`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display verbose VPN-instance information
- 合法语法：

  ```text
  display ip vpn-instance verbose
  ```

## `display ipv6 fib`

读取 VPP 中实际安装的 IPv6 转发项。每条 ECMP 路径显示一个信息块，可按 VPN 限定查询。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 FIB information
- 合法语法：

  ```text
  display ipv6 fib [vpn-instance VRF]
  ```

## `display ipv6 interface brief`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 interface brief
- 合法语法：

  ```text
  display ipv6 interface brief
  ```

## `display ipv6 nd`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 neighbor discovery information
- 合法语法：

  ```text
  display ipv6 nd
  ```

## `display ipv6 neighbors`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 neighbor information
- 合法语法：

  ```text
  display ipv6 neighbors [interface IF | vpn-instance VRF | static | dynamic]
  ```

## `display ipv6 pathmtu`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 path MTU information
- 合法语法：

  ```text
  display ipv6 pathmtu [vpn-instance VRF]
  ```

## `display ipv6 pool`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display IPv6 pool information and server leases
- 合法语法：

  ```text
  display ipv6 pool [name NAME] [all | used] [verbose]
  ```

## `display ipv6 prefix`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 prefix-list information
- 合法语法：

  ```text
  display ipv6 prefix [NAME [verbose|first-match PREFIX]]
  ```

## `display ipv6 route-static group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 static route groups
- 合法语法：

  ```text
  display ipv6 route-static group [name GROUP] [verbose]
  ```

## `display ipv6 routing-table`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the IPv6 routing table
- 合法语法：

  ```text
  display ipv6 routing-table [X:X::X:X [INTEGER<0-128> | X:X::X:X] [longer-match] | vpn-instance NAME | all-vpn-instance | protocol PROTO [inactive | verbose] | statistics | route-number | verbose | all-routes | limit N]
  ```

## `display ipv6 routing-table-group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 static route group applications
- 合法语法：

  ```text
  display ipv6 routing-table-group [name GROUP] [route PREFIX] [verbose]
  ```

## `display ipv6 urpf`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 URPF information
- 合法语法：

  ```text
  display ipv6 urpf
  ```

## `display route-static group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 static route groups
- 合法语法：

  ```text
  display route-static group [name GROUP] [verbose]
  ```

## `ip route-static`

指定目标前缀的下一跳、接口或黑洞。普通路径需要可解析的下一跳。见[静态路由案例](../../examples/static-route.md)。

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static IPv4 route
- 合法语法：

  ```text
  ip route-static [vpn-instance DEST-VPN] DEST MASK { NULL 0 | NH | TYPE N [NH] | vpn-instance NH-VRF [NH] } [preference PREF | tag TAG] * [description TEXT]
  ```

## `ip route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  ip route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

## `ipv4-family`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`
- 用途（设备帮助）：enter the IPv4 address-family view
- 合法语法：

  ```text
  ipv4-family
  ```

## `ipv6 nd max-number`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the IPv6 neighbor database capacity
- 合法语法：

  ```text
  ipv6 nd max-number INTEGER<1-4294967295>
  ```

## `ipv6 nd recycle`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure IPv6 neighbor recycling at capacity
- 合法语法：

  ```text
  ipv6 nd recycle { enable | disable }
  ```

## `ipv6 nd stale-timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the dynamic IPv6 neighbor stale aging time
- 合法语法：

  ```text
  ipv6 nd stale-timeout INTEGER<60-172800>
  ```

## `ipv6 neighbor`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static IPv6 neighbor
- 合法语法：

  ```text
  ipv6 neighbor IPV6 MAC interface IF
  ```

## `ipv6 route-static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static IPv6 route
- 合法语法：

  ```text
  ipv6 route-static [vpn-instance DEST-VPN] DEST PREFIXLEN { NULL 0 | NH | TYPE N [NH] | vpn-instance NH-VRF [NH] } [preference PREF | tag TAG] * [description TEXT]
  ```

## `ipv6 route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  ipv6 route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

## `ipv6-family`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`
- 用途（设备帮助）：enter the IPv6 address-family view
- 合法语法：

  ```text
  ipv6-family
  ```

## `route`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：add a route prefix
- 合法语法：

  ```text
  route PREFIX [MASK|PREFIXLEN]
  ```

## `route-distinguisher`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：configure the route distinguisher；set the EVPN route distinguisher
- 合法语法：

  ```text
  route-distinguisher RD
  ```

## `source file`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：use a CIDR-list file from /VortexROS/route-static-groupd
- 合法语法：

  ```text
  source file FILE
  ```

## `source url`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：set the remote CIDR-list source
- 合法语法：

  ```text
  source url URL [insecure] [vpn-instance NAME] [resolve-address IP]
  ```

## `undo auto-refresh enable`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：disable automatic remote-list refresh
- 合法语法：

  ```text
  undo auto-refresh enable
  ```

## `undo auto-refresh interval`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：restore the 4320-minute refresh interval
- 合法语法：

  ```text
  undo auto-refresh interval
  ```

## `undo ip ip-prefix`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an IP prefix list entry or list
- 合法语法：

  ```text
  undo ip ip-prefix NAME [index SEQ]
  ```

## `undo ip ipv6-prefix`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an IPv6 prefix list entry or list
- 合法语法：

  ```text
  undo ip ipv6-prefix NAME [index SEQ]
  ```

## `undo ip route-static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static IPv4 route
- 合法语法：

  ```text
  undo ip route-static [vpn-instance DEST-VPN] DEST MASK [NULL 0 | NH | TYPE N [NH] [vpn-instance NH-VRF] | vpn-instance NH-VRF [NH]]
  ```

## `undo ip route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  undo ip route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

## `undo ip vpn-instance`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a VPN instance
- 合法语法：

  ```text
  undo ip vpn-instance NAME
  ```

## `undo ipv4-family`

- 类别：配置命令
- 视图：`VPN实例视图`
- 用途（设备帮助）：delete the IPv4 address-family
- 合法语法：

  ```text
  undo ipv4-family
  ```

## `undo ipv6 nd max-number`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the VPP default IPv6 neighbor capacity
- 合法语法：

  ```text
  undo ipv6 nd max-number
  ```

## `undo ipv6 nd recycle`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the VPP default IPv6 neighbor recycle policy
- 合法语法：

  ```text
  undo ipv6 nd recycle
  ```

## `undo ipv6 nd stale-timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default IPv6 neighbor stale aging time
- 合法语法：

  ```text
  undo ipv6 nd stale-timeout
  ```

## `undo ipv6 neighbor`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static IPv6 neighbor
- 合法语法：

  ```text
  undo ipv6 neighbor IPV6 MAC interface IF
  ```

## `undo ipv6 route-static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static IPv6 route
- 合法语法：

  ```text
  undo ipv6 route-static [vpn-instance DEST-VPN] DEST PREFIXLEN [NULL 0 | NH | TYPE N [NH] [vpn-instance NH-VRF] | vpn-instance NH-VRF [NH]]
  ```

## `undo ipv6 route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  undo ipv6 route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

## `undo ipv6-family`

- 类别：配置命令
- 视图：`VPN实例视图`
- 用途（设备帮助）：delete the IPv6 address-family
- 合法语法：

  ```text
  undo ipv6-family
  ```

## `undo route`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：delete a route prefix
- 合法语法：

  ```text
  undo route PREFIX [MASK|PREFIXLEN]
  ```

## `undo route-distinguisher`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：clear the EVPN route distinguisher；delete the route distinguisher
- 合法语法：

  ```text
  undo route-distinguisher
  ```

## `undo source file`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：remove the local CIDR-list source
- 合法语法：

  ```text
  undo source file
  ```

## `undo source url`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：remove the remote CIDR-list source
- 合法语法：

  ```text
  undo source url
  ```

## `undo vpn-target`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：configure an EVPN route target；delete a VPN target
- 合法语法：

  ```text
  undo vpn-target RT [ export-extcommunity | import-extcommunity | both ]
  ```
  ```text
  undo vpn-target RT { export-extcommunity | import-extcommunity }
  ```

## `vpn-target`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：configure a VPN target；configure an EVPN route target
- 合法语法：

  ```text
  vpn-target RT { export-extcommunity | import-extcommunity | both }
  ```
  ```text
  vpn-target RT { export-extcommunity | import-extcommunity }
  ```
