# VRRP 网关

本例配置双栈冗余网关。R1、R2 和客户端路由器 C 的 Ethernet0 接入同一二层网络；R1 与 R2 另用 Ethernet1 互联。R1 的 LoopBack244 提供业务验证地址。R1 优先级 120，R2 保持默认 100。

| 设备 | Ethernet0 | Ethernet1 | 业务地址 |
|---|---|---|---|
| R1 | 198.18.243.1/24、fd00:243::1/64 | 198.19.80.1/30、2001:db8:80::1/64 | 198.18.244.1/32、fd00:244::1/128 |
| R2 | 198.18.243.2/24、fd00:243::2/64 | 198.19.80.2/30、2001:db8:80::2/64 | — |
| C | 198.18.243.3/24、fd00:243::3/64 | — | — |

虚拟地址为 198.18.243.254、fe80::fe 和 fd00:243::fe。三台设备均使用 VortexROS，Ethernet 编号可按实际接线替换。

## R1 配置

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ip address 198.18.243.1 24
 ipv6 enable
 ipv6 address fd00:243::1 64
 vrrp vrid 43 version-3 send-packet-mode v3-only
 vrrp vrid 43 virtual-ip 198.18.243.254
 vrrp vrid 43 priority 120
 vrrp vrid 43 accept-mode enable
 vrrp6 vrid 44 virtual-ip fe80::fe
 vrrp6 vrid 44 virtual-ip fd00:243::fe
 vrrp6 vrid 44 priority 120
 vrrp6 vrid 44 accept-mode enable
#
interface Ethernet 1
 ip address 198.19.80.1 30
 ipv6 enable
 ipv6 address 2001:db8:80::1 64
#
interface LoopBack 244
 ip address 198.18.244.1 32
 ipv6 enable
 ipv6 address fd00:244::1 128
#
ip route-static 198.18.243.3 32 198.19.80.2
ipv6 route-static fd00:243::3 128 2001:db8:80::2
```

CLI 操作：

```text
commit
```

两条主机路由使业务回程经过 R2。这样关闭 R1 的网关接口时，R1 的业务地址仍可通过独立互联返回客户端。

## R2 配置

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ip address 198.18.243.2 24
 ipv6 enable
 ipv6 address fd00:243::2 64
 vrrp vrid 43 version-3 send-packet-mode v3-only
 vrrp vrid 43 virtual-ip 198.18.243.254
 vrrp vrid 43 accept-mode enable
 vrrp6 vrid 44 virtual-ip fe80::fe
 vrrp6 vrid 44 virtual-ip fd00:243::fe
 vrrp6 vrid 44 accept-mode enable
#
interface Ethernet 1
 ip address 198.19.80.2 30
 ipv6 enable
 ipv6 address 2001:db8:80::2 64
#
ip route-static 198.18.244.1 32 198.19.80.1
ipv6 route-static fd00:244::1 128 2001:db8:80::1
```

CLI 操作：

```text
commit
```

## 客户端 C 配置

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ip address 198.18.243.3 24
 ipv6 enable
 ipv6 address fd00:243::3 64
#
ip route-static 198.18.244.1 32 198.18.243.254
ipv6 route-static fd00:244::1 128 fd00:243::fe
```

CLI 操作：

```text
commit
```

## 检查角色与连通性

在 R1、R2 查看：

```text
display vrrp brief
display vrrp6 brief
display vrrp interface Ethernet 0
display vrrp6 44
display vrrp statistics
```

实际验证取得的角色、优先级和间隔如下，接口编号按本例统一表示：

```text
# R1
43  Master  Ethernet0  IPv4  198.18.243.254        120  120  1.00s
44  Master  Ethernet0  IPv6  fe80::fe,fd00:243::fe 120  120  1.00s
# R2
43  Backup  Ethernet0  IPv4  198.18.243.254        100  100  1.00s
44  Backup  Ethernet0  IPv6  fe80::fe,fd00:243::fe 100  100  1.00s
```

在 C 查看实际业务效果：

```text
ping -c 2 -a 198.18.243.3 198.18.244.1
ping ipv6 -c 2 -a fd00:243::3 fd00:244::1
ping -c 1 -t 1000 -a 198.18.243.3 198.18.243.254
ping ipv6 -c 1 -t 1000 -a fd00:243::3 fd00:243::fe
```

已取得 IPv4、IPv6 业务地址各 2/2 回复，以及虚拟地址各 1/1 回复。切换过程中可能丢包，应在角色稳定后区分业务恢复结果；这些结果不代表无损切换或硬件吞吐保证。

## 跟踪、抢占与接收模式

对已经配置且具备相应地址族能力的上联，可配置优先级降低：

```text
interface Ethernet 0
 vrrp vrid 43 track interface Ethernet 2 reduced 50
 vrrp6 vrid 44 track interface Ethernet 2 reduced 50
#
```

CLI 操作：

```text
commit
```

Ethernet2 必须是另一条实际接口，不能是本组的 Ethernet0。跟踪接口须同时满足管理 Up、物理链路 Up 和相应地址族的 IP 能力；没有 IPv4 地址的空接口不满足 IPv4 跟踪条件。它只判断接口可用性，不探测远端服务。省略 reduced 时降低 10。

已验证被跟踪口关闭后，R1 双栈运行优先级均由 120 降到 70，R2 以 100 接管；独立回程仍可用时，C 的双栈业务探测各 2/2。恢复接口后默认允许抢占。若在 R1 配置：

```text
interface Ethernet 0
 vrrp vrid 43 preempt-mode disable
 vrrp6 vrid 44 preempt-mode disable
#
```

CLI 操作：

```text
commit
```

R1 即使恢复到 120，也保持 Backup，当前 R2 Master 不被抢占。执行对应的 undo preempt-mode 并提交后，已验证 R1 重新成为 Master。

默认 accept-mode 关闭。对本例非地址拥有者的 Master，关闭它后，发给虚拟 IP 本身的 ping 不再回复；经虚拟网关访问其他地址仍正常。实际对照取得 VIP 双栈各 0/1、业务地址双栈各 1/1。需要通过虚拟 IP 访问设备本机服务时恢复 accept-mode enable。

## 修改计时器与保存

两端同时改为 `vrrp vrid 43 timer advertise 2` 和 `vrrp6 vrid 44 timer advertise 2` 后，实际通告间隔为 200 厘秒。两端执行对应的 undo timer advertise 后恢复 100 厘秒，默认值不写入配置。

确认两端角色和路由符合预期后执行 save，并确认提示。IPv6 虚拟地址列表会将链路本地地址放在首位；只有全局虚拟地址的组不能提交。

## 撤销

先迁移客户端路由或网关，再在 R1、R2 删除组：

```text
interface Ethernet 0
 undo vrrp vrid 43
 undo vrrp6 vrid 44
#
```

CLI 操作：

```text
commit
display vrrp brief
display vrrp6 brief
```

删除最后一条 virtual-ip 会停止对应组的数据面实例，但可保留一个待配置的空组；删除整个组则清除该组意图。撤销前先核对接口原有地址和其他业务，避免一并删除。

单独清除本例路由时，在 C 撤销两条指向 VIP 的主机路由，在 R2 撤销指向 R1 LoopBack244 的两条路由，在 R1 撤销指向 C 的两条回程路由；不再使用的测试地址最后从各接口删除并提交。
