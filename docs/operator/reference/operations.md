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

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TARGET` | VortexROS system package | 输入值 |

## `clear configuration candidate`

- 类别：Candidate管理命令
- 执行效果：仅丢弃当前会话尚未提交的修改。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：clear uncommitted configuration (two-stage)
- 合法语法：

  ```text
  clear configuration candidate
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `clear interface`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：clear interface traffic and error counters
- 合法语法：

  ```text
  clear interface TYPE N counter
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | interface name or TYPE N | 输入值 |
| IF | `counter` | clear traffic and error counters | 关键字 |

## `clear system-software info`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：Clear completed software transaction history
- 合法语法：

  ```text
  clear system-software info
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display resource-mapping`

- 视图：`任意允许视图`
显示当前记录的有效运行资源映射，不修改配置：

- 合法语法：

  ```text
  display resource-mapping [vpp|linux|frr]
  ```

省略参数时列出所有后端的记录；指定后端时只显示相应记录。Runtime ID 是当前运行编号，数据面重建后可能改变。

```text
<VortexROS> display resource-mapping vpp
Backend  Resource                   Logical key                      Runtime ID
vpp      loopback                   LoopBack201                      7
vpp      vrf-table                  SHOW201                          1024
Total mappings: 2
```

映射随对应对象撤销而清理。例如删除 LoopBack201 和 SHOW201 后，以上两行应消失；其他仍在使用的接口和桥域映射继续保留。零条记录表示当前没有已登记的映射，不能据此推断设备没有接口或 VPN 实例。接口清单使用 `display interface`；VPN 表号使用 `display ip vpn-instance verbose`。本命令不代替后端健康与业务流量检查。


## `display saved-configuration`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the active startup CFG or a named CFG
- 合法语法：

  ```text
  display saved-configuration [FILE.cfg]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `FILE` | configuration file name | 输入值、可选 |

## `display startup`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the configuration file selected for the next start
- 合法语法：

  ```text
  display startup
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display system mac-address`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the system MAC address
- 合法语法：

  ```text
  display system mac-address
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Running（已接受配置）。

此形式没有额外参数。

## `display system-software`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display installed software and upgrade or rollback transactions
- 合法语法：

  ```text
  display system-software [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | include recorded failure evidence | 可选 |

## `display this`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display committed configuration of the current view
- 合法语法：

  ```text
  display this
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Running（已接受配置）。

此形式没有额外参数。

## `display version`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display vortexros, system, VPP, DPDK and FRRouting version information
- 合法语法：

  ```text
  display version
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `mtr`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：run mtr with numeric output (default -n)
- 合法语法：

  ```text
  mtr [OPTIONS] HOST
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `-a IP` | Source address；Source address | 可选、可组合 |
| 命令后 | `-c INTEGER` | Report cycles；Report cycles | 可选、可组合 |
| 命令后 | `-f INTEGER` | First TTL；First TTL | 可选、可组合 |
| 命令后 | `-i MILLISECONDS` | Probe interval in milliseconds；Probe interval in milliseconds | 可选、可组合 |
| 命令后 | `-m INTEGER` | Maximum TTL；Maximum TTL | 可选、可组合 |
| 命令后 | `-n` | Numeric output (default) | 可选、可组合 |
| 命令后 | `-name` | Resolve hop names | 可选、可组合 |
| 命令后 | `-r` | Report mode | 可选、可组合 |
| 命令后 | `-s INTEGER` | Packet size；Packet size | 可选、可组合 |
| 命令后 | `-vpn-instance VRF` | Run in a Linux VRF；Run in a Linux VRF | 可选、可组合 |
| 命令后 | `-w` | Wide report | 可选、可组合 |
| 命令后 | `ip` | IPv4 protocol (default) | 可选、可组合 |
| 命令后 | `ipv6` | IPv6 protocol | 可选、可组合 |
| 命令后 | `HOST` | IP address or hostname of a remote system | 输入值 |

## `ping`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：send ICMP echo requests (default 5 packets)
- 合法语法：

  ```text
  ping [OPTIONS] HOST
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `-a IP` | Select source IPv4/IPv6 address；Select source IPv4/IPv6 address | 可选、可组合 |
| 命令后 | `-c INTEGER` | Number of echo requests (default 5)；Number of echo requests (default 5) | 可选、可组合 |
| 命令后 | `-d` | Set SO_DEBUG | 可选、可组合 |
| 命令后 | `-f` | Set Don't Fragment (IPv4) | 可选、可组合 |
| 命令后 | `-h INTEGER` | TTL / hop limit；TTL / hop limit | 可选、可组合 |
| 命令后 | `-i IF` | Sending interface；Sending interface | 可选、可组合 |
| 命令后 | `-m MILLISECONDS` | Interval in milliseconds；Interval in milliseconds | 可选、可组合 |
| 命令后 | `-n` | Numeric output | 可选、可组合 |
| 命令后 | `-name` | Resolve destination names | 可选、可组合 |
| 命令后 | `-nexthop` | Display nexthop information (no Linux ping equivalent) | 可选、可组合 |
| 命令后 | `-p HEX` | Payload pattern；Payload pattern | 可选、可组合 |
| 命令后 | `-q` | Quiet output | 可选、可组合 |
| 命令后 | `-r` | Record route | 可选、可组合 |
| 命令后 | `-range VALUE` | Payload length range (multi-run operation)；Payload length range (multi-run operation) | 可选、可组合 |
| 命令后 | `-s INTEGER` | Payload size；Payload size | 可选、可组合 |
| 命令后 | `-system-time` | Display send/receive timestamps | 可选、可组合 |
| 命令后 | `-t MILLISECONDS` | Reply timeout in milliseconds；Reply timeout in milliseconds | 可选、可组合 |
| 命令后 | `-tos INTEGER` | IPv4 TOS；IPv4 TOS | 可选、可组合 |
| 命令后 | `-v` | Verbose output | 可选、可组合 |
| 命令后 | `-vpn-instance VRF` | Run in a Linux VRF；Run in a Linux VRF | 可选、可组合 |
| 命令后 | `ignore-mtu` | Do not perform PMTU discovery | 可选、可组合 |
| 命令后 | `ip` | IPv4 protocol (default) | 可选、可组合 |
| 命令后 | `ipv6` | IPv6 protocol | 可选、可组合 |
| 命令后 | `HOST` | IP address or hostname of a remote system | 输入值 |

## `reset running-configuration`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：clear running configuration and restart enabled VPP; keep the saved CFG
- 合法语法：

  ```text
  reset running-configuration
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `reset saved-configuration`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：replace the active startup CFG or a named CFG with factory configuration
- 合法语法：

  ```text
  reset saved-configuration [FILE.cfg]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `FILE` | configuration file name | 输入值、可选 |

## `reset service frr`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart a network service
- 合法语法：

  ```text
  reset service frr
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `reset service vpp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart a network service
- 合法语法：

  ```text
  reset service vpp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `rollback system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：rollback a VortexROS system package
- 合法语法：

  ```text
  rollback system-software package TARGET.tar
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TARGET` | VortexROS system package | 输入值 |

## `simulate system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：simulate a VortexROS system package
- 合法语法：

  ```text
  simulate system-software package TARGET.tar
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TARGET` | VortexROS system package | 输入值 |

## `traceroute`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：alias of tracert
- 合法语法：

  ```text
  traceroute [OPTIONS] HOST
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `-a IP` | Source address；Source address | 可选、可组合 |
| 命令后 | `-f INTEGER` | First TTL；First TTL | 可选、可组合 |
| 命令后 | `-m INTEGER` | Maximum TTL；Maximum TTL | 可选、可组合 |
| 命令后 | `-name` | Resolve hop names | 可选、可组合 |
| 命令后 | `-p INTEGER` | Destination UDP port；Destination UDP port | 可选、可组合 |
| 命令后 | `-q INTEGER` | Probes per hop；Probes per hop | 可选、可组合 |
| 命令后 | `-s INTEGER` | Probe packet length；Probe packet length | 可选、可组合 |
| 命令后 | `-v` | Verbose output | 可选、可组合 |
| 命令后 | `-vpn-instance VRF` | Run in a Linux VRF；Run in a Linux VRF | 可选、可组合 |
| 命令后 | `-w MILLISECONDS` | Reply timeout in milliseconds；Reply timeout in milliseconds | 可选、可组合 |
| 命令后 | `ip` | IPv4 protocol (default) | 可选、可组合 |
| 命令后 | `ipv6` | IPv6 protocol | 可选、可组合 |
| 命令后 | `HOST` | IP address or hostname of a remote system | 输入值 |

## `tracert`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：trace the path with ICMP numeric probes (default -In)
- 合法语法：

  ```text
  tracert [OPTIONS] HOST
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `-a IP` | Source address；Source address | 可选、可组合 |
| 命令后 | `-f INTEGER` | First TTL；First TTL | 可选、可组合 |
| 命令后 | `-m INTEGER` | Maximum TTL；Maximum TTL | 可选、可组合 |
| 命令后 | `-name` | Resolve hop names | 可选、可组合 |
| 命令后 | `-p INTEGER` | Destination UDP port；Destination UDP port | 可选、可组合 |
| 命令后 | `-q INTEGER` | Probes per hop；Probes per hop | 可选、可组合 |
| 命令后 | `-s INTEGER` | Probe packet length；Probe packet length | 可选、可组合 |
| 命令后 | `-v` | Verbose output | 可选、可组合 |
| 命令后 | `-vpn-instance VRF` | Run in a Linux VRF；Run in a Linux VRF | 可选、可组合 |
| 命令后 | `-w MILLISECONDS` | Reply timeout in milliseconds；Reply timeout in milliseconds | 可选、可组合 |
| 命令后 | `ip` | IPv4 protocol (default) | 可选、可组合 |
| 命令后 | `ipv6` | IPv6 protocol | 可选、可组合 |
| 命令后 | `HOST` | IP address or hostname of a remote system | 输入值 |

## `upgrade system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：upgrade a VortexROS system package
- 合法语法：

  ```text
  upgrade system-software package TARGET.tar
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TARGET` | VortexROS system package | 输入值 |
