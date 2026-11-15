# AmneziaWG 互连

## 拓扑

| 位置 | P1 | P2 |
| --- | --- | --- |
| 底层 IPv4 | 10.201.12.1/24 | 10.201.12.2/24 |
| UDP 监听 | 51920 | 51920 |
| Tunnel20 | 198.51.100.41/30 | 198.51.100.42/30 |

两端运行 VortexROS 与配套 VPP。各自 Ethernet0 配置底层地址，双向可达并允许 UDP 51920。先在 Tunnel20 视图配置 tunnel-protocol amneziawg、privatekey auto，再用 display this 取得本端公钥并交换；完成下列 Profile 后一起提交。私钥进入配置和备份，应限制其访问。

两端的填充和消息头范围要相同。示例只允许对端隧道地址进入各自 peer，不通告其他业务网段。

## P1 配置

~~~text
system-view
amneziawg profile AWG-P2
 junk size 16 48
 junk count 3
 padding init 24
 padding response 28
 padding cookie 20
 padding transport 16
 header init 100 110
 header response 200 210
 header cookie 300 310
 header transport 400 410
 padding content 4 16
 random-trailers enable
 peer P2
  publickey REMOTE_PUBLIC_KEY
  allowd-ip 198.51.100.42 32
  source 10.201.12.1
  destination vpn-instance default 10.201.12.2 port 51920
  keepalive 5
 quit
quit
interface Tunnel 20
 tunnel-protocol amneziawg
 source vpn-instance default
 source-port 51920
 amneziawg-profile AWG-P2
 ip address 198.51.100.41 255.255.255.252
quit
commit
~~~

## P2 配置

~~~text
system-view
amneziawg profile AWG-P1
 junk size 16 48
 junk count 3
 padding init 24
 padding response 28
 padding cookie 20
 padding transport 16
 header init 100 110
 header response 200 210
 header cookie 300 310
 header transport 400 410
 padding content 4 16
 random-trailers enable
 peer P1
  publickey REMOTE_PUBLIC_KEY
  allowd-ip 198.51.100.41 32
  source 10.201.12.2
  destination vpn-instance default 10.201.12.1 port 51920
  keepalive 5
 quit
quit
interface Tunnel 20
 tunnel-protocol amneziawg
 source vpn-instance default
 source-port 51920
 amneziawg-profile AWG-P1
 ip address 198.51.100.42 255.255.255.252
quit
commit
~~~

这项配置建立独立的 AmneziaWG 隧道。修改协商相关参数可能重建 peer；不要把此配置直接用于正在承载业务的隧道。

## 验证

先从 P2 向 P1 探测一次，再在 P1 执行：

~~~text
display amneziawg interface Tunnel 20
display amneziawg peer AWG-P2 P2
ping -n -c 3 -t 1500 198.51.100.42
~~~

P2 反向执行 `ping -n -c 3 -t 1500 198.51.100.41`。示例输出：

~~~text
Interface : Tunnel20
  Source Port : 51920
  Profile : AWG-P2

AmneziaWG Profile : AWG-P2
  Junk : count 3, size 16-48
  Padding : init 24, response 28, cookie 20, transport 16, content 4-16
  Headers : init 100-110, response 200-210, cookie 300-310, transport 400-410
  Random Trailers : enabled
  Peer : P2
    Allowed-IP : 198.51.100.42/32

--- 198.51.100.42 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms

--- 198.51.100.41 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
~~~

## 撤销

两端先解除新增业务路由，再删 Tunnel20 和对应 profile。P1 执行：

~~~text
system-view
undo interface Tunnel 20
undo amneziawg profile AWG-P2
commit
display amneziawg interface
~~~

P2 将 profile 换为 `AWG-P1`。示例中两端查询均不再显示 Tunnel20。

[AmneziaWG 配置指南](../operator/amneziawg.md)


## 高级参数配置

以下为高级参数的独立双端配置，包含预共享密钥及 IPv6 内层。先撤销与基础例冲突的 Tunnel20 和 Profile，再生成本例密钥并交换公钥。

| 项目 | P1 | P2 |
| --- | --- | --- |
| 外层接口 | Ethernet0 | Ethernet0 |
| 外层 IPv4 | 198.19.80.1 | 198.19.80.2 |
| Tunnel20 IPv4 | 10.240.20.1/30 | 10.240.20.2/30 |
| Tunnel20 IPv6 | 2001:db8:240:20::1/64 | 2001:db8:240:20::2/64 |
| Profile / peer | AWG-P2 / P2 | AWG-P1 / P1 |
| 监听端口 | 51920 | 51920 |

生成并交换公钥的步骤与上文相同。以下 REMOTE_PUBLIC_KEY 为对端公钥；本端私钥由前置步骤生成，`SHARED_PSK`、`SHARED_HEADER_KEY` 是双方一致的两项独立 32 字节 Base64 密钥，不要直接使用公开文档中的演示值作为秘密。

**P1：**

```text
amneziawg profile AWG-P2
 junk size 16 48
 junk count 3
 padding init 24
 padding response 28
 padding cookie 20
 padding transport 16
 header init 100 110
 header response 200 210
 header cookie 300 310
 header transport 400 410
 padding content 4 16
 timing rekey-after 90 120
 timing rekey-timeout 4 6
 timing reject-after 170 190
 timing keepalive 8 10
 timing max-handshakes 14 18
 header-protection SHARED_HEADER_KEY
 random-trailers enable
 disable-cookies enable
 junk-packet 1 AQIDBA==
 junk-packet 2 expression "<b 0x160301><c><t><r 32><rc 16><rd 8>"
 peer P2
  publickey REMOTE_PUBLIC_KEY
  presharedkey SHARED_PSK
  allowd-ip 10.240.20.2 32
  allowd-ip 2001:db8:240:20::2 128
  source 198.19.80.1
  destination vpn-instance default 198.19.80.2 port 51920
  keepalive 5
  quit
 quit
interface Tunnel 20
 tunnel-protocol amneziawg
 source vpn-instance default
 source-port 51920
 amneziawg-profile AWG-P2
 ip address 10.240.20.1 255.255.255.252
 ipv6 address 2001:db8:240:20::1 64
 quit
commit
save
```

**P2：**

```text
amneziawg profile AWG-P1
 junk size 16 48
 junk count 3
 padding init 24
 padding response 28
 padding cookie 20
 padding transport 16
 header init 100 110
 header response 200 210
 header cookie 300 310
 header transport 400 410
 padding content 4 16
 timing rekey-after 90 120
 timing rekey-timeout 4 6
 timing reject-after 170 190
 timing keepalive 8 10
 timing max-handshakes 14 18
 header-protection SHARED_HEADER_KEY
 random-trailers enable
 disable-cookies enable
 junk-packet 1 AQIDBA==
 junk-packet 2 expression "<b 0x160301><c><t><r 32><rc 16><rd 8>"
 peer P1
  publickey REMOTE_PUBLIC_KEY
  presharedkey SHARED_PSK
  allowd-ip 10.240.20.1 32
  allowd-ip 2001:db8:240:20::1 128
  source 198.19.80.2
  destination vpn-instance default 198.19.80.1 port 51920
  keepalive 5
  quit
 quit
interface Tunnel 20
 tunnel-protocol amneziawg
 source vpn-instance default
 source-port 51920
 amneziawg-profile AWG-P1
 ip address 10.240.20.2 255.255.255.252
 ipv6 address 2001:db8:240:20::2 64
 quit
commit
save
```

### 参数的实际影响

| 设置 | 作用与影响 |
| --- | --- |
| presharedkey | 给该 peer 增加预共享密钥；双方必须一致，撤销时也要协调两端。 |
| header-protection | 加密消息头；此例四类报文的前置填充均不少于 12 字节，两端使用同一头保护密钥。 |
| header init/response/cookie/transport | 对应四类协议消息的随机标识范围；双方必须兼容。 |
| padding init/response/cookie/transport | 对应报文的前置填充字节数，会增加外层报文大小。 |
| padding content / random-trailers | 内容填充与随机尾部，用于改变报文外观，同样增加开销。 |
| junk count / size | 每次握手前额外发送的随机垃圾报文数量与大小范围。 |
| junk-packet | 独立的静态或动态签名槽位；不包含在 junk count 的三个随机报文中。 |
| timing rekey-after / reject-after | 密钥更新和拒绝过期密钥所用的时间范围。 |
| timing rekey-timeout / keepalive | 握手重试和协议保活使用的时间范围；区别于 peer 的持续 keepalive。 |
| timing max-handshakes | 最大握手尝试次数范围。 |
| disable-cookies | 关闭协议 cookie 回复；本例仅用于验证该显式选项，不作为所有部署的默认建议。 |

`timing` 的两个数值是范围，不能将配置范围当成正在使用的单个随机值。`display amneziawg profile` 中的 0-0 表示沿用插件默认时序，不表示零秒；默认项不输出到配置正文。

### 查询、保存与转发

```text
display amneziawg profile AWG-P2
display amneziawg interface Tunnel 20
ping -c 3 -a 10.240.20.1 10.240.20.2
ping ipv6 -c 3 -a 2001:db8:240:20::1 2001:db8:240:20::2
```

P1 Profile 示例输出：

```text
Junk : count 3, size 16-48
Padding : init 24, response 28, cookie 20, transport 16, content 4-16
Headers : init 100-110, response 200-210, cookie 300-310, transport 400-410
Timing : rekey-after 90-120, rekey-timeout 4-6, reject-after 170-190, keepalive-timeout 8-10, handshake-attempts 14-18
Header Protection : enabled
Random Trailers : enabled
Disable Cookies : enabled
Junk Packet 1 : raw 4 bytes
Junk Packet 2 : expression <b 0x160301><c><t><r 32><rc 16><rd 8>
```

两端分别检查 IPv4/IPv6 内层可达、握手及收发。保存并重建一端数据面后，再次检查恢复。需要确认签名或填充时，用报文分析设备核对静态载荷 01 02 03 04 与以 16 03 01 开头的动态载荷；仅配置存在不能证明字段已发出。

混淆参数可能增加包长和处理开销，应与对端保持一致，另行检查实际路径 MTU。

### 恢复协议默认值

保留 peer 和隧道，只撤销高级参数：

```text
amneziawg profile AWG-P2
 undo timing rekey-after
 undo timing rekey-timeout
 undo timing reject-after
 undo timing keepalive
 undo timing max-handshakes
 undo header-protection
 undo random-trailers enable
 undo disable-cookies enable
 undo junk-packet 1
 undo junk-packet 2
 undo junk count
 undo junk size
 undo padding content
 undo padding init
 undo padding response
 undo padding cookie
 undo padding transport
 undo header init
 undo header response
 undo header cookie
 undo header transport
 quit
commit
```

P2 对 AWG-P1 执行相同撤销。默认项不在 display this 中展开；查询运行参数并重新探测，确认不再使用自定义填充、标识、签名和头保护。

最后删除业务时，先撤销 Tunnel 引用或删除专用 Tunnel，再删除不再使用的 Profile。保存已确认的最终配置，避免下次加载恢复到示例参数。


### 命名 VPN 中的 IPv6 外层

保留本页高级参数及内层配置，将两端 AWG peer 的外层改到 `CLI-UNDER`，拓扑和 VPN/接口配置见 [WireGuard 的 IPv6 外层案例](wireguard.md#ipv6-外层与-vpn-实例)。AWG 使用自己的 profile 和 UDP 51920：

P1：

```text
amneziawg profile AWG-P2
 peer P2
  undo source
  destination vpn-instance CLI-UNDER 2001:db8:180::2 port 51920
  source 2001:db8:180::1
  quit
 quit
interface Tunnel20
 source-port 51920
 quit
commit
```

P2：

```text
amneziawg profile AWG-P1
 peer P1
  undo source
  destination vpn-instance CLI-UNDER 2001:db8:180::1 port 51920
  source 2001:db8:180::2
  quit
 quit
interface Tunnel20
 source-port 51920
 quit
commit
```

运行 peer 的源与目的应为所配 IPv6 地址。分别检查内层两族流量；外层 VPN 选择不改变内层路由归属。恢复地址族时按 WireGuard 案例顺序执行，并使用本例 Profile 与端口。
