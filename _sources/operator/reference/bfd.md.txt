# BFD

[配置指南](../bfd.md)

## `bfd`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enable BFD or configure a static session
- 合法语法：

  ```text
  bfd [NAME bind peer-ip PEER ...]
  ```

## `detect-multiplier`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：Detect multiplier
- 合法语法：

  ```text
  detect-multiplier INTEGER
  ```

## `display bfd`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display BFD information
- 合法语法：

  ```text
  display bfd [configuration|session [all|NAME]|statistics]
  ```

## `log-session-changes`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：log-session-changes
- 合法语法：

  ```text
  log-session-changes
  ```

## `min-rx-interval`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：Minimum receive interval in milliseconds
- 合法语法：

  ```text
  min-rx-interval INTEGER
  ```

## `min-tx-interval`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：Minimum transmit interval in milliseconds
- 合法语法：

  ```text
  min-tx-interval INTEGER
  ```

## `reset service bfd`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed bfd routing service
- 合法语法：

  ```text
  reset service bfd
  ```

## `undo bfd`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete a BFD session or disable BFD
- 合法语法：

  ```text
  undo bfd [NAME]
  ```

## `undo detect-multiplier`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：restore the default Detect multiplier
- 合法语法：

  ```text
  undo detect-multiplier
  ```

## `undo log-session-changes`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：undo log-session-changes
- 合法语法：

  ```text
  undo log-session-changes
  ```

## `undo min-rx-interval`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：restore the default Minimum receive interval in milliseconds
- 合法语法：

  ```text
  undo min-rx-interval
  ```

## `undo min-tx-interval`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：restore the default Minimum transmit interval in milliseconds
- 合法语法：

  ```text
  undo min-tx-interval
  ```
