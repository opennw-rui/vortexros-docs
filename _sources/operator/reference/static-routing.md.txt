# 静态路由

[配置指南](../static-routing.md)

## `ip route-static`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure a static IPv4 route
- 合法语法：

  ```text
  ip route-static [vpn-instance DEST-VPN] DEST MASK { NULL 0 | NH | TYPE N [NH] | vpn-instance NH-VRF [NH] } [preference PREF | tag TAG] * [description TEXT]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | destination VPN instance | 可选 |
| vpn-instance | `ROUTE-VRF` | VPN instance name | 输入值 |
| ROUTE-VRF / 命令后 | `X.X.X.X` | Destination IP address | 输入值 |
| X.X.X.X | `MASK` | mask or prefix length | 输入值 |
| MASK | `NULL` | discard route | 关键字 |
| NULL | `0` | NULL interface number | 关键字 |
| 0 / IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `preference INTEGER<1-255>` | preference (default 60)；preference 1-255 | 可选、可组合 |
| 0 / IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `tag INTEGER<1-4294967295>` | tag；tag 1-4294967295 | 可选、可组合 |
| 0 / IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X.X.X.X | `description` | description (stored in vortexros only) | 可选、可组合 |
| description | `TEXT` | description | 输入值 |
| MASK | `vpn-instance` | nexthop VPN instance | 关键字 |
| vpn-instance | `NH-VRF` | nexthop VPN | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH-VRF | `NH` | Next-hop IP address | 输入值、可选 |
| NH / NH-VRF / X.X.X.X | `vbdif` | Vbdif interface (service BD BVI) | 可选 |
| vbdif | `N` | bridge-domain ID | 输入值 |
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
| MASK | `X.X.X.X` | Next-hop IP address | 输入值 |
| MASK | `vbdif` | Vbdif interface (service BD BVI) | 关键字 |
| MASK | `vlanif` | Vlanif interface (BVI) | 关键字 |
| MASK | `eth` | Ethernet interface | 关键字 |
| MASK | `loopback` | LoopBack interface | 关键字 |
| MASK | `tunnel` | Tunnel interface | 关键字 |
| MASK | `IFNAME` | outgoing interface | 输入值 |

## `ipv6 route-static`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure a static IPv6 route
- 合法语法：

  ```text
  ipv6 route-static [vpn-instance DEST-VPN] DEST PREFIXLEN { NULL 0 | NH | TYPE N [NH] | vpn-instance NH-VRF [NH] } [preference PREF | tag TAG] * [description TEXT]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | destination VPN instance | 可选 |
| vpn-instance | `ROUTE-VRF` | VPN instance name | 输入值 |
| ROUTE-VRF / 命令后 | `X:X::X:X` | Destination IPv6 address | 输入值 |
| X:X::X:X | `PREFIXLEN` | prefix length | 输入值 |
| PREFIXLEN | `NULL` | discard route | 关键字 |
| NULL | `0` | NULL interface number | 关键字 |
| 0 / IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `preference INTEGER<1-255>` | preference (default 60)；preference 1-255 | 可选、可组合 |
| 0 / IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `tag INTEGER<1-4294967295>` | tag；tag 1-4294967295 | 可选、可组合 |
| 0 / IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / NH-VRF / X:X::X:X | `description` | description (stored in vortexros only) | 可选、可组合 |
| description | `TEXT` | description | 输入值 |
| PREFIXLEN | `vpn-instance` | nexthop VPN instance | 关键字 |
| vpn-instance | `NH-VRF` | nexthop VPN | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH-VRF | `NH` | Next-hop IPv6 address | 输入值、可选 |
| NH / NH-VRF / X:X::X:X | `vbdif` | Vbdif interface (service BD BVI) | 可选 |
| vbdif | `N` | bridge-domain ID | 输入值 |
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
| PREFIXLEN | `X:X::X:X` | Next-hop IPv6 address | 输入值 |
| PREFIXLEN | `vbdif` | Vbdif interface (service BD BVI) | 关键字 |
| PREFIXLEN | `vlanif` | Vlanif interface (BVI) | 关键字 |
| PREFIXLEN | `eth` | Ethernet interface | 关键字 |
| PREFIXLEN | `loopback` | LoopBack interface | 关键字 |
| PREFIXLEN | `tunnel` | Tunnel interface | 关键字 |
| PREFIXLEN | `IFNAME` | outgoing interface | 输入值 |

## `undo ip route-static`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a static IPv4 route
- 合法语法：

  ```text
  undo ip route-static [vpn-instance DEST-VPN] DEST MASK [NULL 0 | NH | TYPE N [NH] [vpn-instance NH-VRF] | vpn-instance NH-VRF [NH]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | destination VPN instance | 可选 |
| vpn-instance | `ROUTE-VRF` | VPN instance name | 输入值 |
| ROUTE-VRF / 命令后 | `X.X.X.X` | destination | 输入值 |
| X.X.X.X | `MASK` | mask | 输入值 |
| MASK | `NULL` | discard route | 可选 |
| NULL | `0` | NULL interface number | 关键字 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / MASK / N / NH / X.X.X.X | `vpn-instance` | nexthop VPN instance | 可选 |
| vpn-instance | `NH-VRF` | nexthop VPN | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH-VRF | `NH` | next-hop IP | 输入值、可选 |
| MASK / NH / X.X.X.X | `vbdif` | Vbdif interface (service BD BVI) | 可选 |
| vbdif | `N` | bridge-domain ID | 输入值 |
| MASK / NH / X.X.X.X | `vlanif` | Vlanif interface (BVI) | 可选 |
| vlanif | `N` | VLAN ID | 输入值 |
| MASK / NH / X.X.X.X | `eth` | Ethernet interface | 可选 |
| eth | `N` | interface number | 输入值 |
| MASK / NH / X.X.X.X | `loopback` | LoopBack interface | 可选 |
| loopback | `INTEGER<0-255>` | LoopBack interface number 0-255 | 输入值 |
| MASK / NH / X.X.X.X | `tunnel` | Tunnel interface | 可选 |
| tunnel | `INTEGER<0-4294967295>` | Tunnel interface number | 输入值 |
| MASK / NH / X.X.X.X | `IFNAME` | outgoing interface | 输入值、可选 |
| MASK | `X.X.X.X` | next-hop IP | 输入值、可选 |

## `undo ipv6 route-static`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a static IPv6 route
- 合法语法：

  ```text
  undo ipv6 route-static [vpn-instance DEST-VPN] DEST PREFIXLEN [NULL 0 | NH | TYPE N [NH] [vpn-instance NH-VRF] | vpn-instance NH-VRF [NH]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | destination VPN instance | 可选 |
| vpn-instance | `ROUTE-VRF` | VPN instance name | 输入值 |
| ROUTE-VRF / 命令后 | `X:X::X:X` | destination | 输入值 |
| X:X::X:X | `PREFIXLEN` | prefix length | 输入值 |
| PREFIXLEN | `NULL` | discard route | 可选 |
| NULL | `0` | NULL interface number | 关键字 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH / PREFIXLEN / X:X::X:X | `vpn-instance` | nexthop VPN instance | 可选 |
| vpn-instance | `NH-VRF` | nexthop VPN | 输入值 |
| IFNAME / INTEGER<0-255> / INTEGER<0-4294967295> / N / NH-VRF | `NH` | next-hop IPv6 | 输入值、可选 |
| NH / PREFIXLEN / X:X::X:X | `vbdif` | Vbdif interface (service BD BVI) | 可选 |
| vbdif | `N` | bridge-domain ID | 输入值 |
| NH / PREFIXLEN / X:X::X:X | `vlanif` | Vlanif interface (BVI) | 可选 |
| vlanif | `N` | VLAN ID | 输入值 |
| NH / PREFIXLEN / X:X::X:X | `eth` | Ethernet interface | 可选 |
| eth | `N` | interface number | 输入值 |
| NH / PREFIXLEN / X:X::X:X | `loopback` | LoopBack interface | 可选 |
| loopback | `INTEGER<0-255>` | LoopBack interface number 0-255 | 输入值 |
| NH / PREFIXLEN / X:X::X:X | `tunnel` | Tunnel interface | 可选 |
| tunnel | `INTEGER<0-4294967295>` | Tunnel interface number | 输入值 |
| NH / PREFIXLEN / X:X::X:X | `IFNAME` | outgoing interface | 输入值、可选 |
| PREFIXLEN | `X:X::X:X` | next-hop IPv6 | 输入值、可选 |
