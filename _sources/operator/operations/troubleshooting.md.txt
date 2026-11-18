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

## 服务状态与健康

服务显示区分 Running、Ready 和 Converged。进程运行不等于控制连接就绪，已提交配置代号相同也不等于所有依赖服务可用。一次路由服务停止时，display health 为 not-ready，health check 返回失败；服务恢复后重新为 ready，配置代号保持不变。

进程与版本信息按服务监视周期更新；控制连接的就绪状态更新更频繁。因此短暂故障中 Running/PID 与 Ready 的更新时间可能不同，应以严格健康结果及实际业务综合判断。

历史告警的实际示例：

```text
Severity  Subsystem  Code              Resource  Count
major     reconcile  RECONCILE_FAILED  running   4
```

故障恢复后，该记录仍可在 display alarm history last 10 中查看，而 display alarm active 返回 No alarms。Count 是同类故障累计次数，不是丢包数。
