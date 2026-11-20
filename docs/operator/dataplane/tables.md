# 邻居与 MAC 容量


```text
dataplane
 neighbor ipv4 limit 102400
 neighbor ipv6 limit 102400
 mac-address learn-limit 102400
#
```

CLI 操作：

```text
commit
save
display current-configuration configuration dataplane
display dataplane verbose
```
IPv4 邻居、IPv6 邻居和动态 MAC 学习的上限**各自默认为 102400**，不是三者合计 102400。IPv4/IPv6 分别在各自协议族内统计，动态 MAC 为跨桥域的全局学习计数。同一个 MAC 在不同桥域中占用不同表项。配置省略上限时，直接应用当前版本的默认值。等于默认值的命令不会写入配置。
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


[数据面总览](../dataplane.md) · [逐条命令](../reference/dataplane.md)


## 在线修改的实际对照

在 dataplane 视图将 IPv4、IPv6 上限都设为110000并提交后，display dataplane tables 的两族活动容量均为110000，Linux回收阈值均为27500/55000/110000。对应 undo 并提交后，两族活动容量恢复102400，阈值恢复25600/51200/102400。该过程未重启VPP；MAC学习容量保持102400。

## 扩容与承载验证

需要提高容量时，例如设置为默认值的两倍：

```text
dataplane
 neighbor ipv4 limit 204800
 neighbor ipv6 limit 204800
 mac-address learn-limit 204800
#
```

提交后，两族邻居容量在线更新；MAC 学习容量需要保存后重置数据面，重置会中断数据面业务，应安排维护窗口。

```text
commit
return
save
reset dataplane
display dataplane tables
```

恢复默认配置：

```text
dataplane
 undo neighbor ipv4 limit
 undo neighbor ipv6 limit
 undo mac-address learn-limit
#
```

再执行 `commit`、`save`、`reset dataplane` 并查询。默认值不会出现在配置中。

动态 MAC 学习名额不包含静态 MAC；达到学习上限不等于对所有未知目的流量执行丢弃。IPv4/IPv6 的 VPP 邻居分配计数与 Linux 的 GC 策略也不同，Linux 永久邻居不按非永久邻居阈值计算，不能把这些参数视为同一种硬配额。三张表的项数不能直接相加当作可连接终端数。

Debug 5 定向测试已验证 IPv4 邻居和动态 MAC 同时各有102400项、提高后同时各有204800项，在指定1.0Mpps负载下均完成转发。条件和限制见[性能参考](../../release/performance.md)。该结果不承诺所有CPU、功能组合及长期老化负载下都达到相同规模或速率。
