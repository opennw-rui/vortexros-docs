# L2VPN

L2VNI 把本地 VLAN/桥域映射到 VXLAN。Type-2 通告 MAC/IP，Type-3 发现泛洪成员；两端 VNI 和 RT 对应同一业务，RD 区分发布者。它扩展二层广播域，不自动提供跨 VLAN 路由。

## 配置顺序和参数

1. 配置并验证 underlay 到远端 VTEP 的路由。
2. 创建 VLAN、bridge-domain 和 L2VNI；在桥域 EVPN 视图设置 RD、RT。
3. 配置接入端口 VLAN、NVE 源地址及 BGP 动态 peer-list。
4. 建立 BGP EVPN 地址族邻居，提交。
5. 核对实际 MAC 路由、隧道和两端流量，再保存。

每个 VNI 只能由一个 NVE 拥有，静态 peer-list 与 protocol bgp 不可混用。全部 BGP VNI 使用同一个本地 NVE Source 与 underlay VPN-instance；缺省不自动建立业务。

## 完整案例和真实验证

[双 VLAN L2VPN 案例](../../examples/evpn/l2vpn.md)列出 P1/P2/P3、主机配置及实际输出。VLAN101/VNI5010 与 VLAN102/VNI5020 独立转发：

~~~text
display bgp evpn all routing-table
display vxlan tunnel
display mac-address
display bridge-domain 101
~~~

真实实验得到4条 MAC 路由、4条 Inclusive Multicast 路由，两组 VLAN 双向均3/3。实际 display 和探测输出保留在案例页。

## 修改和撤销

改 RT 会改变路由导入/导出范围，改 VNI 会改变业务映射，需协调对端。仅撤销 VNI5010 后，实测 VLAN101 为3发0收，VLAN102仍3/3，隧道从2条变为1条。

先撤销 NVE 中该 VNI 绑定，再清理业务端口、桥域和 RD/RT，不为单个租户关闭全局 EVPN。仍有依赖时 Candidate 会拒绝。[精确撤销](lifecycle.md)

[支持范围](../11-vxlan-evpn.md) · [命令参数](../reference/evpn.md)
