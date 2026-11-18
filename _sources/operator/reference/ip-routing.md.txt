# 路由表与 FIB

[配置指南](../routing-tables.md)

## `display ip fib`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the effective VPP IPv4 forwarding table
- 合法语法：

  ```text
  display ip fib [vpn-instance VRF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | VPN instance name | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |

## `display ip interface brief`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv4 interface brief
- 合法语法：

  ```text
  display ip interface brief
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display ip routing-table`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the IPv4 routing table
- 合法语法：

  ```text
  display ip routing-table [vpn-instance NAME | all-vpn-instance] [X.X.X.X [INTEGER<0-32> | X.X.X.X] [longer-match]] [protocol PROTO [inactive]] [statistics | route-number | verbose | all-routes] [limit N]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| DISPLAY-VRF / 命令后 | `X.X.X.X` | Destination IP address | 输入值、可选 |
| X.X.X.X | `INTEGER<0-32>` | Length of the IP address mask | 输入值、可选 |
| INTEGER<0-32> / X.X.X.X | `longer-match` | Display routes equal to or more specific than the specified network/mask | 可选 |
| DISPLAY-VRF / INTEGER<0-32> / X.X.X.X / bgp / direct / isis / kernel / ospf / rip / static / 命令后 | `verbose` | Verbose information of the routing table | 可选 |
| X.X.X.X | `X.X.X.X` | IP address mask | 输入值、可选 |
| DISPLAY-VRF / 命令后 | `all-routes` | All routes | 可选 |
| 命令后 | `all-vpn-instance` | All VPN instances | 可选 |
| DISPLAY-VRF / 命令后 | `limit` | Route limit or prefix limit | 可选 |
| limit | `INTEGER<1-4294967295>` | maximum routes to display | 输入值 |
| DISPLAY-VRF / 命令后 | `protocol` | Specify a routing protocol | 可选 |
| protocol | `bgp` | Border Gateway Protocol (BGP) routes | 关键字 |
| bgp / direct / isis / kernel / ospf / rip / static | `inactive` | Display inactive routes | 可选 |
| protocol | `direct` | Direct routes | 关键字 |
| protocol | `isis` | IS-IS routing protocol defined by ISO | 关键字 |
| protocol | `kernel` | Kernel routes | 关键字 |
| protocol | `ospf` | Open Shortest Path First (OSPF) routes | 关键字 |
| protocol | `rip` | Routing Information Protocol (RIP) routes | 关键字 |
| protocol | `static` | Static routes | 关键字 |
| DISPLAY-VRF / 命令后 | `route-number` | Actual total route number | 可选 |
| DISPLAY-VRF / 命令后 | `statistics` | Summary statistics of all routes | 可选 |
| 命令后 | `vpn-instance` | VPN instance route information | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |

## `display ipv6 fib`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 FIB information
- 合法语法：

  ```text
  display ipv6 fib [vpn-instance VRF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | VPN instance name | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |

## `display ipv6 interface brief`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 interface brief
- 合法语法：

  ```text
  display ipv6 interface brief
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display ipv6 pathmtu`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 path MTU information
- 合法语法：

  ```text
  display ipv6 pathmtu [vpn-instance VRF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | VPN instance name | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |

## `display ipv6 routing-table`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the IPv6 routing table
- 合法语法：

  ```text
  display ipv6 routing-table [vpn-instance NAME | all-vpn-instance] [X:X::X:X [INTEGER<0-128> | X:X::X:X] [longer-match]] [protocol PROTO [inactive]] [statistics | route-number | verbose | all-routes] [limit N]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| DISPLAY-VRF / 命令后 | `X:X::X:X` | Destination IPv6 address | 输入值、可选 |
| X:X::X:X | `INTEGER<0-128>` | Length of the IP address mask | 输入值、可选 |
| INTEGER<0-128> / X:X::X:X | `longer-match` | Display routes equal to or more specific than the specified network/mask | 可选 |
| DISPLAY-VRF / INTEGER<0-128> / X:X::X:X / bgp / direct / isis / kernel / ospfv3 / ripng / static / 命令后 | `verbose` | Verbose information of the routing table | 可选 |
| X:X::X:X | `X:X::X:X` | IPv6 address mask | 输入值、可选 |
| DISPLAY-VRF / 命令后 | `all-routes` | All routes | 可选 |
| 命令后 | `all-vpn-instance` | All VPN instances | 可选 |
| DISPLAY-VRF / 命令后 | `limit` | Route limit or prefix limit | 可选 |
| limit | `INTEGER<1-4294967295>` | maximum routes to display | 输入值 |
| DISPLAY-VRF / 命令后 | `protocol` | Specify a routing protocol | 可选 |
| protocol | `bgp` | Border Gateway Protocol (BGP) routes | 关键字 |
| bgp / direct / isis / kernel / ospfv3 / ripng / static | `inactive` | Display inactive routes | 可选 |
| protocol | `direct` | Direct routes | 关键字 |
| protocol | `isis` | IS-IS routing protocol defined by ISO | 关键字 |
| protocol | `kernel` | Kernel routes | 关键字 |
| protocol | `ospfv3` | Open Shortest Path First version 3 (OSPFv3) routes | 关键字 |
| protocol | `ripng` | Routing Information Protocol next generation (RIPng) routes | 关键字 |
| protocol | `static` | Static routes | 关键字 |
| DISPLAY-VRF / 命令后 | `route-number` | Actual total route number | 可选 |
| DISPLAY-VRF / 命令后 | `statistics` | Summary statistics of all routes | 可选 |
| 命令后 | `vpn-instance` | VPN instance route information | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |
