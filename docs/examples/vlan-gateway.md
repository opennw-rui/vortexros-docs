# VLAN 网关

**用途**。将带 VLAN 100 标签的流量送入独立二层广播域，并用 Vlanif 100 提供三层网关。

**前提**。VPP 正常运行，Ethernet 1 是专用测试口，对端允许 VLAN 100。端口转换为二层前，先处理原有三层地址及依赖。

## 配置

~~~text
system-view
enable switch
vlan batch 100
interface Ethernet 1
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 100
 quit
interface Vlanif 100
 ip address 192.0.2.1 255.255.255.0
 quit
commit
~~~

Trunk 放行 VLAN 100。Vlanif 为该 VLAN 提供网关和直连路由。VLAN 没有可用成员时，Vlanif 会 Down，相关直连路由撤销。

## 验证

使用 display vlan 100 和 display ip interface brief 查看成员及 Vlanif 状态。从对端 VLAN 100 的主机 Ping 192.0.2.1。配置符合预期后再保存。

## 撤销

先解除 Vlanif 100 上的 DHCP、ACL 或协议绑定，再用 undo interface Vlanif 100 删除网关。在 trunk 接口执行 undo port trunk allow-pass vlan 100，然后提交。只在确定没有其他端口或业务引用时删除 VLAN。
