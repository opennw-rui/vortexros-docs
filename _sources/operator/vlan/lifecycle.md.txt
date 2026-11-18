# 交换功能与保存

enable switch 启用交换功能并建立默认 VLAN1。重新启用后仍需恢复业务 VLAN、二层端口及网关。
关闭交换功能不会替代业务依赖的撤销：仍有 switchport、显式 VLAN、Vlanif 或其他关联对象时，
命令会明确拒绝，原业务保持不变。

## 关闭交换功能

以下示例原先由 Ethernet0 承载 access VLAN110，Vlanif110 是该网段的三层网关。
执行后该 VLAN 的交换和网关转发停止；先确认不会撤销当前唯一的管理链路。

~~~text
display vlan
system-view
interface Ethernet0
 undo portswitch
#
undo interface Vlanif110
undo vlan 110
undo enable switch
commit
display vlan
display interface Ethernet0
display health
~~~

示例的实际结果：

- 存在 switchport 时直接关闭被拒绝，同一业务仍通过3/3。
- 撤销依赖并关闭后，display vlan 返回0个VLAN，原双栈业务均收到0/3。
- Ethernet0 回到三层端口；未显式指定MTU时，VPP及Linux端点均恢复默认1500。
  显式配置的接口MTU仍以配置为准，不应把本例的1500用于覆盖业务要求。
- 本例健康状态为ready、Running/Actual为4/4，数据面进程保持运行。

确认需要将此作为启动配置后，再执行 save。

## 重新启用并恢复业务

~~~text
enable switch
commit
display vlan
~~~

实际此时只有默认 VLAN1，不会自动恢复已撤销的 VLAN110。
下面恢复原端口和网关，Ethernet1 的服务器侧三层配置应保持存在：

~~~text
vlan 110
#
interface Ethernet0
 portswitch
 port link-type access
 port default vlan 110
#
interface Vlanif110
 ipv6 enable
 ip address 198.18.30.15 255.255.255.0
 ipv6 address 2001:db8:30::1 64
#
commit
display vlan
display interface brief
display ip interface brief
display ipv6 interface brief
display health
~~~

实际恢复后，VLAN110列出UT:Ethernet0(U)，Vlanif110双栈地址恢复，
健康状态为ready、Running/Actual为6/6。
客户端到服务器侧的IPv4、IPv6实际流量均恢复3/3。
本例整个关闭、重新启用及恢复过程没有重启数据面进程。

端口重新成为二层业务口后，未指定MTU时按设备二层能力使用相应帧长；
本例物理口恢复为9706，Vlanif网关仍为1500。
检查业务后执行 save，确保重启后恢复的是所需配置。

## 使用已保存配置恢复

需要直接恢复启动配置时，先查看 display startup，再执行 apply config 并确认。
该命令会替换当前 Running，并按其规定重建数据面，业务可能中断；
不要把它用于只恢复某一个 VLAN。
需要保留当前修改时先保存或另存命名备份。

[VLAN端口](ports.md) · [配置管理](../cli/configuration.md)
