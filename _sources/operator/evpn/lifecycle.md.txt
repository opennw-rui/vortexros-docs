# EVPN 变更与恢复

## 撤销 ESI

改变或撤销 ESI 会重建多归属通告及远端下一跳，应先协调同一客户的两台接入 PE 和 CE。仅在一台 PE 撤销 ESI、另一台仍按原 ESI 发布同一双归属客户时，可能触发 MAC 移动保护并使部分 VLAN 不通，不能把“聚合仍 Up”当作业务无影响。

在聚合接口视图执行`undo esi`并提交。聚合恢复为普通桥接成员，原有 VLAN、成员接口及管理状态保留：

~~~text
interface Eth-Trunk 11
 undo esi
#
~~~

CLI 操作：

~~~text
commit
display interface Eth-Trunk 11
display bgp evpn all routing-table
~~~

多归属业务的远端下一跳组会随ES通告变化。变更期间检查剩余路径和客户业务，不能只查看本地聚合是否Up。

## 删除 VNI

`undo vni VNI`删除选定VNI的整个head-end绑定；带静态peer后缀时只删除该对端，带`protocol bgp`时只撤销动态发现。其他VNI保留。

先在NVE视图撤销绑定，提交后核对隧道、MAC及对应业务路由。删除BGP EVPN地址族前，必须先解除使用它的NVE依赖。

## 保存与重建

完成变更并确认业务正常后执行`save`。重建数据面后检查BGP邻居、EVPN路由、VXLAN隧道、业务FIB和客户连通性。

共用的NVE、BGP进程和底层路由不应随单个业务一起删除。完整操作见[二层业务](../../examples/evpn/l2vpn.md)、[三层业务](../../examples/evpn/l3vpn.md)和[多归属](../../examples/evpn/all-active.md)。


## 完整停用并恢复 EVPN

本例为未承担客户多归属 ESI 的 PE，原有 VNI 为 50460、50461，租户 D1-TYPE5 使用 L3VNI50081。承担多归属接入的 PE 还需先按客户迁移方案处理 ESI，不能直接中断该接入。

先撤销租户 Type-5 通告和全部 VNI 依赖：

```text
bgp 65000
 ipv4-family vpn-instance D1-TYPE5
  undo advertise l2vpn evpn
 #
 ipv6-family vpn-instance D1-TYPE5
  undo advertise l2vpn evpn
 #
#
ip vpn-instance D1-TYPE5
 undo vxlan vni
#
interface Nve 1
 undo vni 50460
 undo vni 50461
#
```

```text
commit
display interface Nve1
display vxlan tunnel
```

实际查询为 Nve1 Down/Down、VXLAN 成员 0；远端租户 IPv4/IPv6 测试前缀均撤销。此时才删除 BGP EVPN 地址族和全局开关：

```text
bgp 65000
 undo l2vpn-family evpn
#
undo evpn-overlay enable
```

```text
commit
display bgp evpn all routing-table
display bgp peer
```

实际 EVPN 路由为 0，原有两个 IPv4 单播邻居仍为 Established。关闭一个地址族不会删除这些独立的单播会话。

恢复顺序如下；使用本设备实际的邻居和 VNI：

```text
evpn-overlay enable
bgp 65000
 l2vpn-family evpn
  peer 198.19.80.1 enable
  peer 198.19.80.2 enable
 #
 ipv4-family vpn-instance D1-TYPE5
  advertise l2vpn evpn
 #
 ipv6-family vpn-instance D1-TYPE5
  advertise l2vpn evpn
 #
#
ip vpn-instance D1-TYPE5
 vxlan vni 50081
#
interface Nve 1
 vni 50460 head-end peer-list protocol bgp
 vni 50461 head-end peer-list protocol bgp
#
```

```text
commit
display interface Nve1
display vxlan tunnel
display bgp evpn all routing-table
display health
save
```

实际恢复 4 个 L2 dynamic 和 1 个 L3 dynamic 成员，Nve1 Up/Up；租户双栈及两个 VNI 的客户探测均成功，健康状态 ready、无活动告警。该过程保留 NVE 源地址、租户、桥域和底层路由，只撤销和恢复本例明确列出的 EVPN 依赖。
