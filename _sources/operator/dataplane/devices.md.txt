# 设备与接管


```text
dataplane
 cpu main-core 2
 cpu worker-cores 3-5
#
 device 0000:03:00.0 name Ethernet 0
  mode dpdk
  queues rx 2 tx 2
  descriptors rx 1024 tx 1024
  undo hardware offload tso
 #
#
interface user-defined Ethernet0
 ip address 192.0.2.10 255.255.255.0
#
```

CLI 操作：

```text
commit
save
display dataplane verbose
reset dataplane
```

PCI 地址用于定位硬件，`name Ethernet 0` 将接口命名为 `Ethernet0`。物理口默认为
`kernel`。`undo mode` 恢复 Linux 驱动。按 `interface user-defined` 预配置的接口
以普通 `interface Ethernet0` 视图保存，地址和静态路由在设备就绪后下发。

CPU 编号从 0 开始，`cpu main-core 0` 是有效的显式配置，会保留在已提交配置和保存文件中。指定 `cpu worker-cores` 时必须同时指定主核；先撤销 worker，再撤销主核。`undo queues`、`undo descriptors` 和 `undo cpu worker-cores` 清除显式设置，实际线程与硬件参数在保存并执行 `reset dataplane` 后更新。配置查询显示已提交值，不能替代运行状态查询。

队列和描述符是交给驱动的启动请求，实际能力由网卡和驱动决定。使用 `display dataplane interfaces` 查看当前/最大 RX 队列；例如 `1/1` 表示当前 1 队列、最多 1 队列，不代表已启用多队列。配置文件中的请求值不能代替实际值，规划 worker 时应以运行查询为准。

未加入 `device` 清单的物理接口继续由 Linux 管理。启用一个 DPDK 设备不会要求其他 Linux 物理口也出现在 VPP 中；混合部署下，接口详情、描述、统计和简表同时显示两类接口，分别读取对应后端。

CPU 隔离、大页和 IOMMU 的引导参数由数据面激活流程生成到受管 GRUB 片段。安装包包含提供 `update-grub` 的必要依赖。需要重启主机的参数会给出提示；配置和片段已经生成不代表当前内核已使用这些参数。使用自定义引导方式时，应确认该方式实际加载了所需内核参数。

`reset dataplane` 确认后生成 udev 规则、变更物理网卡名称并核对 Linux 配置。
之后为选择 DPDK 的设备生成 VPP 启动配置并接管。接管失败时恢复 Linux 驱动和回放地址、
路由，保留已经验证的 Ethernet 名称。外部网络管理器由用户维护。


[数据面总览](../dataplane.md) · [逐条命令](../reference/dataplane.md)


## 先配置、后出现的接口

在接口暂时不存在时，可以先建立普通三层配置。示例：

```text
interface user-defined Ethernet97
 ip address 198.18.247.1 255.255.255.252
 ipv6 enable
 ipv6 address 2001:db8:247:97::1 64
#
ip route-static 198.18.246.97 255.255.255.255 198.18.247.2
ipv6 route-static 2001:db8:246:97::2 128 2001:db8:247:97::2
```

提交后，配置保存在接口的普通配置段中，user-defined 不写入保存配置。该命令不会创建网卡。Linux 数据面下，接口出现后自动下发地址及依赖路由，不需要再执行一次 commit；VPP 数据面仍要求相应 VPP 接口实际存在。

接口就绪后查询：

```text
display interface Ethernet97
display ip routing-table 198.18.246.97
display ipv6 routing-table 2001:db8:246:97::2
ping -c 2 198.18.246.97
ping ipv6 -c 2 2001:db8:246:97::2
```

实际验证中，预配置接口出现后，IPv4、IPv6 地址及两条静态路由自动安装；两条路由的 Preference 均为 60，双栈探测各为 2/2。应以接口实际地址和路由查询为准，不以首次提交成功作为接口已经存在的证明。

撤销依赖路由后再删除接口配置：

```text
undo ip route-static 198.18.246.97 255.255.255.255 198.18.247.2
undo ipv6 route-static 2001:db8:246:97::2 128 2001:db8:247:97::2
undo interface Ethernet97
```

提交后核对路由和接口配置已移除，按需 save。删除配置不等于删除 Linux 中由其他方式创建的网卡。

## 预配置接口的再次进入

用 interface user-defined 声明的接口可以继续使用普通接口命令进入，例如 interface Ethernet 98 或 interface Ethernet98。接口尚未出现时，配置仍保留；问号帮助和按编号补全也包含这些已声明的接口。未声明、设备中也不存在的普通物理接口仍不能直接进入，避免误拼名称生成配置。

## 待生效模式与业务状态

提交把接口改为 DPDK 后，现有数据面归属保持到执行 `reset dataplane`。用 `display dataplane interfaces` 核对期望模式和实际模式，再用 `display interface Ethernet9` 核对实际业务口。变更待生效期间，仍归 Kernel 的接口继续使用原地址和转发。

实测对照中，提交后期望模式为 DPDK、实际模式为 Kernel，接口的 IPv4、IPv6 探测各 2/2。未安排数据面切换时，在设备视图执行 `undo mode` 恢复默认 Kernel，提交并核对两种模式。
