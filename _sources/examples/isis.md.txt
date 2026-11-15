# IS-IS 双栈

在两台路由器之间建立 IS-IS 邻接，让 P1 学到 P2 的 IPv4、IPv6 LoopBack 路由。只看到邻居 Up 不代表路由已经恢复，验收同时检查 LSDB、路由优先级和实际连通性。

## 拓扑与前提

```text
P1 host-p1a12 ---------------- host-p2a12 P2
   198.19.80.1/30              198.19.80.2/30
   2001:db8:80::1/64           2001:db8:80::2/64
                              LoopBack98
                              172.66.98.2/32
                              2001:db8:98::2/128
```

两端端口必须已存在、链路 Up，并由当前数据面管理。本例名称是开发服务器隔离拓扑中的实际 AF_PACKET 接口；物理设备应替换成对应的 Ethernet 接口名称。双方系统 ID 必须不同。

启用后会在该链路交换 IS-IS 拓扑并安装学习路由。两端地址族、Level 和链路类型需要一致；不要在承载管理的端口上直接试验 Level 切换。

## P1 配置

```text
system-view
isis 1
 network-entity 49.0001.0000.0000.0001.00
 is-level level-2
 cost-style wide
 quit
interface host-p1a12
 ip address 198.19.80.1 255.255.255.252
 ipv6 address 2001:db8:80::1 64
 isis enable 1
 isis ipv6-enable 1
 isis circuit-type p2p
 quit
commit
save
```

## P2 配置

```text
system-view
isis 1
 network-entity 49.0001.0000.0000.0002.00
 is-level level-2
 cost-style wide
 quit
interface host-p2a12
 ip address 198.19.80.2 255.255.255.252
 ipv6 address 2001:db8:80::2 64
 isis enable 1
 isis ipv6-enable 1
 isis circuit-type p2p
 quit
interface LoopBack 98
 ip address 172.66.98.2 255.255.255.255
 ipv6 address 2001:db8:98::2 128
 isis enable 1
 isis ipv6-enable 1
 quit
commit
save
```

`save` 按提示确认。提交影响当前运行，保存决定下次启动时恢复的配置。

## 验证

在 P1 执行：

```text
display isis 1 peer
display isis 1 lsdb
display isis 1 route
display ip routing-table 172.66.98.2
display ipv6 routing-table 2001:db8:98::2
ping -c 3 172.66.98.2
ping ipv6 -c 3 2001:db8:98::2
```

已有功能验收在 Ubuntu 26.04.1 QEMU、两个独立 VPP/FRR 节点上以真实交互 CLI 验证。以下是实际输出的相关行，省略无关表项和终端折行：

```text
System Id        Interface       Circuit Id   State HoldTime Type PRI
ubuntu           host-p1a12      2020.2020.2020 Up    28s      2    -
Total Peer(s): 1

ISIS(IPv4) Level-2 Forwarding Table
Destination/Mask    Cost  Flags NextHop         Interface
172.66.98.2/32      20    D     198.19.80.2     host-p1a12

ISIS(IPv6) Level-2 Forwarding Table
2001:db8:98::2/128  20    D     fe80::2c57:8ff:fe43:1c11  host-p1a12

Destination/Mask   Proto   Pre  Cost  Flags NextHop         Interface
172.66.98.2/32     ISIS    15   20    D     198.19.80.2     host-p1a12

3 packets transmitted, 3 received, 0% packet loss
```

这里的 `Pre 15` 是本次更新后的协议缺省路由优先级，`Cost 20` 是这条学习路径的度量值，两者含义不同。链路本地 IPv6 下一跳和邻居动态主机名会随环境变化。

本轮另行做了 Level-2 → Level-1 → Level-1-2 → Level-2 的在线切换，检查各活动 Level 的邻居计数、LSP、双栈路由及实际报文路径。FRR 可能受 LSP 最小生成间隔限制，邻居先 Up、前缀稍后出现，应继续查看 LSDB 和路由；不要反复修改配置催促恢复。这些结果不代表已验证所有厂商互通组合或规模性能。

## 撤销

先在两端承载链路上撤销协议绑定，再删除本例专用进程；P2 的 LoopBack 绑定也要撤销：

```text
system-view
interface host-p1a12
 undo isis ipv6-enable 1
 undo isis enable
 quit
undo isis 1
commit
save
```

P2 将接口名换成 `host-p2a12`，并在 `LoopBack 98` 下撤销相同两条协议绑定后再删除进程。删除进程时按提示确认。本例的 IP 地址保留，不会因此清除接口上的其他配置；若不再需要实验地址，应另外明确撤销。

验证 `display isis 1 peer` 不再有该进程的邻居，路由表不再存在本例的 IS-IS 学习项。有静态或其他协议备份时，同一前缀仍可能通过备份路径存在，不能把“前缀仍存在”误判为 IS-IS 撤销失败。

[IS-IS 使用说明](../operator/isis.md) · [命令参考](../operator/reference/isis.md)
