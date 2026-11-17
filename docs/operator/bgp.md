# BGP

BGP 以邻居交换路由，各地址族控制发布和接收的前缀。全系统一个主 BGP AS；重复输入同一 AS 进入已有视图，不同 AS 被拒绝，65535 不可用。

按会话、组继承、路由属性或地址族进入子页。先验证会话建立，再确认路由选择及业务，不以配置存在代替路由生效。

~~~{toctree}
:maxdepth: 2

bgp/peers
bgp/groups
bgp/reflection
bgp/attributes
bgp/multipath
bgp/families
bgp/queries
~~~

[完整双端案例](../examples/bgp.md) · [路由策略案例](../examples/bgp-policy.md) · [命令参数](reference/bgp.md) · [EVPN](11-vxlan-evpn.md)
