# 升级与回退

首次安装、升级、检查和模拟统一使用对应版本的单文件 `.run`。包内包含 VortexROS、配套 VPP 和 FRR；安装器比较版本，只更新变化的组件。

## 使用单文件安装包

从[Debug 9 发布页](https://github.com/opennw-rui/VortexROS/releases/tag/v0.28-dev-debug9)下载 `.run` 和 `SHA256SUMS`，核对校验值。更新前在 CLI 执行 `save`，确认当前配置和服务收敛，然后运行：

~~~bash
sha256sum -c SHA256SUMS
sudo sh ./vortexros_0.28-dev-debug9_amd64.run --check-only
sudo sh ./vortexros_0.28-dev-debug9_amd64.run --simulate
sudo sh ./vortexros_0.28-dev-debug9_amd64.run
~~~

检查和模拟不安装软件、不重启服务。实际执行保留用户启动 CFG。后端版本相同则保留对应包和进程；后端版本变化时安装器重启受影响的服务，需预留相应的业务中断窗口。

已安装的 Linux-only 设备可以更新，VPP 服务保持停止；VPP 模式继续检查进程及适用的运行版本。安装器要求升级和回退前后的数据面归属一致。

## 回退材料与健康观察

安装器从上次保留的系统包、本地软件包目录或 APT 缓存取得待更新组件的精确旧版本包。统一 `.run` 入口不要求预先创建 `/VortexROS/install`。缺少回退材料时，预检会报告实际缺少的包名和版本。

Debug 9 在预检中逐项检查 `vortexros.target`、FRR、route-zapi、switchd 和 vortexrosd；观察期间逐项检查四个关键服务，并验证配置、数据面和严格健康状态。最后一次严格健康采样后，还会再次核对服务与数据面不变量。服务刚停时，daemon 的健康快照可能尚未刷新，不能只看一个 ready 结果。

默认目标版本稳定观察为 **180 秒**，回退版本稳定观察为 **90 秒**。目标失败时自动尝试回退。用 CLI 查看事务：

~~~text
display system-software verbose
~~~

| 状态 | 含义 |
| --- | --- |
| `committed` | 目标版本完成连续健康观察 |
| `rolled-back` | 目标失败，原版本已恢复并通过观察 |
| `rollback-failed` | 原版本未能恢复健康，需使用救援入口检查失败原因 |

外部故障仍持续时，须先解除故障才能恢复健康；回退旧软件不能代替修复持续不可用的依赖。

## CLI 系统包入口

需要在设备 CLI 操作时，将系统 tar 放到软件目录，使用单目标包命令。此入口与 `.run` 共用通用安装器。

~~~text
check system-software package /VortexROS/install/vortexros-system_VERSION_amd64.tar
simulate system-software package /VortexROS/install/vortexros-system_VERSION_amd64.tar
upgrade system-software package /VortexROS/install/vortexros-system_VERSION_amd64.tar
~~~

主动回退用 `rollback system-software package TARGET.tar`，旧版 `.run` 也可作为更新目标。目标必须能读取当前启动 CFG，并具备当前已安装版本的精确回退材料。较早的 Debug 6 无法读取包含 Debug 7 受管账号的 CFG，需保留原文件并选择兼容的启动配置，操作时保留独立救援入口。

首次安装恢复材料可用时，且尚未执行数据面重置，可按安装器说明执行 `sudo vortexros-safe-upgrade --restore-install` 恢复首次安装前状态。

[系统命令参考](../operator/reference/system.md) · [最终包验证](../release/vortexros.md)
