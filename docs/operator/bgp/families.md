# 地址族与聚合


```text
bgp 64512
 ipv4-family vpn-instance BLUE
  import-route direct
 #
 ipv6-family vpn-instance BLUE
```

VPN地址族使用VPN实例下配置的RD和全部RT，系统自动分配所需的VPN导出标签，无需另行配置。`undo default ipv4-unicast`用于取消自动启用新IPv4邻居；此后需要在IPv4 unicast地址族中显式启用邻居。

全局VPNv4/VPNv6传输地址族缺省启用VPN-Target过滤，缺省配置不显示。RR或Inter-AS Option B需要保留所有VPN路由时使用：

```text
bgp 64512
 ipv4-family vpnv4
  undo policy vpn-target
 #
 ipv6-family vpnv6
  undo policy vpn-target
```

`policy vpn-target`恢复缺省过滤行为；默认项在当前配置中省略。

6PE使用IPv4邻居承载全局IPv6标签路由：

```text
bgp 64512
 peer 10.0.0.2 as-number 64512
 peer 10.0.0.2 connect-interface LoopBack0
 ipv6-family unicast
  peer 10.0.0.2 enable
  peer 10.0.0.2 label-route-capability
```

6PE交换IPv6标签路由，并通过MPLS承载IPv6业务；会话建立后仍需核对标签路径与双向业务。

VortexROS对外只有一个BGP进程。VPN地址族未单独配置`router-id`时继承BGP视图的全局Router-ID；只有在对应VPN地址族中显式配置时才覆盖该值。修改全局Router-ID会同步改变未覆写的VPN实例身份，并可能使相关邻居重新建立。显式配置的RD/RT保持原值。

IPv4与IPv6邻居只能在对应的unicast地址族视图下修改。引用了IPv4 `ip ip-prefix`的route-policy不能挂载到IPv6邻居、IPv6 network或IPv6 `import-route`；IPv6地址族应使用`ip ipv6-prefix`和`if-match ipv6 address prefix-list`。IPv6地址族使用`import-route ospfv3`，由系统映射到后端OSPFv3路由类型。

地址族中可以生成聚合路由：

```text
bgp 64512
 ipv4-family unicast
  aggregate 10.0.0.0 255.0.0.0 detail-suppressed
 #
 ipv6-family unicast
  aggregate 2001:db8:: 32 as-set detail-suppressed
```

`detail-suppressed`只发布聚合路由；`as-set`保留组成路由的AS信息。显式使用`as-set`时，系统会同步调整该BGP实例的后端AS_SET接收模式，使配置不会被FRR静默忽略。两项均未配置时，聚合路由与组成路由同时发布。


## VPN-Target过滤

`policy vpn-target` 是产品默认行为，配置中省略；`undo policy vpn-target` 保留传输地址族收到的全部 VPN 路由，适用于明确需要此行为的 RR/中转场景。它不替代业务 VPN 的 import/export RT。

```text
bgp 65000
 ipv4-family vpnv4
  undo policy vpn-target
 #
 ipv6-family vpnv6
  undo policy vpn-target
#
```

CLI 操作：

```text
commit
display current-configuration configuration bgp
```

关闭VPN-Target过滤会保留更广的VPN路由，可能增加路由数量。恢复默认时，在对应地址族执行`policy vpn-target`并提交；默认行随后从当前配置省略。请结合VPN路由查询确认实际导入范围。

[会话与路由查询、精确撤销](queries.md) · [完整双端案例](../../examples/bgp.md) · [策略实际结果](../../examples/bgp-policy.md)

## 聚合的实际查询结果

当已有 10.253.29.2/32 和 2001:db8:253::2/128 时，分别配置 10.253.0.0/16、2001:db8:253::/48 并启用 detail-suppressed。实际对端能收到两条汇总，查询两条精确明细均为 0；访问两个明细地址各发送 2 个探测，均收到 2 个回复。

本地明细仍保留在 BGP 表中，以 s 标记抑制。例如实际输出摘录：

```text
 *>  10.253.0.0/16      0.0.0.0               0            i
 s>  10.253.29.2/32     0.0.0.0               0            i
```

s 表示不对外发布该明细，> 仍表示它是本地选中的路径。它不表示明细已从本地路由或转发表删除。撤销 aggregate 并提交后，汇总消失，明细恢复通告和普通最佳路径标记。

## VPN-Target 过滤的实际结果

对端以RD65000:4902、导出RT65000:9999发布172.30.254.2/32和2001:db8:254::2/128，本端没有匹配的业务VPN导入RT时，默认不会在传输VPN表保留这两条路由。分别关闭VPNv4、VPNv6的过滤并提交后，可以查询到它们：

```text
display bgp vpnv4 all routing-table 172.30.254.2 32
display bgp vpnv6 all routing-table 2001:db8:254::2 128
```

实际输出摘录：

```text
Route Distinguisher  Network            NextHop
65000:4902           172.30.254.2/32    198.19.80.2
Total Number of Routes: 1
```

IPv6精确查询同样显示RD65000:4902和一条2001:db8:254::2/128。随后在两个传输地址族分别执行 `policy vpn-target` 并提交，测试RD下两条路由均不再保留。关闭传输过滤只改变全局VPN路由保留范围，不能代替业务VPN的导入RT；业务路由和连通性仍需在对应VPN中验证。

## 删除整个地址族

全局传输地址族可使用：

```text
bgp 65000
 undo ipv4-family vpnv4
 undo ipv6-family vpnv6
#
commit
```

本例实际撤销了VPNv4/VPNv6的邻居地址族启用，普通单播和EVPN会话保留。重新进入对应地址族并配置邻居启用后，测试VPN前缀恢复。原业务VPN的地址族、RD/RT及接口不会因删除传输地址族自动删除。

`undo ipv6-family unicast` 则删除全局IPv6单播地址族的配置。实测远端2001:db8:253::2/128从全局BGP表撤销，独立租户的IPv6 Type-5路由继续存在；恢复原IPv6邻居启用后，全局IPv6目标探测成功。删除会丢弃该地址族中的网络、策略和邻居设置，恢复时应按保存的配置逐项重建，而不是只重新进入空视图。
