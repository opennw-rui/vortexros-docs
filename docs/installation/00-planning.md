# 规划与前置条件

## 硬件与虚拟机

| 项目 | 建议 | 检查方法 |
|---|---|---|
| 架构 | x86_64 | `uname -m` |
| 系统 | Ubuntu 26.04 | `cat /etc/os-release` |
| CPU | 为控制面预留至少 1 个逻辑核；VPP worker 不与繁忙控制面长期重叠 | `lscpu -e` |
| NUMA | 网卡、hugepage、VPP worker 尽量处于同一 NUMA 节点 | `lspci -vv`、`numactl -H` |
| hugepage | 按实际端口、队列和buffer规划；安装器可生成保守默认值，投产前仍需核对 | `grep -i huge /proc/meminfo` |
| IOMMU | PCI 直通场景必须启用并形成 IOMMU group | `find /sys/kernel/iommu_groups -maxdepth 2 -type l` |
| 存储 | `/VortexROS`、`/var/lib/vortexros` 和日志保留量留出余量 | `df -h` |

## 接口与地址规划

安装前记录：

- Linux 管理接口、地址、默认路由和精确管理明细路由；
- 每个待接管接口的 PCI BDF、原生驱动、MAC、MTU 和 Linux 名称；
- 哪些接口由 VPP 接管，哪些永久保留给 Linux；
- VPN-instance、VLAN、子接口和动态路由地址规划；
- TCP/22上的Linux OpenSSH是否可用，以及哪些Linux用户可通过sudo进入VortexROS CLI。

建议将清单保存在设备外部。不要把唯一管理接口直接列入首次 VPP 接管范围。

## 只读预检查和安装预演

安装依赖前可以从源码树运行：

```bash
sudo deploy/first-install.sh --plan --verbose
sudo vortexros-bootstrap install --dry-run
sudo vortexros-bootstrap install --dry-run --nic 0000:03:00.0 --nic 0000:03:00.1
```

把示例BDF替换为计划交给VPP的接口；正式安装会拒绝没有`--nic`的调用，也会默认拒绝SSH路径或默认路由所在接口。如果VortexROS或必要组件尚未安装，检查结果会列出对应的`WARN/FAIL`。上述命令不会创建目录或改变服务。

## 影响说明

本章只有读取操作，不改变软件包、服务、文件、网络、路由或驱动状态。
