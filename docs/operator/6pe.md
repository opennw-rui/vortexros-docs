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
