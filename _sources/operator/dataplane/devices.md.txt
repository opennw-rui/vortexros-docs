# 设备与接管


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

CPU 编号从 0 开始，`cpu main-core 0` 是有效的显式配置，会保留到保存文件和 daemon 通信中。指定 `cpu worker-cores` 时必须同时指定主核；先撤销 worker，再撤销主核。`undo queues`、`undo descriptors` 和 `undo cpu worker-cores` 清除显式设置，实际线程与硬件参数在保存并执行 `reset dataplane` 后更新。配置查询显示已提交值，不能替代运行状态查询。

未加入 `device` 清单的物理接口继续由 Linux 管理。启用一个 DPDK 设备不会要求其他 Linux 物理口也出现在 VPP 中；混合部署下，接口详情、描述、统计和简表同时显示两类接口，分别读取对应后端。

CPU 隔离、大页和 IOMMU 的引导参数由数据面激活流程生成到受管 GRUB 片段。安装包包含提供 `update-grub` 的必要依赖。需要重启主机的参数会给出提示；配置和片段已经生成不代表当前内核已使用这些参数。使用外部内核或直接传入 QEMU 内核的实验环境，还需由其启动方式应用内核参数。

`reset dataplane` 确认后生成 udev 规则、变更物理网卡名称并核对 Linux 配置。
之后为选择 DPDK 的设备生成 VPP 启动配置并接管。接管失败时恢复 Linux 驱动和回放地址、
路由，保留已经验证的 Ethernet 名称。外部网络管理器由用户维护。


[数据面总览](../dataplane.md) · [逐条命令](../reference/dataplane.md)
