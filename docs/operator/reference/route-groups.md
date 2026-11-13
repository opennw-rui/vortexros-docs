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

## `auto-refresh interval`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：set the remote-list refresh interval
- 合法语法：

  ```text
  auto-refresh interval INTEGER<5-10080>
  ```

## `display ip routing-table-group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 static route group applications
- 合法语法：

  ```text
  display ip routing-table-group [name GROUP] [route PREFIX] [verbose]
  ```

## `display ipv6 route-static group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 static route groups
- 合法语法：

  ```text
  display ipv6 route-static group [name GROUP] [verbose]
  ```

## `display ipv6 routing-table-group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 static route group applications
- 合法语法：

  ```text
  display ipv6 routing-table-group [name GROUP] [route PREFIX] [verbose]
  ```

## `display route-static group`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 static route groups
- 合法语法：

  ```text
  display route-static group [name GROUP] [verbose]
  ```

## `ip route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  ip route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

## `ipv6 route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter an IPv6 static route group
- 合法语法：

  ```text
  ipv6 route-static group name GROUP
  ```

## `ipv6 route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  ipv6 route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

## `reset ipv6 route-static group`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reload an IPv6 route-static group external list
- 合法语法：

  ```text
  reset ipv6 route-static group {name GROUP|all}
  ```

## `reset route-static group`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reload an IPv4 route-static group external list
- 合法语法：

  ```text
  reset route-static group {name GROUP|all}
  ```

## `route`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：add a route prefix
- 合法语法：

  ```text
  route PREFIX [MASK|PREFIXLEN]
  ```

## `route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter an IPv4 static route group
- 合法语法：

  ```text
  route-static group name GROUP
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

## `undo ip route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  undo ip route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

## `undo ipv6 route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete an IPv6 static route group
- 合法语法：

  ```text
  undo ipv6 route-static group name GROUP
  ```

## `undo ipv6 route-static-group`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：apply a static route group
- 合法语法：

  ```text
  undo ipv6 route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

## `undo route`

- 类别：配置命令
- 视图：`静态路由组视图`
- 用途（设备帮助）：delete a route prefix
- 合法语法：

  ```text
  undo route PREFIX [MASK|PREFIXLEN]
  ```

## `undo route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete an IPv4 static route group
- 合法语法：

  ```text
  undo route-static group name GROUP
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
