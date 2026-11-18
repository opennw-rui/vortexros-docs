# 6PE

通过 IPv4 LDP 核心承载全局 IPv6 路由。

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

后端使用 FRR 原生 `ipv6 labeled-unicast` 地址族。Zebra 将 6PE 路由写入 Linux
netlink，LCP 再同步到 VPP；VortexROS 不直接向 VPP 或内核下发 6PE 路由。


在对端检查 IPv6 BGP 路由、VPP MPLS 转发表和 IPv6 业务连通性。

## 完整双端案例

[6PE 案例](../examples/mpls/6pe.md)提供双端 IPv4 承载、LDP、BGP labeled-unicast、标签查询、双向业务和撤销步骤。配置 6PE 邻居后，所需 IPv6 显式空标签处理由设备自动完成，无需额外配置。

## 普通IPv6与标签模式切换

对已有IPv4承载邻居执行undo peer ADDRESS label-route-capability会撤销标签能力，同时保留该邻居的普通IPv6启用意图；这与删除整个邻居不同。两端模式应一致，普通IPv6路径还必须具备可解析的IPv6下一跳。重新启用标签能力后，已有network前缀会重新发布。

实际切换验证覆盖普通模式与6PE模式双向转换、会话摘要、标签撤销/恢复及恢复后的源地址指定探测。恢复后两个方向各1/1，核心侧请求和回复均携带IPv6显式空标签2。此前已通过的双向3/3流量未再重复执行。
