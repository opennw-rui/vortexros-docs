# 系统、健康与服务


## `display alarm active`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display active alarms
- 合法语法：

  ```text
  display alarm active
  ```

## `display alarm history`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display cleared alarm history
- 合法语法：

  ```text
  display alarm history [last N]
  ```

## `display configuration candidate`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display uncommitted candidate configuration
- 合法语法：

  ```text
  display configuration candidate [merge | sessions]
  ```

## `display configuration storage`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display running and saved configuration storage status
- 合法语法：

  ```text
  display configuration storage
  ```

## `display cpu-usage`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display CPU usage
- 合法语法：

  ```text
  display cpu-usage [verbose]
  ```

## `display current-configuration`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the current configuration
- 合法语法：

  ```text
  display current-configuration [configuration TYPE [name NAME] | interface [TYPE [N]] | all]
  ```

## `display health`

检查 Running、Actual、Saved 的代号及告警。verbose 用于查看未就绪原因。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display control-plane health
- 合法语法：

  ```text
  display health [verbose]
  ```

## `display history`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display command history for this connection
- 合法语法：

  ```text
  display history
  ```

## `display memory-usage`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display memory usage
- 合法语法：

  ```text
  display memory-usage
  ```

## `display service`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display network service status
- 合法语法：

  ```text
  display service [verbose]
  ```

## `display vpp api compatibility`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VPP binary API compatibility
- 合法语法：

  ```text
  display vpp api compatibility [verbose]
  ```

## `display vpp interface-ownership`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display physical-interface dataplane ownership and recovery state
- 合法语法：

  ```text
  display vpp interface-ownership [verbose]
  ```

## `display vpp takeover transaction`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the current or most recent VPP takeover transaction
- 合法语法：

  ```text
  display vpp takeover transaction
  ```

## `enable lldp`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable LLDP globally and on all physical interfaces
- 合法语法：

  ```text
  enable lldp
  ```

## `enable switch`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable the L2 switch instance
- 合法语法：

  ```text
  enable switch
  ```

## `health check`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：strict machine-readable control-plane readiness gate
- 合法语法：

  ```text
  health check [--wait] [--timeout DURATION] [--json] [--allow-weak-vpp] [--require-saved]
  ```

## `sysname`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the device name
- 合法语法：

  ```text
  sysname HOSTNAME
  ```

## `undo enable lldp`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable LLDP globally
- 合法语法：

  ```text
  undo enable lldp
  ```

## `undo enable switch`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable the L2 switch instance
- 合法语法：

  ```text
  undo enable switch
  ```

## `undo sysname`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default device name
- 合法语法：

  ```text
  undo sysname
  ```

## `undo vpp startup-config`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore default VPP startup configuration path
- 合法语法：

  ```text
  undo vpp startup-config
  ```

## `vpp startup-config`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：VPP process startup configuration file (-c)
- 合法语法：

  ```text
  vpp startup-config PATH
  ```
