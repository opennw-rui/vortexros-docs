# RIP 路由

## 拓扑

~~~text
P1 host-p1e12 ─── host-p2e12 P2
链路：10.201.12.1/24 → 10.201.12.2/24
LoopBack20：10.255.20.1 → 10.255.20.2
~~~

两端运行独立的 IPv4 路由实验，不应在有同前缀的其他动态协议时评估此例。下列直连重分发只用于隔离实验；生产环境应按需限制发布前缀。

## 配置 P1

~~~text
system-view
interface host-p1e12
 ip address 10.201.12.1 255.255.255.0
 quit
interface LoopBack 20
 ip address 10.255.20.1 255.255.255.255
 quit
commit
rip 10
 version 2
 network 10.0.0.0
 import-route direct
 timers rip 10 30 20
 quit
commit
~~~

## 配置 P2

使用相同配置，将物理接口改成 `host-p2e12`，接口地址改为 `10.201.12.2`，LoopBack 地址改为 `10.255.20.2`。双方的协议和计时参数相同。

`network` 让实验链路参加协议，`import-route direct` 使本端 LoopBack 前缀可以发布。例中的计时值用于缩短观察时间。

## 验证

~~~text
display rip 10 route
ping -n -c 3 -t 1500 10.255.20.2
~~~

P1 实际输出节选：

~~~text
10.255.20.2/32                              2     10.201.12.2                              10.201.12.2            0    00:29
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
~~~

收到路由说明协议已交换前缀；探测同时验证了远端前缀的转发。

## 撤销

在两端执行：

~~~text
system-view
undo rip 10
commit
display ip routing-table
~~~

实测 P1 不再保留对端 LoopBack 路由。保留双方接口地址；若只用于这次实验，再单独清理。不要删除其他链路正在使用的协议进程。

[RIP 配置指南](../operator/rip.md)
