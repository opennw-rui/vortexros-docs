# IPv4/IPv6 路由引入

`import-route`用于导入IPv4路由，`ipv6 import-route`用于导入IPv6路由：

```text
isis 10
 import-route static
 ipv6 import-route static
 ipv6 import-route ospfv3
```

系统根据进程的IS-IS level生成FRR要求的`level-1`或`level-2`重分发命令；默认level-1-2会同时下发两级，避免后端接受命令时因缺少level而拒绝配置。


[双端配置和真实路由](../../examples/isis.md) · [全部参数](../reference/isis.md)
