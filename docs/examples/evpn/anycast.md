# Anycast 网关

## 拓扑与前提

本例在已建立的 EVPN 网络上增加分布式网关：

```text
PE1 —— EVPN / VXLAN —— PE3 —— CE3
                         网关     客户
```

| 项目 | PE1 | PE3 |
| --- | --- | --- |
| VTEP 地址 | 198.19.80.1 | 198.19.23.3 |
| 客户桥域 / L2VNI | 460 / 50460 | 460 / 50460 |
| 租户 VPN / L3VNI | D1-TYPE5 / 50081 | D1-TYPE5 / 50081 |
| 网关地址 | 192.0.2.254/24 | 192.0.2.254/24 |
| 网关 MAC | 0200-0000-0460 | 0200-0000-0460 |
| 租户环回 | 198.18.196.1/32 | 198.18.196.3/32 |

CE3 地址为 192.0.2.3/24，经网关访问 PE1 的租户环回。先完成 [L2VPN](l2vpn.md) 的接入、桥域、NVE 和 EVPN 邻居，以及 [L3VPN](l3vpn.md) 的租户、L3VNI 和 Type-5 通告；按上表使用本例的地址、桥域和 VNI。开始前，两台 PE 应已学习对端的租户环回前缀。

两台网关使用相同 IP、MAC 和租户绑定。相同网关 MAC 不应作为普通客户 MAC 使用。修改网关 MAC 会影响客户 ARP/ND 缓存；应安排维护窗口并验证邻居更新后的业务。

## 两台 PE 的网关配置

PE1 和 PE3 均配置以下内容：

```text
interface Vbdif 460
 mac-address 0200-0000-0460
 ip binding vpn-instance D1-TYPE5
 ip address 192.0.2.254 255.255.255.0
 vxlan anycast-gateway enable
#
```

将接口绑定到 VPN 会清除该接口已有的 IPv4/IPv6 地址，因此先完成绑定，再配置地址。提交并检查：

```text
commit
display interface Vbdif460
display bgp evpn all routing-table | include 0200-0000-0460
```

实际状态摘录：

```text
Vbdif460 current state : UP
Line protocol current state : UP
Internet Address is 192.0.2.254/24
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 0200-0000-0460
VPN-Instance Name is D1-TYPE5
Bridge-domain: 460 (bvi)

*>    0:48:0200-0000-0460:32:192.0.2.254     198.19.23.3
```

最后一条为网关 MAC/IP 的 Type-2 通告。只看到接口 Up 还不够，远端 PE 也应有相应的 EVPN 路由和可用下一跳。

## 客户配置与双向验证

CE3 使用普通三层接口；本例只增加到测试前缀的静态路由，不改变其他业务的默认路由：

```text
interface Ethernet0
 ip address 192.0.2.3 255.255.255.0
#
ip route-static 198.18.196.1 255.255.255.255 192.0.2.254
```

CE3 提交后验证网关和远端租户前缀：

```text
commit
display arp
ping -a 192.0.2.3 -c 2 192.0.2.254
ping -a 192.0.2.3 -c 2 198.18.196.1
```

PE1 检查返回方向：

```text
display ip routing-table vpn-instance D1-TYPE5 192.0.2.3 32
ping -vpn-instance D1-TYPE5 -a 198.18.196.1 -c 2 192.0.2.3
```

业务验证中，客户经过 PE3 网关和 L3VNI 到达 PE1，返回经 L3VNI、PE3 网关回到客户。实际输出：

```text
64 bytes from 198.18.196.1: icmp_seq=1 ttl=63 time=1.26 ms
1 packets transmitted, 1 received, 0% packet loss

64 bytes from 192.0.2.3: icmp_seq=1 ttl=63 time=1026 ms
64 bytes from 192.0.2.3: icmp_seq=2 ttl=63 time=4.49 ms
2 packets transmitted, 2 received, 0% packet loss
```

第二组保留了邻居收敛期间首包延迟较高的结果。首次 ARP/ND 解析可能出现首包丢失或延迟；若持续失败，检查客户邻居、租户前缀、每条 VTEP 下一跳及路由器 MAC，不能只根据 BGP 路由存在判定业务正常。

多归属客户的所有三层转发 PE 都需要对应租户和 L3VNI。只在部分 PE 配置网关，却让未配置租户的 PE 成为客户的等价三层下一跳，会产生部分路径不通；详见 [多归属与路由条件](../../operator/evpn/anycast.md#多归属与路由条件)。

## 撤销与保存

先在两个 PE 撤销 Anycast 通告：

```text
interface Vbdif 460
 undo vxlan anycast-gateway enable
#
```

```text
commit
display current-configuration interface Vbdif460
display bgp evpn all routing-table | include 0200-0000-0460
```

实际撤销后，网关 MAC/IP Type-2 查询不再输出该表项，接口配置仍保留显式 MAC、VPN 绑定和 IP：

```text
interface Vbdif460
 mac-address 0200-0000-0460
 ip binding vpn-instance D1-TYPE5
 ip address 192.0.2.254 255.255.255.0
#
```

Anycast 开关不负责删除普通接口地址。若要完全移除本例网关，在两个 PE 删除 Vbdif；客户同时删除测试路由：

```text
undo interface Vbdif460
commit
save
```

```text
undo ip route-static 198.18.196.1 255.255.255.255 192.0.2.254
commit
save
```

实际删除后，两台 PE 健康状态均为 ready、无活动告警。保留的 VLAN460 普通客户流量和 VLAN461 标记流量各 1/1，原租户 Type-5 双栈探测各 1/1。桥域、L2VNI、NVE、EVPN 邻居及租户环回均保留；删除单一网关无需关闭整个 EVPN 网络。

[功能与限制](../../operator/evpn/anycast.md)
