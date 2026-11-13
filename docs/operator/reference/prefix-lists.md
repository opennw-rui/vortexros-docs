# 前缀列表

[配置指南](../prefix-lists.md)

## `display ip ip-prefix`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IP prefix lists
- 合法语法：

  ```text
  display ip ip-prefix [NAME [verbose|first-match PREFIX]]
  ```

## `display ip ipv6-prefix`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 prefix lists
- 合法语法：

  ```text
  display ip ipv6-prefix [NAME [verbose|first-match PREFIX]]
  ```

## `display ipv6 prefix`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 prefix-list information
- 合法语法：

  ```text
  display ipv6 prefix [NAME [verbose|first-match PREFIX]]
  ```

## `ip ip-prefix`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：configure an IP prefix list entry
- 合法语法：

  ```text
  ip ip-prefix NAME [index SEQ] {permit|deny} IP MASK [greater-equal GE] [less-equal LE]
  ```

## `ip ipv6-prefix`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：configure an IPv6 prefix list entry
- 合法语法：

  ```text
  ip ipv6-prefix NAME [index SEQ] {permit|deny} IPV6 PREFIX-LENGTH [greater-equal GE] [less-equal LE]
  ```

## `undo ip ip-prefix`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an IP prefix list entry or list
- 合法语法：

  ```text
  undo ip ip-prefix NAME [index SEQ]
  ```

## `undo ip ipv6-prefix`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an IPv6 prefix list entry or list
- 合法语法：

  ```text
  undo ip ipv6-prefix NAME [index SEQ]
  ```
