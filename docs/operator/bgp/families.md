# 地址族与聚合


```text
bgp 64512
 ipv4-family vpn-instance BLUE
  import-route direct
 ipv6-family vpn-instance BLUE
```

VPN地址族使用VPN实例下配置的RD和全部RT。进入VPN-instance地址族后，设备按缺省语义向FRR下发自动导出标签，不在公开配置中显示后端的`label vpn export auto`。`undo default ipv4-unicast`用于取消自动启用新IPv4邻居；此后需要在IPv4 unicast地址族中显式启用邻居。

全局VPNv4/VPNv6传输地址族缺省启用VPN-Target过滤，缺省配置不显示。RR或Inter-AS Option B需要保留所有VPN路由时使用：

```text
bgp 64512
 ipv4-family vpnv4
  undo policy vpn-target
 ipv6-family vpnv6
  undo policy vpn-target
```

`policy vpn-target`恢复缺省过滤行为。FRR后端分别使用`no bgp retain route-target all`和`bgp retain route-target all`表达这两个状态。

6PE使用IPv4邻居承载全局IPv6标签路由：

```text
bgp 64512
 peer 10.0.0.2 as-number 64512
 peer 10.0.0.2 connect-interface LoopBack0
 ipv6-family unicast
  peer 10.0.0.2 enable
  peer 10.0.0.2 label-route-capability
```

设备使用FRR原生IPv6 labeled-unicast地址族，路由仍经Zebra、Linux netlink和LCP进入VPP。

VortexROS对外只有一个BGP进程。VPN地址族未单独配置`router-id`时继承BGP视图的全局Router-ID；只有在对应VPN地址族中显式配置时才覆盖该值。全局Router-ID修改会同步更新后端VPN实例，并在同一事务恢复IPv4/IPv6的RD/RT投影，防止后端自动身份刷新改变已配置的VPN目标。

IPv4与IPv6邻居只能在对应的unicast地址族视图下修改。引用了IPv4 `ip ip-prefix`的route-policy不能挂载到IPv6邻居、IPv6 network或IPv6 `import-route`；IPv6地址族应使用`ip ipv6-prefix`和`if-match ipv6 address prefix-list`。IPv6地址族使用`import-route ospfv3`，由系统映射到后端OSPFv3路由类型。

地址族中可以生成聚合路由：

```text
bgp 64512
 ipv4-family unicast
  aggregate 10.0.0.0 255.0.0.0 detail-suppressed
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
  quit
 ipv6-family vpnv6
  undo policy vpn-target
  quit
 quit
commit
display current-configuration configuration bgp
```

关闭VPN-Target过滤会保留更广的VPN路由，可能增加路由数量。恢复默认时，在对应地址族执行`policy vpn-target`并提交；默认行随后从当前配置省略。请结合VPN路由查询确认实际导入范围。

[会话与路由查询、精确撤销](queries.md) · [完整双端案例](../../examples/bgp.md) · [策略实际结果](../../examples/bgp-policy.md)
