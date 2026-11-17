# VLAN

使用 VLAN 划分二层广播域，需要三层网关时创建 Vlanif。

[命令参考](reference/vlan.md) · [配置案例](../examples/vlan-gateway.md)

~~~{toctree}
:maxdepth: 2

vlan/ports
vlan/gateway
vlan/lifecycle
vlan/service-bd
~~~

## 网关激活

Vlanif 未 shutdown、所属 VLAN 至少有一个实际成员端口处于管理 Up 且链路 Up 时，PHY 才能 Up；还需有效网关 IP 地址，三层 Protocol 才能 Up。全部成员不可用时自动 Down，恢复后自动 Up。详见[Vlanif 网关](vlan/gateway.md)。
