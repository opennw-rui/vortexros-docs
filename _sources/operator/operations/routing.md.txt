# 路由服务恢复

## 动态路由服务恢复

动态路由服务异常时，先检查具体协议的邻居和路由，再重启最小范围的服务。重启协议服务不会修改已保存配置，服务恢复后设备会重新应用已经提交的协议配置。

```text
display service verbose
display ip routing-table
display ospf peer brief
display bgp peer
display bfd
```


[目录](../09-operations.md)
