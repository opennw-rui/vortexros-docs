# VRRP

在多台设备之间提供冗余的 IPv4 或 IPv6 网关。

[命令参考](reference/vrrp.md) · [配置案例](../examples/vrrp.md)

## 工作原理与适用场景

VRRP（IPv4/IPv6 可参照 RFC 5798）让同一二层网络上的多台路由器共享一个虚拟网关地址，依靠通告和优先级选出 Master。终端使用虚拟地址作为网关，设备切换时不要求终端修改默认路由。

VRID、地址族和虚拟地址要一致，各设备仍需各自的真实接口地址。VRRP 只解决网关冗余，不自动同步 NAT 会话、应用状态或远端路由。接口 Up 也不代表上游可达，需要按实际需求使用本产品支持的跟踪选项。

验证先检查角色，再从终端访问网关外业务；关闭 Master 的有效业务路径后检查 Backup 接管，恢复后按抢占设置观察角色。不要让两台设备长期都处于 Master，再用偶然可通的 ping 代替正确选举。

~~~{toctree}
:maxdepth: 2

vrrp/ipv4
vrrp/ipv6
vrrp/operations
~~~
