# GRE

使用 GRE 在 IP 网络上建立三层点到点隧道。

[命令参考](reference/gre.md) · [配置案例](../examples/gre.md)

## 配置与验证

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

source 和 destination 使用同一底层 VPN 实例，GRE key 可以与 VPN 绑定同时配置。修改或撤销 GRE key 并执行 commit 后，系统会重新提交隧道配置并重建隧道，接口会短暂 Down 后恢复 Up，经过该隧道的业务可能瞬时中断。缺省未配置 MTU 时，IPv4 底层的 GRE 三层 MTU 为 1476；配置非零 key 后为 1472。IPv6 底层对应为 1456 和 1452。显式 mtu 覆盖这些默认值，两端应选择适合底层路径的值。两端的 key 应保持一致；无需重新输入未修改的源、目的和 VPN 参数。

```text
display interface Tunnel 1
```

提交后，Tunnel源地址必须能在指定underlay VPN中找到，目的地址也必须通过该VPN可达。隧道up后，Tunnel上的直连路由才应进入路由表。删除GRE隧道：

```text
undo interface Tunnel 1
```

CLI 操作：

```text
commit
```

## 激活条件

GRE 接口未 shutdown，已配置 tunnel-protocol gre、source 和 destination，且本机在所选底层 VPN 拥有 source 地址、该 VPN 有到 destination 的有效路由后，隧道才能激活。三层 Protocol Up 还需 Tunnel 上有有效 IP 地址。

远端未启动 GRE 或 key 不匹配，不一定使本机接口 Down；Up 不代表端到端业务已通。请结合底层可达性、两端参数、隧道地址探测和业务路由检查。源地址或底层路由失效时，接口会 Down，条件恢复后自动激活。状态标记见[隧道状态](tunnel-settings/lifecycle.md)。
