# ARP 与 ND

[配置指南](../neighbors.md)

## `arp proxy`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a Linux proxy-neighbour address range
- 合法语法：

  ```text
  arp proxy X.X.X.X X.X.X.X interface IFNAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | start IPv4 address | 输入值 |
| X.X.X.X | `X.X.X.X` | end IPv4 address | 输入值 |
| X.X.X.X | `interface` | incoming Layer-3 interface | 关键字 |
| interface | `ARP-IF` | Layer-3 Ethernet ARP interface | 输入值 |

## `arp static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static ARP entry in a bridge-domain
- 合法语法：

  ```text
  arp static IP MAC bridge-domain BD
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 address | 输入值 |
| IP | `MAC` | MAC address | 输入值 |
| MAC | `bridge-domain` | bridge-domain | 关键字 |
| bridge-domain | `ID` | bridge-domain ID | 输入值 |

## `arp timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the dynamic IPv4 neighbor aging time
- 合法语法：

  ```text
  arp timeout INTEGER<60-86400>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<60-86400>` | aging time in seconds | 输入值 |

## `display arp`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the ARP table
- 合法语法：

  ```text
  display arp [all | interface IF | vpn-instance VRF | static | dynamic]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `all` | all ARP entries including VPN instances | 可选 |
| 命令后 | `interface` | ARP entries on an interface | 可选 |
| interface | `IF` | interface name | 输入值 |
| 命令后 | `vpn-instance` | ARP entries in a VPN instance | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |
| 命令后 | `static` | static ARP entries | 可选 |
| 命令后 | `dynamic` | dynamic ARP entries | 可选 |

## `display arp proxy`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display configured proxy-neighbour entries and Linux state
- 合法语法：

  ```text
  display arp proxy
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display ipv6 nd`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 neighbor discovery information
- 合法语法：

  ```text
  display ipv6 nd
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display ipv6 neighbors`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 neighbor information
- 合法语法：

  ```text
  display ipv6 neighbors [interface IF | vpn-instance VRF | static | dynamic]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | interface name | 输入值、可选 |
| 命令后 | `interface` | IPv6 neighbors on an interface | 可选 |
| interface | `IF` | interface name | 输入值 |
| 命令后 | `vpn-instance` | IPv6 neighbors in a VPN instance | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |
| 命令后 | `static` | static IPv6 neighbors | 可选 |
| 命令后 | `dynamic` | dynamic IPv6 neighbors | 可选 |

## `ipv6 nd max-number`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the IPv6 neighbor database capacity
- 合法语法：

  ```text
  ipv6 nd max-number INTEGER<1-4294967295>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4294967295>` | maximum IPv6 neighbor entries | 输入值 |

## `ipv6 nd recycle`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure IPv6 neighbor recycling at capacity
- 合法语法：

  ```text
  ipv6 nd recycle { enable | disable }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `enable` | recycle the oldest dynamic entry | 关键字 |
| 命令后 | `disable` | reject new entries at capacity | 关键字 |

## `ipv6 nd stale-timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the dynamic IPv6 neighbor stale aging time
- 合法语法：

  ```text
  ipv6 nd stale-timeout INTEGER<60-172800>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<60-172800>` | aging time in seconds | 输入值 |

## `ipv6 neighbor`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static IPv6 neighbor
- 合法语法：

  ```text
  ipv6 neighbor IPV6 MAC interface IF
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IPV6` | IPv6 neighbor address | 输入值 |
| IPV6 | `MAC` | unicast link-layer address | 输入值 |
| MAC | `interface` | outgoing interface | 关键字 |
| interface | `IF` | interface name | 输入值 |

## `reset ip arp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reset dynamic IPv4 ARP entries
- 合法语法：

  ```text
  reset ip arp [interface TYPE N] [ip X.X.X.X]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 ARP address | 输入值、可选、可组合 |
| 命令后 | `interface` | select a Layer 3 interface | 可选、可组合 |
| interface | `IF` | interface name or TYPE N | 输入值 |
| 命令后 | `ip` | select one IPv4 ARP address | 可选、可组合 |
| ip | `X.X.X.X` | IPv4 ARP address | 输入值 |

## `undo arp proxy`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a Linux proxy-neighbour address range
- 合法语法：

  ```text
  undo arp proxy X.X.X.X X.X.X.X interface IFNAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | start IPv4 address | 输入值 |
| X.X.X.X | `X.X.X.X` | end IPv4 address | 输入值 |
| X.X.X.X | `interface` | incoming Layer-3 interface | 关键字 |
| interface | `ARP-IF` | Layer-3 Ethernet ARP interface | 输入值 |

## `undo arp static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static ARP entry
- 合法语法：

  ```text
  undo arp static IP MAC bridge-domain BD
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 address | 输入值 |
| IP | `MAC` | MAC address | 输入值 |
| MAC | `bridge-domain` | bridge-domain | 关键字 |
| bridge-domain | `ID` | bridge-domain ID | 输入值 |

## `undo arp timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default IPv4 neighbor aging time
- 合法语法：

  ```text
  undo arp timeout
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6 nd max-number`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the VPP default IPv6 neighbor capacity
- 合法语法：

  ```text
  undo ipv6 nd max-number
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6 nd recycle`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the VPP default IPv6 neighbor recycle policy
- 合法语法：

  ```text
  undo ipv6 nd recycle
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6 nd stale-timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default IPv6 neighbor stale aging time
- 合法语法：

  ```text
  undo ipv6 nd stale-timeout
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6 neighbor`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static IPv6 neighbor
- 合法语法：

  ```text
  undo ipv6 neighbor IPV6 MAC interface IF
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IPV6` | IPv6 neighbor address | 输入值 |
| IPV6 | `MAC` | unicast link-layer address | 输入值 |
| MAC | `interface` | outgoing interface | 关键字 |
| interface | `IF` | interface name | 输入值 |
