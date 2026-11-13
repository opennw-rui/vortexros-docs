# VPN 实例

[配置指南](../vrf.md)

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

## `ip binding vpn-instance`

把接口划入指定 VPN 的路由域。调整前规划该实例的地址、网关和路由，调整后从同一 VPN 验证连通性。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind the interface to a VPN instance
- 合法语法：

  ```text
  ip binding vpn-instance NAME
  ```

## `ip vpn-instance`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a VPN instance and enter its view
- 合法语法：

  ```text
  ip vpn-instance NAME
  ```

## `ipv4-family`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`
- 用途（设备帮助）：enter the IPv4 address-family view
- 合法语法：

  ```text
  ipv4-family
  ```

## `ipv6-family`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`
- 用途（设备帮助）：enter the IPv6 address-family view
- 合法语法：

  ```text
  ipv6-family
  ```

## `route-distinguisher`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：configure the route distinguisher；set the EVPN route distinguisher
- 合法语法：

  ```text
  route-distinguisher RD
  ```

## `undo ip binding vpn-instance`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind the interface from a VPN instance
- 合法语法：

  ```text
  undo ip binding vpn-instance
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

## `undo ipv6-family`

- 类别：配置命令
- 视图：`VPN实例视图`
- 用途（设备帮助）：delete the IPv6 address-family
- 合法语法：

  ```text
  undo ipv6-family
  ```

## `undo route-distinguisher`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：clear the EVPN route distinguisher；delete the route distinguisher
- 合法语法：

  ```text
  undo route-distinguisher
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
