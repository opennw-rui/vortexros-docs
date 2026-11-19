# OSPFv3

在 IPv6 路由域内建立链路状态邻接并交换前缀。

[命令参考](reference/ospfv3.md) · [配置案例](../examples/ospfv3.md)

## 工作原理与前提

OSPFv3 按 RFC 5340 为 IPv6 计算链路状态路由。Router ID 仍是 32 位标识，不是接口的 IPv6 地址；邻居通信通常使用链路本地地址。因此接口必须启用 IPv6，并具有可用的链路本地通信条件。

区域和网络类型决定邻接及 LSDB 的范围，接口 Cost 影响 SPF，系统 Preference 决定与其他协议的同前缀竞争。缺省内部/外部优先级分别为 10/150。IPv4 的 OSPF 进程与 OSPFv3 分开配置，不能因为 IPv4 邻居正常就认定 IPv6 路径正常。

适合内部 IPv6 路由。变更后依次核对接口、邻居、IPv6 LSDB、路由及双向 IPv6 业务；只看到 Full 不能证明重分发或业务路由已安装。

~~~{toctree}
:maxdepth: 2

ospfv3/configuration
ospfv3/lsdb
~~~
