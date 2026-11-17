# RIP

[配置指南](../rip.md)

共用命令：[`network`](dynamic-routing.md#cmd-network)、[`import-route`](dynamic-routing.md#cmd-import-route)。

## `display rip`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display RIP information
- 合法语法：

  ```text
  display rip [process-id] [database|route|interface|statistics]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值、可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `database` | Database information | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `interface` | Interface information | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `route` | Route information | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `statistics` | Statistical information | 可选 |
| 命令后 | `vpn-instance` | VPN instance | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |

## `reset service rip`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart the managed rip routing service
- 合法语法：

  ```text
  reset service rip [ipv4|ipv6|all]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ipv4` | restart the IPv4 protocol daemon | 可选 |
| 命令后 | `ipv6` | restart the IPv6 protocol daemon | 可选 |
| 命令后 | `all` | restart both address-family daemons | 可选 |

## `rip`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a RIP process and enter process view
- 合法语法：

  ```text
  rip INTEGER<1-65535> [vpn-instance NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值 |
| INTEGER<1-65535> | `vpn-instance` | VPN instance | 可选、可组合 |
| vpn-instance | `VPN` | VPN instance name | 输入值 |

## `rip bfd`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure RIP BFD timers
- 合法语法：

  ```text
  rip bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `min-tx-interval` | Minimum transmit interval in milliseconds | 关键字 |
| min-tx-interval | `INTEGER<100-1000>` | Minimum transmit interval in milliseconds | 输入值 |
| INTEGER<100-1000> / INTEGER<3-50> | `min-rx-interval` | Minimum receive interval in milliseconds | 可选、可组合 |
| min-rx-interval | `INTEGER<100-1000>` | Minimum receive interval in milliseconds | 输入值 |
| INTEGER<100-1000> | `detect-multiplier` | BFD detection multiplier | 可选、可组合 |
| detect-multiplier | `INTEGER<3-50>` | Detection multiplier | 输入值 |
| 命令后 | `min-rx-interval` | Minimum receive interval in milliseconds | 关键字 |
| INTEGER<100-1000> / INTEGER<3-50> | `min-tx-interval` | Minimum transmit interval in milliseconds | 可选、可组合 |
| 命令后 | `detect-multiplier` | BFD detection multiplier | 关键字 |

## `rip bfd enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable RIP BFD on this interface
- 合法语法：

  ```text
  rip bfd enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `timers rip`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：set RIP update, timeout and garbage timers
- 合法语法：

  ```text
  timers rip INTEGER<1-32767> INTEGER<1-32767> INTEGER<1-32767>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-32767>` | Update timer in seconds | 输入值 |
| INTEGER<1-32767> | `INTEGER<1-32767>` | Timeout timer in seconds | 输入值 |
| INTEGER<1-32767> | `INTEGER<1-32767>` | Garbage timer in seconds | 输入值 |

## `undo rip`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a RIP process
- 合法语法：

  ```text
  undo rip INTEGER<1-65535> [vpn-instance NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ARGS` | process id and optional vpn-instance | 输入值、后续文本 |

## `undo rip bfd`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore RIP BFD timers
- 合法语法：

  ```text
  undo rip bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `min-tx-interval` | Minimum transmit interval in milliseconds | 关键字 |
| detect-multiplier / min-tx-interval | `min-rx-interval` | Minimum receive interval in milliseconds | 可选、可组合 |
| min-rx-interval / min-tx-interval | `detect-multiplier` | BFD detection multiplier | 可选、可组合 |
| 命令后 | `min-rx-interval` | Minimum receive interval in milliseconds | 关键字 |
| detect-multiplier / min-rx-interval | `min-tx-interval` | Minimum transmit interval in milliseconds | 可选、可组合 |
| 命令后 | `detect-multiplier` | BFD detection multiplier | 关键字 |

## `undo rip bfd enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable RIP BFD on this interface
- 合法语法：

  ```text
  undo rip bfd enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo timers rip`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：restore RIP timers
- 合法语法：

  ```text
  undo timers rip
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
