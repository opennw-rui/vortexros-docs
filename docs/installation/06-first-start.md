# 首次启动与验收

通用安装器会启动 VortexROS 服务。安装成功后，执行 sudo vortexros 进入 CLI，再运行：

~~~text
display health
display interface brief
display license
~~~

健康状态应为 ready。接口列表用于确认实际业务口和链路状态。配置首条路由并检查连通性的完整步骤见[从零到 Ping](../quickstart.md)。

## 授权与试用

从 0.30-dev Debug 9 起，默认安装包在设备首次启动 VortexROS 时自动启用 **72 小时试用**。
可用 `display license` 查看授权状态、开始时间、到期时间和剩余秒数。关机期间计时继续，重启和升级沿用原到期时间。

开发版和正式版需要管理员导入签发的授权。先在用户视图导出本机申请，再交给签发方：

~~~text
license request export router01.vreq
~~~

把收到的 `router01.vlic` 放到设备的 `/VortexROS/license/`，导入后确认 `License status` 为 `active`，且 `Configuration access` 为 `enabled`：

~~~text
license import router01.vlic
display license
~~~

试用到期后仍可查看状态、运行诊断和导入授权，已配置的业务继续转发。安装含签发要求的版本前，应准备该设备的有效授权。

## 有异常时

| 现象 | 查看 | 处理 |
| --- | --- | --- |
| CLI 无法连接 | Linux 终端执行 systemctl status vortexrosd | 查看服务报错与同次安装日志 |
| 服务已启动，但配置尚未收敛 | display health verbose、display alarm active | 按告警定位后端或接口 |
| 接口不存在或链路未恢复 | display interface brief | 核对实际名称、连接与当前驱动归属 |

部署到业务环境前，可按[硬件验收](08-hardware-acceptance.md)检查相关功能。
