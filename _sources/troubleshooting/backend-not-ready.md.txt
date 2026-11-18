# 提交后后端未收敛

先检查 CLI 是拒绝了提交，还是已经接受了 Running。拒绝时根据错误修正 Candidate。Running 已接受时，定位当前未就绪的服务。

~~~text
display configuration candidate
display current-configuration
display health verbose
display service verbose
display alarm active
~~~

- `running` 只确认进程状态。检查 `ready`、`converged` 和当前告警，确认服务已可查询且配置已应用。
- VPP 未就绪时，核对数据面模式、PCI 和大页配置。FRR 或 route-zapi 未就绪时，收集同一时段的日志，先等正在进行的回放结束。
- 需要维护性重启且问题已定位到 FRR 时，按[诊断与恢复](../operator/09-operations.md)使用 `reset service frr`。该操作会引起邻居重新收敛。恢复后核对协议邻居、路由表、活动 FIB 和业务流量，再保存配置。

在 Ubuntu 终端采集受影响的服务日志：

~~~bash
sudo journalctl -b -u vortexrosd -u vortexros-vpp -u vortexros-frr -u vortexros-route-zapi --since '-15 min'
~~~
