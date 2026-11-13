# 数据面

选择由 Linux 或 DPDK 管理的设备，并配置 CPU、内存、队列和容量。

[命令参考](reference/dataplane.md)

## 设备配置

```text
dataplane
 device 0000:03:00.0 name Ethernet 0
  mode dpdk
  queues rx 2 tx 2
  descriptors rx 1024 tx 1024
  undo hardware offload tso
 quit
 cpu main-core 2
 cpu worker-cores 3-5
quit
interface user-defined Ethernet0
 ip address 192.0.2.10 255.255.255.0
quit
commit
save
display dataplane verbose
reset dataplane
```

PCI 地址用于定位硬件，`name Ethernet 0` 将接口命名为 `Ethernet0`。物理口默认为
`kernel`。`undo mode` 恢复 Linux 驱动。按 `interface user-defined` 预配置的接口
以普通 `interface Ethernet0` 视图保存，地址和静态路由在设备就绪后下发。

`reset dataplane` 确认后生成 udev 规则、变更物理网卡名称并核对 Linux 配置。
之后为选择 DPDK 的设备生成 VPP 启动配置并接管。接管失败时恢复 Linux 驱动和回放地址、
路由，保留已经验证的 Ethernet 名称。外部网络管理器由用户维护。

### 邻居与 MAC 学习上限

```text
dataplane
 neighbor ipv4 limit 102400
 neighbor ipv6 limit 102400
 mac-address learn-limit 102400
quit
commit
save
display current-configuration configuration dataplane
display dataplane verbose
```
IPv4、IPv6 和 MAC 学习上限默认为 102400。配置省略上限时，直接应用当前版本的默认值。等于默认值的命令不会写入配置。
IPv4 和 IPv6 邻居上限范围为 4–2147483647，分别作用于 ARP 和 ND。提交后 Linux
立即更新对应协议族的三个回收阈值，分别为上限的四分之一、二分之一和全值（向下取整）。
VPP 在线时同步更新容量，VPP 启动和 Linux 重启时根据保存的配置回放。
`ipv6 nd max-number` 修改同一个 IPv6 容量值。

MAC 学习上限范围为 1–2147483647。它约束 VPP 全局动态学习，桥域还受自身学习限制。
MAC 配置变更后，保存并执行 `reset dataplane` 才生效。该参数不修改 Linux bridge 的学习上限。
三个 `undo` 命令分别恢复 102400。配置上限和实际可承载规模需要分别核验。

在 `dataplane` 视图中，`display this` 只显示该视图的已提交配置。进入设备子视图后，
它只显示选中的 PCI 设备。`display dataplane` 显示活动后端和 PCI 接管状态。`display dataplane verbose` 汇总运行信息，各部分也可单独查询。

- `display dataplane interfaces` 显示期望与活动模式、PCI 驱动及 VPP 当前和最大 RX 队列数。
- `display dataplane cpu` 显示 Linux 隔离 CPU 和 VPP 线程。
- `display dataplane memory` 显示 Linux 大页总量、空闲和保留量。
- `display dataplane iommu` 显示 IOMMU 组及受管设备所在组。
- `display dataplane tables` 对照期望容量、VPP 运行容量及 Linux GC 阈值。L2FIB 为空时，运行值不可读，显式生成的 MAC 启动值会单独标出。
