# IPv6 与 RA

全局 IPv6 能力始终可用，没有全局关闭命令。每个三层接口默认关闭 IPv6；先配置 `ipv6 enable`，再配置地址、RA、DHCPv6 或 IPv6 路由协议。默认不发送 RA、不接受 RA 自动地址或默认路由、不生成临时隐私地址。

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
