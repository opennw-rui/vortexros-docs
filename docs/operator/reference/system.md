# 系统

[配置指南](../02-system-services.md)

## `display alarm active`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display active alarms
- 合法语法：

  ```text
  display alarm active
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display alarm history`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display cleared alarm history
- 合法语法：

  ```text
  display alarm history [last N]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `last` | show the most recent records | 可选 |
| last | `N` | INTEGER<1-1000> | 输入值 |

## `display configuration candidate`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display uncommitted candidate configuration
- 合法语法：

  ```text
  display configuration candidate [merge | sessions]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `merge` | all configuration including uncommitted changes | 可选 |
| 命令后 | `sessions` | private candidate session summary (administrator only) | 可选 |

## `display configuration storage`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display running and saved configuration storage status
- 合法语法：

  ```text
  display configuration storage
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display cpu-usage`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display CPU usage
- 合法语法：

  ```text
  display cpu-usage [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | VPP graph runtime (show runtime) and error counters | 可选 |

## `display current-configuration`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the current configuration
- 合法语法：

  ```text
  display current-configuration [configuration TYPE [name NAME] | interface [TYPE [N]] | all]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Running（已接受配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `configuration` | configuration by type | 可选 |
| configuration | `service` | Service configuration | 可选 |
| configuration | `dataplane` | Dataplane configuration | 可选 |
| configuration | `users` | Local user configuration | 可选 |
| configuration | `vpn-instance` | VPN instance configuration | 可选 |
| configuration | `acl` | ACL configuration | 可选 |
| acl | `name` | ACL name | 可选 |
| name | `ACL` | ACL name | 输入值 |
| configuration / 命令后 | `interface` | interface configuration | 可选 |
| configuration | `vlan` | VLAN configuration | 可选 |
| configuration | `bridge-domain` | bridge-domain configuration | 可选 |
| bridge-domain | `ID` | bridge-domain ID | 输入值、可选 |
| configuration | `traffic` | MQC traffic configuration | 可选 |
| traffic | `classifier` | traffic classifier | 可选 |
| classifier | `CLASSIFIER` | classifier name | 输入值、可选 |
| traffic | `behavior` | traffic behavior | 可选 |
| behavior | `BEHAVIOR` | behavior name | 输入值、可选 |
| traffic | `policy` | traffic policy | 可选 |
| policy | `POLICY` | policy name | 输入值、可选 |
| configuration | `nat-policy` | NAT policy configuration | 可选 |
| nat-policy | `NAT-POLICY` | NAT policy name | 输入值、可选 |
| configuration | `route-static` | static route configuration | 可选 |
| configuration | `route-static-group` | static route group configuration | 可选 |
| route-static-group | `GROUP` | group name | 输入值、可选 |
| configuration | `ip-prefix` | IP prefix-list configuration | 可选 |
| configuration | `ipv6-prefix` | IPv6 prefix-list configuration | 可选 |
| configuration | `route-policy` | route-policy configuration | 可选 |
| configuration | `ospf` | OSPF configuration | 可选 |
| configuration | `ospfv3` | OSPFv3 configuration | 可选 |
| configuration | `bgp` | BGP configuration | 可选 |
| configuration | `rip` | RIP configuration | 可选 |
| configuration | `ripng` | RIPng configuration | 可选 |
| configuration | `isis` | IS-IS configuration | 可选 |
| configuration | `bfd` | BFD configuration | 可选 |
| configuration | `wireguard` | WireGuard configuration | 可选 |
| configuration | `amneziawg` | AmneziaWG configuration | 可选 |
| configuration | `dhcp` | DHCP configuration | 可选 |
| configuration | `snmp-agent` | SNMP agent configuration | 可选 |
| configuration | `lcp` | LCP pair configuration | 可选 |
| configuration | `sysname` | sysname configuration | 可选 |
| interface | `IF` | interface name or TYPE | 输入值、可选 |
| IF | `N` | interface number | 输入值、可选 |
| 命令后 | `all` | all configuration | 可选 |

## `display health`

检查 Running、Actual、Saved 的代号及告警。verbose 用于查看未就绪原因。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display control-plane health
- 合法语法：

  ```text
  display health [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | include module and compatibility details | 可选 |

## `display history`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display command history for this connection
- 合法语法：

  ```text
  display history
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：当前会话。

此形式没有额外参数。

## `display memory-usage`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display memory usage
- 合法语法：

  ```text
  display memory-usage
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display service`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display network service status
- 合法语法：

  ```text
  display service [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | include daemon module readiness and errors | 可选 |

## `display vpp interface-ownership`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display physical-interface dataplane ownership and recovery state
- 合法语法：

  ```text
  display vpp interface-ownership [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | include PCI, driver and per-interface recovery details | 可选 |

## `health check`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：strict machine-readable control-plane readiness gate
- 合法语法：

  ```text
  health check [--wait] [--timeout DURATION] [--json] [--allow-weak-vpp] [--require-saved]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `--wait` | wait until strict health converges | 可选、可组合 |
| 命令后 | `--timeout DURATION` | maximum wait duration；duration such as 90s or 2m | 可选、可组合 |
| 命令后 | `--json` | emit one JSON result | 可选、可组合 |
| 命令后 | `--allow-weak-vpp` | accept only process-bound VPP weak readback | 可选、可组合 |
| 命令后 | `--require-saved` | require Running to match the saved startup configuration | 可选、可组合 |

## `sysname`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the device name
- 合法语法：

  ```text
  sysname HOSTNAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | device name | 输入值 |

## `undo sysname`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default device name
- 合法语法：

  ```text
  undo sysname
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
