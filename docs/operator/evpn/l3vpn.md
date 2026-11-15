# L3VPN

L3VNI 为租户路由提供 VXLAN 传输；BGP EVPN Type-5 交换 IP 前缀。它与 MPLS L3VPN 的标签传输不同，不能将 VPNv4 学到的前缀当作 Type-5 成功。

## 配置和限制

在 VPN-instance 中配置 L3VNI、对应地址族 RD/RT，把租户接口绑定到该 VPN。BGP 的租户 IPv4/IPv6 地址族配置路由引入及 `advertise l2vpn evpn`。内部服务 SVI/桥域由系统管理，不在 NVE 下重复创建同编号 L2VNI。

[完整双 PE 案例](../../examples/evpn/l3vpn.md)使用 CLI-TYPE5、VNI50081、RT65000:50081，没有 VPNv4/VPNv6 传输邻居。两端均通过 EVPN 交换租户双栈前缀。

## 真实验证

~~~text
display bgp evpn all routing-table
display ip routing-table vpn-instance CLI-TYPE5 198.18.196.2 32
display ipv6 routing-table vpn-instance CLI-TYPE5 2001:db8:196::2 128
ping -vpn-instance CLI-TYPE5 -c 2 -a 198.18.196.1 198.18.196.2
ping ipv6 -vpn-instance CLI-TYPE5 -c 2 -a 2001:db8:196::1 2001:db8:196::2
~~~

开发服务器真实终端四次双向探测各2/2，VPP 重启后路由和转发恢复；还核对了 VXLAN 封装、解封装和本机回复路径。完整输出在案例中，不将路由存在等同于流量已通。

## 撤销与保存

在两个租户地址族撤销 `advertise l2vpn evpn` 后提交，实测远端 IPv4/IPv6 前缀归零，L2VNI 保留。再撤销 BGP 租户地址族、接口、VPN-instance，完整交互命令见案例。NVE、EVPN 邻居和 underlay 可能共用，不能无差别删除。验证后 `save` 保存当前状态。

[功能范围](../11-vxlan-evpn.md) · [MPLS L3VPN](../l3vpn.md)
