# 数据面

[配置指南](../dataplane.md)

共用命令：[`mode`](interfaces.md#cmd-mode)、[`hardware offload`](interfaces.md#cmd-hardware-offload)。

## `cpu isolation enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Isolate VPP CPUs at Linux boot
- 合法语法：

  ```text
  cpu isolation enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `cpu main-core`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Pin the VPP main thread
- 合法语法：

  ```text
  cpu main-core NUMBER
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NUMBER` | Logical CPU | 输入值 |

## `cpu worker-cores`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Pin VPP worker threads
- 合法语法：

  ```text
  cpu worker-cores CPU-LIST
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `CPU-LIST` | CPU list such as 3-5,8 | 输入值 |

## `dataplane`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：Configure dataplane startup
- 合法语法：

  ```text
  dataplane
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `descriptors`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Set RX and TX descriptors
- 合法语法：

  ```text
  descriptors rx COUNT tx COUNT
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `rx` | Receive | 关键字 |
| rx | `COUNT` | RX count | 输入值 |
| COUNT | `tx` | Transmit | 关键字 |
| tx | `COUNT` | TX count | 输入值 |

## `device`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Assign a physical PCI port to an Ethernet interface
- 合法语法：

  ```text
  device PCI-BDF name Ethernet NUMBER
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PCI-BDF` | PCI address | 输入值 |
| PCI-BDF | `name` | Assign interface name | 关键字 |
| name | `Ethernet` | Ethernet interface | 关键字 |
| Ethernet | `NUMBER` | Interface number starting at 0 | 输入值 |

## `display dataplane`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：Display active dataplane resources
- 合法语法：

  ```text
  display dataplane [verbose|interfaces|cpu|memory|iommu|tables]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | Show all dataplane status sections | 可选 |
| 命令后 | `interfaces` | Show PCI devices, drivers and receive queues | 可选 |
| 命令后 | `cpu` | Show VPP threads and Linux CPU isolation | 可选 |
| 命令后 | `memory` | Show reserved and free Linux hugepages | 可选 |
| 命令后 | `iommu` | Show IOMMU groups and PCI bindings | 可选 |
| 命令后 | `tables` | Show neighbor and MAC learning limits | 可选 |

## `display vpp api compatibility`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VPP binary API compatibility
- 合法语法：

  ```text
  display vpp api compatibility [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | include compatibility failure details | 可选 |

## `display vpp takeover transaction`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the current or most recent VPP takeover transaction
- 合法语法：

  ```text
  display vpp takeover transaction
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `iommu enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Enable IOMMU at Linux boot
- 合法语法：

  ```text
  iommu enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `mac-address learn-limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Set the VPP global dynamic MAC learning limit
- 合法语法：

  ```text
  mac-address learn-limit INTEGER<1-2147483647>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-2147483647>` | Maximum entries | 输入值 |

## `memory hugepages`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Reserve huge pages at boot
- 合法语法：

  ```text
  memory hugepages size { 2M | 1G } count NUMBER
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `size` | Page size | 关键字 |
| size | `SIZE` | 2M or 1G | 输入值 |
| SIZE | `count` | Number of pages | 关键字 |
| count | `NUMBER` | Page count | 输入值 |

## `neighbor ipv4 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Set the Linux and VPP IPv4 neighbor limit
- 合法语法：

  ```text
  neighbor ipv4 limit INTEGER<4-2147483647>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<4-2147483647>` | Maximum entries | 输入值 |

## `neighbor ipv6 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Set the Linux and VPP IPv6 neighbor limit
- 合法语法：

  ```text
  neighbor ipv6 limit INTEGER<4-2147483647>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<4-2147483647>` | Maximum entries | 输入值 |

## `queues`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Set RX and TX queues
- 合法语法：

  ```text
  queues rx COUNT tx COUNT
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `rx` | Receive | 关键字 |
| rx | `COUNT` | RX count | 输入值 |
| COUNT | `tx` | Transmit | 关键字 |
| tx | `COUNT` | TX count | 输入值 |

## `reset dataplane`

应用需重启的数据面配置。VPP 和选中网卡的驱动归属可能变化，须安排业务窗口并保留管理通道。

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：Activate saved dataplane settings
- 合法语法：

  ```text
  reset dataplane
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `undo cpu isolation enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu isolation enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo cpu main-core`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu main-core
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo cpu worker-cores`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu worker-cores
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo descriptors`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Restore default descriptors
- 合法语法：

  ```text
  undo descriptors
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo device`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove a PCI port assignment
- 合法语法：

  ```text
  undo device PCI-BDF
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PCI-BDF` | PCI address | 输入值 |

## `undo iommu enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo iommu enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo mac-address learn-limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Restore the default table limit
- 合法语法：

  ```text
  undo mac-address learn-limit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo memory hugepages`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo memory hugepages
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo neighbor ipv4 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Restore the default table limit
- 合法语法：

  ```text
  undo neighbor ipv4 limit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo neighbor ipv6 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Restore the default table limit
- 合法语法：

  ```text
  undo neighbor ipv6 limit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo queues`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Restore default queues
- 合法语法：

  ```text
  undo queues
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo vpp startup-config`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore default VPP startup configuration path
- 合法语法：

  ```text
  undo vpp startup-config
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `vpp startup-config`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：VPP process startup configuration file (-c)
- 合法语法：

  ```text
  vpp startup-config PATH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PATH` | Linux path to VPP startup.conf (default /VortexROS/startup.conf) | 输入值 |
