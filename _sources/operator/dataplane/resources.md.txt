# 资源与运行查询

## 查询实际状态

`display current-configuration configuration dataplane` 和 dataplane 视图中的 `display this` 显示配置；它们不证明当前 Linux 或 VPP 已应用参数。进入设备子视图后，`display this` 只显示选中的 PCI 设备。

| 命令 | 实际状态和用途 |
|---|---|
| `display dataplane` | 活动后端和 PCI 接管阶段 |
| `display dataplane interfaces` | PCI 所属 NUMA 节点、期望/活动模式、PCI 驱动、当前和最大 RX 队列 |
| `display dataplane cpu` | Linux 隔离 CPU、VPP 线程及 CPU |
| `display dataplane cpu topological` | 全部 CPU 的 NUMA、Socket、物理核心对应关系和在线状态 |
| `display dataplane memory` | 各 NUMA 节点内存、大页配置与实际页数，以及整机保留量 |
| `display dataplane iommu` | IOMMU 组、受管设备所属组及 NUMA 节点 |
| `display dataplane tables` | 期望容量、VPP 实际容量、Linux 邻居 GC 阈值 |
| `display dataplane verbose` | 汇总上述运行信息 |

L2FIB 为空时不能凭空读出实时容量，查询单独标记显式 MAC 启动值。大页总量是单页大小乘页数，例如 2M ×1024 为2GiB，不能用进程 VSZ 替代。


## 网卡所属 NUMA

`display dataplane interfaces` 的 NUMA 列表示 PCI 网卡实际关联的节点，`display dataplane` 和 `display dataplane verbose` 中的接口表也包含该列。它不是按接口编号推算，也不随 CPU 配置改变；DPDK 接管后仍按 PCI 设备身份查询。

节点为 0、1 等整数时，可与 `display dataplane cpu topological` 和 `display dataplane memory` 的节点号对照。`unknown` 表示固件或系统未提供设备的 NUMA 归属，`unavailable` 表示当前无法读取，例如设备已移除。二者都不能当作节点 0。

以下是系统没有报告 PCI 节点关联时的实际查询节选；实际设备有明确关联时，该列显示对应的数字：

~~~text
<VortexROS> display dataplane interfaces
Dataplane interfaces
  PCI            Interface       NUMA     Desired    Active       Driver       RX queues
  0000:00:02.0   Ethernet0       unknown  dpdk       DPDK         vfio-pci     1/1
~~~

配置中的资源参数按 CPU、内存和其他全局设置在前，设备子段在后显示。`#` 只作分隔，不是需要手工执行的命令；保存后的配置可按相同层次加载。选择设备子视图时，`display this` 只显示该设备，不重复全局资源。

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


## 数据面内存预算

大页预留、主堆、统计区和报文缓冲池是不同的资源。预留 2 GiB 大页不表示某一张表可以独占 2 GiB，也不会自动扩大统计区。

正常生成的数据面启动参数包括：

| 资源 | 默认预算 | 作用 |
|---|---:|---|
| 主堆 | 1 GiB | 路由、邻接及其他控制对象的分配空间 |
| 统计区 | 128 MiB，全进程共享 | 接口、路由等对象的统计；部分计数按 worker 分开保存 |
| 报文缓冲池 | 每个使用的 NUMA 节点 32768 个缓冲的配置值 | 收发报文、排队和突发流量；实际数量按页面布局取整 |

预算不等于当前已使用量。使用 `display memory-usage` 查看实际堆使用情况，使用 `display dataplane memory` 核对逐节点大页。更多 worker、更多路由或更多邻居会增加内存需求；默认预算不是任意表量的容量承诺。

启动资源在 `reset dataplane` 时生成和应用。先 `commit`、`save`，再安排维护窗口执行重置；普通提交不会在线调整这些启动内存区域。重置会短暂中断数据面。

## 以吞吐为主选择 CPU 和队列

网卡、worker 和报文缓冲池尽量位于同一 NUMA 节点，避免跨节点访问。先用 `display dataplane interfaces` 与 `display dataplane cpu topological` 核对设备和核心位置，再配置 CPU；同一物理核心的两个 SMT 线程不应当作两个独立物理核心估算性能。

RX 队列需要网卡及驱动实际支持。单个端口仅有一条 RX 队列时，增加 worker 不会自动把该队列并行交给多个线程处理；多流量分配还取决于 RSS。单一流量通常仍由同一队列处理。显式队列设置不会因为修改 worker 数量而被自动覆盖。队列、描述符不是越多越好，它们同时消耗缓冲和缓存资源。

例如已确认端口支持两条接收队列时：

~~~text
dataplane
 cpu main-core 2
 cpu worker-cores 3-4
#
 device 0000:03:00.0 name Ethernet 0
  mode dpdk
  queues rx 2 tx 2
 #
#
commit
save
reset dataplane
~~~

PCI 地址和核心编号须按本机拓扑填写。此示例说明配置方法，不代表所有设备适合相同队列数量。只增加 worker 不会使 ARP/MAC 同步等控制面操作按核心数成倍加速。
