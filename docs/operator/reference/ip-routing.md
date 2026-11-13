# 路由表与 FIB

[配置指南](../routing-tables.md)

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

## `display ip routing-table`

核对控制面选路。protocol static 只查询静态路由，指定目的地址可进一步缩小范围。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the IPv4 routing table
- 合法语法：

  ```text
  display ip routing-table [X.X.X.X [INTEGER<0-32> | X.X.X.X] [longer-match] | vpn-instance NAME | all-vpn-instance | protocol PROTO [inactive | verbose] | statistics | route-number | verbose | all-routes | limit N]
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

## `display ipv6 pathmtu`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 path MTU information
- 合法语法：

  ```text
  display ipv6 pathmtu [vpn-instance VRF]
  ```

## `display ipv6 routing-table`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the IPv6 routing table
- 合法语法：

  ```text
  display ipv6 routing-table [X:X::X:X [INTEGER<0-128> | X:X::X:X] [longer-match] | vpn-instance NAME | all-vpn-instance | protocol PROTO [inactive | verbose] | statistics | route-number | verbose | all-routes | limit N]
  ```
