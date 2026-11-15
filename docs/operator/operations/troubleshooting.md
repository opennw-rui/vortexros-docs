# 故障定位

## 告警与日志

告警显示严重度、功能模块、错误码、受影响对象、首次/最近发生时间、累计次数以及当前是否已恢复。相同故障会合并计数，避免重复信息淹没有效日志。

```text
display alarm active
display alarm history last 100
journalctl -u vortexrosd -u vortexros-vpp -u vortexros-frr -u vortexros-route-zapi
```


## 故障处理顺序

1. 保住管理连接和当前会话；
2. 记录 `display health/service/alarm`；
3. 判断是配置错误、接口/路由依赖缺失，还是相关服务未就绪；
4. 先等待当前自动恢复动作完成；
5. 再执行最小范围reset；
6. 修复待提交配置后重新commit并检查状态；
7. 业务验证通过后save。

不要直接删除 `/var/lib/vortexros`、`/run/vortexros` 或服务运行目录来“清错”，否则可能破坏自动恢复所需的信息。无法恢复时先保存display和日志信息，再按安装手册中的恢复流程处理。

[目录](../09-operations.md)
