# 重启 OSPF 进程

需要重新建立指定OSPF进程的运行状态时执行：

~~~text
reset ospf 1 process
~~~

按提示确认后，指定进程的运行状态按已提交配置重新建立。该命令会中断目标进程的邻接，可能导致路由撤销和重新收敛；它不是无影响的查询命令。

完成后检查：

~~~text
display ospf 1 peer
display ospf 1 lsdb
display ospf 1 routing
display ip routing-table protocol ospf
~~~

确认邻居恢复Full、所需路由重新进入FIB，再检查业务连通性。配置修改尚未提交时，应先决定提交或放弃，避免把候选配置误认为重启后生效的配置。

[OSPF案例](../../examples/ospf.md) · [命令参考](../reference/ospf.md)

## Router ID 修改与自动选择

在 OSPF 进程视图使用 `router-id 10.0.0.1` 显式指定标识；`undo router-id` 恢复自动选择。自动选择优先使用同 VPN 的 LoopBack IPv4 地址，没有时使用其他合适的 IPv4 接口地址。配置改变不会无提示地重建既有邻接；如果当前运行的 Router ID 尚未切换，提交会明确提示需要重置。

单个 OSPFv2 进程可以使用上面的定向命令。设备同时配置多个 OSPFv2 进程时，当前实现不能隔离重置其中一个，必须使用服务级操作：

~~~text
reset service ospf
~~~

该操作重启本机 OSPFv2 和 OSPFv3 服务，并回放已提交配置，所有相关邻接都会重新建立。不要在需要保留其他邻接的业务窗口执行。OSPFv3 可使用 `reset ospfv3 2 process` 重置指定 VPN 中的进程，不需要重启整个服务。

一次自动选择的实际结果是：同 VPN 环回地址为 203.0.113.104，撤销显式 Router ID 并完成所需重置后，OSPFv2 与 OSPFv3 均显示 Router ID 203.0.113.104，邻居 Full；OSPF 学习的 203.0.113.102/32 为 Preference10、Cost20，指定源探测2/2。该数值来自本例接口地址，不是固定默认值。

恢复显式 Router ID 时，在对应进程重新执行 `router-id 地址`、提交并按同样原则重置；随后确认邻接、路由和业务均恢复，再保存配置。
