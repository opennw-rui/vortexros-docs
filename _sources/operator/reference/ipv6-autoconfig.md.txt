# RA 与 SLAAC

[配置指南](../ipv6-autoconfig.md)

## `ipv6 address auto global default`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：derive global IPv6 addresses and the default route from router advertisements
- 合法语法：

  ```text
  ipv6 address auto global default
  ```

## `ipv6 address auto slaac`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：derive IPv6 addresses from router advertisements
- 合法语法：

  ```text
  ipv6 address auto slaac
  ```

## `ipv6 nd ra default-route enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：install default routes learned from router advertisements
- 合法语法：

  ```text
  ipv6 nd ra default-route enable
  ```

## `undo ipv6 address auto global default`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable automatic global IPv6 addresses and RA default routes
- 合法语法：

  ```text
  undo ipv6 address auto global default
  ```

## `undo ipv6 address auto slaac`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable derive IPv6 addresses from router advertisements
- 合法语法：

  ```text
  undo ipv6 address auto slaac
  ```

## `undo ipv6 nd ra default-route enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable install default routes learned from router advertisements
- 合法语法：

  ```text
  undo ipv6 nd ra default-route enable
  ```
