# 升级与回退

首次安装、升级、检查和模拟统一使用对应版本的单文件 `.run`。包内包含 VortexROS、配套 VPP 和 FRR；安装器比较版本，只更新变化的组件。

## 使用单文件安装包

从[项目Release](https://github.com/opennw-rui/VortexROS/releases)或已提供的0.30-dev安装包位置取得 `.run` 和 `SHA256SUMS`，核对校验值。更新前在 CLI 执行 `save`，确认当前配置和服务收敛，然后运行：

~~~bash
sudo sh ./vortexros-0.30-dev-amd64.run
~~~

安装器自动执行必要的兼容、回退材料和健康检查。需要提前核对下载或查看执行计划时，可选择以下操作：

~~~bash
sha256sum -c SHA256SUMS
sudo sh ./vortexros-0.30-dev-amd64.run --check-only
sudo sh ./vortexros-0.30-dev-amd64.run --simulate
~~~

检查和模拟不安装软件、不重启服务。实际执行保留用户启动 CFG。后端版本相同则保留对应包和进程；后端版本变化时安装器重启受影响的服务，需预留相应的业务中断窗口。

已安装的 Linux-only 设备可以更新，VPP 服务保持停止；VPP 模式继续检查进程及适用的运行版本。安装器要求升级和回退前后的数据面归属一致。

## 回退材料与健康观察

安装器从上次保留的系统包、本地软件包目录或 APT 缓存取得待更新组件的精确旧版本包。统一 `.run` 入口不要求预先创建 `/VortexROS/install`。缺少回退材料时，预检会报告实际缺少的包名和版本。

VPP 软件包声明允许修改的配置文件会按配置文件处理；例如调整大页预留后，不需要先恢复发行版默认值才能升级。程序、共享库、插件和安装脚本仍须与已安装的软件包一致。若曾手工替换这些文件，预检可能报告回退材料不匹配，应核对软件来源和具体不一致项。

恢复按实际依赖推进，每个阶段完成下发与回读后再继续：

| 阶段 | 主要内容 |
| --- | --- |
| 基础层 | 控制进程、接口归属、适用的 Linux 或 VPP/LCP、VRF 和接口配置 |
| 路由层 | FRR、route-zapi、静态与动态路由配置及下发 |
| 业务层 | 当前配置启用的 DHCP、SNMP 等服务 |

FRR 同时负责部分接口地址，进程启动依赖与上述配置恢复阶段不同，不能简单把它延迟到所有接口恢复之后。未启用的业务不要求运行；宿主 SSH、独立管理地址和外部协议邻居上线不属于安装器的稳定判据。

默认基础层稳定观察为 **180 秒**，回退后观察为 **90 秒**。异常首先交给对应服务恢复；安装器每个阶段只允许一次对停止服务的定点启动，不反复重启整个系统。基础层无法恢复时，自动安装准确旧包并重新检查。只有路由或业务服务未恢复时，保留正常的基础系统，明确报告未恢复项目；不能把这种结果当作全部业务正常。

~~~text
display health
display alarm active
display service
display system-software verbose
~~~

`display health`分别显示基础、路由和业务状态。全局 Running/Actual 不一致仍如实保留，不会因为基础层可用就抹掉业务故障。DHCP 恢复只处理实际偏离配置的实例，其他实例保持运行。

| 事务状态 | 含义 |
| --- | --- |
| `committed` | 软件事务已提交；仍需核对是否有业务未恢复提示 |
| `rolled-back` | 目标基础层恢复失败，原版本已恢复并通过观察 |
| `rollback-failed` | 原版本仍未恢复，需检查记录的具体失败原因 |

业务未恢复时，安装器打印 `Software installed; configured services are not fully restored` 警告。通过上面的健康、告警和服务查询定位具体对象，解除实际故障后由对应服务继续恢复。不要用反复执行 `reset dataplane` 代替单个业务服务的修复。

外部故障仍持续时，须先解除故障才能恢复健康；回退旧软件不能代替修复持续不可用的依赖。

## CLI 系统包入口

需要在设备 CLI 操作时，将系统 tar 放到软件目录，使用单目标包命令。此入口与 `.run` 共用通用安装器。

~~~text
check system-software package /VortexROS/install/vortexros-system_VERSION_amd64.tar
simulate system-software package /VortexROS/install/vortexros-system_VERSION_amd64.tar
upgrade system-software package /VortexROS/install/vortexros-system_VERSION_amd64.tar
~~~

主动回退用 `rollback system-software package TARGET.tar`，旧版 `.run` 也可作为更新目标。目标必须能读取当前启动 CFG，并具备当前已安装版本的精确回退材料。本手册从0.29-dev开始维护，不提供此前试验版本的配置迁移保证；操作时保留独立救援入口。

首次安装恢复材料可用时，且尚未执行数据面重置，可按安装器说明执行 `sudo vortexros-safe-upgrade --restore-install` 恢复首次安装前状态。

[系统命令参考](../operator/reference/system.md) · [最终包验证](../release/vortexros.md)
