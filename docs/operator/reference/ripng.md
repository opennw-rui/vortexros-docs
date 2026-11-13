# RIPng

[配置指南](../ripng.md)

共用命令：[`network`](dynamic-routing.md#cmd-network)、[`import-route`](dynamic-routing.md#cmd-import-route)。

## `aggregate-address`

- 类别：配置命令
- 视图：`RIPng视图`
- 用途（设备帮助）：advertise a RIPng aggregate
- 合法语法：

  ```text
  aggregate-address X:X::X/M
  ```

## `display ripng`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display RIPng information
- 合法语法：

  ```text
  display ripng [process-id] [database|route|interface|statistics]
  ```

## `offset-list`

- 类别：配置命令
- 视图：`RIPng视图`
- 用途（设备帮助）：adjust RIPng route metrics selected by an IPv6 ACL
- 合法语法：

  ```text
  offset-list ACL {in|out} INTEGER<0-16> [interface IF]
  ```

## `ripng`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a RIP process and enter process view
- 合法语法：

  ```text
  ripng INTEGER<1-65535> [vpn-instance NAME]
  ```

## `undo aggregate-address`

- 类别：配置命令
- 视图：`RIPng视图`
- 用途（设备帮助）：withdraw a RIPng aggregate
- 合法语法：

  ```text
  undo aggregate-address X:X::X/M
  ```

## `undo offset-list`

- 类别：配置命令
- 视图：`RIPng视图`
- 用途（设备帮助）：remove a RIPng metric offset
- 合法语法：

  ```text
  undo offset-list {in|out} [interface IF]
  ```

## `undo ripng`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a RIP process
- 合法语法：

  ```text
  undo ripng INTEGER<1-65535> [vpn-instance NAME]
  ```
