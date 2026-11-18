# 资源与运行查询

## 查询实际状态

`display current-configuration configuration dataplane` 和 dataplane 视图中的 `display this` 显示配置；它们不证明当前 Linux 或 VPP 已应用参数。进入设备子视图后，`display this` 只显示选中的 PCI 设备。

| 命令 | 实际状态和用途 |
|---|---|
| `display dataplane` | 活动后端和 PCI 接管阶段 |
| `display dataplane interfaces` | 期望/活动模式、PCI 驱动、VPP 当前和最大 RX 队列 |
| `display dataplane cpu` | Linux 隔离 CPU、VPP 线程及 CPU |
| `display dataplane cpu topological` | 全部 CPU 的 NUMA、Socket、物理核心对应关系和在线状态 |
| `display dataplane memory` | 各 NUMA 节点内存、大页配置与实际页数，以及整机保留量 |
| `display dataplane iommu` | IOMMU 组和受管设备所属组 |
| `display dataplane tables` | 期望容量、VPP 实际容量、Linux 邻居 GC 阈值 |
| `display dataplane verbose` | 汇总上述运行信息 |

L2FIB 为空时不能凭空读出实时容量，查询单独标记显式 MAC 启动值。大页总量是单页大小乘页数，例如 2M ×1024 为2GiB，不能用进程 VSZ 替代。


## 按拓扑选择 CPU

~~~text
display dataplane cpu topological
~~~

下面为双 NUMA、8 个逻辑 CPU、每物理核两个 SMT 线程的实际查询输出：

~~~text
CPU NODE SOCKET CORE ONLINE
  0    0      0    0    yes
  1    0      0    0    yes
  2    0      0    1    yes
  3    0      0    1    yes
  4    1      1    2    yes
  5    1      1    2    yes
  6    1      1    3    yes
  7    1      1    3    yes
~~~

- CPU：配置main-core和worker-cores时使用的逻辑CPU编号。
- NODE：该CPU的NUMA节点。
- SOCKET、CORE：拓扑中的插槽和核心编号。相同且已知的Socket/Core表示同一物理核，例如CPU0/1为同胞线程，不能当作两个独立物理核。
- ONLINE：当前能否被调度。查询包含离线CPU；内核没有报告的拓扑显示为“-”，不推断其归属。

优先让同一业务的主线程、worker和网卡位于合适的同一NUMA节点。上面拓扑中的CPU4和6属于同一节点的不同物理核。现有隔离配置只针对指定的逻辑CPU，不会自动选择核心、离线SMT或隔离未指定的同胞线程；不同Core只能避免VPP线程彼此共享物理核，不代表系统任务不会使用同胞线程。

该查询在Linux数据面或VPP停止时也可使用。只读取信息，不改变CPU配置。

## NUMA与内存

内存和大页也有NUMA归属。CPU可以访问其他节点的内存，但会发生跨节点访问；应结合CPU和网卡所在节点安排数据面资源。

大页按 NUMA 节点预留，命令末尾使用 `numa NODE` 指定节点。省略时只为节点 0 预留，不会平均分配到其他节点。

~~~text
dataplane
 memory hugepages size 2M count 1024
 memory hugepages size 2M count 512 numa 1
#
~~~

以上分别为节点 0 预留 2GiB、节点 1 预留 1GiB。同一节点再次配置会替换该节点页数，不累加；其他节点保持原值。各节点共用所选页大小（2M 或 1G），修改页大小前需先撤销其他节点的预留。

执行 `commit`、`save` 后，使用 `reset dataplane` 应用启动设置；需要主机重启时，CLI 会给出提示。按提示重启后，再检查：

~~~text
display dataplane memory
display current-configuration configuration dataplane
~~~

`NUMA memory` 显示每个节点的总内存和空闲内存（KiB）；`Hugepages by NUMA node` 中 Configured 为配置页数，Total/Free 为内核实际总页数和空闲页数。Configured 为 `-` 表示该节点和页大小没有显式预留。整机 Reserved 在 Global hugepage pools 中显示，不将它错误分摊到各节点。

以下查询对应节点 0 配置 1024 页、节点 1 配置 512 页并重启后的实际结果：

~~~text
Hugepages by NUMA node
  Node     Page size      Configured        Total         Free
  0        1048576kB               -            0            0
  0        2048kB               1024         1024         1024
  1        1048576kB               -            0            0
  1        2048kB                512          512          512

Global hugepage pools
  Page size             Total       Free   Reserved
  1048576kB                 0          0          0
  2048kB                 1536       1536          0
~~~

预留成功不代表全部大页仍然空闲；VPP 和其他使用者会消耗大页。实际总页数不足时，应检查该节点可用内存和启动结果。大页预留不会自动修改 CPU、迁移既有内存，也不等于强制将 VPP 所有内存绑定到该节点。

撤销节点 1，保留节点 0：

~~~text
dataplane
 undo memory hugepages numa 1
#
~~~

`undo memory hugepages` 只撤销节点 0。撤销后同样需要提交、保存，并按重置数据面的提示完成重启。

## CPU、大页与 IOMMU

~~~text
system-view
~~~

配置清单：

~~~text
dataplane
 cpu main-core 4
 cpu worker-cores 6
 cpu isolation enable
 memory hugepages size 2M count 1024
 iommu enable
#
~~~

CLI 操作：

~~~text
commit
save
display dataplane cpu
display dataplane memory
display dataplane iommu
reset dataplane
~~~

CPU4/6对应上面的拓扑示例，其他设备必须按本机查询结果选择；CPU/NUMA/PCI 条件按本机调整，不能覆盖唯一管理路径。主核和 worker 不重叠，CPU 编号从0开始。配置 worker 时必须同时指定主核。引导参数需要主机重启时会提示；只生成 GRUB 片段不代表当前内核已生效。

激活后核对线程、队列和描述符的运行值。撤销显式设置后采用设备或驱动默认值；默认值并非所有网卡相同。

## 撤销

先按[设备接管](devices.md)确认是否需保留 DPDK。单独撤销 worker 时：

~~~text
system-view
~~~

配置清单：

~~~text
dataplane
 undo cpu worker-cores
 undo cpu main-core
 undo cpu isolation enable
 undo memory hugepages
 undo iommu enable
#
~~~

CLI 操作：

~~~text
commit
save
reset dataplane
~~~

先撤销 worker 再撤销主核。仍有设备依赖特定启动条件时，不能靠撤销资源参数强制实现可用的 DPDK；应按激活提示处理，检查[恢复结果](recovery.md)。生产变更前确保可恢复管理路径。

[完整参数](../reference/dataplane.md)

## DMA 地址模式

自动生成的 VFIO/DPDK 启动配置使用 PA 地址模式，避免虚拟地址超出设备可接受的 DMA 地址范围。这不会关闭 IOMMU，设备隔离仍由已配置的 IOMMU 提供；不需要另配 CLI 参数。修改启动配置后按数据面激活提示操作，不能仅根据大页有剩余判断 DPDK 一定能够启动。

地址模式原理见 [DPDK IOVA 说明](https://www.dpdk.org/memory-in-dpdk-part-2-deep-dive-into-iova/)。
