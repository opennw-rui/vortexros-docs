# 前缀列表

前缀列表按规则序号匹配网络和掩码长度；由引用它的路由策略决定是否接收或发布路由。

[命令参考](reference/prefix-lists.md) · [配置案例](../examples/bgp-policy.md)

## 配置与查询

```text
ip ip-prefix PL-IN index 10 permit 10.0.0.0 8 greater-equal 16 less-equal 24
ip ipv6-prefix V6-IN index 10 permit 2001:db8:: 32 greater-equal 48 less-equal 64
commit
display ip ip-prefix PL-IN
display ipv6 prefix V6-IN
```

第一条只匹配 10.0.0.0/8 以内且长度为 /16 至 /24 的前缀。可以追加不同序号的规则。用 `first-match` 检查给定 CIDR 的首条命中。创建列表本身不会过滤已安装的路由。删除前先解除 [路由策略](route-policy.md) 的引用。
