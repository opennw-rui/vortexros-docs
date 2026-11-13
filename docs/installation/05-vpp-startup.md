# 准备 VPP startup

使用新数据面视图时，`commit` 和 `save` 保存硬件配置，由 `reset dataplane`
生成 VPP 启动文件及 Linux 启动参数。操作示例见[数据面设备配置](../operator/03-interfaces-l2.md#数据面设备配置)。

`vortexros-bootstrap install --nic PCI-BDF ...`可以依据CPU、内存、PCI父设备和内核队列能力生成`/VortexROS/startup.conf`。`--nic`是必需的精确白名单；已有配置默认保留，只有使用`--replace-startup`才会替换。管理员仍须在投产前核对NUMA、队列和业务接口范围。

## 最小原则

- 只列入确实需要 VPP 接管的 PCI 设备；不要动保留给 Linux 的管理网卡。
- 安装器默认拒绝当前SSH路径或默认路由所在接口；`--allow-management-nic`只适用于已有带外控制台并完成外部恢复演练的场景。
- worker、RX queue 和 NUMA 分配应与实际硬件一致。
- 不启用 LRO；其他 offload 由运行时驱动能力管理。
- 插件保持产品要求的启用策略，明确禁用会与 LCP 冲突的 ARP/ping 数据面处理。
- 建议将运行日志保留为`notice`、systemd journal输出限制为`warning`，避免邻居和Netlink普通事件持续占用journal：

  ```text
  logging {
    default-log-level notice
    default-syslog-log-level warn
  }
  ```

  该设置不隐藏warning/error，也不改变Binary API错误和`display health`结果。
- 在远程单网卡环境中，先完成 Linux 模式配置和保存，再尝试接管。

## 权限与验证

```bash
sudo install -d -m 0755 /VortexROS
sudoedit /VortexROS/startup.conf
sudo chmod 0640 /VortexROS/startup.conf
sudo vortexros-safe-upgrade --host-check --verbose
```

检查器会读取配置、核对 PCI BDF 和 IOMMU 条件，但不会改写 startup、绑定驱动或启动 VPP。

## 接管失败的预期行为

若接口已脱离 Linux，但 VPP 未识别：

1. 本次 `reset dataplane` 激活失败；
2. VPP 接管事务停止；
3. 所有本次接管接口整体恢复原生驱动；
4. Linux netdev、MAC、MTU、admin、IP、VRF 和路由恢复并回读；
5. 已保存的数据面设置保留供修正，Running 继续使用 Linux 数据面。

使用 `display vpp takeover transaction` 和 `display vpp interface-ownership verbose` 查看阶段及失败原因。

## 已有 VPP 设备迁移

记录原 PCI 地址、端口名、CPU、队列、大页及 VPP 启动文件中的其他设置，再准备并校验
转换后的 CFG。物理口改名时同步转换接口配置和引用。大页总量按页大小乘以页数计算，
例如 `2M count 1024` 为 2 GiB。VPP 主堆是另一项独立设置。

如果 SSH 经过 Vlanif、隧道或其他依赖 VPP 的接口，先准备独立的恢复入口。
Linux 回退恢复物理网卡的驱动、接口名、地址和路由，原来依赖 VPP 的管理链路会随
VPP 停止而中断。
