# 资源与运行查询

## 查询实际状态

`display current-configuration configuration dataplane` 和 dataplane 视图中的 `display this` 显示配置；它们不证明当前 Linux 或 VPP 已应用参数。进入设备子视图后，`display this` 只显示选中的 PCI 设备。

| 命令 | 实际状态和用途 |
|---|---|
| `display dataplane` | 活动后端和 PCI 接管阶段 |
| `display dataplane interfaces` | 期望/活动模式、PCI 驱动、VPP 当前和最大 RX 队列 |
| `display dataplane cpu` | Linux 隔离 CPU、VPP 线程及 CPU |
| `display dataplane memory` | Linux 大页总量、空闲和保留量 |
| `display dataplane iommu` | IOMMU 组和受管设备所属组 |
| `display dataplane tables` | 期望容量、VPP 实际容量、Linux 邻居 GC 阈值 |
| `display dataplane verbose` | 汇总上述运行信息 |

L2FIB 为空时不能凭空读出实时容量，查询单独标记显式 MAC 启动值。大页总量是单页大小乘页数，例如 2M ×1024 为2GiB，不能用进程 VSZ 替代。

## CPU、大页与 IOMMU

~~~text
system-view
dataplane
 cpu main-core 2
 cpu worker-cores 3-5
 cpu isolation enable
 memory hugepages size 2M count 1024
 iommu enable
quit
commit
save
display dataplane cpu
display dataplane memory
display dataplane iommu
reset dataplane
~~~

这是参数示例，CPU/NUMA/PCI 条件按本机调整，不能覆盖唯一管理路径。主核和 worker 不重叠，CPU 编号从0开始。配置 worker 时必须同时指定主核。引导参数需要主机重启时会提示；只生成 GRUB 片段不代表当前内核已生效。

真实 QEMU PCI 验收用 main0/worker1、RX/TX各1队列、描述符512，激活后实际线程/队列与配置一致、业务2/2；撤销 worker/队列/描述符后，恢复单 main0 和该 virtio 驱动默认256描述符，业务仍2/2。该默认值不外推到其他驱动。

## 撤销

先按[设备接管](devices.md)确认是否需保留 DPDK。单独撤销 worker 时：

~~~text
system-view
dataplane
 undo cpu worker-cores
 undo cpu main-core
 undo cpu isolation enable
 undo memory hugepages
 undo iommu enable
quit
commit
save
reset dataplane
~~~

先撤销 worker 再撤销主核。仍有设备依赖特定启动条件时，不能靠撤销资源参数强制实现可用的 DPDK；应按激活提示处理，检查[恢复结果](recovery.md)。生产变更前确保可恢复管理路径。

[完整参数](../reference/dataplane.md)
