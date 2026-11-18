# 进程与发布

## 配置


```text
rip 1
 version 2
 network 10.0.0.0
 default-metric 2
 maximum load-balancing 4
 timers rip 30 180 120
 silent-interface LoopBack 0
#
```

`network`使用IPv4主类网络地址。提交后匹配接口参加RIP，silent-interface仍发布该接口网络，但不从该接口发送更新。


[功能目录](../rip.md) · [命令参数](../reference/rip.md)

## 缺省版本与 metric

未配置 `version` 时，进程发送 RIPv2，并接受 RIPv1 与 RIPv2。显式 `version 2` 同时将接收限制为 RIPv2，因此不等同于“只把默认发送版本写一遍”。每个实际运行接口的发送、接收版本以 `display rip 1 interface` 为准。

默认重分发 metric 为 1；它不是把每条已学习路由的跳数固定为 1。默认不启用 ECMP，相同前缀只保留一条转发路径；需要多路径时配置进程的 `maximum load-balancing` 并核对实际路由。摘要使用生效默认值，不用配置模型中的 0 代表协议运行值。


## 重分发开销和默认路由

在 RIP 进程中配置 import-route static 后，default-metric 决定引入静态前缀的通告开销。对端通常在接收时增加一跳：本例使用 4 时，对端 Cost 为 5；改为 6 后为 7，undo default-metric 恢复默认值 1 后为 2。应以对端显示的实际跳数验证效果。

default-route originate 发布默认路由；undo default-route originate 停止发布。接收端已有更优默认路由时，RIP 默认路由可能只保留在协议数据库中，因此应同时检查 display rip 1 database 和 IP 路由表。撤销后，其他来源的默认路由可以继续存在。

## 定时器与静默接口

默认 Update/Timeout/Garbage 为 30/180/120 秒。timers rip 5 15 10 可缩短实验中的更新和失效等待；两端应协调设置，避免对端仍每 30 秒更新、本端却每 15 秒超时。undo timers rip 恢复默认。

silent-interface 不从指定接口发送更新，但该接口的网段仍可经其他接口发布。使用全局静默时，可显式开放需要交换路由的接口。已学习路由按老化计时器到期，不保证执行静默命令后立即撤销。一次双端配置中，停止更新后 IPv4 选路回退到 OSPF，IPv6 RIPng 选中路由归零；恢复发送后，RIP 与 RIPng 重新学到 Cost 2 的主机路由，双栈探测各 2/2。恢复定时器后，对端新收到的 RIP 路由 TimeLeft 为 02:55，符合 180 秒超时设置。

## 全局静默与例外

`passive-interface default` 停止从本进程的接口发送更新。需要保留邻接的接口可用 `undo silent-interface Ethernet0` 作为活跃例外；再次执行 `silent-interface Ethernet0` 撤销该例外。`undo passive-interface default` 恢复普通模式，同时清除静默列表和活跃例外。RIPng 采用相同的命令行为。

```text
rip 1
 passive-interface default
 undo silent-interface Ethernet0
#
commit
display rip 1 interface
display rip 1 route
```

恢复全部接口正常发送：

```text
rip 1
 undo passive-interface default
#
commit
```

`preference 137` 修改 RIP 路由优先级，值越小越优；`undo preference` 恢复默认100。实际学习路由由100变为137，撤销后回到100。协议数据库中存在路由不保证该路由胜出，还应核对 `display ip routing-table protocol rip`。
