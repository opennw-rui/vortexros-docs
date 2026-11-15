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

先从 P2 向 P1 发起一次探测，让 peer 完成初始交换，再分别检查两端。若要定位握手问题，可以在外层链路仅观察 UDP 51820 的收发；不要公开密钥或配置转储。下面沿用已有实验的实际输出节选；本轮未重复执行该未受影响的用例。

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


## IPv6 外层与 VPN 实例

下面沿用开发服务器的补充实测，使用已建立的 Tunnel10。两端隧道内层仍为 `10.240.10.1/30`、`10.240.10.2/30` 和 `2001:db8:240:10::1/64`、`::2/64`；只把加密 UDP 外层从公网 IPv4 改为命名 VPN 实例中的 IPv6。内层接口不必加入外层 VPN 实例。

```text
P1 Tunnel10 ── 加密 UDP/IPv6 ── P2 Tunnel10
  host-p1b12                    host-p2b12
  2001:db8:180::1/64             2001:db8:180::2/64
  └──────── VPN CLI-UNDER ────────────┘
```

P1：

```text
system-view
ip vpn-instance CLI-UNDER
 ipv4-family
  quit
 ipv6-family
  quit
 quit
interface host-p1b12
 ip binding vpn-instance CLI-UNDER
 ipv6 address 2001:db8:180::1 64
 quit
wireguard profile WG-P2
 peer P2
  undo source
  destination vpn-instance CLI-UNDER 2001:db8:180::2 port 51820
  source 2001:db8:180::1
  quit
 quit
interface Tunnel10
 source-port 51820
 quit
commit
```

P2：

```text
system-view
ip vpn-instance CLI-UNDER
 ipv4-family
  quit
 ipv6-family
  quit
 quit
interface host-p2b12
 ip binding vpn-instance CLI-UNDER
 ipv6 address 2001:db8:180::2 64
 quit
wireguard profile WG-P1
 peer P1
  undo source
  destination vpn-instance CLI-UNDER 2001:db8:180::1 port 51820
  source 2001:db8:180::2
  quit
 quit
interface Tunnel10
 source-port 51820
 quit
commit
```

`ip binding vpn-instance` 会清除该接口原有 IP 地址，应先确认接口用途，再在绑定后配置地址。改变外层地址族时先撤销旧 `source`，再设置新目的和新源，避免保留地址族不匹配的中间配置。示例使用两端已完成的密钥及 allowed-IP 配置，不会另行生成或覆盖密钥。

实测查询与流量：

```text
display current-configuration configuration wireguard
display ip vpn-instance verbose
ping -c 3 -a 10.240.10.1 10.240.10.2
ping ipv6 -c 3 -a 2001:db8:240:10::2 2001:db8:240:10::1
```

配置查询显示 `destination vpn-instance CLI-UNDER 2001:db8:180::2 port 51820`；实际 peer 外层端点也是两端的 `2001:db8:180::` 地址。IPv4 两个方向均为 3/3；上述 IPv6 P2→P1 为 3/3。这里是实际转发验证，不是吞吐测量。

恢复原外层时，在两端 peer 视图先 `undo source`，然后把 `destination` 和 `source` 改回原地址、端口及外层实例，提交并复测。只有没有接口、路由、协议或其他隧道引用时，才能删除 `CLI-UNDER`。

## 漫游端点

固定服务器在 Tunnel 视图配置 `source-port`；服务器 peer 可以撤销 `source` 和 `destination`，让经过认证的客户端握手更新远端地址与端口。客户端通过 `destination ... port ...` 指定服务器，`undo source-port` 使用自动分配的本地端口。`keepalive 0` 是不发送周期保活，不会禁止业务触发握手。

本轮实测客户端重启 VPP 后，服务器学到的新 WireGuard 端口为 58120，AmneziaWG 为 60103，均与重启前不同；对应 IPv4 双向探测均为 3/3。自动端口没有固定数值，不能在真实配置中照抄这些观测值。
