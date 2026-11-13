# Tunnel 接口

配置源地址、目的地址和封装前，先确认两端 underlay 可达。

[命令参考](reference/tunnels.md)

## 接口状态

Tunnel配置可以在Candidate中分步编辑；协议、源和目的等必需参数不完整时，`commit`会拒绝该配置。参数完整并提交后，设备创建隧道；underlay或对端不可用时接口显示down。

underlay源接口变更IP或VPN时，隧道可以暂时down；恢复依赖后应自动收敛，不应阻止underlay配置进入Candidate。


## 通用命令

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


## 功能范围

VortexROS 将 Linux/FRR 作为动态路由控制面、VPP 作为转发面。控制层维持
Linux 全局 IPv6 forwarding 为开启状态，使 FRR 能够把 LCP 接口上的 IPv6
直连网络作为隧道 underlay 的有效路由证据；这不会把隧道业务流量切换到
Linux 数据面。

当前版本不提供IPsec和MACsec配置命令。
