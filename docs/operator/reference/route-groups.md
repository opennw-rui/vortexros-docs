# 静态路由组

[配置指南](../route-groups.md)

## `auto-refresh enable`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：enable automatic remote-list refresh
- 合法语法：

  ```text
  auto-refresh enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `auto-refresh interval`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：set the remote-list refresh interval
- 合法语法：

  ```text
  auto-refresh interval INTEGER<5-10080>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<5-10080>` | minutes | 输入值 |

## `display ip routing-table-group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 static route group applications
- 合法语法：

  ```text
  display ip routing-table-group [name GROUP] [route PREFIX] [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name ROUTE-GROUP4` | group name；IPv4 route-static group name | 可选、可组合 |
| 命令后 | `route PREFIX` | specific route；route prefix | 可选、可组合 |
| 命令后 | `verbose` | verbose output | 可选、可组合 |

## `display ipv6 route-static group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 static route groups
- 合法语法：

  ```text
  display ipv6 route-static group [name GROUP] [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | group name | 可选 |
| name | `ROUTE-GROUP6` | IPv6 route-static group name | 输入值 |
| ROUTE-GROUP6 / 命令后 | `verbose` | display all prefixes | 可选 |

## `display ipv6 routing-table-group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 static route group applications
- 合法语法：

  ```text
  display ipv6 routing-table-group [name GROUP] [route PREFIX] [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name ROUTE-GROUP6` | group name；IPv6 route-static group name | 可选、可组合 |
| 命令后 | `route PREFIX` | specific route；route prefix | 可选、可组合 |
| 命令后 | `verbose` | verbose output | 可选、可组合 |

## `display route-static group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 static route groups
- 合法语法：

  ```text
  display route-static group [name GROUP] [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | group name | 可选 |
| name | `ROUTE-GROUP4` | IPv4 route-static group name | 输入值 |
| ROUTE-GROUP4 / 命令后 | `verbose` | display all prefixes | 可选 |

## `ip route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  ip route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | destination VPN instance | 可选 |
| vpn-instance | `ROUTE-VRF` | VPN instance name | 输入值 |
| ROUTE-VRF / 命令后 | `ROUTE-GROUP4` | route-static group name | 输入值 |
| ROUTE-GROUP4 | `vpn-instance` | nexthop VPN instance | 关键字 |
| vpn-instance | `NH-VRF` | nexthop VPN | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH-VRF | `NH` | Next-hop IP address | 输入值、可选 |
| NH / NH-VRF / X.X.X.X | `vbdif` | Vbdif interface (service BD BVI) | 可选 |
| vbdif | `N` | bridge-domain ID | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `preference INTEGER<1-255>` | preference (default 60)；preference 1-255 | 可选、可组合 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `tag INTEGER<1-4294967295>` | tag；tag 1-4294967295 | 可选、可组合 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `description` | description (stored in vortexros only) | 可选、可组合 |
| description | `TEXT` | description | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `vpn-instance` | nexthop VPN instance | 可选、可组合 |
| NH / NH-VRF / X.X.X.X | `vlanif` | Vlanif interface (BVI) | 可选 |
| vlanif | `N` | VLAN ID | 输入值 |
| NH / NH-VRF / X.X.X.X | `eth` | Ethernet interface | 可选 |
| eth | `N` | interface number | 输入值 |
| NH / NH-VRF / X.X.X.X | `loopback` | LoopBack interface | 可选 |
| loopback | `INTEGER<0-255>` | LoopBack interface number 0-255 | 输入值 |
| NH / NH-VRF / X.X.X.X | `tunnel` | Tunnel interface | 可选 |
| tunnel | `INTEGER<0-4294967295>` | Tunnel interface number | 输入值 |
| NH / NH-VRF / X.X.X.X | `IFNAME` | outgoing interface | 输入值、可选 |
| ROUTE-GROUP4 | `X.X.X.X` | Next-hop IP address | 输入值 |
| ROUTE-GROUP4 | `vbdif` | Vbdif interface (service BD BVI) | 关键字 |
| ROUTE-GROUP4 | `vlanif` | Vlanif interface (BVI) | 关键字 |
| ROUTE-GROUP4 | `eth` | Ethernet interface | 关键字 |
| ROUTE-GROUP4 | `loopback` | LoopBack interface | 关键字 |
| ROUTE-GROUP4 | `tunnel` | Tunnel interface | 关键字 |
| ROUTE-GROUP4 | `IFNAME` | outgoing interface | 输入值 |

## `ipv6 route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter an IPv6 static route group
- 合法语法：

  ```text
  ipv6 route-static group name GROUP
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | route-static group name | 关键字 |
| name | `ROUTE-GROUP6` | IPv6 route-static group name | 输入值 |

## `ipv6 route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  ipv6 route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | destination VPN instance | 可选 |
| vpn-instance | `ROUTE-VRF` | VPN instance name | 输入值 |
| ROUTE-VRF / 命令后 | `ROUTE-GROUP6` | route-static group name | 输入值 |
| ROUTE-GROUP6 | `vpn-instance` | nexthop VPN instance | 关键字 |
| vpn-instance | `NH-VRF` | nexthop VPN | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH-VRF | `NH` | Next-hop IPv6 address | 输入值、可选 |
| NH / NH-VRF / X:X::X:X | `vbdif` | Vbdif interface (service BD BVI) | 可选 |
| vbdif | `N` | bridge-domain ID | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `preference INTEGER<1-255>` | preference (default 60)；preference 1-255 | 可选、可组合 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `tag INTEGER<1-4294967295>` | tag；tag 1-4294967295 | 可选、可组合 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `description` | description (stored in vortexros only) | 可选、可组合 |
| description | `TEXT` | description | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `vpn-instance` | nexthop VPN instance | 可选、可组合 |
| NH / NH-VRF / X:X::X:X | `vlanif` | Vlanif interface (BVI) | 可选 |
| vlanif | `N` | VLAN ID | 输入值 |
| NH / NH-VRF / X:X::X:X | `eth` | Ethernet interface | 可选 |
| eth | `N` | interface number | 输入值 |
| NH / NH-VRF / X:X::X:X | `loopback` | LoopBack interface | 可选 |
| loopback | `INTEGER<0-255>` | LoopBack interface number 0-255 | 输入值 |
| NH / NH-VRF / X:X::X:X | `tunnel` | Tunnel interface | 可选 |
| tunnel | `INTEGER<0-4294967295>` | Tunnel interface number | 输入值 |
| NH / NH-VRF / X:X::X:X | `IFNAME` | outgoing interface | 输入值、可选 |
| ROUTE-GROUP6 | `X:X::X:X` | Next-hop IPv6 address | 输入值 |
| ROUTE-GROUP6 | `vbdif` | Vbdif interface (service BD BVI) | 关键字 |
| ROUTE-GROUP6 | `vlanif` | Vlanif interface (BVI) | 关键字 |
| ROUTE-GROUP6 | `eth` | Ethernet interface | 关键字 |
| ROUTE-GROUP6 | `loopback` | LoopBack interface | 关键字 |
| ROUTE-GROUP6 | `tunnel` | Tunnel interface | 关键字 |
| ROUTE-GROUP6 | `IFNAME` | outgoing interface | 输入值 |

## `reset ipv6 route-static group`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reload an IPv6 route-static group external list
- 合法语法：

  ```text
  reset ipv6 route-static group {name GROUP|all}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | route-static group name | 可选、可组合 |
| name | `ROUTE-GROUP6` | IPv6 route-static group name | 输入值 |
| 命令后 | `all` | all IPv6 route-static groups | 可选、可组合 |

## `reset route-static group`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reload an IPv4 route-static group external list
- 合法语法：

  ```text
  reset route-static group {name GROUP|all}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | route-static group name | 可选、可组合 |
| name | `ROUTE-GROUP4` | IPv4 route-static group name | 输入值 |
| 命令后 | `all` | all IPv4 route-static groups | 可选、可组合 |

## `route`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：add a route prefix
- 合法语法：

  ```text
  route PREFIX [MASK|PREFIXLEN]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PREFIX` | IP prefix or host address | 输入值 |
| PREFIX | `MASK` | mask or prefix length | 输入值、可选 |

## `route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter an IPv4 static route group
- 合法语法：

  ```text
  route-static group name GROUP
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | route-static group name | 关键字 |
| name | `ROUTE-GROUP4` | IPv4 route-static group name | 输入值 |

## `source file`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：use a CIDR-list file from /VortexROS/route-static-groupd
- 合法语法：

  ```text
  source file FILE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ROUTE-FILE` | existing route-static group CIDR-list file | 输入值 |

## `source url`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：set the remote CIDR-list source
- 合法语法：

  ```text
  source url URL [insecure] [vpn-instance NAME] [resolve-address IP]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `URL` | HTTP or HTTPS CIDR-list URL | 输入值 |
| URL | `insecure` | allow an explicitly configured HTTP source | 可选、可组合 |
| URL | `vpn-instance` | VPN instance | 可选、可组合 |
| vpn-instance | `VPN` | VPN instance name | 输入值 |
| URL | `resolve-address` | bootstrap connection address | 可选、可组合 |
| resolve-address | `IP` | IPv4 or IPv6 address | 输入值 |

## `undo auto-refresh enable`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：disable automatic remote-list refresh
- 合法语法：

  ```text
  undo auto-refresh enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo auto-refresh interval`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：restore the 4320-minute refresh interval
- 合法语法：

  ```text
  undo auto-refresh interval
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ip route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  undo ip route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | destination VPN instance | 可选 |
| vpn-instance | `ROUTE-VRF` | VPN instance name | 输入值 |
| ROUTE-VRF / 命令后 | `ROUTE-GROUP4` | route-static group name | 输入值 |
| ROUTE-GROUP4 | `vpn-instance` | nexthop VPN instance | 关键字 |
| vpn-instance | `NH-VRF` | nexthop VPN | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH-VRF | `NH` | Next-hop IP address | 输入值、可选 |
| NH / NH-VRF / X.X.X.X | `vbdif` | Vbdif interface (service BD BVI) | 可选 |
| vbdif | `N` | bridge-domain ID | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `preference INTEGER<1-255>` | preference (default 60)；preference 1-255 | 可选、可组合 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `tag INTEGER<1-4294967295>` | tag；tag 1-4294967295 | 可选、可组合 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `description` | description (stored in vortexros only) | 可选、可组合 |
| description | `TEXT` | description | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `vpn-instance` | nexthop VPN instance | 可选、可组合 |
| NH / NH-VRF / X.X.X.X | `vlanif` | Vlanif interface (BVI) | 可选 |
| vlanif | `N` | VLAN ID | 输入值 |
| NH / NH-VRF / X.X.X.X | `eth` | Ethernet interface | 可选 |
| eth | `N` | interface number | 输入值 |
| NH / NH-VRF / X.X.X.X | `loopback` | LoopBack interface | 可选 |
| loopback | `INTEGER<0-255>` | LoopBack interface number 0-255 | 输入值 |
| NH / NH-VRF / X.X.X.X | `tunnel` | Tunnel interface | 可选 |
| tunnel | `INTEGER<0-4294967295>` | Tunnel interface number | 输入值 |
| NH / NH-VRF / X.X.X.X | `IFNAME` | outgoing interface | 输入值、可选 |
| ROUTE-GROUP4 | `X.X.X.X` | Next-hop IP address | 输入值 |
| ROUTE-GROUP4 | `vbdif` | Vbdif interface (service BD BVI) | 关键字 |
| ROUTE-GROUP4 | `vlanif` | Vlanif interface (BVI) | 关键字 |
| ROUTE-GROUP4 | `eth` | Ethernet interface | 关键字 |
| ROUTE-GROUP4 | `loopback` | LoopBack interface | 关键字 |
| ROUTE-GROUP4 | `tunnel` | Tunnel interface | 关键字 |
| ROUTE-GROUP4 | `IFNAME` | outgoing interface | 输入值 |

## `undo ipv6 route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete an IPv6 static route group
- 合法语法：

  ```text
  undo ipv6 route-static group name GROUP
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | route-static group name | 关键字 |
| name | `ROUTE-GROUP6` | IPv6 route-static group name | 输入值 |

## `undo ipv6 route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  undo ipv6 route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | destination VPN instance | 可选 |
| vpn-instance | `ROUTE-VRF` | VPN instance name | 输入值 |
| ROUTE-VRF / 命令后 | `ROUTE-GROUP6` | route-static group name | 输入值 |
| ROUTE-GROUP6 | `vpn-instance` | nexthop VPN instance | 关键字 |
| vpn-instance | `NH-VRF` | nexthop VPN | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH-VRF | `NH` | Next-hop IPv6 address | 输入值、可选 |
| NH / NH-VRF / X:X::X:X | `vbdif` | Vbdif interface (service BD BVI) | 可选 |
| vbdif | `N` | bridge-domain ID | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `preference INTEGER<1-255>` | preference (default 60)；preference 1-255 | 可选、可组合 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `tag INTEGER<1-4294967295>` | tag；tag 1-4294967295 | 可选、可组合 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `description` | description (stored in vortexros only) | 可选、可组合 |
| description | `TEXT` | description | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `vpn-instance` | nexthop VPN instance | 可选、可组合 |
| NH / NH-VRF / X:X::X:X | `vlanif` | Vlanif interface (BVI) | 可选 |
| vlanif | `N` | VLAN ID | 输入值 |
| NH / NH-VRF / X:X::X:X | `eth` | Ethernet interface | 可选 |
| eth | `N` | interface number | 输入值 |
| NH / NH-VRF / X:X::X:X | `loopback` | LoopBack interface | 可选 |
| loopback | `INTEGER<0-255>` | LoopBack interface number 0-255 | 输入值 |
| NH / NH-VRF / X:X::X:X | `tunnel` | Tunnel interface | 可选 |
| tunnel | `INTEGER<0-4294967295>` | Tunnel interface number | 输入值 |
| NH / NH-VRF / X:X::X:X | `IFNAME` | outgoing interface | 输入值、可选 |
| ROUTE-GROUP6 | `X:X::X:X` | Next-hop IPv6 address | 输入值 |
| ROUTE-GROUP6 | `vbdif` | Vbdif interface (service BD BVI) | 关键字 |
| ROUTE-GROUP6 | `vlanif` | Vlanif interface (BVI) | 关键字 |
| ROUTE-GROUP6 | `eth` | Ethernet interface | 关键字 |
| ROUTE-GROUP6 | `loopback` | LoopBack interface | 关键字 |
| ROUTE-GROUP6 | `tunnel` | Tunnel interface | 关键字 |
| ROUTE-GROUP6 | `IFNAME` | outgoing interface | 输入值 |

## `undo route`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：delete a route prefix
- 合法语法：

  ```text
  undo route PREFIX [MASK|PREFIXLEN]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PREFIX` | IP prefix or host address | 输入值 |
| PREFIX | `MASK` | mask or prefix length | 输入值、可选 |

## `undo route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete an IPv4 static route group
- 合法语法：

  ```text
  undo route-static group name GROUP
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | route-static group name | 关键字 |
| name | `ROUTE-GROUP4` | IPv4 route-static group name | 输入值 |

## `undo source file`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：remove the local CIDR-list source
- 合法语法：

  ```text
  undo source file
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo source url`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：remove the remote CIDR-list source
- 合法语法：

  ```text
  undo source url
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
