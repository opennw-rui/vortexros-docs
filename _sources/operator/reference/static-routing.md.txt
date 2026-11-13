# 静态路由

[配置指南](../static-routing.md)

## `ip route-static`

指定目标前缀的下一跳、接口或黑洞。普通路径需要可解析的下一跳。见[静态路由案例](../../examples/static-route.md)。

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static IPv4 route
- 合法语法：

  ```text
  ip route-static [vpn-instance DEST-VPN] DEST MASK { NULL 0 | NH | TYPE N [NH] | vpn-instance NH-VRF [NH] } [preference PREF | tag TAG] * [description TEXT]
  ```

## `ipv6 route-static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static IPv6 route
- 合法语法：

  ```text
  ipv6 route-static [vpn-instance DEST-VPN] DEST PREFIXLEN { NULL 0 | NH | TYPE N [NH] | vpn-instance NH-VRF [NH] } [preference PREF | tag TAG] * [description TEXT]
  ```

## `undo ip route-static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static IPv4 route
- 合法语法：

  ```text
  undo ip route-static [vpn-instance DEST-VPN] DEST MASK [NULL 0 | NH | TYPE N [NH] [vpn-instance NH-VRF] | vpn-instance NH-VRF [NH]]
  ```

## `undo ipv6 route-static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static IPv6 route
- 合法语法：

  ```text
  undo ipv6 route-static [vpn-instance DEST-VPN] DEST PREFIXLEN [NULL 0 | NH | TYPE N [NH] [vpn-instance NH-VRF] | vpn-instance NH-VRF [NH]]
  ```
