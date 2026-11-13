# 静态路由

**用途**。为 203.0.113.0/24 指定下一跳 192.0.2.1。适合上游固定、无需交换动态路由的链路。

**前提**。Ethernet 1 是独立三层实验口，能连接到 192.0.2.1。上游需要有返回 192.0.2.0/24 的路径。此例可在 Linux 数据面试用。

## 配置

~~~text
system-view
interface Ethernet 1
 description LAB-UPLINK
 ip address 192.0.2.2 255.255.255.0
 quit
ip route-static 203.0.113.0 255.255.255.0 192.0.2.1
display configuration candidate
commit
~~~

接口地址形成直连网段。静态路由让目标前缀经指定网关转发。网关未解析时，配置可能已保存但实际转发仍不可达。默认路由和其他前缀的行为由现有路由决定。

## 验证

~~~text
display ip interface brief
display ip routing-table 203.0.113.0 24
ping 192.0.2.1
ping 203.0.113.1
~~~

先确认直连网关，再确认远端。启用 VPP 的设备可另查 display ip fib 确认转发表。通过后 return，再按提示 save。

## 撤销

~~~text
system-view
undo ip route-static 203.0.113.0 255.255.255.0 192.0.2.1
commit
~~~

核对只撤销了指定静态路径。若实验地址也应删除，再在接口视图精确撤销该地址。删除地址会同时影响使用该地址的服务和直连路由。
