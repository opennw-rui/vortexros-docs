# 路由反射

同一 AS 内，路由反射器可以把一个 iBGP 客户端学到的路由通告给其他客户端，减少全互联会话。路由反射不代替下一跳可达性；应先由静态路由或 IGP 保证各端下一跳互通。

## 两个客户端和一个反射器

三台设备依次连接：CE1 — RR — CE2，同属 AS 65000。

| 设备 | Ethernet0 | Ethernet1 | LoopBack255 |
| --- | --- | --- | --- |
| CE1 | 2001:db8:80::1/64 | — | 2001:db8:255::1/128 |
| RR | 2001:db8:80::2/64 | 2001:db8:23::2/64 | — |
| CE2 | 2001:db8:23::3/64 | — | 2001:db8:256::3/128 |

下列为系统视图配置清单。接口须先物理连通。配置后返回系统视图执行 commit；检查实际结果后 save。# 是配置分隔符，不是需要在终端执行的命令。

CE1：

```text
interface Ethernet 0
 ipv6 enable
 ipv6 address 2001:db8:80::1 64
#
interface LoopBack 255
 ipv6 enable
 ipv6 address 2001:db8:255::1 128
#
ipv6 route-static 2001:db8:23:: 64 2001:db8:80::2
bgp 65000
 router-id 1.1.1.1
 peer 2001:db8:80::2 as-number 65000
 ipv6-family unicast
  peer 2001:db8:80::2 enable
  network 2001:db8:255::1 128
 #
#
```

RR：

```text
interface Ethernet 0
 ipv6 enable
 ipv6 address 2001:db8:80::2 64
#
interface Ethernet 1
 ipv6 enable
 ipv6 address 2001:db8:23::2 64
#
bgp 65000
 router-id 2.2.2.2
 reflector cluster-id 2.2.2.22
 peer 2001:db8:80::1 as-number 65000
 peer 2001:db8:23::3 as-number 65000
 ipv6-family unicast
  peer 2001:db8:80::1 enable
  peer 2001:db8:80::1 reflect-client
  peer 2001:db8:23::3 enable
  peer 2001:db8:23::3 reflect-client
 #
#
```

CE2：

```text
interface Ethernet 0
 ipv6 enable
 ipv6 address 2001:db8:23::3 64
#
interface LoopBack 255
 ipv6 enable
 ipv6 address 2001:db8:256::3 128
#
ipv6 route-static 2001:db8:80:: 64 2001:db8:23::2
bgp 65000
 router-id 3.3.3.3
 peer 2001:db8:23::2 as-number 65000
 ipv6-family unicast
  peer 2001:db8:23::2 enable
  network 2001:db8:256::3 128
 #
#
```

## 查询路由和业务

在 CE2 查询：

```text
display bgp ipv6 peer
display bgp ipv6 routing-table 2001:db8:255::1 128
display ipv6 routing-table 2001:db8:255::1
ping ipv6 -c 2 -a 2001:db8:256::3 2001:db8:255::1
```

实际查询关键结果：

```text
Network: 2001:db8:255::1/128
NextHop: 2001:db8:80::1
LocPrf: 100
Total Number of Routes: 1

2 packets transmitted, 2 received, 0% packet loss
```

上面的路由字段是查询结果摘录，不是整张原始表。路由保留 CE1 的下一跳，因此 CE2 必须能够经 RR 到达 2001:db8:80::1。普通 next-hop-local 不保证改写反射的 iBGP 路由。改变反射或 GR 参数可能重新协商会话，配置提交完成后仍需等待邻居和路由恢复。

## 禁止客户端间反射

默认允许客户端间反射。RR 的 BGP 进程视图执行：

```text
undo reflect between-clients
commit
```

没有其他可用通告路径时，CE2 对上述 CE1 前缀的实际查询变为 Total Number of Routes: 0。若同一前缀同时从非客户端会话学习，仍可能通告给客户端；不能用这种替代路径判断开关无效。

恢复：

```text
reflect between-clients
commit
```

实际路由恢复为 1 条。undo reflector cluster-id 恢复以 Router ID 为 Cluster ID，不会撤销客户端绑定。

## 撤销

先在 CE1 和 CE2 的 IPv6 地址族撤销各自的 network，再提交，确认对端不再收到对应前缀。随后在 RR 的 IPv6 地址族撤销客户端绑定：

```text
undo peer 2001:db8:80::1 reflect-client
undo peer 2001:db8:23::3 reflect-client
```

如果这些会话只用于本例，再在 BGP 进程视图删除相应 peer；最后删除测试 LoopBack、静态路由及接口地址。不要删除承载其他业务的 BGP 进程或共享链路。完整命令参数见[邻居与会话](peers.md)。
