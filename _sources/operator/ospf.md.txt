# OSPF

OSPF 在同一路由域内建立 IPv4 链路状态邻接并交换前缀。创建进程不代表所有接口自动参与；选择 network 或接口激活方式，区域、网络类型、认证和计时等条件兼容后才建立邻居。

OSPFv3 用于 IPv6，见独立[OSPFv3](ospfv3.md)章节。

~~~{toctree}
:maxdepth: 2

ospf/activation
ospf/areas
ospf/redistribution
ospf/queries
ospf/reset
~~~

[完整双端案例与实际 E2 查询](../examples/ospf.md) · [命令参数](reference/ospf.md)
