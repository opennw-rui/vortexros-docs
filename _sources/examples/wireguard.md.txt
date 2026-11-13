# WireGuard 互连

## 拓扑

~~~text
P1 host-p1e12 ─────────── host-p2e12 P2
   10.201.12.1/24         10.201.12.2/24
   Tunnel10              Tunnel10
   198.51.100.1/30       198.51.100.2/30
~~~

两端均运行 VPP。先确认外层地址已配置、在 default 路由域互通，且双方允许 UDP 51820。实验中 `host-p1e12` 和 `host-p2e12` 是 VPP 的 AF_PACKET 接口名；使用物理设备时，换成实际端口名。若尚未配置外层地址，先在两端的相应接口上分别提交 `ip address 10.201.12.1 255.255.255.0` 和 `ip address 10.201.12.2 255.255.255.0`。

在各自设备上生成一对密钥。以下是 Linux 命令，需要 `wireguard-tools`：

~~~bash
umask 077
wg genkey > lab-wg.key
wg pubkey < lab-wg.key > lab-wg.pub
~~~

只交换公钥。下列大写占位符要替换为实际值；私钥只填到本端，且会进入设备配置和备份。示例输出省略了公钥行。

## 配置 P1

~~~text
system-view
wireguard profile WG-P2
 peer P2
  publickey P2_PUBLIC_KEY
  allowd-ip 198.51.100.2 32
  source 10.201.12.1
  destination vpn-instance default 10.201.12.2 port 51820
  keepalive 5
  quit
 quit
interface Tunnel 10
 tunnel-protocol wireguard
 privatekey P1_PRIVATE_KEY
 source vpn-instance default
 source-port 51820
 wireguard-profile WG-P2
 ip address 198.51.100.1 255.255.255.252
 quit
commit
~~~

## 配置 P2

~~~text
system-view
wireguard profile WG-P1
 peer P1
  publickey P1_PUBLIC_KEY
  allowd-ip 198.51.100.1 32
  source 10.201.12.2
  destination vpn-instance default 10.201.12.1 port 51820
  keepalive 5
  quit
 quit
interface Tunnel 10
 tunnel-protocol wireguard
 privatekey P2_PRIVATE_KEY
 source vpn-instance default
 source-port 51820
 wireguard-profile WG-P1
 ip address 198.51.100.2 255.255.255.252
 quit
commit
~~~

每个 peer 只匹配对端的隧道地址。隧道直连路由不会让任意站点网段自动进入隧道；新增业务网段时，还需要配置业务路由和相应 Allowed IP。原外层路径保持不变。

## 验证

先从 P2 向 P1 发起一次探测，让 peer 完成初始交换，再分别检查两端。若要定位握手问题，可以在外层链路仅观察 UDP 51820 的收发；不要公开密钥或配置转储。下面是 Debug 5 实验的实际输出节选。

**P1：查询接口与 peer**

~~~text
display wireguard interface Tunnel 10
display wireguard peer WG-P2 P2
~~~

~~~text
Interface : Tunnel10
  Underlay VPN : default
  Source Port : 51820
  Profile : WG-P2

WireGuard Profile : WG-P2
  Peer : P2
    Source : 10.201.12.1
    Destination : 10.201.12.2
    Underlay VPN : default
    Port : 51820
    Keepalive : 5
    Allowed-IP : 198.51.100.2/32
~~~

**P1：** `ping -n -c 3 -t 1500 198.51.100.2`；**P2：** `ping -n -c 3 -t 1500 198.51.100.1`。

~~~text
--- 198.51.100.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms

--- 198.51.100.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms
~~~

接口显示能确认绑定；双向隧道地址探测验证了实际转发。若首次探测超时，核对公钥是否放在对端、源地址是否属于对应 VPN，以及 UDP 端口是否可达。

## 撤销

先解除新增的业务路由引用。在 P1 执行：

~~~text
system-view
undo interface Tunnel 10
undo wireguard profile WG-P2
commit
display wireguard interface
~~~

P2 同样删除 Tunnel 10，将 profile 名换为 `WG-P1`。实测两端查询均不再列出 Tunnel10。保留原外层链路；若已经保存过实验配置，撤销后再保存。

[WireGuard 配置指南](../operator/wireguard.md)
