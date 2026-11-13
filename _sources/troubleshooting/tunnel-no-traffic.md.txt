# 隧道 Up 但业务不通

以下以 WireGuard 为例。先分别验证底层地址、隧道地址和业务前缀，确认失败发生在哪一段。

~~~text
display interface Tunnel 10
display wireguard interface Tunnel 10
display wireguard peer WG-P2 P2
display ip routing-table
~~~

1. 底层目标不可达时，检查 peer 的源地址、目标 UDP 端口及 underlay VPN。两端核对外层回程和防火墙策略。
2. 底层可达但隧道地址不通时，检查双方是否使用了各自的私钥及正确的对端公钥，再核对两端的 Allowed‑IP 和监听端口。
3. 隧道地址可通但业务不通时，两端分别核对业务前缀是否进入正确隧道、是否包含在相应 peer 的 Allowed‑IP 中，以及对端是否有回程路由。只有大包失败时，再按外层封装开销检查隧道和底层 MTU。

隔离案例的 P1 回读如下。用它核对 peer 的外层目标、VPN 和允许的隧道地址，再以双向 Ping 验证数据通路。

~~~text
    Source : 10.201.12.1
    Destination : 10.201.12.2
    Underlay VPN : default
    Port : 51820
    Allowed-IP : 198.51.100.2/32
~~~

修正后先双向探测隧道地址，再由两端业务主机探测实际业务网段。完整配置和实际输出见[WireGuard 案例](../examples/wireguard.md)；静态 VXLAN 的 VNI、桥域和 MAC 核对见[静态 VXLAN 案例](../examples/vxlan.md)。
