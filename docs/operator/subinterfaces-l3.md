# L3 子接口

L3 子接口按 VLAN 标签区分独立三层链路，可在本接口配置 IPv4/IPv6 和路由协议。它使用 `vlan-type`，L2 的 `encapsulation` 不是相同命令。

## 创建与约束

使用 `interface PARENT.NUMBER` 创建，配置 `vlan-type dot1q VLAN` 后设置地址。双标签使用案例中对应形式。父端口须存在，不能与同一父口其他分类规则抢占相同标签；无需将 L3 子接口加入 bridge-domain。

L3 子接口有自己的 LCP 端点，Linux/FRR 使用同一三层身份。父口关闭会影响子口实际状态；恢复不能把显式 shutdown 的子口强制拉起。

## 配置、真实查询和撤销

[完整双端案例](../examples/subinterfaces/l3.md)包含 VLAN700 地址、接口及直连路由查询、稳定探测3/3，双标签及保存/恢复和父接口删除约束。

~~~text
display interface host-p1b12.700
display ip interface brief
display ip routing-table protocol direct
~~~

先撤销协议、策略等引用，再删除子接口。真实删除结果、保存回放和对照业务见案例；父口可能还承载其他子接口，不应为删除单一业务而删除父口。

[L2 子接口](subinterfaces-l2.md) · [接口参数](reference/interfaces.md)
