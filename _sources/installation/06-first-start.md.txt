# 首次启动与验收

通用安装器会启动 VortexROS 服务。安装成功后，执行 sudo vortexros 进入 CLI，再运行：

~~~text
display health
display interface brief
~~~

健康状态应为 ready。接口列表用于确认实际业务口和链路状态。配置首条路由并检查连通性的完整步骤见[从零到 Ping](../quickstart.md)。

## 有异常时

| 现象 | 查看 | 处理 |
| --- | --- | --- |
| CLI 无法连接 | Linux 终端执行 systemctl status vortexrosd | 查看服务报错与同次安装日志 |
| 服务已启动，但配置尚未收敛 | display health verbose、display alarm active | 按告警定位后端或接口 |
| 接口不存在或链路未恢复 | display interface brief | 核对实际名称、连接与当前驱动归属 |

部署到业务环境前，可按[硬件验收](08-hardware-acceptance.md)检查相关功能。
