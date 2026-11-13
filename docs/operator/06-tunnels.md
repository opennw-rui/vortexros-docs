# GRE、IP-in-IP、VXLAN/NVE、WireGuard 与 AmneziaWG

## 通用隧道状态

Tunnel配置可以在Candidate中分步编辑；协议、源和目的等必需参数不完整时，`commit`会拒绝该配置。参数完整并提交后，设备创建隧道；underlay或对端不可用时接口显示down。

underlay源接口变更IP或VPN时，隧道可以暂时down；恢复依赖后应自动收敛，不应阻止underlay配置进入Candidate。

## GRE

```text
interface Tunnel 1
 description P1-P2-GRE
 tunnel-protocol gre
 source 192.0.2.1
 destination 192.0.2.2 vpn-instance default
 gre key 100
 mtu 1476
 ip address 10.0.12.1 255.255.255.252
```

source和destination必须按同一underlay VPN解析；GRE key可以与VPN绑定并存。修改/undo key后应重建所需参数且保持正确外层源地址，不能出现0.0.0.0。

```text
display interface Tunnel 1
display gre tunnel
```

提交后，Tunnel源地址必须能在指定underlay VPN中找到，目的地址也必须通过该VPN可达。隧道up后，Tunnel上的直连路由才应进入路由表。删除GRE隧道：

```text
undo interface Tunnel 1
commit
```

## 手工IP-in-IP隧道

手工IP隧道使用点到点三层接口，支持四种内层与外层地址族组合：

| `tunnel-protocol` | 内层报文 | 外层传输 |
|---|---|---|
| `ipv4-ipv4` | IPv4 | IPv4 |
| `ipv6-ipv4` | IPv6 | IPv4 |
| `ipv4-ipv6` | IPv4 | IPv6 |
| `ipv6-ipv6` | IPv6 | IPv6 |

外层`source`与`destination`必须属于协议指定的同一外层地址族。Tunnel接口地址必须属于协议指定的内层地址族。`destination ... vpn-instance`选择外层目的地址查路使用的underlay VPN；未指定时使用`default`。本功能是手工点到点隧道，不提供自动隧道、6to4、ISATAP或隧道发现。

IPv4 over IPv4示例：

```text
system-view
interface Tunnel 10
 description SITE-A-SITE-B-IPIP
 tunnel-protocol ipv4-ipv4
 source 192.0.2.1
 destination 198.51.100.2 vpn-instance default
 ip address 10.10.10.1 255.255.255.252
quit
commit
display interface Tunnel 10
ping 10.10.10.2
```

IPv6 over IPv4示例：

```text
interface Tunnel 11
 tunnel-protocol ipv6-ipv4
 source 192.0.2.1
 destination 198.51.100.2
 ipv6 address 2001:db8:10::1 64
quit
commit
display interface Tunnel 11
ping 2001:db8:10::2
```

当未显式配置MTU时，系统根据外层IP头自动使用1476字节（GRE over IPv4）、1456字节（GRE over IPv6）、1480字节（IP-in-IP over IPv4）或1460字节（IP-in-IP over IPv6）的有效三层MTU；显式`mtu`始终优先。修改`tunnel-protocol`会清除旧协议的源、目的、underlay及协议专用参数，避免把旧封装参数误用于新协议。

## Tunnel命令参考

### `tunnel-protocol`

**功能**：配置Tunnel接口使用的封装协议。
**命令格式**：`tunnel-protocol { gre | ipv4-ipv4 | ipv6-ipv4 | ipv4-ipv6 | ipv6-ipv6 | wireguard | amneziawg }`
**视图**：Tunnel接口视图。
**缺省情况**：未配置封装协议，接口不能创建。
**参数**：`ipvX-ipvY`中第一个地址族表示内层报文，第二个地址族表示外层传输。
**注意事项**：切换协议会删除旧协议身份参数；配置仍须`commit`才生效。
**撤销命令**：`undo tunnel-protocol`，同时清除该Tunnel的协议身份参数。

### `source`

**功能**：配置GRE或手工IP隧道的外层源IP地址。
**命令格式**：`source IP`
**视图**：已配置GRE或手工IP协议的Tunnel接口视图。
**缺省情况**：未配置。
**参数**：`IP`必须是规范IPv4或IPv6地址，并与协议的外层地址族一致。
**注意事项**：该地址必须在相应underlay中由本机实际拥有；VPN选择由`destination`命令完成。
**撤销命令**：`undo source`。

### `destination`

**功能**：配置GRE或手工IP隧道的外层目的地址及查路VPN。
**命令格式**：`destination IP [vpn-instance NAME]`
**视图**：已配置GRE或手工IP协议的Tunnel接口视图。
**缺省情况**：未配置；未指定`vpn-instance`时使用`default`。
**参数**：`IP`为远端外层地址；`NAME`为已存在的VPN实例。
**注意事项**：源与目的必须属于同一外层地址族；提交后应在所选VPN中验证到目的地址的路由。
**撤销命令**：`undo destination`，同时撤销该目的地址关联的underlay VPN。

### `gre key`

**功能**：为GRE封装配置可选的32位Key。
**命令格式**：`gre key KEY`
**视图**：`tunnel-protocol gre`的Tunnel接口视图。
**缺省情况**：不携带GRE Key。
**注意事项**：两端Key必须一致；该命令不适用于IP-in-IP、WireGuard或AmneziaWG。
**撤销命令**：`undo gre key`。

### `undo interface Tunnel`

**功能**：删除Tunnel逻辑接口及其隧道、地址、LCP和相关接口配置。
**命令格式**：`undo interface Tunnel INSTANCE`
**视图**：系统视图。
**注意事项**：命令进入Candidate，执行`commit`后才从控制面与数据面删除；删除前应确认路由和协议不再引用该接口。

## VXLAN与NVE

NVE用于集中保存VXLAN源地址和远端VTEP信息，不承载普通三层转发。因此NVE可以进入配置视图、display和undo，但不会出现在路由、BFD、VRRP或ACL等需要真实转发接口的命令补全中。

```text
interface Nve 1
 source 192.0.2.1
 vni 1011 head-end peer-list 192.0.2.2
```

BD/VNI和Vbdif见接口章节。验证：

```text
display vxlan tunnel
display vxlan statistics
display bridge-domain 11
display mac-address
```

underlay变化导致VXLAN暂时不可用时，应撤销相关数据面接口/路由并在恢复后自动重建。

使用BGP自动发现远端VTEP和MAC时，将静态peer命令替换为
`vni VNI head-end peer-list protocol bgp`，并配置bridge-domain EVPN RD/RT和BGP
EVPN地址族。完整步骤、限制及Type-2/Type-3验证见[VXLAN EVPN](11-vxlan-evpn.md)。

NVE是控制层逻辑对象，没有独立的VPP收发计数器和MTU，因此`display interface brief`中的利用率显示`0.0%`、MTU显示`--`。实际VXLAN成员的原始计数使用`display vxlan statistics`查看，避免把父接口、子接口和多个VXLAN成员重复相加。创建、管理状态、MTU、桥域绑定及删除属于同一VPP会话事务；VPP在中途重启时本次操作失败关闭，由下一轮权威收敛重建，不会继续使用旧接口索引。

删除远端或整个NVE配置：

```text
interface Nve 1
 undo vni 1011 head-end peer-list 192.0.2.2
undo interface Nve 1
commit
```

## WireGuard

Profile保存peer及其各自的外层source、destination和underlay VPN；Tunnel保存private key、兼容用的默认underlay、监听端口和profile引用。peer未指定underlay时继承Tunnel默认值。

```text
wireguard profile WG-PROFILE
 peer SITE-B
  publickey BASE64-PUBLIC-KEY
  allowd-ip 10.20.0.0 16
  source 192.0.2.1
  destination vpn-instance default 198.51.100.2 port 51820
  keepalive 25
#
interface Tunnel 10
 tunnel-protocol wireguard
 privatekey auto
 source vpn-instance default
 wireguard-profile WG-PROFILE
 mtu 1500
 ip address 10.255.0.1 255.255.255.252
```

WG/AWG profile和peer名称是区分大小写的单个CLI token，长度为1至64个字符，不允许空白、引号或命令分隔符。为兼容旧版已经保存且能够无歧义重放的配置，字母、数字、`_`、`-`、`.`和`:`均可使用；命令关键字本身仍不区分大小写。

peer下的`destination vpn-instance NAME [IP port PORT]`选择该peer的underlay VPN；`source IP`可选地固定该peer的外层源地址。未配置peer source时，VPP先使用该peer经过认证报文学习到的本地外层地址，再按endpoint和underlay路由自动选源；兼容配置中的Tunnel source只作为旧配置默认值。客户端省略`source-port`，每次创建接口时使用随机临时源端口。只有作为监听端的服务端才配置固定`source-port`。CFG中始终先输出peer `source`，再输出`destination`。

`privatekey auto`生成后，配置规范化为实际privatekey，并追加public key。WG/AWG的privatekey、presharedkey和header-protection key在Running、Candidate和CFG中均以明文保存，display也显示原值。因此必须保持`/VortexROS/config`、备份、审计采集和root终端的最小权限。旧版`cipher`行仅在启动回放时受理，daemon会将它一次性迁移为明文CFG；新配置不再生成密文。

Allowed IP限制该peer允许收发的地址范围，并参与Tunnel接口内的最长前缀peer选择。Tunnel使用点到点三层接口语义，路由可以只指定WG/AWG出接口而不写下一跳；数据面按报文最终内层目的地址选择peer，不依赖创建该邻接时偶然选中的peer，也不需要ARP。Allowed IP不会为任意业务网段自动创建系统路由；业务前缀仍需静态或动态路由。

每个peer的显式source与destination必须属于同一外层地址族；不同peer可以使用不同underlay VPN及不同外层地址族。IPv6 overlay可以与IPv4或IPv6 underlay组合，需为peer配置相应IPv6 `allowd-ip`。未配置任何`allowd-ip`表示该peer不匹配任何业务地址，不再隐式扩展成`0.0.0.0/0`。不同peer可以配置嵌套前缀，数据面按最长前缀选择；完全相同的前缀不能由两个peer同时拥有。

VortexROS默认启用WG和AWG异步加密。加密、解密和post节点可由VPP加密调度器分配到其他worker，发送和接收方向也可在不同核心执行；控制层每次收敛相关隧道时都会显式恢复该默认值，若切换失败则停止继续修改，避免配置成功但实际仍落在非预期执行模式。

服务端peer可以不配置`destination`，首个通过认证的报文会学习并更新该peer的漫游endpoint；这种模式必须在Tunnel上配置固定监听端口：

```text
wireguard profile WG-SERVER
 peer ROAMING-CLIENT
  publickey BASE64-PUBLIC-KEY
  allowd-ip 10.40.0.0 24
  destination vpn-instance default
#
interface Tunnel 11
 tunnel-protocol wireguard
 privatekey auto
 source vpn-instance default
 source-port 51820
 wireguard-profile WG-SERVER
 ip address 10.40.0.1 255.255.255.0
```

## 修改和删除

- 新增或删除peer只影响该peer；
- 修改密钥、目的地址或监听参数时，相关Tunnel可能短暂重新建立；
- profile仍被Tunnel引用时不能删除；
- 修改peer underlay、source或destination后，应重新检查对应VPN中到公网地址的路由。

```text
interface Tunnel 10
 undo wireguard-profile WG-PROFILE
 undo source
undo wireguard profile WG-PROFILE
commit
```

## 验证

```text
display wireguard
display interface Tunnel 10
display ip routing-table
ping -vpn-instance BLUE 10.255.0.2
```

除接口状态外，还应从对端确认握手、收发计数和业务路由。只有Tunnel地址可达而业务前缀没有路由时，WireGuard不会自动补充路由。

## AmneziaWG

AmneziaWG使用独立的数据面插件、接口和peer对象，不替换WireGuard；两类隧道可以同时配置。Profile除peer外，还保存握手前垃圾包、报文前置填充、消息头范围、内容填充、随机尾部和定时参数。两端必须使用一致的协议参数。

下面示例启用3个随机垃圾包、不同消息头范围和固定前置填充。启用header protection时，四类报文的前置填充都必须不少于12字节。

```text
amneziawg profile AWG-PROFILE
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
 timing rekey-timeout 4 6
 header-protection BASE64-32-BYTE-KEY
 random-trailers enable
 junk-packet 1 expression "<b 0x160301><c><t><r 32><rc 16><rd 8>"
 #
 peer SITE-B
  publickey BASE64-PUBLIC-KEY
  allowd-ip 10.30.0.0 16
  source 192.0.2.1
  destination vpn-instance default 198.51.100.2 port 51820
  keepalive 25
#
interface Tunnel 20
 tunnel-protocol amneziawg
 privatekey auto
 source vpn-instance default
 amneziawg-profile AWG-PROFILE
 mtu 1500
 ip address 10.255.20.1 255.255.255.252
commit
```

`junk-packet SLOT BASE64`用于配置1至5号静态原始报文槽位；`junk-packet SLOT expression "EXPRESSION"`用于动态生成握手前报文。表达式支持：`<b 0x...>`固定字节、`<c>`每次握手随机起始且逐槽递增的32位网络序计数、`<t>`当前Unix秒、`<r N>`随机字节、`<rc N>`随机英文字母和`<rd N>`随机数字。表达式最多4096字节，展开后的单个报文最多4096字节，动态标签最多128个；错误表达式在进入Candidate前拒绝。表达式在配置时编译，握手热路径只复制模板并填充动态字段。Jc/Jmin/Jmax产生的随机垃圾包与这些槽位相互独立。

Allowed IP、underlay VPN、动态客户端源端口、固定服务端监听端口和漫游endpoint的语义与WireGuard相同。Tunnel直连前缀会按Allowed IP最长前缀映射到peer，非直连业务网段仍由路由配置决定。修改协议参数时，已存在的peer会被最小化重建；修改单个peer只影响该peer。

验证命令：

```text
display amneziawg profile AWG-PROFILE
display amneziawg peer AWG-PROFILE SITE-B
display amneziawg interface Tunnel 20
display interface Tunnel 20
ping 10.255.20.2
```

删除时先解除Tunnel引用，再删除profile：

```text
interface Tunnel 20
 undo amneziawg-profile
undo amneziawg profile AWG-PROFILE
commit
```

当前版本已经验证IPv4与IPv6 overlay、IPv4 underlay、header protection、内容填充、随机尾部、cookie关闭、静态/动态垃圾包以及peer反复增删。动态表达式采用上述明确语法，非法或超过边界的输入不会部分生效。

## 功能范围

VortexROS 将 Linux/FRR 作为动态路由控制面、VPP 作为转发面。控制层维持
Linux 全局 IPv6 forwarding 为开启状态，使 FRR 能够把 LCP 接口上的 IPv6
直连网络作为隧道 underlay 的有效路由证据；这不会把隧道业务流量切换到
Linux 数据面。

当前版本不提供IPsec和MACsec配置命令。
