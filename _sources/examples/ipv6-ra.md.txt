# IPv6 自动配置

**目标**：从上游 RA 获得 SLAAC 地址和默认路由。

**前提**：独立的三层实验口 Ethernet 1；上游发送包含有效自主地址前缀和非零 Router Lifetime 的 RA。

## 配置

~~~text
system-view
interface Ethernet 1
 ipv6 address auto global default
 quit
commit
~~~

该命令同时启用本接口的 SLAAC 和 RA 默认路由接收。它不启动 DHCPv6。参见 [RA 与 SLAAC](../operator/ipv6-autoconfig.md)。

## 验证

使用 `display ipv6 interface brief` 和 `display ipv6 routing-table` 分别确认地址和默认路由。等待地址冲突检测完成后，探测上游 IPv6 地址。

## 撤销

在 Ethernet 1 执行 `undo ipv6 address auto global default` 并提交。确认本接口由 RA 学到的地址和路由清理，手工地址和 DHCPv6 地址应保留。
