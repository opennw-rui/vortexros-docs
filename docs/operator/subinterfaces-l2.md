# L2 子接口

L2 子接口按 VLAN 标签识别报文，加入 bridge-domain 后转发。它自身不配置 IP，三层网关地址位于该桥域 Vbdif。

## 创建与约束

使用 `interface PARENT.NUMBER mode l2` 创建，`encapsulation dot1q vid VLAN` 指定单标签；双层标签、802.1ad 与 QinQ 见案例。子接口编号和 VLAN ID 不要求相同，父端口必须存在。父端口的 trunk 派生成员不能抢占相同标签分类。

创建后补齐封装并绑定桥域；不能在已有接口上通过重复进入时改写 mode 完成二三层转换。应先解除业务引用、删除接口，再创建目标模式。

## 配置、实际显示和撤销

[完整双端案例](../examples/subinterfaces/l2.md)包含 P1 L2 子接口/Vbdif、P2 L3 对端，VLAN701 的真实接口与桥域查询、稳定探测3/3，以及 dot1ad/QinQ 和父端口生命周期。

~~~text
display interface host-p1b12.701
display bridge-domain 701
~~~

撤销先解除依赖，再删除子接口；网关、桥域和父端口是独立对象，只删除不再共用的部分。完整撤销及实际查询结果见案例。确认后保存，不以接口配置存在替代报文分类正确。

[L3 子接口](subinterfaces-l3.md) · [接口参数](reference/interfaces.md)
