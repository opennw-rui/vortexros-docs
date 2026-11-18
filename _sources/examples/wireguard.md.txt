# WireGuard 互连

## 拓扑

~~~text
P1 Ethernet0 ─────────── Ethernet0 P2
   10.201.12.1/24         10.201.12.2/24
   Tunnel10              Tunnel10
   198.51.100.1/30       198.51.100.2/30
~~~

两端运行 VortexROS 与配套 VPP，底层地址 10.201.12.1/24、10.201.12.2/24 配置在各自 Ethernet0，default 路由域双向可达，并允许 UDP 51820。

两端先在 Tunnel10 视图生成各自密钥，保持当前 Candidate，交换 display configuration candidate 中的公钥；完成下方 Profile 及隧道配置后再统一提交：

~~~text
system-view
~~~

配置清单：

~~~text
interface Tunnel 10
 tunnel-protocol wireguard
 privatekey auto
#
~~~

CLI 操作：

~~~text
display configuration candidate
~~~

只交换公钥，私钥随配置保存，应限制配置和备份的访问。后续不再重复执行 privatekey auto，以免更换已交换的密钥。

## 配置 P1

~~~text
system-view
~~~

配置清单：

~~~text
wireguard profile WG-P2
 peer P2
  publickey P2_PUBLIC_KEY
  allowd-ip 198.51.100.2 32
  source 10.201.12.1
  destination vpn-instance default 10.201.12.2 port 51820
  keepalive 5
#
interface Tunnel 10
 tunnel-protocol wireguard
 source vpn-instance default
 source-port 51820
 wireguard-profile WG-P2
 ip address 198.51.100.1 255.255.255.252
#
~~~

CLI 操作：

~~~text
commit
~~~

## 配置 P2

~~~text
system-view
~~~

配置清单：

~~~text
wireguard profile WG-P1
 peer P1
  publickey P1_PUBLIC_KEY
  allowd-ip 198.51.100.1 32
  source 10.201.12.2
  destination vpn-instance default 10.201.12.1 port 51820
  keepalive 5
#
interface Tunnel 10
 tunnel-protocol wireguard
 source vpn-instance default
 source-port 51820
 wireguard-profile WG-P1
 ip address 198.51.100.2 255.255.255.252
#
~~~

CLI 操作：

~~~text
commit
~~~

每个 peer 只匹配对端的隧道地址。隧道直连路由不会让任意站点网段自动进入隧道；新增业务网段时，还需要配置业务路由和相应 Allowed IP。原外层路径保持不变。

## 验证

先向对端隧道地址发起探测，再查询接口绑定、端点与接口收发计数。外层 UDP 可达、密钥和 Allowed IP 正确才可能建立隧道。示例输出省略密钥，不应公开实际配置转储。

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
~~~

配置清单：

~~~text
undo interface Tunnel 10
undo wireguard profile WG-P2
~~~

CLI 操作：

~~~text
commit
display wireguard interface
~~~

P2 同样删除 Tunnel 10，将 profile 名换为 `WG-P1`。两端查询应不再列出 Tunnel10。保留原外层链路；若已经保存过示例配置，撤销后再保存。

[WireGuard 配置指南](../operator/wireguard.md)


## IPv6 外层与 VPN 实例

本节是独立双端配置，先按上一节撤销冲突的 Tunnel10 和 Profile。双方 Ethernet0 位于 CLI-UNDER，内层 Tunnel10 位于 default VPN，内外层路由归属独立。

先按本页开头在两端创建 Tunnel10、执行 privatekey auto，并交换公钥；保留该 Candidate，再补齐以下配置。将 P1_PUBLIC_KEY、P2_PUBLIC_KEY 替换为对应实际公钥。

### P1

~~~text
system-view
~~~

配置清单：

~~~text
ip vpn-instance CLI-UNDER
 ipv6-family
#
interface Ethernet0
 ipv6 enable
 ip binding vpn-instance CLI-UNDER
 ipv6 address 2001:db8:180::1 64
#
wireguard profile WG-P2
 peer P2
  publickey P2_PUBLIC_KEY
  allowd-ip 10.240.10.2 32
  allowd-ip 2001:db8:240:10::2 128
  source 2001:db8:180::1
  destination vpn-instance CLI-UNDER 2001:db8:180::2 port 51820
  keepalive 5
#
interface Tunnel10
 ipv6 enable
 tunnel-protocol wireguard
 source vpn-instance CLI-UNDER
 source-port 51820
 wireguard-profile WG-P2
 ip address 10.240.10.1 255.255.255.252
 ipv6 address 2001:db8:240:10::1 64
#
~~~

CLI 操作：

~~~text
commit
~~~

### P2

~~~text
system-view
~~~

配置清单：

~~~text
ip vpn-instance CLI-UNDER
 ipv6-family
#
interface Ethernet0
 ipv6 enable
 ip binding vpn-instance CLI-UNDER
 ipv6 address 2001:db8:180::2 64
#
wireguard profile WG-P1
 peer P1
  publickey P1_PUBLIC_KEY
  allowd-ip 10.240.10.1 32
  allowd-ip 2001:db8:240:10::1 128
  source 2001:db8:180::2
  destination vpn-instance CLI-UNDER 2001:db8:180::1 port 51820
  keepalive 5
#
interface Tunnel10
 ipv6 enable
 tunnel-protocol wireguard
 source vpn-instance CLI-UNDER
 source-port 51820
 wireguard-profile WG-P1
 ip address 10.240.10.2 255.255.255.252
 ipv6 address 2001:db8:240:10::2 64
#
~~~

CLI 操作：

~~~text
commit
~~~

两端查询 display wireguard interface Tunnel10 和各自 peer；端点应是 2001:db8:180::1、::2。P1 执行以下命令，P2 使用本端源地址反向检查：

~~~text
ping -a 10.240.10.1 -c 3 10.240.10.2
ping ipv6 -a 2001:db8:240:10::1 -c 3 2001:db8:240:10::2
~~~

检查握手和计数更新，确认两族内层双向可达。保存使用 save。

撤销时先删除 Tunnel10，再删除 WG-P1/WG-P2；两端解除 Ethernet0 的 VPN 绑定并撤销本例地址，删除不再引用的 CLI-UNDER，提交并保存。其他共用接口、VPN 和业务不能随本例删除。

## 漫游端点

固定服务器在 Tunnel 视图配置 `source-port`；服务器 peer 可以撤销 `source` 和 `destination`，让经过认证的客户端握手更新远端地址与端口。客户端通过 `destination ... port ...` 指定服务器，`undo source-port` 使用自动分配的本地端口。`keepalive 0` 是不发送周期保活，不会禁止业务触发握手。

使用自动端口时，数据面重建后端口可能变化。对端需允许端点更新，检查新握手及双向流量；不要把一次运行的动态端口固定写入配置。


## 双栈内层与漫游客户端

固定公网入口的一端可不配置对端地址，由认证报文学习客户端当前的地址和 UDP 端口。固定端必须保留 source-port；客户端必须知道固定端地址。双方仍须配置对方公钥和允许的业务前缀。

以下在已有双端隧道上修改。固定端使用 Tunnel95、profile WG-CLIENT、peer CLIENT；客户端使用 profile WG-SERVER、peer SERVER。两端外层地址为 Ethernet0 上的 198.19.80.1/30、198.19.80.2/30，内层为 198.18.245.1/30、198.18.245.2/30 和 fd00:245::1/64、fd00:245::2/64。创建密钥、profile 及 Tunnel 的步骤与基础例相同，替换相应名称和地址。

固定端：

```text
wireguard profile WG-CLIENT
 peer CLIENT
  allowd-ip 198.18.245.2 32
  allowd-ip fd00:245::2 128
  undo source
  undo destination
  undo keepalive
#
interface Tunnel 95
 source vpn-instance default 198.19.80.1
 source-port 51895
 ipv6 enable
 ipv6 address fd00:245::1 64
#
```

CLI 操作：

```text
commit
```

客户端：

```text
wireguard profile WG-SERVER
 peer SERVER
  allowd-ip 198.18.245.1 32
  allowd-ip fd00:245::1 128
  undo source
  destination vpn-instance default 198.19.80.1 port 51895
  keepalive 7
#
interface Tunnel 95
 undo source
 undo source-port
 ipv6 enable
 ipv6 address fd00:245::2 64
#
```

CLI 操作：

```text
commit
```

客户端的外层源地址由路由选择，源端口动态分配。固定端的 display wireguard peer 仍显示配置中的空 destination、port 0；这表示漫游响应配置，不代表没有实际对端。该查询不显示已学习端点或握手时间。应通过 display interface Tunnel95 的非零计数和双向业务探测确认效果。

本例固定端监听 51895，客户端自动取得端口 59537，固定端学习该端点。自动源地址模式下，IPv4 和 IPv6 探测各 1/1。自动端口可在重建后变化，无需将这次分配结果写入客户端配置。固定端保存并重启控制服务后，配置和密钥恢复，双栈探测仍各 1/1；等待健康状态 ready、无告警后检查业务。

### 验证 Allowed IP 与预共享密钥

- 删除固定端对客户端 IPv6 的 allowd-ip 后，IPv6 探测为 0/1，同一隧道 IPv4 为 1/1；补回该前缀后双栈恢复。
- 只给一端增加 presharedkey 时，探测为 0/1；两端使用相同密钥后为 1/1。双方协调执行 undo presharedkey 后，原隧道仍为 1/1。
- 从完整 peer 中撤销 publickey 后提交被拒绝，原 Running 和运行隧道保留，服务仍 ready；补全公钥后再提交。
- 这些配置不自动发布业务路由，也不允许 Allowed IP 之外的内层来源。动态地址场景仍需底层路由、UDP 可达及适当的网络访问控制。
