# GRE 互连

**目标**：在两个已可通过 IPv4 互通的实验站点之间建立 GRE。

**前提**：已启用 VPP，双方外层地址 192.0.2.1 和 192.0.2.2 在 default 路由域中互相可达。

## 配置

~~~text
system-view
interface Tunnel 1
 tunnel-protocol gre
 source 192.0.2.1
 destination 192.0.2.2 vpn-instance default
 gre key 100
 ip address 198.51.100.1 255.255.255.252
 quit
commit
~~~

对端调换外层源、目的地址，保持同一个 Key，并将隧道地址改为 198.51.100.2/30。GRE 增加封装开销，Key 用于匹配，不能加密流量。参见 [GRE](../operator/gre.md)。

## 验证

先核对 `display interface Tunnel 1` 和到外层目的地址的路由，再 Ping 198.51.100.2。若需要承载站点网段，还要单独配置业务路由。

## 撤销

先解除引用 Tunnel 1 的业务路由和协议，在系统视图执行 `undo interface Tunnel 1` 并提交。底层接口配置仍保留。
