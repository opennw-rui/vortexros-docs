# AmneziaWG 互连

## 拓扑

| 位置 | P1 | P2 |
| --- | --- | --- |
| 底层 IPv4 | 10.201.12.1/24 | 10.201.12.2/24 |
| UDP 监听 | 51920 | 51920 |
| Tunnel20 | 198.51.100.41/30 | 198.51.100.42/30 |

两端运行同一配套 VPP，底层地址已双向可达。两端生成各自密钥对，例如在 Linux 上用 `wg genkey`、`wg pubkey` 生成 X25519 密钥，只交换公钥。替换下面的 `LOCAL_PRIVATE_KEY` 和 `REMOTE_PUBLIC_KEY`。私钥随配置保存，不应写入公开日志。

两端的填充和消息头范围要相同。实验只允许对端隧道地址进入各自 peer，不通告其他业务网段。

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
 privatekey LOCAL_PRIVATE_KEY
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
 privatekey LOCAL_PRIVATE_KEY
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

P2 反向执行 `ping -n -c 3 -t 1500 198.51.100.41`。实际输出节选：

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

P2 将 profile 换为 `AWG-P1`。实测两端查询均不再显示 Tunnel20。

[AmneziaWG 配置指南](../operator/amneziawg.md)
