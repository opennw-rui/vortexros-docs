# 6PE

通过 IPv4 LDP 核心承载全局 IPv6 路由。

## 工作原理与适用边界

6PE 按 RFC 4798 在 IPv4 MPLS 核心上承载全局 IPv6 可达性。PE 通过 IPv4 邻居交换带标签 IPv6 路由，核心沿标签转发，不要求所有 P 设备参与客户 IPv6 路由。

6PE 面向全局 IPv6 互联，与采用独立 VPN 实例的 IPv6 VPN 不同。IPv4 底层、LDP 标签路径、BGP 标签路由能力和 IPv6 业务路由均需成立，不能把普通 IPv6 unicast 邻居启用等同于已启用 6PE。

验证包括标签路由、实际 MPLS 转发表和双向 IPv6 流量。改变标签能力会影响相关路由发布和转发方式，修改两端时预留收敛窗口。

## 配置与验证

6PE 使用 IPv4 LDP 核心承载全局 IPv6 路由。邻居仍使用 IPv4 LoopBack 建立会话，
在 IPv6 unicast 地址族中启用邻居及标签路由能力：

```text
bgp 65000
 peer 10.0.0.4 as-number 65000
 peer 10.0.0.4 connect-interface LoopBack0
 ipv6-family unicast
  peer 10.0.0.4 enable
  peer 10.0.0.4 label-route-capability
  network 2001:db8:101::1 128
```

标签能力用于交换 IPv6 带标签路由。两端都应启用相应能力，并确保 IPv4 标签路径可用；普通 IPv6 路由的可达性不能代替标签转发检查。


在对端检查 IPv6 BGP 路由、VPP MPLS 转发表和 IPv6 业务连通性。

## 完整双端案例

[6PE 案例](../examples/mpls/6pe.md)提供双端 IPv4 承载、LDP、BGP labeled-unicast、标签查询、双向业务和撤销步骤。配置 6PE 邻居后，所需 IPv6 显式空标签处理由设备自动完成，无需额外配置。

## 普通IPv6与标签模式切换

对已有IPv4承载邻居执行undo peer ADDRESS label-route-capability会撤销标签能力，同时保留该邻居的普通IPv6启用意图；这与删除整个邻居不同。两端模式应一致，普通IPv6路径还必须具备可解析的IPv6下一跳。重新启用标签能力后，已有network前缀会重新发布。

实际切换验证覆盖普通模式与6PE模式双向转换、会话摘要、标签撤销/恢复及恢复后的源地址指定探测。恢复后两个方向各1/1，核心侧请求和回复均携带IPv6显式空标签2。此前已通过的双向3/3流量未再重复执行。
