# VLAN

使用 VLAN 划分二层广播域，需要三层网关时创建 Vlanif。

[命令参考](reference/vlan.md) · [配置案例](../examples/vlan-gateway.md)

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
1    common  enable  enable   VLAN 1         UT:eth2(D)  eth3(D)
10   common  enable  enable   To_CTC_ISP     UT:eth0(U)
20   common  enable  enable   To_LAN_Client  UT:eth1(U)
-----------------------------------------------------------------
```

`display ip interface brief`和`display ipv6 interface brief`保持相同的状态列布局，便于同时核对Physical、Protocol和VPN-Instance。

隐式默认MAC不进入 `display current-configuration` 或 `display this`。

`enable switch`还会启用LCP二层控制通道。创建LCP对时，VortexROS根据配置模型明确下发L2或L3角色；linux-cp不根据接口名称、BVI、业务VLAN或VPP瞬时mode再次猜测。`vortexros-switchd`创建一座名为`switch`的VLAN-aware Linux bridge；只要接口配置了`portswitch`，对应父LCP TAP就加入其中，包括尚未配置`port link-type`的缺省VLAN端口和链路Down端口。VLAN配置只决定该bridge端口的VLAN成员关系，不决定端口是否属于bridge。Vlanif、Vbdif、路由物理口、LoopBack和隧道等L3 LCP均不加入`switch`，其IP地址仍属于各自Linux L3接口。trunk的业务VLAN仍由VPP隐式子接口承载，不为每个VLAN再创建一套Linux TAP或bridge，因此接口数量不会随VLAN/VNI线性膨胀。

`switch`自身不承载业务IP，其MTU自动设置为当前L2控制端口的最大MTU。switchd创建或重新校准bridge时会直接查询Linux bridge能力；若内核支持`fdb_local_vlan_0`则自动开启，不支持时不设置。接口从L3切换为switchport或从switchport切回L3时，只更新既有LCP对的角色和bridge成员关系，不删除重建TAP。

这座bridge只表示控制面状态：VPP继续负责MAC学习、老化、未知单播/广播泛洪和报文转发；Linux bridge端口关闭自主学习和泛洪。VPP新学、迁移或老化的动态MAC通过现有MAC事件同步为Linux `extern_learn` FDB；Linux内核的`offload`标记只由真实switchdev驱动设置，控制通道不会伪造该标记。Linux控制程序下发的静态FDB再经linux-cp进入对应VPP bridge-domain。普通业务报文不会为了同步MAC而复制到Linux，也没有新增VPP转发节点。ARP/ND、接口、地址、路由、MPLS和IS-IS继续使用原LCP通道。

```text
display lcp
display vlan
display mac-address
```

`display lcp`会同时显示二层控制通道、Linux bridge ifindex、控制端口数和原有LCP接口对。静态VXLAN继续使用NVE中的显式peer；BGP EVPN使用一座single VXLAN device（SVD）`vxlan0`承载所有动态VNI，不为每个VNI创建一套Linux bridge和VXLAN设备。完整配置和验证见[VXLAN EVPN](11-vxlan-evpn.md)。
