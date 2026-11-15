# 状态与撤销

## 接口状态

Tunnel配置可以在Candidate中分步编辑；协议、源和目的等必需参数不完整时，`commit`会拒绝该配置。参数完整并提交后，设备创建隧道；underlay或对端不可用时接口显示down。

underlay源接口变更IP或VPN时，隧道可以暂时down；恢复依赖后应自动收敛，不应阻止underlay配置进入Candidate。



## `undo interface Tunnel`

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

[功能目录](../tunnel-settings.md) · [命令参数](../reference/tunnels.md)
