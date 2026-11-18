# 创建与地址族

VPN 实例隔离接口的路由表。RD 用于区分 VPN 路由身份，RT 决定 VPN 路由的导入、导出范围；RD 和 RT 本身不代替接口绑定或路由协议配置。

普通 VPN 实例可为 IPv4、IPv6 分别设置 RD 和 RT。使用 EVPN L3VNI 时，还须遵守 [EVPN 三层 VPN](../evpn/l3vpn.md) 的共享 RD/RT 约束。不要把 VPN 地址族配置与接口下的 ipv6 enable 混为一项开关。

## 创建

以下实例尚未绑定接口，也未配置 L3VNI，可独立创建：

~~~text
ip vpn-instance BLUE
 ipv4-family
  route-distinguisher 65000:5801
  vpn-target 65000:5811 import-extcommunity
  vpn-target 65000:5812 export-extcommunity
 ipv6-family
  route-distinguisher 65000:5802
  vpn-target 65000:5821 import-extcommunity
  vpn-target 65000:5822 export-extcommunity
#
~~~

提交操作：

~~~text
commit
display ip vpn-instance BLUE
display current-configuration configuration vpn-instance
display resource-mapping
~~~

本例查询结果：

~~~text
VPN-Instance Name                RD                     Address-family
BLUE                             65000:5801             IPv4
BLUE                             65000:5802             IPv6
~~~

同一实例内，两族的属性分别保存。RD/RT 只有与相应 BGP VPN 配置关联后才用于路由交换；单独创建上述实例不会自动建立 BGP 邻居、发布业务前缀或形成 MPLS 转发能力。完整组网见 [MPLS L3VPN 案例](../../examples/mpls-l3vpn.md)。

## 修改与撤销 RD/RT

在目标地址族视图操作。只移除一个导出 RT 时，其他 RT 和导入方向保持不变：

~~~text
ip vpn-instance BLUE
 ipv4-family
  undo vpn-target 65000:5812 export-extcommunity
  undo route-distinguisher
#
commit
~~~

undo route-distinguisher 清除当前族的 RD。undo vpn-target 不带方向时移除同一 RT 的导入、导出；带 import-extcommunity 或 export-extcommunity 时只撤销指定方向。修改已用于 BGP VPN 的 RD 或 RT 会改变路由身份、发布范围或导入集合，可能引起路由撤销和重新学习。

## 撤销和恢复地址族

在 VPN 实例视图执行：

~~~text
ip vpn-instance BLUE
 undo ipv4-family
#
commit
display ip vpn-instance BLUE
~~~

该操作删除 IPv4 族及其 RD/RT 配置，IPv6 的 65000:5802 与 RT 保持不变。实例本身和共用的路由表仍存在。

恢复 IPv4 族时重新进入 ipv4-family，并按创建示例重新配置所需 RD/RT；已删除的属性不会自动恢复。随后可同样用 undo ipv6-family 删除 IPv6 族，不影响刚恢复的 IPv4 族。实际独立撤销、恢复两族后，查询先只显示 IPv6，再只显示 IPv4，恢复后重新显示两行不同 RD。

这不是关闭整个设备 IPv6 或删除该实例的命令。已有 VPN 路由业务应结合对应 BGP 地址族、接口和路由依赖检查变化。

## 删除实例

不再需要该实例时，在系统视图执行并按提示确认：

~~~text
undo ip vpn-instance BLUE
commit
display ip vpn-instance
display resource-mapping
~~~

删除会清理该实例及其相关配置，确认提示中的影响范围后再继续。本例未绑定接口，删除后实例及运行表映射消失，其他实例保持不变，健康状态仍就绪。需要重启后保留自己的配置时执行 save。

[接口绑定](interfaces.md) · [逐条参数](../reference/vrf.md) · [功能目录](../vrf.md)
