# 链路聚合

[配置指南](../link-aggregation.md)

共用命令：[`mode`](interfaces.md#cmd-mode)。

## `display eth-trunk`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display aggregate interface state
- 合法语法：

  ```text
  display eth-trunk [INTEGER<0-63>]
  ```

## `eth-trunk`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：join an aggregate interface
- 合法语法：

  ```text
  eth-trunk INTEGER<0-63>
  ```

## `trunkport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：add physical member ports
- 合法语法：

  ```text
  trunkport INTERFACE [to INTERFACE]
  ```

## `undo eth-trunk`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：leave the aggregate interface
- 合法语法：

  ```text
  undo eth-trunk [INTEGER<0-63>]
  ```

## `undo trunkport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove physical member ports
- 合法语法：

  ```text
  undo trunkport INTERFACE [to INTERFACE]
  ```
