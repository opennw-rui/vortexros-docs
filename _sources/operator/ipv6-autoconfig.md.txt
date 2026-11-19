# IPv6 与 RA

全局 IPv6 能力始终可用，没有全局关闭命令。每个三层接口默认关闭 IPv6；先配置 `ipv6 enable`，再配置地址、RA、DHCPv6 或 IPv6 路由协议。默认不发送 RA、不接受 RA 自动地址或默认路由、不生成临时隐私地址。

## 地址获取与路由获取

IPv6 接口可能同时具有链路本地、手工全局、SLAAC 和 DHCPv6 地址。地址数量取决于配置和收到的前缀，不应仅以“不是一个地址”认定异常。链路本地地址用于同链路控制通信，全局地址用于相应业务范围。

| 机制 | 取得的内容 | 需要的对端 |
| --- | --- | --- |
| SLAAC（RFC 4862） | 根据 RA 前缀生成地址 | 发布有效自主前缀的路由器 |
| RA（RFC 4861） | 前缀、路由器及相关链路信息 | IPv6 路由器 |
| DHCPv6 IA_NA / IA_TA | 地址租约 | DHCPv6 服务器或中继 |
| DHCPv6 IA_PD | 授权给下游使用的前缀 | 支持前缀委派的服务器 |

本产品全局 IPv6 能力常开，接口缺省不启用；按页内命令显式启用接口。DHCPv6 不提供默认网关，默认路由应按 RA 或静态/动态路由方式取得。隐私临时地址、稳定地址和租约地址也不是相同概念，详见地址选择页面。

验证时检查地址来源、前缀长度、有效期、默认路由和实际双向通信。停止接收 RA 与停止通告 RA 是两种方向不同的操作；撤销时还要核对原来学习的地址和路由的生命周期。

~~~{toctree}
:maxdepth: 2

ipv6-autoconfig/interface
ipv6-autoconfig/slaac
ipv6-autoconfig/default-route
ipv6-autoconfig/advertisements
ipv6-autoconfig/address-selection
ipv6-autoconfig/combined
ipv6-autoconfig/prefix-delegation
~~~

[双端配置案例](../examples/ipv6-ra.md) · [DHCPv6 与前缀委派](../examples/dhcpv6.md) · [命令参考](reference/ipv6-autoconfig.md)
