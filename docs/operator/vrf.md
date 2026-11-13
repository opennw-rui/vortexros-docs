# VPN 实例

使用独立路由表隔离接口、协议和业务流量。

[命令参考](reference/vrf.md)

## 配置与影响

VPN-instance 默认可用，直接用 `ip vpn-instance NAME` 创建。已分配的表号继续使用，
新表从 1024 起查找可用值，可以超过 2048。VortexROS 跳过 Linux 和 VPP 已使用的表，
并按受管标记清理自身创建的 Linux VRF。默认实例仍对应 Linux main 表 254 和 VPP 表 0。


```text
ip vpn-instance BLUE
 ipv4-family
  route-distinguisher 65000:100
  vpn-target 65000:100 both
 ipv6-family
```

接口、路由和动态路由协议可以引用VPN实例。仍有配置引用时不能删除VPN。RD/RT只需在VPN实例下配置，在BGP VPN地址族中无需重复输入。
