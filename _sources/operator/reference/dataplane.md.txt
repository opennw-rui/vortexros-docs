# 数据面

[配置指南](../dataplane.md)

共用命令：[`mode`](interfaces.md#cmd-mode)、[`hardware offload`](interfaces.md#cmd-hardware-offload)。

## `cpu isolation enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Isolate VPP CPUs at Linux boot
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Pin the VPP main thread
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Pin VPP worker threads
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：Configure dataplane startup
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane-if`
- CLI 帮助：Set RX and TX descriptors
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Assign a physical PCI port to an Ethernet interface
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
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：Display active dataplane resources
- 合法语法：

  ```text
  display dataplane [verbose|interfaces|cpu [topological]|memory|iommu|tables]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | Show all dataplane status sections | 可选 |
| 命令后 | `interfaces` | Show PCI devices, drivers and receive queues | 可选 |
| 命令后 | `cpu` | Show VPP threads and Linux CPU isolation | 可选 |
| `cpu` 后 | `topological` | Show all host CPUs and NUMA/core relationships | 可选 |
| 命令后 | `memory` | Show reserved and free Linux hugepages | 可选 |
| 命令后 | `iommu` | Show IOMMU groups and PCI bindings | 可选 |
| 命令后 | `tables` | Show neighbor and MAC learning limits | 可选 |

## `display vpp api compatibility`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VPP binary API compatibility
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
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the current or most recent VPP takeover transaction
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Enable IOMMU at Linux boot
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Set the VPP global dynamic MAC learning limit
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
- 执行效果：修改当前会话配置；提交后保存；通过 reset dataplane 生成启动设置，并按提示重启主机后生效。
- 视图：`dataplane`
- CLI 帮助：Reserve huge pages at boot
- 合法语法：

  ```text
  memory hugepages size { 2M | 1G } count NUMBER [numa NODE]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `size` | Page size | 关键字 |
| size | `SIZE` | 2M or 1G | 输入值 |
| SIZE | `count` | Number of pages | 关键字 |
| count | `NUMBER` | 大页页数，范围 1–4294967295 | 输入值 |
| NUMBER | `numa` | 指定 NUMA 节点，可省略 | 关键字 |
| numa | `NODE` | NUMA 节点编号，省略为 0 | 输入值 |

`NODE` 为 NUMA 节点编号，省略时为 0。重复配置替换该节点页数；不改变其他节点。同一配置使用一种页大小。页数必须大于 0。节点必须实际存在，预留量应小于该节点可提供的内存。参见[逐节点配置与查询](../dataplane/resources.md#numa与内存)。

## `neighbor ipv4 limit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Set the Linux and VPP IPv4 neighbor limit
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Set the Linux and VPP IPv6 neighbor limit
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane-if`
- CLI 帮助：Set RX and TX queues
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

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：Activate saved dataplane settings
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove this dataplane setting
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove this dataplane setting
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove this dataplane setting
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane-if`
- CLI 帮助：Restore default descriptors
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove a PCI port assignment
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove this dataplane setting
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Restore the default table limit
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
- 执行效果：在当前会话中撤销对应配置；提交并保存后，通过 reset dataplane 应用，并按提示重启。
- 视图：`dataplane`
- CLI 帮助：Remove a NUMA hugepage reservation
- 合法语法：

  ```text
  undo memory hugepages [numa NODE]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

`numa NODE` 为可选参数，选择需要撤销预留的节点。

省略 `numa NODE` 时只撤销节点 0，不清除其他节点的预留。

## `undo neighbor ipv4 limit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Restore the default table limit
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Restore the default table limit
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane-if`
- CLI 帮助：Restore default queues
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore default VPP startup configuration path
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：VPP process startup configuration file (-c)
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
