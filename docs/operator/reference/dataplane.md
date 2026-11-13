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

## `cpu main-core`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Pin the VPP main thread
- 合法语法：

  ```text
  cpu main-core NUMBER
  ```

## `cpu worker-cores`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Pin VPP worker threads
- 合法语法：

  ```text
  cpu worker-cores CPU-LIST
  ```

## `dataplane`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：Configure dataplane startup
- 合法语法：

  ```text
  dataplane
  ```

## `descriptors`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Set RX and TX descriptors
- 合法语法：

  ```text
  descriptors rx COUNT tx COUNT
  ```

## `device`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Assign a physical PCI port to an Ethernet interface
- 合法语法：

  ```text
  device PCI-BDF name Ethernet NUMBER
  ```

## `display dataplane`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：Display active dataplane resources
- 合法语法：

  ```text
  display dataplane [verbose|interfaces|cpu|memory|iommu|tables]
  ```

## `display vpp api compatibility`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VPP binary API compatibility
- 合法语法：

  ```text
  display vpp api compatibility [verbose]
  ```

## `display vpp takeover transaction`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the current or most recent VPP takeover transaction
- 合法语法：

  ```text
  display vpp takeover transaction
  ```

## `iommu enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Enable IOMMU at Linux boot
- 合法语法：

  ```text
  iommu enable
  ```

## `mac-address learn-limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Set the VPP global dynamic MAC learning limit
- 合法语法：

  ```text
  mac-address learn-limit INTEGER<1-2147483647>
  ```

## `memory hugepages`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Reserve huge pages at boot
- 合法语法：

  ```text
  memory hugepages size { 2M | 1G } count NUMBER
  ```

## `neighbor ipv4 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Set the Linux and VPP IPv4 neighbor limit
- 合法语法：

  ```text
  neighbor ipv4 limit INTEGER<4-2147483647>
  ```

## `neighbor ipv6 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Set the Linux and VPP IPv6 neighbor limit
- 合法语法：

  ```text
  neighbor ipv6 limit INTEGER<4-2147483647>
  ```

## `queues`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Set RX and TX queues
- 合法语法：

  ```text
  queues rx COUNT tx COUNT
  ```

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

## `undo cpu isolation enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu isolation enable
  ```

## `undo cpu main-core`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu main-core
  ```

## `undo cpu worker-cores`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu worker-cores
  ```

## `undo descriptors`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Restore default descriptors
- 合法语法：

  ```text
  undo descriptors
  ```

## `undo device`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove a PCI port assignment
- 合法语法：

  ```text
  undo device PCI-BDF
  ```

## `undo iommu enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo iommu enable
  ```

## `undo mac-address learn-limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Restore the default table limit
- 合法语法：

  ```text
  undo mac-address learn-limit
  ```

## `undo memory hugepages`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo memory hugepages
  ```

## `undo neighbor ipv4 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Restore the default table limit
- 合法语法：

  ```text
  undo neighbor ipv4 limit
  ```

## `undo neighbor ipv6 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Restore the default table limit
- 合法语法：

  ```text
  undo neighbor ipv6 limit
  ```

## `undo queues`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Restore default queues
- 合法语法：

  ```text
  undo queues
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
