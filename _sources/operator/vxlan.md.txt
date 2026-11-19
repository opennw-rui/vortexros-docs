# VXLAN

使用静态 VTEP 列表在三层网络上延伸二层桥域。

[命令参考](reference/vxlan.md) · [配置案例](../examples/vxlan.md)

## 工作原理与业务标识

VXLAN（RFC 7348）用 UDP 在三层底层网络上封装以太网帧，24 位 VNI 区分二层业务。VTEP 地址属于底层路由域，客户 MAC/IP 属于覆盖业务；两套地址的可达性分别规划。

静态部署手工指定远端 VTEP，EVPN 部署通过 BGP 交换 MAC、IP 和业务成员信息。建立隧道不等于完成客户 MAC 学习，也不等于业务网关可用。VNI、桥域、客户接入口和可用远端成员须对应一致。

底层 MTU 需容纳外层以太网、IP、UDP、VXLAN 及可能保留的客户 VLAN 标签。VNI 不自动提供加密或跨业务访问控制。增加远端、改变 VNI 或标签重写可能改变洪泛和学习范围，应同时检查单播、ARP/ND 和业务隔离。

## 配置与验证

NVE用于集中保存VXLAN源地址和远端VTEP信息，不承载普通三层转发。因此NVE可以进入配置视图、display和undo，但不会出现在路由、BFD、VRRP或ACL等需要真实转发接口的命令补全中。

```text
interface Nve 1
 source 192.0.2.1
 vni 1011 head-end peer-list 192.0.2.2
```

BD、VNI 和 Vbdif 见[桥域](bridge-domains.md)。验证：

```text
display vxlan tunnel
display vxlan statistics source 192.0.2.1 peer 192.0.2.2 vni 1011
display bridge-domain 11
display mac-address
```

源地址或底层路由变化时，受影响的 VXLAN 成员会随可用条件自动停用、恢复。确认受影响的 VNI，待底层恢复后检查成员状态和业务。

使用BGP自动发现远端VTEP和MAC时，将静态peer命令替换为
`vni VNI head-end peer-list protocol bgp`，并配置bridge-domain EVPN RD/RT和BGP
EVPN地址族。完整步骤、限制及Type-2/Type-3验证见[VXLAN EVPN](11-vxlan-evpn.md)。

NVE 汇总 VXLAN 业务配置，没有独立的收发计数器和 MTU，因此`display interface brief`中的利用率显示`--`、MTU显示`--`。实际VXLAN成员的原始计数使用`display vxlan statistics source LOCAL peer REMOTE [vni VNI]`查看，避免把父接口、子接口和多个VXLAN成员重复相加。创建、变更或删除后，检查隧道、业务桥域和流量；数据面重建期间的操作可能尚未完成，应等待健康状态恢复后再检查业务。

删除远端或整个NVE配置：

```text
interface Nve 1
 undo vni 1011 head-end peer-list 192.0.2.2
#
undo interface Nve 1
```

CLI 操作：

```text
commit
```


`display vxlan tunnel [ID]` 的 Type 区分手工peer-list的 `static`、EVPN的 `L2 dynamic` 和 `L3 dynamic`。汇总仅统计当前筛选范围；`unmanaged` 表示实际隧道没有匹配到当前已提交配置的归属，不能把它当成配置已生效。单个隧道编号属于运行态，数据面重建后可能改变。隧道表的 State 表示实际成员接口状态，不能代替底层路由和远端可达性检查。

静态 NVE 也可以通过 source ADDRESS vpn-instance NAME 选择底层 VPN。
配置了命名底层 VPN 的静态成员实际查询如下：

~~~text
<VortexROS> display vxlan tunnel
Tunnel ID       Source            Destination       State       Type
8               198.18.77.1       198.18.77.2       up          static
Total: 1    Static: 1    L2 dynamic: 0    L3 dynamic: 0    Unmanaged: 0
~~~

此输出确认该成员归属于手工 peer-list，不表示远端已可达。仍需核对所选 VPN 的路由、
VTEP 地址、桥域成员及实际业务；没有业务流量时，收发计数为0是正常观察结果。


EVPN双VNI的实际查询示例：

```text
<VortexROS> display vxlan tunnel
Tunnel ID       Source            Destination       State       Type
9               198.19.23.3       198.19.80.2       up          L2 dynamic
10              198.19.23.3       198.19.80.1       up          L2 dynamic
12              198.19.23.3       198.19.80.2       up          L2 dynamic
14              198.19.23.3       198.19.80.1       up          L2 dynamic
Total: 4    Static: 0    L2 dynamic: 4    L3 dynamic: 0    Unmanaged: 0
```

按业务VNI查询收发计数，避免将不同VNI合并：

```text
<VortexROS> display vxlan statistics source 198.19.23.3 peer 198.19.80.1 vni 50460
Item                 Packets                      Bytes
Inbound              4                            340
Outbound             2                            212
```

## QinQ 业务的 VXLAN 载荷

显式 QinQ 子接口采用 `rewrite pop single` 时，入方向移除固定外层标签，VXLAN 载荷保留内层客户标签。回程经过该子接口时恢复固定外层标签。采用 `rewrite pop none` 时保留原有标签。[二层子接口标签处理](subinterfaces-l2.md#标签处理)

例如在本端设置外层 200、内层 10 或 12–13，并接入使用 VNI 5310 的 BD 310。对端将同一 VNI 接入其 BD 310，由客户接入口转发。以下为本端业务接入配置，底层链路与 NVE 使用前面的配置方式。

```text
bridge-domain 310 uu-flood
 vxlan vni 5310
#
interface Ethernet 1.17 mode l2
 encapsulation qinq vid 200 ce-vid 10 12 to 13
 rewrite pop single
 bridge-domain 310
#
```

用 `display bridge-domain 310` 和 `display vxlan statistics source 198.18.250.1 peer 198.18.250.2 vni 5310` 检查成员和收发。实测内层 VID 13 的接入帧带 200/13 两层标签，VNI 5310 线上载荷和对端接入口均只带内层 13，回程恢复 200/13。改用 `encapsulation dot1ad vid 200 ce-vid 10 12 to 13` 后，实测出口恢复 0x88a8 外层，内层 12 和 13 均通过。处在范围空洞的内层 11 不进入该隧道。

撤销接入时在系统视图执行 `undo interface Ethernet 1.17`，提交后用 `display bridge-domain 310` 复查剩余成员。若同时撤销 VXLAN 业务，再移除对应远端和 VNI。

## 激活条件

NVE 必须未 shutdown，本机须在所选底层 VPN 拥有 VTEP 源地址。VNI 须绑定业务桥域，并存在远端 VTEP 和到该地址的有效底层路由。至少一个 peer 满足这些条件时，NVE 可显示 Up；这不表示其余 peer 或所有 VNI 均可用。

静态 VXLAN 的远端来自手工 peer-list；EVPN 的远端和业务路由由 BGP 交换，还需邻居、VNI、RD/RT 和导入规则正确。逐个查询 display vxlan tunnel、桥域成员和 MAC 表，再验证业务。源地址或底层路由失效后，受影响的隧道会停用，条件恢复后自动重建。


## NVE 汇总状态

静态 peer-list 使用源地址、VNI 和所选底层路由判断可用条件。EVPN 动态成员还需已学习远端 VTEP，并建立属于该 NVE 的 VXLAN 成员；成员的源地址、底层 VPN 和 VNI 必须匹配，且实际成员处于 Up。L2VNI 与租户 L3VNI 都纳入汇总，其他源地址或其他底层 VPN 的隧道不计入。

实际包含两个 L2VNI 和一个 L3VNI 时：

```text
Nve1 current state : UP
Line protocol current state : UP
Interface type: VXLAN overlay
Source address: 198.19.23.3
EVPN VNIs: 50460, 50461
L3VNIs: 50081
Underlay VPN-Instance: default
```

本例实际有 4 个 L2 dynamic、1 个 L3 dynamic 成员。撤销最后的 VNI 绑定后，成员数为 0，NVE 的物理及协议状态均为 Down；恢复绑定和 EVPN 控制配置后，5 个成员及 NVE Up 状态恢复。部分成员 Up 仅表示该 NVE 至少有一条可用业务路径，各 VNI 仍需分别检查路由、MAC 和流量。

[完整撤销与恢复顺序](evpn/lifecycle.md)
