# 为 VLAN 客户端分配 IPv4 地址

**用途**。在已有 Vlanif 100 上为客户端提供动态地址和默认网关。

**前提**。Vlanif 100 已配置 192.0.2.1/24，VLAN 二层连通，同一广播域没有其他提供冲突地址的 DHCP 服务器。

## 配置

~~~text
system-view
enable dhcp server
interface Vlanif 100
 dhcp select interface
 dhcp server ip-range 192.0.2.100 192.0.2.200
 dhcp server lease day 1
 quit
commit
~~~

全局开关允许 DHCP 服务端运行，接口命令才决定此接口提供租约。接口地址池默认把接口主地址作为网关，动态分配范围不含网关地址。

## 验证

使用 display dhcp service verbose 检查服务 Ready。令测试客户端重新获取地址，核对分配地址、默认网关和实际连通性。用 display ip pool interface Vlanif 100 verbose 查看池与租约。

## 撤销

在 Vlanif 100 执行 undo dhcp select 并提交。该接口停止服务，已有客户端可能继续使用现有租约，直到续租或过期。其他接口仍有 DHCP 需求时，保留全局服务开关。
