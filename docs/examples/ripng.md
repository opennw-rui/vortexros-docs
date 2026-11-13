# RIPng 路由

## 拓扑

~~~text
P1 host-p1e12 ─── host-p2e12 P2
链路：2001:db8:12::1/64 → 2001:db8:12::2/64
LoopBack20：2001:db8:20::1 → 2001:db8:20::2
~~~

两端运行独立的 IPv6 路由实验，不应在有同前缀的其他动态协议时评估此例。下列直连重分发只用于隔离实验；生产环境应按需限制发布前缀。

## 配置 P1

~~~text
system-view
interface host-p1e12
 ipv6 address 2001:db8:12::1 64
 quit
interface LoopBack 20
 ipv6 address 2001:db8:20::1 128
 quit
commit
ripng 11
 network 2001:db8:12::/64
 import-route direct
 timers rip 10 30 20
 quit
commit
~~~

## 配置 P2

使用相同配置，将物理接口改成 `host-p2e12`，接口地址改为 `2001:db8:12::2`，LoopBack 地址改为 `2001:db8:20::2`。双方的协议和计时参数相同。

`network` 让实验链路参加协议，`import-route direct` 使本端 LoopBack 前缀可以发布。例中的计时值用于缩短观察时间。

## 验证

~~~text
display ripng 11 route
ping ipv6 -n -c 3 -t 1500 2001:db8:20::2
~~~

P1 实际输出节选：

~~~text
2001:db8:20::2/128                          2     fe80::fe:78ff:fe2a:b801                  host-p1e12             0    00:21
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
~~~

收到路由说明协议已交换前缀；探测同时验证了远端前缀的转发。

## 撤销

在两端执行：

~~~text
system-view
undo ripng 11
commit
display ipv6 routing-table
~~~

实测 P1 不再保留对端 LoopBack 路由。保留双方接口地址；若只用于这次实验，再单独清理。不要删除其他链路正在使用的协议进程。

[RIPng 配置指南](../operator/ripng.md)
