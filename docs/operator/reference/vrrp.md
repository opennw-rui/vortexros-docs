# VRRP

[配置指南](../vrrp.md)

## `display vrrp`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 VRRPv3 information
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
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 VRRPv3 information
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
- 视图：`接口视图`
- 用途（设备帮助）：delete or reset an IPv4 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp vrid INTEGER<1-255> [...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/vlanif, interface/vbdif

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
- 视图：`接口视图`
- 用途（设备帮助）：delete or reset an IPv6 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp6 vrid INTEGER<1-255> [...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/vlanif, interface/vbdif

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
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv4 VRRPv3 group
- 合法语法：

  ```text
  vrrp vrid INTEGER<1-255> ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/vlanif, interface/vbdif

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
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv6 VRRPv3 group
- 合法语法：

  ```text
  vrrp6 vrid INTEGER<1-255> ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/vlanif, interface/vbdif

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
