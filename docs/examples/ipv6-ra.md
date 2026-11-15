# IPv6 自动配置

本例验证从上游 RA 获取地址与默认路由、分别关闭两项功能，以及完全撤销。DHCPv6 不提供默认网关；本例不使用 DHCPv6。

## 拓扑与前提

```text
Ubuntu 测试虚拟机：Linux 数据面 eth2 ── 隔离链路 ── QEMU 网络端点
  从 RA 学习地址和路由                           发送 PIO 与 Router Lifetime
```

这是开发服务器上的实际 Virtio 端口测试。QEMU 端点使用其既定实验前缀 `fec0::/64`，因此下面真实输出包含该前缀；生产网络应使用自己的正常 IPv6 地址规划，不应照搬实验前缀。设备上将 `eth2` 替换为实际三层接口名。

上游必须发送有效的自主地址前缀选项和非零 Router Lifetime。只有前缀、没有 Router Lifetime 时，不会得到默认路由；只有默认路由、没有自主前缀时，不会得到 SLAAC 地址。

## 配置

```text
system-view
interface eth2
 undo shutdown
 ipv6 address auto global default
 quit
commit
```

只在指定接口开启接收。组合命令同时启用 SLAAC 和 RA 默认路由。内核仍执行 DAD；地址处于 tentative 时不能把立即发出的探测计为有效连通性测试。确认后可 `save`。

## 实际查询与流量

```text
display ipv6 interface brief
display ipv6 routing-table
ping ipv6 -c 3 -a fec0::5054:ff:fe11:2242 fec0::2
```

实际接口摘要节选：

```text
Interface   IPv6 Address/Mask              Physical  Protocol  VPN-Instance
eth2        fec0::5054:ff:fe11:2242/64     up        up        default
```

实际默认路由节选：

```text
Destination  : ::
PrefixLength : 0
NextHop      : fe80::2
Preference   : 0
Cost         : 1024
Protocol     : Kernel
Interface    : eth2
```

路由由本实验环境的 Linux RA 学习而来，因此显示为 Kernel；这里不是静态路由或 DHCPv6 网关。探测实际为 3 packets transmitted、3 received、0% packet loss。地址后缀、有效时间和上游链路本地地址会随环境变化。

## 分别启用与撤销

只保留 SLAAC，撤销默认路由：

```text
interface eth2
 undo ipv6 nd ra default-route enable
 ipv6 address auto slaac
 quit
commit
```

本例实际保留 SLAAC 地址，默认路由消失。再切换为仅接收默认路由：

```text
interface eth2
 undo ipv6 address auto slaac
 ipv6 nd ra default-route enable
 quit
commit
```

实际 SLAAC 地址被清理，只保留链路本地地址；收到新的 RA 后重新安装默认路由，不重新生成 SLAAC 地址。

最后关闭剩余 RA 接收：

```text
interface eth2
 undo ipv6 nd ra default-route enable
 quit
commit
```

本例再次向上游发起路由器发现后，既未生成 SLAAC 地址，也未重新安装 RA 默认路由。组合模式也可用 `undo ipv6 address auto global default` 一次关闭。保存撤销结果需再执行 `save`。

清理范围是 RA 学习状态，手工地址与 DHCPv6 地址不属于这套清理范围。本例实际完成 Linux 数据面的三种模式及撤销；不能将本例等同于所有 VPP/LCP、VPN、DHCPv6 组合均已验证。参见 [RA 与 SLAAC](../operator/ipv6-autoconfig.md)。
