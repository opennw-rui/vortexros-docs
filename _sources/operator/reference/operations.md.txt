# 诊断与恢复

[配置指南](../09-operations.md)

## `check system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：check a VortexROS system package
- 合法语法：

  ```text
  check system-software package TARGET.tar
  ```

## `clear configuration candidate`

- 类别：Candidate管理命令
- 执行效果：仅丢弃当前会话尚未提交的修改。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：clear uncommitted configuration (two-stage)
- 合法语法：

  ```text
  clear configuration candidate
  ```

## `clear interface`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：clear interface traffic and error counters
- 合法语法：

  ```text
  clear interface TYPE N counter
  ```

## `clear system-software info`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：Clear completed software transaction history
- 合法语法：

  ```text
  clear system-software info
  ```

## `display resource-mapping`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display runtime resource-mapping storage policy
- 合法语法：

  ```text
  display resource-mapping [vpp|linux|frr]
  ```

## `display saved-configuration`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the active startup CFG or a named CFG
- 合法语法：

  ```text
  display saved-configuration [FILE.cfg]
  ```

## `display startup`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the configuration file selected for the next start
- 合法语法：

  ```text
  display startup
  ```

## `display system mac-address`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the system MAC address
- 合法语法：

  ```text
  display system mac-address
  ```

## `display system-software`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display installed software and upgrade or rollback transactions
- 合法语法：

  ```text
  display system-software [verbose]
  ```

## `display this`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display committed configuration of the current view
- 合法语法：

  ```text
  display this
  ```

## `display version`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display vortexros, system, VPP, DPDK and FRRouting version information
- 合法语法：

  ```text
  display version
  ```

## `mtr`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：run mtr with numeric output (default -n)
- 合法语法：

  ```text
  mtr [OPTIONS] HOST
  ```

## `ping`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：send ICMP echo requests (default 5 packets)
- 合法语法：

  ```text
  ping [OPTIONS] HOST
  ```

## `reset running-configuration`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：clear running configuration and restart enabled VPP; keep the saved CFG
- 合法语法：

  ```text
  reset running-configuration
  ```

## `reset saved-configuration`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：replace the active startup CFG or a named CFG with factory configuration
- 合法语法：

  ```text
  reset saved-configuration [FILE.cfg]
  ```

## `reset service frr`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart a network service
- 合法语法：

  ```text
  reset service frr
  ```

## `reset service vpp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart a network service
- 合法语法：

  ```text
  reset service vpp
  ```

## `rollback system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：rollback a VortexROS system package
- 合法语法：

  ```text
  rollback system-software package TARGET.tar
  ```

## `simulate system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：simulate a VortexROS system package
- 合法语法：

  ```text
  simulate system-software package TARGET.tar
  ```

## `traceroute`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：alias of tracert
- 合法语法：

  ```text
  traceroute [OPTIONS] HOST
  ```

## `tracert`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：trace the path with ICMP numeric probes (default -In)
- 合法语法：

  ```text
  tracert [OPTIONS] HOST
  ```

## `upgrade system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：upgrade a VortexROS system package
- 合法语法：

  ```text
  upgrade system-software package TARGET.tar
  ```
