# 建立单区域 OSPF 邻接

**用途**。在两台路由器之间交换 IPv4 路由。示例使用 Area 0，每端使用独立 Router ID。

**前提**。两端已经配置可互通的三层接口。示例以 Ethernet 1 为承载口，双方使用相同的区域、网络类型及兼容的认证和计时器。

## 配置

~~~text
system-view
ospf 1 router-id 192.0.2.11
 quit
interface Ethernet 1
 ospf enable 1 area 0.0.0.0
 ospf network-type p2p
 quit
commit
~~~

对端使用相同的接口激活方式和区域，Router ID 改为 192.0.2.12。提交后接口开始发送 Hello。接口激活和区域 network 匹配是两种方式，同一进程选择一种。

## 验证

运行 display ospf peer 查看邻居，点到点链路应达到 Full。运行 display ip routing-table protocol ospf 查看学到的路由，并用业务流量验证。邻居已建立只证明邻接成立。

## 撤销

在接口视图执行 undo ospf enable 1 并提交。该接口上的邻接和由此学到的路径会撤销。只有确定进程不再承载其他接口时，才在系统视图删除整个进程。
