# RA 通告

## 用途与默认值

RA 告诉同链路设备默认路由器、IPv6 前缀及地址获取方式。发送 RA 与接收 RA 是独立配置：作为下游网关时配置发送；向上游获取地址时配置 SLAAC/默认路由接收。

默认抑制发送，M/O 标志关闭，路由器生存期 1800 秒。使用 `undo ipv6 nd ra halt` 开启发送；正向 `ipv6 nd ra halt` 恢复默认抑制。默认项不会出现在保存配置中。

|命令/参数|作用与影响|
|---|---|
|`ipv6 nd autoconfig managed-address-flag`|设置 M 标志，告知终端可通过 DHCPv6 获取地址；不会自动替终端创建 DHCPv6 客户端|
|`ipv6 nd autoconfig other-flag`|设置 O 标志，告知终端可通过 DHCPv6 获取 DNS 等其他信息|
|`ipv6 nd ra lifetime SECONDS`|0 表示不作为默认路由器；非零值 4–9000，启用发送时须至少为默认最大通告间隔 600 秒|
|`ipv6 nd ra prefix ADDRESS LENGTH VALID PREFERRED`|指定通告前缀及有效/首选寿命，单位秒；PREFERRED 不得大于 VALID|
|`no-autoconfig`|清除该前缀的 A 标志，不允许终端用它生成 SLAAC 地址|
|`off-link`|清除该前缀的 L 标志，不把该前缀声明为链路直连|

寿命是无符号 32 位秒数；配置 4294967295 表示协议规定的无限寿命。普通 SLAAC 使用 /64；其他长度不能假定终端会生成地址。前缀的 A/L 标志与 RA 的 M/O 标志相互独立。

## 配置

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 0
 ipv6 enable
 ipv6 address 2001:db8:229::1 64
 ipv6 nd ra prefix 2001:db8:229:: 64 3600 1800
 ipv6 nd autoconfig managed-address-flag
 ipv6 nd autoconfig other-flag
 undo ipv6 nd ra halt
#
~~~

CLI 操作：

~~~text
commit
~~~

需要 DHCPv6 地址而不要同前缀的 SLAAC 地址时，在前缀命令末尾添加 `no-autoconfig`。需要继续提供地址前缀但不提供默认路由时，把 router lifetime 设为 0。

## 验证

~~~text
display ipv6 interface Ethernet 0
display current-configuration interface Ethernet 0
~~~

在对端执行 `display ipv6 interface`、`display ipv6 routing-table`，并进行实际 IPv6 Ping。详细显示中的配置字段不替代对端回读。实际报文验证已取得 M/O 标志、300/150 秒前缀寿命和 1800 秒路由器寿命；完整步骤见[RA 案例](../../examples/ipv6-ra.md)。

## 撤销

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 0
 ipv6 nd ra halt
 undo ipv6 nd autoconfig managed-address-flag
 undo ipv6 nd autoconfig other-flag
 undo ipv6 nd ra prefix
 undo ipv6 nd ra lifetime
#
~~~

CLI 操作：

~~~text
commit
~~~

带 ADDRESS、LENGTH 的 undo prefix 只删除指定前缀；不带参数删除所有显式 RA 前缀。停止发送或删除前缀不等于远端立即遗忘历史地址；终端还会遵守此前收到的有效期。确认对端结果后再保存。

默认参数参照[华为 ND 数据模型](https://www.netconfcentral.org/modules/huawei-ipv6-nd/2021-07-16/source/raw/)；实际支持的参数以本页和当前 CLI 为准。
