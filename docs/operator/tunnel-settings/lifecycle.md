# 状态与撤销

## 接口状态

隧道配置可以在 Candidate 中分步编辑。GRE、IP-in-IP 必须填写所选封装的 source 和 destination 后才能提交；仅撤销其中一项而不补齐时，commit 会拒绝，已生效配置保持不变。临时停用完整隧道使用 shutdown，完整删除使用 undo interface Tunnel。参数完整、未 shutdown 且运行依赖满足后，接口才激活。状态中的 ^down 表示尚未具备创建条件，*down 表示被 shutdown，普通 down 表示运行条件未满足。

修改底层源接口的地址或 VPN、撤销远端路由时，依赖它的隧道可能 Down；恢复条件后自动重新激活。GRE 和 IP-in-IP 的 Up 依据本机端点及底层路由条件，并不检测远端设备是否在线；ARP/ND 未解析、对端配置错误或路径过滤，仍可能导致 Up 状态下业务不通。WireGuard、AmneziaWG 的握手和每个 peer 的可达性需要单独查询。


## `undo interface Tunnel`

**功能**：删除Tunnel逻辑接口及其隧道、地址、LCP和相关接口配置。
**命令格式**：`undo interface Tunnel INSTANCE`
**视图**：系统视图。
**注意事项**：命令进入Candidate，执行`commit`后才从控制面与数据面删除；删除前应确认路由和协议不再引用该接口。


## 功能范围

IPv4 和 IPv6 底层网络均需在选定 VPN 中配置本机源地址和远端路由。需要 IPv6 时，先在承载接口执行 ipv6 enable 并配置相应地址。隧道地址、底层地址、远端业务路由分别检查，避免将其中一项 Up 视为整条业务路径已经可用。

当前版本不提供IPsec和MACsec配置命令。

[功能目录](../tunnel-settings.md) · [命令参数](../reference/tunnels.md)

## 各类隧道的激活条件

| 类型 | 接口激活条件 | 仍需单独验证 |
|---|---|---|
| GRE、四种 IP-in-IP | 接口未 shutdown，封装和端点完整；本机在指定底层 VPN 拥有源地址，该 VPN 有覆盖远端地址的有效路由，隧道已创建 | 对端封装和 GRE key 一致，底层报文可达，业务路由和 MTU 合适 |
| WireGuard、AmneziaWG | 接口未 shutdown，已绑定完整 profile 和私钥，隧道已创建；显式源地址须属于相应底层 VPN，自动源地址按 peer 的出口选择 | peer 的握手、端点、允许前缀及双向流量；单个 peer 不可达不会使共享接口整体 Down |
| VXLAN/NVE | 接口未 shutdown，VTEP 源地址属于底层 VPN；至少一个 peer 的 VNI 绑定业务桥域，且底层路由覆盖该 peer | 每个 VNI/peer、MAC 表、业务端口及实际转发；EVPN 还需正确的路由通告与导入 |

GRE、IP-in-IP、WireGuard 和 AmneziaWG 的 Tunnel 要显示三层 Protocol Up，还需配置有效接口 IP 地址。IPv6 enable 本身不等于已经配置地址。NVE 不配置普通网关地址；其状态取决于 VXLAN 业务依赖。

各功能的具体条件见 [GRE](../gre.md)、[IP-in-IP](../ip-in-ip.md)、[WireGuard](../wireguard.md)、[AmneziaWG](../amneziawg.md) 和 [VXLAN](../vxlan.md)。
