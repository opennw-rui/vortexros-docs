# 硬件验收

投入业务前，按实际拓扑核对以下项目。空白系统首装见[首次安装](index.md)。

| 项目 | 检查方法 | 预期 |
| --- | --- | --- |
| 软件和配置 | display version、display health、display configuration storage | 版本符合计划，设备 ready，保存状态符合预期 |
| 网卡归属 | display dataplane、display interface brief | 管理连接可用，业务口状态与驱动归属符合规划 |
| 路由和业务 | 查询邻居及路由，从业务端双向发包 | 路由已安装，实际业务可通过 |
| 重启恢复 | 在维护窗口重启，重复受影响的查询和流量验证 | 保存配置、路由和业务恢复 |
