# RIP

[配置指南](../rip.md)

共用命令：[`network`](dynamic-routing.md#cmd-network)、[`import-route`](dynamic-routing.md#cmd-import-route)。

## `display rip`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display RIP information
- 合法语法：

  ```text
  display rip [process-id] [database|route|interface|statistics]
  ```

## `reset service rip`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed rip routing service
- 合法语法：

  ```text
  reset service rip [ipv4|ipv6|all]
  ```

## `rip`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a RIP process and enter process view
- 合法语法：

  ```text
  rip INTEGER<1-65535> [vpn-instance NAME]
  ```

## `rip bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure RIP BFD timers
- 合法语法：

  ```text
  rip bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

## `rip bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable RIP BFD on this interface
- 合法语法：

  ```text
  rip bfd enable
  ```

## `timers rip`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：set RIP update, timeout and garbage timers
- 合法语法：

  ```text
  timers rip INTEGER<1-32767> INTEGER<1-32767> INTEGER<1-32767>
  ```

## `undo rip`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a RIP process
- 合法语法：

  ```text
  undo rip INTEGER<1-65535> [vpn-instance NAME]
  ```

## `undo rip bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore RIP BFD timers
- 合法语法：

  ```text
  undo rip bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

## `undo rip bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable RIP BFD on this interface
- 合法语法：

  ```text
  undo rip bfd enable
  ```

## `undo timers rip`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：restore RIP timers
- 合法语法：

  ```text
  undo timers rip
  ```
