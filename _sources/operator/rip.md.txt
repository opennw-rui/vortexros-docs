# RIP

使用 RIPv2 在 IPv4 网络交换路由。当前配套FRR 缺省优先级为 100，可在进程视图用 `preference <值>` 调整。默认 100 不显示在配置中；`undo preference` 恢复默认。修改优先级后，已有路由在后续 RIP 更新时重新选路，应以实际路由表为准。

[命令参考](reference/rip.md) · [配置案例](../examples/rip.md)

~~~{toctree}
:maxdepth: 2

rip/configuration
rip/queries
rip/recovery
~~~
