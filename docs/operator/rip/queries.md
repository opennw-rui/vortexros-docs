# 查询与撤销

## 验证与撤销

```text
display rip 1 interface
display rip 1 database
display rip 1 route
```

在系统视图执行 `undo rip 1` 并提交会删除该进程学习和通告的路由。


[功能目录](../rip.md) · [命令参数](../reference/rip.md)

## 邻居统计与优先级

`display rip 1 interface` 显示实际运行的接口及发送、接收版本；接收列的 `1 2` 表示接受两个版本，不是两个接口。`display rip 1 statistics` 显示已经收到更新的邻居及坏报文、坏路由计数：

```text
Gateway                                 BadPackets BadRoutes Distance Last Update
198.19.80.2                                      0         0      100 00:00:05
Distance: (default is 100)
```

一次双设备验证中，学习的主机路由 Cost 为 2、Preference 为 100，IPv4 ping 为 5/5。协议数据库有路由，还应核对 IP 路由表是否选中及 FIB 是否安装；更高优先级协议可以使 RIP 路由成为备选。

## 计时列

路由表的 TimeLeft 表示当前老化或垃圾回收计时器的剩余时间，格式为分:秒；本地条目显示 -。它不是路由已存在的时长。配置定时器后，用实际更新和路由变化核对，不能只依据当前配置判定旧条目的计时器已经重新开始。
