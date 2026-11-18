# RIP 故障排查

## 接口未参与协议

先检查接口管理状态、链路、IPv4地址和RIP进程的network范围：

~~~text
display interface brief
display ip interface brief
display current-configuration
display rip 1 interface
display rip 1 statistics
~~~

接口Up后，RIP需要短暂启动时间。若接口持续不出现在协议列表中，检查当前接口是否属于正确的VPN实例，以及配置范围是否包含该接口地址。不要仅以邻居或系统路由存在判断本接口已参与RIP。

## 路由未恢复

分别检查RIP协议表和系统路由表。协议中有路由而系统未选中时，检查是否有更优路由或下一跳不可达：

~~~text
display rip 1 route
display ip routing-table protocol rip
display ip fib
display service verbose
display health
~~~

当前配套版本会在接口重建后重新加入协议，并在路由服务恢复后重新安装已有RIP路由。仍有异常时，保留当前配置、协议状态和服务日志以便定位；重启前先收集信息，避免丢失故障状态。

[双端配置案例](../../examples/rip.md) · [RIP参数](../reference/rip.md)
