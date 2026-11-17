# VRRP

[配置指南](../vrrp.md)

默认优先级 100、通告间隔 1 秒、允许抢占、accept-mode 关闭，默认项不显示在配置中。IPv6 组必须至少配置一条链路本地虚拟地址，系统将其排在地址列表首位；可以暂存尚未完整的 Candidate，但缺少链路本地地址的完整组不能提交。

跟踪接口可以是当前已发现、尚未配置其他属性的物理接口，不能跟踪组所在的接口。省略 reduced 时减值为 10。后端按对应地址族的协议可用性判断跟踪状态：管理状态、链路状态和 IP 能力必须同时满足；只有物理 Up、没有 IPv4 地址的接口不会被 IPv4 组视为可用。它不能代替远端故障检测。

## `display vrrp`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv4 VRRPv3 information
- 合法语法：

  ```text
  display vrrp [brief|interface INTERFACE|statistics|protocol-information|VRID]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `brief` | Brief VRRP information | 可选、可组合 |
| 命令后 | `interface` | Interface information | 可选、可组合 |
| interface | `INTERFACE` | Interface name | 输入值 |
| 命令后 | `protocol-information` | VRRP protocol information | 可选、可组合 |
| 命令后 | `statistics` | VRRP statistics | 可选、可组合 |
| 命令后 | `INTEGER<1-255>` | Virtual router identifier | 输入值、可选、可组合 |

## `display vrrp6`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 VRRPv3 information
- 合法语法：

  ```text
  display vrrp6 [brief|interface INTERFACE|statistics|protocol-information|VRID]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `brief` | Brief VRRP information | 可选、可组合 |
| 命令后 | `interface` | Interface information | 可选、可组合 |
| interface | `INTERFACE` | Interface name | 输入值 |
| 命令后 | `protocol-information` | VRRP protocol information | 可选、可组合 |
| 命令后 | `statistics` | VRRP statistics | 可选、可组合 |
| 命令后 | `INTEGER<1-255>` | Virtual router identifier | 输入值、可选、可组合 |

## `undo vrrp vrid`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete or reset an IPv4 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp vrid INTEGER<1-255> [...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-255>` | Virtual router identifier | 输入值 |
| INTEGER<1-255> | `virtual-ip` | Delete a virtual IP address | 可选 |
| virtual-ip | `X.X.X.X` | Virtual IP address | 输入值 |
| INTEGER<1-255> | `priority` | Restore default priority | 可选 |
| INTEGER<1-255> | `timer` | Restore default timer | 可选 |
| timer | `advertise` | Restore advertisement timer | 关键字 |
| INTEGER<1-255> | `preempt-mode` | Enable preemption | 可选 |
| INTEGER<1-255> | `accept-mode` | Disable accept mode | 可选 |
| INTEGER<1-255> | `track` | Delete tracked interface | 可选 |
| track | `interface` | Interface information | 关键字 |
| interface | `INTERFACE` | Interface name | 输入值 |
| INTEGER<1-255> | `version-3` | Delete the IPv4 VRRPv3 group | 可选 |

## `undo vrrp6 vrid`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete or reset an IPv6 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp6 vrid INTEGER<1-255> [...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-255>` | Virtual router identifier | 输入值 |
| INTEGER<1-255> | `virtual-ip` | Delete a virtual IP address | 可选 |
| virtual-ip | `X:X::X:X` | Virtual IPv6 address | 输入值 |
| INTEGER<1-255> | `priority` | Restore default priority | 可选 |
| INTEGER<1-255> | `timer` | Restore default timer | 可选 |
| timer | `advertise` | Restore advertisement timer | 关键字 |
| INTEGER<1-255> | `preempt-mode` | Enable preemption | 可选 |
| INTEGER<1-255> | `accept-mode` | Disable accept mode | 可选 |
| INTEGER<1-255> | `track` | Delete tracked interface | 可选 |
| track | `interface` | Interface information | 关键字 |
| interface | `INTERFACE` | Interface name | 输入值 |

## `vrrp vrid`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure an IPv4 VRRPv3 group
- 合法语法：

  ```text
  vrrp vrid INTEGER<1-255> ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-255>` | Virtual router identifier | 输入值 |
| INTEGER<1-255> | `virtual-ip` | Specify virtual IP address | 关键字 |
| virtual-ip | `X.X.X.X` | Virtual IP address | 输入值 |
| INTEGER<1-255> | `priority` | Specify priority | 关键字 |
| priority | `INTEGER<1-254>` | The level of priority(default is 100) | 输入值 |
| INTEGER<1-255> | `timer` | Specify timer | 关键字 |
| timer | `advertise` | Specify the value of advertise timer | 关键字 |
| advertise | `INTEGER<1-40>` | Value of timer, in seconds(default is 1) | 输入值 |
| INTEGER<1-255> | `preempt-mode` | Specify preempt mode | 关键字 |
| preempt-mode | `disable` | Disable preemption | 关键字 |
| INTEGER<1-255> | `accept-mode` | Accept packets addressed to the virtual IP | 关键字 |
| accept-mode | `enable` | Enable accept mode | 关键字 |
| INTEGER<1-255> | `track` | Specify the track configuration | 关键字 |
| track | `interface` | Interface information | 关键字 |
| interface | `INTERFACE` | Interface name | 输入值 |
| INTERFACE | `reduced` | Reduce priority | 可选 |
| reduced | `INTEGER<1-255>` | Reduced value of priority | 输入值 |
| INTEGER<1-255> | `version-3` | Specify VRRPv3 | 关键字 |
| version-3 | `send-packet-mode` | VRRP advertisement send mode | 关键字 |
| send-packet-mode | `v3-only` | Send VRRPv3 advertisement packets only | 关键字 |

## `vrrp6 vrid`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure an IPv6 VRRPv3 group
- 合法语法：

  ```text
  vrrp6 vrid INTEGER<1-255> ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-255>` | Virtual router identifier | 输入值 |
| INTEGER<1-255> | `virtual-ip` | Specify virtual IP address | 关键字 |
| virtual-ip | `X:X::X:X` | Virtual IPv6 address | 输入值 |
| INTEGER<1-255> | `priority` | Specify priority | 关键字 |
| priority | `INTEGER<1-254>` | The level of priority(default is 100) | 输入值 |
| INTEGER<1-255> | `timer` | Specify timer | 关键字 |
| timer | `advertise` | Specify the value of advertise timer | 关键字 |
| advertise | `INTEGER<1-40>` | Value of timer, in seconds(default is 1) | 输入值 |
| INTEGER<1-255> | `preempt-mode` | Specify preempt mode | 关键字 |
| preempt-mode | `disable` | Disable preemption | 关键字 |
| INTEGER<1-255> | `accept-mode` | Accept packets addressed to the virtual IP | 关键字 |
| accept-mode | `enable` | Enable accept mode | 关键字 |
| INTEGER<1-255> | `track` | Specify the track configuration | 关键字 |
| track | `interface` | Interface information | 关键字 |
| interface | `INTERFACE` | Interface name | 输入值 |
| INTERFACE | `reduced` | Reduce priority | 可选 |
| reduced | `INTEGER<1-255>` | Reduced value of priority | 输入值 |
