# 成员与网关

## 配置与验证

显式二层子接口未配置 `mtu` 时使用父端口的硬件 MTU 能力，三层子接口缺省使用 1500。父接口 MTU 下发后，VortexROS 恢复各子接口的目标值，可用 `display interface` 检查。

```text
vlan batch 100 200
interface Ethernet 1
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 100 200
interface Vlanif 100
 ip address 10.100.0.1 255.255.255.0
```

配置在二层物理接口或VLAN上的策略会作用于对应的trunk业务流量。Vlanif只有在VLAN中至少存在一个可用成员端口时才能正常up；没有可用成员时显示普通down，并撤销相关直连路由。

策略投影遵循实际承载对象：access和`dot1q-tunnel`的VLAN QoS/MQC绑定在整个父
接口，trunk的VLAN策略绑定在对应隐式业务子接口。简单QinQ不再生成客户侧
`父接口.VLAN`对象，因此不会把策略下发到不存在的接口；VLAN classifier中的匹配
条件仍保留。

`display vlan`使用一张表同时显示状态、MAC学习、描述和端口成员，端口状态中的`U/D`表示up/down，`TG/UT`表示tagged/untagged。表格宽度根据实际内容调整；端口之间间隔两个字符，每行最多显示四个端口，更多端口在下一行按首个接口位置继续显示：

```text
-----------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
-----------------------------------------------------------------

VID  Type    Status  MAC-LRN  Description    Ports
-----------------------------------------------------------------
1    common  enable  enable   VLAN 1         UT:Ethernet2(D)  Ethernet3(D)
10   common  enable  enable   To_CTC_ISP     UT:Ethernet0(U)
20   common  enable  enable   To_LAN_Client  UT:Ethernet1(U)
-----------------------------------------------------------------
```

`display ip interface brief`和`display ipv6 interface brief`保持相同的状态列布局，便于同时核对Physical、Protocol和VPN-Instance。

隐式默认MAC不进入 `display current-configuration` 或 `display this`。

enable switch 后，portswitch 将接口作为二层业务口。缺省 VLAN、trunk 允许列表和 PVID 分别控制其业务成员关系。Vlanif、Vbdif 及路由口保持三层角色，不作为普通交换成员。

`switch`自身不承载业务IP，其MTU自动设置为当前L2控制端口的最大MTU。switchd创建或重新校准bridge时会直接查询Linux bridge能力；若内核支持`fdb_local_vlan_0`则自动开启，不支持时不设置。接口从L3切换为switchport或从switchport切回L3时，只更新既有LCP对的角色和bridge成员关系，不删除重建TAP。

普通业务由 VPP 学习、泛洪并转发；控制面同步 MAC、邻居及路由状态。用户只需通过 VortexROS 配置业务，不需要创建额外 Linux bridge、TAP 或逐 VLAN 的控制接口。

```text
display lcp
display vlan
display mac-address
```

display lcp 用于诊断控制通道和接口配对。静态 VXLAN 在 NVE 配置显式对端，动态 EVPN 由 BGP 学习，见[VXLAN EVPN](../11-vxlan-evpn.md)。


[功能目录](../vlan.md) · [命令参数](../reference/vlan.md)
