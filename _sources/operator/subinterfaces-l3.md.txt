# L3 子接口

L3 子接口按 VLAN 标签区分独立三层链路，可在本接口配置 IPv4/IPv6 和路由协议。它使用 `vlan-type`，L2 的 `encapsulation` 不是相同命令。

## 创建与约束

使用 `interface PARENT.NUMBER` 创建，配置 `vlan-type dot1q VLAN` 后设置地址。双标签使用案例中对应形式。父端口须存在，不能与同一父口其他分类规则抢占相同标签；无需将 L3 子接口加入 bridge-domain。

父接口关闭或链路断开时，L3 子接口随之 Down；父接口恢复后，未被 shutdown 的子接口自动恢复。子接口有有效 IP 地址时，三层 Protocol 才能 Up；仅配置封装不能作为三层网关。

## 配置、示例输出和撤销

[完整双端案例](../examples/subinterfaces/l3.md)包含 VLAN700 地址、接口及直连路由查询、稳定探测3/3，双标签及保存/恢复和父接口删除约束。

~~~text
display interface Ethernet0.700
display ip interface brief
display ip routing-table protocol direct
~~~

在系统视图执行 `undo interface Ethernet0.700` 删除该子接口。绑定在该接口上的 NAT、Proxy ARP 和 DHCP 配置随接口删除，共享 NAT 策略和其他接口的绑定保留。其他独立对象对该接口的引用仍须先解除。提交前可用 `display configuration candidate merge` 检查待删除内容；提交后用 `display current-configuration interface` 和 `display interface` 检查结果，再保存配置。

父口可能承载其他子接口，不应为删除单一业务而删除父口。

[L2 子接口](subinterfaces-l2.md) · [接口参数](reference/interfaces.md)
