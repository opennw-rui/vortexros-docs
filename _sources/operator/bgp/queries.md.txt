# 状态与撤销


```text
display bgp peer
display bgp peer 10.0.0.2 verbose
display bgp vpnv4 vpn-instance BLUE peer 10.0.0.2 verbose
display bgp vpnv4 vpn-instance BLUE peer 10.0.0.2 log-info
display bgp vpnv6 all peer verbose
display bgp routing-table
display bgp routing-table peer 10.0.0.2 received-routes
display bgp vpnv4 vpn-instance BLUE routing-table
display bgp vpnv4 vpn-instance BLUE routing-table statistics
display bgp tcp-protection verbose
```

BGP 大型路由表逐项显示，总数位于表尾。Path/Ogn 与 AS Path 列表使用十进制 AS 号；routing-table statistics 显示前缀、通告和重分发数量。邻居 verbose 用于检查会话、协商能力及计时器，log-info 显示当前状态、可用的建立时间，以及最近重置和 Notification 原因。指定 all 时按 VPN 实例列出结果。

默认TCP保护只接受已经配置的BGP邻居源地址。需要关闭时：

```text
bgp 64512
 undo default tcp-protected
```

精确删除邻居或单项参数：

```text
bgp 64512
 undo peer 10.0.0.2 route-policy RP-IN import
 undo peer 10.0.0.2 description
 undo peer 10.0.0.2
#
undo bgp 64512
```

CLI 操作：

```text
commit
```


## 接收原始路由的前提

`received-routes`读取保留的原始入站更新，需要先在对应单播地址族为邻居配置`peer ADDRESS keep-all-routes`并提交。未启用时，实际查询会明确报`Inbound soft reconfiguration not enabled`，不能据此认定邻居没有路由。启用后，VPN实例中的IPv4/IPv6查询已实际读到发布的前缀。

保留被策略拒绝的路由会增加内存占用。不再需要原始更新时用`undo peer ADDRESS keep-all-routes`撤销；正常已接受路由的查询和转发不依赖此开关。

## 地址族与空邻居表

未指定地址族的 display bgp peer 只显示IPv4 unicast邻居，不会因同时启用VPNv4、VPNv6或EVPN而改变查询范围。IPv6邻居使用display bgp ipv6 peer；VPN-instance内的单播邻居使用display bgp vpnv4/vpnv6 vpn-instance对应名称 peer。

display bgp vpnv4 all peer和vpnv6形式汇总各VPN实例的单播邻居，排除public-net邻居。现有BGP进程中没有启用这些邻居时，显示Total number of peers:0，不能据此推断BGP进程未运行。全局MP-BGP的VPN路由用display bgp vpnv4 all routing-table或vpnv6形式核对。

IPv6邻居摘要同时覆盖普通IPv6单播和6PE的IPv6 labeled-unicast；6PE使用IPv4传输地址，也应出现在display bgp ipv6 peer中。同一BGP会话只计一次，接收前缀数汇总该IPv6地址族范围的通告。IPv4 unicast、VPN及EVPN的计数不混入这条摘要。

## 重启 BGP 服务

`reset service bgp` 重启 BGP 服务并重新应用已提交的配置，包含普通单播、VPN 和 EVPN 地址族。它不删除配置，也不代替 `save`；重启期间会话、路由通告和相关业务可能短暂中断，应安排维护窗口。

```text
reset service bgp
Y
display bgp peer
display bgp evpn all routing-table
display ip routing-table vpn-instance BLUE
display ipv6 routing-table vpn-instance BLUE
display health
```

根据实际启用的地址族增加对应查询。IPv4 邻居摘要不能证明 IPv6、VPN 或 EVPN 的路由已恢复；还应使用租户源地址检查双向业务。例如：

```text
ping -vpn-instance BLUE -a 198.18.196.3 -c 2 198.18.196.1
ping ipv6 vpn-instance BLUE -a 2001:db8:196::3 -c 2 2001:db8:196::1
```

实际重启验证中，两个邻居恢复 Established，租户 IPv4/IPv6 各恢复一条 BGP 路由，两族业务探测分别成功。EVPN 的原有普通和带 VLAN 标记客户流量也恢复。若命令报告重放或回读失败，应保留报错并查看活动告警，不能仅因进程已经启动便认定恢复完成；其他协议或隧道告警也应分别处理。

EVPN 常用查询：

```text
display bgp evpn all routing-table
display bgp evpn all routing-table mac-route
display bgp evpn all routing-table inclusive-route
display vxlan tunnel
display vxlan tunnel 26
display vxlan statistics source 198.19.23.3 peer 198.19.80.1 vni 50081
```

MAC 路由用于核对客户或网关 MAC/IP，Inclusive 路由用于核对远端 VTEP 的 BUM 成员。隧道编号为运行时编号，应先查询清单再选择；统计按实际 VTEP、VNI 选择，不能把某一成员有数据外推为所有租户都正常。

## 邻居 ORF 能力

~~~text
display bgp peer 198.19.80.2 orf ip-prefix
display bgp ipv6 peer 2001:db8:80::2 orf ip-prefix
~~~

查询按地址族显示邻居已观测到的前缀 ORF 发送、接收能力和收到的过滤条目数；not negotiated 表示该方向未协商 ORF，0 表示当前收到的条目数为零。这些结果不表示普通入站或出站路由策略失效，路由策略与 ORF 是不同机制。当前 CLI 不提供 ORF 能力配置入口，不应通过该查询推断已启用 ORF。

检查普通路由策略效果时，仍使用 accepted-routes、advertised-routes 和在满足保留条件后的 received-routes，并核对实际业务。
