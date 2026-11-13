# uRPF

[配置指南](../urpf.md)

## `display ipv6 urpf`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 URPF information
- 合法语法：

  ```text
  display ipv6 urpf
  ```

## `display urpf`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：show per-interface uRPF mode
- 合法语法：

  ```text
  display urpf
  ```

## `ip urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure ip uRPF on the interface
- 合法语法：

  ```text
  ip urpf { loose | strict | disable }
  ```

## `ipv6 urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure ipv6 uRPF on the interface
- 合法语法：

  ```text
  ipv6 urpf { loose | strict | disable }
  ```

## `undo ip urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ip uRPF on the interface
- 合法语法：

  ```text
  undo ip urpf
  ```

## `undo ipv6 urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ipv6 uRPF on the interface
- 合法语法：

  ```text
  undo ipv6 urpf
  ```
