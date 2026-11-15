# L3VPN

L3VNI 为租户路由提供 VXLAN 传输；BGP EVPN Type-5 交换 IP 前缀。它与 MPLS L3VPN 的标签传输不同，不能将 VPNv4 学到的前缀当作 Type-5 成功。

## 配置和限制

在 VPN-instance 中配置 L3VNI、对应地址族 RD/RT，把租户接口绑定到该 VPN。BGP 的租户 IPv4/IPv6 地址族配置路由引入及 `advertise l2vpn evpn`。内部服务 SVI/桥域由系统管理，不在 NVE 下重复创建同编号 L2VNI。

[完整双 PE 案例](../../examples/evpn/l3vpn.md)使用 CLI-TYPE5、VNI50081、RT65000:50081，没有 VPNv4/VPNv6 传输邻居。两端均通过 EVPN 交换租户双栈前缀。

## 验证

~~~text
display bgp evpn all routing-table
display ip routing-table vpn-instance CLI-TYPE5 198.18.196.2 32
display ipv6 routing-table vpn-instance CLI-TYPE5 2001:db8:196::2 128
ping -vpn-instance CLI-TYPE5 -c 2 -a 198.18.196.1 198.18.196.2
ping ipv6 -vpn-instance CLI-TYPE5 -c 2 -a 2001:db8:196::1 2001:db8:196::2
~~~

检查远端 Type-5、租户路由与实际下一跳，并用对应 VPN 源地址发起 IPv4/IPv6 双向探测。重建数据面后应再次检查路由与连通性。

## 撤销与保存

在两个租户地址族撤销 advertise l2vpn evpn 并提交，远端租户前缀应消失，而未撤销的 L2VNI 保留。再按依赖顺序撤销 BGP 租户地址族、接口和 VPN。共用 NVE、EVPN 邻居及底层路由应保留，核对后 save。

[功能范围](../11-vxlan-evpn.md) · [MPLS L3VPN](../l3vpn.md)
