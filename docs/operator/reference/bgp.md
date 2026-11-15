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

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4294967295>` | AS number in asplain format (number<1-4294967295>) | 输入值 |
| 命令后 | `STRING<3-11>` | AS number in asdot format (number<1-65535>.number<0-65535>) | 输入值 |

## `default ipv4-unicast`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：activate IPv4 unicast by default
- 合法语法：

  ```text
  default ipv4-unicast
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `default tcp-protected`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：protect the BGP TCP listener with configured peers
- 合法语法：

  ```text
  default tcp-protected
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `display bgp`

peer 查询会话，routing-table 查询前缀，vpnv4 和 vpnv6 切换地址族。见[BGP 案例](../../examples/bgp.md)。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display BGP information
- 合法语法：

  ```text
  display bgp {peer|routing-table|ipv6|vpnv4|vpnv6|...}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `bfd` | Bidirectional forwarding detection | 关键字 |
| 命令后 | `evpn` | EVPN address family | 关键字 |
| evpn | `all` | All EVPN instances | 关键字 |
| all | `routing-table` | EVPN routing table | 关键字 |
| routing-table | `mac-route` | MAC advertisement routes | 可选 |
| routing-table | `inclusive-route` | Inclusive multicast routes | 可选 |
| 命令后 | `group` | Peer groups | 关键字 |
| 命令后 | `ipv6` | IPv6 unicast address family | 关键字 |
| DISPLAY-VRF / all / ipv6 | `peer` | A BGP neighbor | 可选 |
| peer | `X.X.X.X` | Neighbor address | 输入值、可选 |
| X.X.X.X / X:X::X | `log-info` | Log information | 关键字 |
| X.X.X.X / X:X::X | `orf` | Outbound route filter capability | 关键字 |
| orf | `ip-prefix` | Outbound route filter based on IP prefix | 关键字 |
| X.X.X.X / X:X::X | `verbose` | Verbose information | 关键字 |
| peer | `X:X::X` | IPv6 neighbor address | 输入值、可选 |
| peer | `verbose` | Verbose information | 可选 |
| DISPLAY-VRF / all / ipv6 | `routing-table` | BGP routing table | 可选 |
| routing-table | `peer` | Peer routes | 可选 |
| peer | `X.X.X.X` | IPv4 peer address | 输入值 |
| X.X.X.X / X:X::X | `accepted-routes` | Routes accepted by routing policy | 关键字 |
| X.X.X.X / X:X::X | `advertised-routes` | Routes advertised to the remote peer | 关键字 |
| X.X.X.X / X:X::X | `received-routes` | Routes received from the remote peer | 关键字 |
| peer | `X:X::X` | IPv6 peer address | 输入值 |
| routing-table | `X:X::X` | Specify an IPv6 network address | 输入值、可选 |
| X:X::X | `INTEGER<0-128>` | IPv6 prefix length | 输入值、可选 |
| routing-table | `cidr` | Classless inter-domain routes | 可选 |
| routing-table | `statistics` | Route statistics | 可选 |
| 命令后 | `network` | Routes advertised through network command | 关键字 |
| 命令后 | `paths` | Path attribute information | 关键字 |
| 命令后 | `peer` | A BGP neighbor | 关键字 |
| 命令后 | `routing-table` | BGP routing table | 关键字 |
| routing-table | `X.X.X.X` | Specify an IPv4 network address | 输入值、可选 |
| X.X.X.X | `INTEGER<0-32>` | Length of IP address mask | 输入值、可选 |
| X.X.X.X | `X.X.X.X` | IPv4 network mask | 输入值、可选 |
| 命令后 | `update-peer-group` | Update peer group | 关键字 |
| update-peer-group | `statistics` | Update group counters | 可选 |
| 命令后 | `vpnv4` | VPNv4 address family | 关键字 |
| vpnv4 / vpnv6 | `all` | All VPN routes | 可选 |
| vpnv4 / vpnv6 | `vpn-instance` | Specify a VPN instance | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |
| 命令后 | `vpnv6` | VPNv6 address family | 关键字 |

## `display bgp tcp-protection`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display BGP TCP listener source protection
- 合法语法：

  ```text
  display bgp tcp-protection [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | include kernel ownership details | 可选 |

## `group`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`
- 用途（设备帮助）：create a case-sensitive BGP peer-group
- 合法语法：

  ```text
  group NAME [internal|external]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `BGP-GROUP` | Case-sensitive peer-group name | 输入值 |
| BGP-GROUP | `internal` | Create an internal peer-group | 可选 |
| BGP-GROUP | `external` | Create an external peer-group | 可选 |

## `ipv4-family unicast`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the IPv4 unicast address family
- 合法语法：

  ```text
  ipv4-family unicast
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `ipv4-family vpn-instance`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the IPv4 VPN address family
- 合法语法：

  ```text
  ipv4-family vpn-instance VPN
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VPN` | VPN instance name | 输入值 |

## `ipv4-family vpnv4`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the VPNv4 address family
- 合法语法：

  ```text
  ipv4-family vpnv4
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `ipv6-family unicast`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the IPv6 unicast address family
- 合法语法：

  ```text
  ipv6-family unicast
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `ipv6-family vpn-instance`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the IPv6 VPN address family
- 合法语法：

  ```text
  ipv6-family vpn-instance VPN
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VPN` | VPN instance name | 输入值 |

## `ipv6-family vpnv6`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the VPNv6 address family
- 合法语法：

  ```text
  ipv6-family vpnv6
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `load-balancing as-path-ignore`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：allow equal-length different AS paths in BGP ECMP
- 合法语法：

  ```text
  load-balancing as-path-ignore
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `maximum-paths`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：set the maximum OSPF ECMP paths
- 合法语法：

  ```text
  maximum-paths INTEGER<1-256>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-256>` | Number of paths | 输入值 |

## `policy vpn-target`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：control VPN route-target filtering
- 合法语法：

  ```text
  policy vpn-target
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `reflect between-clients`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：allow route reflection between clients
- 合法语法：

  ```text
  reflect between-clients
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `reflector cluster-id`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set the route-reflector cluster ID
- 合法语法：

  ```text
  reflector cluster-id X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | cluster ID | 输入值 |

## `reset service bgp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed bgp routing service
- 合法语法：

  ```text
  reset service bgp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `timer keepalive`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set BGP keepalive and hold timers
- 合法语法：

  ```text
  timer keepalive INTEGER<0-21845> hold INTEGER<0-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-21845>` | seconds | 输入值 |
| INTEGER<0-21845> | `hold` | hold time | 关键字 |
| hold | `INTEGER<0-65535>` | seconds | 输入值 |

## `undo bgp`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a BGP instance
- 合法语法：

  ```text
  undo bgp ASNUM
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4294967295>` | AS number in asplain format (number<1-4294967295>) | 输入值 |
| 命令后 | `STRING<3-11>` | AS number in asdot format (number<1-65535>.number<0-65535>) | 输入值 |

## `undo default ipv4-unicast`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`
- 用途（设备帮助）：disable automatic IPv4-unicast peer activation
- 合法语法：

  ```text
  undo default ipv4-unicast
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo default tcp-protected`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：disable BGP TCP listener peer protection
- 合法语法：

  ```text
  undo default tcp-protected
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo group`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`
- 用途（设备帮助）：delete an unused BGP peer-group
- 合法语法：

  ```text
  undo group NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `BGP-GROUP` | Case-sensitive peer-group name | 输入值 |

## `undo ipv4-family vpn-instance`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove an IPv4 VPN address family
- 合法语法：

  ```text
  undo ipv4-family vpn-instance VPN
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VPN` | VPN instance name | 输入值 |

## `undo ipv4-family vpnv4`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove the VPNv4 address family
- 合法语法：

  ```text
  undo ipv4-family vpnv4
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6-family unicast`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove the IPv6 unicast address family
- 合法语法：

  ```text
  undo ipv6-family unicast
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6-family vpn-instance`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove an IPv6 VPN address family
- 合法语法：

  ```text
  undo ipv6-family vpn-instance VPN
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VPN` | VPN instance name | 输入值 |

## `undo ipv6-family vpnv6`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove the VPNv6 address family
- 合法语法：

  ```text
  undo ipv6-family vpnv6
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo load-balancing as-path-ignore`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：require identical AS paths for BGP ECMP
- 合法语法：

  ```text
  undo load-balancing as-path-ignore
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo maximum-paths`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：restore the default OSPF ECMP path count
- 合法语法：

  ```text
  undo maximum-paths
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo policy vpn-target`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：control VPN route-target filtering
- 合法语法：

  ```text
  undo policy vpn-target
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo reflect between-clients`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：disable route reflection between clients
- 合法语法：

  ```text
  undo reflect between-clients
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo reflector cluster-id`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore the router ID as the cluster ID
- 合法语法：

  ```text
  undo reflector cluster-id
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo timer keepalive`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore BGP keepalive and hold timers
- 合法语法：

  ```text
  undo timer keepalive
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
