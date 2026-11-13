# BGP

[配置指南](../bgp.md)

共用命令：[`import-route`](dynamic-routing.md#cmd-import-route)、[`network`](dynamic-routing.md#cmd-network)、[`router-id`](dynamic-routing.md#cmd-router-id)、[`peer`](tunnels.md#cmd-peer)。

## `bgp`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a BGP instance and enter BGP view
- 合法语法：

  ```text
  bgp ASNUM
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

## `group`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`
- 用途（设备帮助）：create a case-sensitive BGP peer-group
- 合法语法：

  ```text
  group NAME [internal|external]
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

## `load-balancing as-path-ignore`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：allow equal-length different AS paths in BGP ECMP
- 合法语法：

  ```text
  load-balancing as-path-ignore
  ```

## `maximum-paths`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：set the maximum OSPF ECMP paths
- 合法语法：

  ```text
  maximum-paths INTEGER<1-256>
  ```

## `policy vpn-target`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：control VPN route-target filtering
- 合法语法：

  ```text
  policy vpn-target
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

## `reset service bgp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed bgp routing service
- 合法语法：

  ```text
  reset service bgp
  ```

## `timer keepalive`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set BGP keepalive and hold timers
- 合法语法：

  ```text
  timer keepalive INTEGER<0-21845> hold INTEGER<0-65535>
  ```

## `undo bgp`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a BGP instance
- 合法语法：

  ```text
  undo bgp ASNUM
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

## `undo group`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`
- 用途（设备帮助）：delete an unused BGP peer-group
- 合法语法：

  ```text
  undo group NAME
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

## `undo load-balancing as-path-ignore`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：require identical AS paths for BGP ECMP
- 合法语法：

  ```text
  undo load-balancing as-path-ignore
  ```

## `undo maximum-paths`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：restore the default OSPF ECMP path count
- 合法语法：

  ```text
  undo maximum-paths
  ```

## `undo policy vpn-target`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：control VPN route-target filtering
- 合法语法：

  ```text
  undo policy vpn-target
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

## `undo timer keepalive`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore BGP keepalive and hold timers
- 合法语法：

  ```text
  undo timer keepalive
  ```
