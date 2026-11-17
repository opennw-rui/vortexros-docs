# IPv4/IPv6 路由引入

`import-route` 引入 IPv4 路由，`ipv6 import-route` 引入 IPv6 路由。可选来源分别包括直连、静态、OSPF/OSPFv3 与 BGP。只配置需要发布的地址族与来源；引入直连会覆盖同一 VPN 内符合条件的直连前缀，不仅是建立邻接的接口。

```text
isis 10
 import-route static
 ipv6 import-route static
 ipv6 import-route ospfv3
#
```

引入路由按进程参与的级别发布：Level1发布到L1，Level2发布到L2，Level1-2可同时发布到两级。双栈应采用默认 wide 或 transition 编码，narrow 不支持 IPv6 IS-IS。

## 直连前缀的实际效果

两端同属 O101，Ethernet0 为198.18.201.2/30、198.18.201.1/30及2001:db8:201::2/64、::3/64；均以 IS-IS2 Level2 建立邻接。发送端另外有未直接激活 IS-IS 的 LoopBack248，地址203.0.113.104/32和2001:db8:104::3/128。

发送端配置：

```text
interface LoopBack248
 ip binding vpn-instance O101
 ip address 203.0.113.104 32
 ipv6 enable
 ipv6 address 2001:db8:104::3 128
#
isis 2 vpn-instance O101
 import-route direct
 ipv6 import-route direct
#
commit
```

接收端查询：

```text
display isis 2 peer
display isis 2 lsdb
display isis 2 route
display ip routing-table vpn-instance O101 203.0.113.104 32
display ipv6 routing-table vpn-instance O101 2001:db8:104::3 128
ping -vpn-instance O101 -a 198.18.201.2 -c 1 203.0.113.104
ping ipv6 vpn-instance O101 -a 2001:db8:201::2 -c 1 2001:db8:104::3
```

实际引入后两族前缀均可选中 ISIS，Preference15、Cost10。窄度量 IPv4 探测1/1；transition 编码下的 IPv6 探测1/1。编码、邻接和路由优先级是不同概念：有 IPv6 Reachability TLV 不代表 narrow 模式会计算 IPv6 路由。

## 撤销与其他协议接替

```text
isis 2 vpn-instance O101
 undo import-route direct
 undo ipv6 import-route direct
#
commit
```

撤销不会删除本机 LoopBack 地址。对端须等待 LSP 更新和 SPF 完成，再核对精确前缀；不能把紧接 commit 的旧路由显示当作最终结果。

实际撤销后，IPv4精确前缀退出路由表；IPv6因为同时存在另一条 OSPFv3 E1 路径，改选 Preference150、Cost53。这说明应同时查看 IS-IS 协议表和选中的 IP 路由，不能要求已有其他协议路径的目标也必须变成不可达。接口邻接保持 Up，未重启协议服务。

[双端基础配置](../../examples/isis.md) · [编码与激活条件](activation.md) · [全部参数](../reference/isis.md)

## L1/L2 同时运行时的撤销

同一条导入前缀可能同时出现在 L1 和 L2 协议表中，而最终路由表只选择一条有效转发路径。撤销发布时，必须同时核对协议表和设备路由表，不能只看其中一级已清空。

一组运行结果中，203.0.113.104/32 和 2001:db8:104::3/128 同时存在于 L1/L2 两族表，设备选择 ISIS、Preference15、Cost10。撤销 `import-route direct` 与 `ipv6 import-route direct` 并提交后，两级协议表中的这两个目标均消失，IPv4/IPv6 设备路由查询也均为0。如果另一个协议仍发布相同前缀，最终路由可以切换到该协议，而不是消失。
