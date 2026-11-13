# OSPFv3 邻接

## 拓扑

~~~text
LoopBack20 2001:db8:20::1/128          LoopBack20 2001:db8:20::2/128
P1 host-p1e12 2001:db8:12::1/64 ─── 2001:db8:12::2/64 host-p2e12 P2
~~~

两端使用默认 VPN、进程 1、Area 0。链路使用点到点网络类型，两端 Hello/Dead 设置相同。链路地址和测试 LoopBack 先提交，然后启用协议。

## 配置 P1

~~~text
system-view
interface host-p1e12
 ipv6 address 2001:db8:12::1 64
 quit
interface LoopBack 20
 ip address 10.255.20.1 255.255.255.255
 ipv6 address 2001:db8:20::1 128
 quit
commit
ospfv3 1 router-id 10.255.20.1
 area 0.0.0.0
  quit
 quit
interface host-p1e12
 ospfv3 1 area 0.0.0.0
 ospfv3 network-type p2p
 ospfv3 timer hello 3
 ospfv3 timer dead 12
 quit
interface LoopBack 20
 ospfv3 1 area 0.0.0.0
 quit
commit
~~~

## 配置 P2

使用同一命令块，将接口改为 `host-p2e12`，三个本端地址分别改为 `2001:db8:12::2`、`10.255.20.2` 和 `2001:db8:20::2`；Router ID 也改为 `10.255.20.2`。Area、网络类型和计时器不变。

协议通过链路建立邻接，并发布 LoopBack IPv6 前缀。这个配置不引入静态路由或默认路由。

## 验证

**P1：**

~~~text
display ospfv3 1 peer brief
display ospfv3 1 routing
ping ipv6 -n -c 3 -t 1500 2001:db8:20::2
~~~

实际输出节选：

~~~text
Neighbor ID     Pri  State          Dead Time  Interface
10.255.20.2     1    Full/PointToPoint 00:00:10   host-p1e12

2001:db8:20::2/128                          IA           fe80::fe:78ff:fe2a:b801                  host-p1e12

--- 2001:db8:20::2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
~~~

## 撤销

在两端先解除接口绑定，再删专用进程。以下为 P1，P2 替换物理接口名。

~~~text
system-view
interface LoopBack 20
 undo ospfv3 1 area 0.0.0.0
 quit
interface host-p1e12
 undo ospfv3 1 area 0.0.0.0
 quit
undo ospfv3 1
commit
display ipv6 routing-table
~~~

实测 P1 的路由表不再包含对端 LoopBack 前缀，本地接口地址仍可保留。

[OSPFv3 配置指南](../operator/ospfv3.md)
