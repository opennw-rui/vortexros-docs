# OSPF 单区域

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


## VPN 实例的静态引入

本轮开发服务器另以 `CLI-UNDER` 验证完整链路：P1 `host-p1b12` 为198.18.180.1/30，P2 `host-p2b12` 为198.18.180.2/30；两端接口属于这个 VPN。P2 的 LoopBack80 同属该 VPN，地址198.18.181.2/32。两端先创建 `ip vpn-instance CLI-UNDER` 并启用 `ipv4-family`，再绑定接口、配置地址；绑定会清除原接口地址。

P1：

```text
ospf 80 router-id 10.255.80.1 vpn-instance CLI-UNDER
 area 0
  network 198.18.180.0 0.0.0.3
  quit
 quit
commit
```

P2：

```text
interface LoopBack80
 ip binding vpn-instance CLI-UNDER
 ip address 198.18.181.2 255.255.255.255
 quit
ip route-static vpn-instance CLI-UNDER 198.18.181.0 24 NULL 0
ospf 80 router-id 10.255.80.2 vpn-instance CLI-UNDER
 area 0
  network 198.18.180.0 0.0.0.3
  quit
 import-route static cost 37 type 2
 quit
commit
```

两端广播网络先经历 DR/BDR 选举和邻接同步，随后才是 Full。P1 的实际查询：

```text
display ospf vpn-instance CLI-UNDER peer
display ospf vpn-instance CLI-UNDER lsdb ase 198.18.181.0
display ospf vpn-instance CLI-UNDER lsdb
display ip routing-table vpn-instance CLI-UNDER 198.18.181.2 verbose
ping -vpn-instance CLI-UNDER -c 3 -a 198.18.180.1 198.18.181.2
```

实际明细包含：

```text
Type      : External
Ls id     : 198.18.181.0
Adv rtr   : 10.255.80.2
Len       : 36
TOS 0  Metric: 37
E type    : 2
```

摘要中同一 External 行的 Len 为36、Metric 为37；实际选中路由为 OSPF、Preference150、Cost37，经host-p1b12到198.18.180.2，流量3/3。不能以 NULL 汇总路由自身作为响应端：本例由更具体的 LoopBack80 地址响应。

在 P2 的 `ospf 80 vpn-instance CLI-UNDER` 视图执行 `undo import-route static` 并提交，停止发布该静态前缀。撤销测试期间没有其他协议替代发布时，P1 成功查询的 Summary Count 为0；LSDB 中可能暂时保留 Age3600 的撤销 LSA，这不是仍有有效路由。恢复原引入命令后再查询协议、出口和流量。保存当前结果使用 `save`，退出时确认 Y。

## 多区域、汇总与区域类型

在上面的 CLI-UNDER 实例上增加第二条链路：b12 属于骨干区域，q12 属于区域 1。P2 的两个 LoopBack 地址位于区域 1。两台路由器都连接区域 0 和区域 1，因此都是 ABR；这与只有一个 ABR 的单出口 stub 拓扑不同。

```text
      area 0: 198.18.180.0/30
P1 b12 -------------------- b12 P2
   q12 -------------------- q12
      area 1: 198.18.182.0/30
                         LoopBack81 198.18.184.2/32
                         LoopBack82 198.18.185.2/32
```

P1 在已创建的 OSPF80 中增加区域；P2 使用相同配置，将本端接口及地址替换为 P2：

```text
ospf 80
 area 0.0.0.1
  network 198.18.182.0 0.0.0.3
  quit
 quit
interface host-p1q12
 ip binding vpn-instance CLI-UNDER
 ip address 198.18.182.1 255.255.255.252
 ospf network-type p2p
 ospf timer hello 1
 ospf timer dead 4
 quit
commit
```

P2 另外增加两个三层接口并将它们发布到区域 1：

```text
interface LoopBack 81
 ip binding vpn-instance CLI-UNDER
 ip address 198.18.184.2 255.255.255.255
 quit
interface LoopBack 82
 ip binding vpn-instance CLI-UNDER
 ip address 198.18.185.2 255.255.255.255
 quit
ospf 80
 area 0.0.0.1
  network 198.18.184.0 0.0.1.255
  abr-summary 198.18.184.0 255.255.254.0
  quit
 quit
commit
```

为了单独验证区域间汇总，经 P1 的 q12 设置 `ospf passive` 并提交，使测试流量经骨干链路。实测 P1 学到 `198.18.184.0/23`、优先级 10、代价 11，指定源地址的 IPv4 探测为 3/3。把 P2 的汇总改成 `abr-summary 198.18.184.0 255.255.254.0 not-advertise` 后，成功查询显示该前缀路由数为 0，目标探测为 0/1。恢复汇总后再执行 `undo ospf passive` 恢复区域 1 邻接。汇总控制区域间发布，不是本机接口地址的替代配置。

两端一致切换区域类型；先删除本例的汇总，再配置 NSSA：

```text
ospf 80
 area 0.0.0.1
  undo abr-summary 198.18.184.0 255.255.254.0
  nssa no-summary
  quit
 quit
commit
display ospf vpn-instance CLI-UNDER peer
display ospf vpn-instance CLI-UNDER lsdb nssa
```

P1 无该汇总时省略对应的 `undo abr-summary`。本例实测区域 1 邻居 Full；P2 引入的静态前缀 `198.18.181.0` 出现在 Type7 LSA，长度 36、E2、Metric 37。它不再是普通区域的 Type5 发布方式。双方区域选项必须一致。

切换为完全 stub 区域：

```text
ospf 80
 area 0.0.0.1
  undo nssa
  stub no-summary
  quit
 quit
commit
```

两端原生后端配置均出现 `area 0.0.0.1 stub no-summary`，区域 0 和区域 1 邻居均保持 Full。此双 ABR 案例验证了在线类型切换和邻接；不能据此声称已验证单出口 stub 路由器收到默认路由。

恢复普通区域使用 `undo stub` 并在两端提交；删除实验接口前，先撤销区域中的 `network`、汇总及协议选项，再删除接口和不再使用的区域。确认查询与业务符合预期后再 `save`。
