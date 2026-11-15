# 重启 OSPF 进程

需要重新建立指定OSPF进程的运行状态时执行：

~~~text
reset ospf 1 process
~~~

按提示确认后，进程按已提交配置重新启动。该命令会中断目标进程的邻接，可能导致路由撤销和重新收敛；它不是无影响的查询命令。

完成后检查：

~~~text
display ospf 1 peer
display ospf 1 lsdb
display ospf 1 routing
display ip routing-table protocol ospf
~~~

确认邻居恢复Full、所需路由重新进入FIB，再检查业务连通性。配置修改尚未提交时，应先决定提交或放弃，避免把候选配置误认为重启后生效的配置。

[OSPF案例](../../examples/ospf.md) · [命令参考](../reference/ospf.md)
