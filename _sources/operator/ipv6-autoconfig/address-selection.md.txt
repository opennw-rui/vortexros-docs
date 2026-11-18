# 地址选择

## 为什么一个接口会有多个 IPv6 地址

|来源|典型形式|是否进入静态配置|
|---|---|---|
|手工配置|全局单播 /64、/128 等|是|
|SLAAC|上游 RA 前缀生成的稳定地址|保存获取方式，地址重新学习|
|SLAAC 隐私扩展|同一前缀的临时地址|本版默认关闭，不生成|
|DHCPv6 IA_NA|服务器分配的地址，通常为 /128|保存客户端设置，地址重新申请|
|链路本地|fe80::/10|自动地址不作为全局地址保存|

同时启用 SLAAC 和 DHCPv6 IA_NA，可以正常获得两个全局地址，另有链路本地地址。旧环境若同时开启隐私扩展，还可能出现第三个全局地址。这不等于重复租约。

本版对受管三层接口禁用临时隐私地址，并在接管已有接口时清理其临时地址，保留稳定地址、手工地址和独立 DHCPv6 地址。没有增加“最多一个 IPv6 地址”的硬限制。多个 RA 前缀、多条手工地址及过渡期前缀都可能合法并存。

## 只通过 SLAAC 获取全局地址

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 0
 ipv6 enable
 undo ipv6 address auto dhcp
 ipv6 address auto global default
#
~~~

CLI 操作：

~~~text
commit
~~~

还应删除不再使用的手工全局地址。上游只发布一个可用于自主配置的 /64 时，通常得到一个稳定 SLAAC 全局地址，加一个链路本地地址。

## 只通过 DHCPv6 获取全局地址

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 0
 ipv6 enable
 undo ipv6 address auto global
 ipv6 address auto dhcp
 ipv6 nd ra default-route enable
#
~~~

CLI 操作：

~~~text
commit
~~~

最后一条仅学习 RA 默认路由，不启用 SLAAC；DHCPv6 本身不提供默认网关。若之前通过组合命令启用了 RA 默认路由，撤销 global 不会顺带关闭独立的默认路由学习意图。

不要把 hint 当成固定保留地址；服务器仍有权分配其他可用地址。委派前缀 IA_PD 供下游使用，也不等于客户端本接口的 IA_NA 地址。

## 查询与撤销

~~~text
display ipv6 interface Ethernet 0
display dhcpv6 client interface Ethernet 0
display ipv6 routing-table
~~~

确认地址来源后撤销对应获取方式；不要用删除静态地址命令代替停止动态客户端。关闭全部自动获取时，分别执行 `undo ipv6 address auto global default` 和 `undo ipv6 address auto dhcp`，提交后再检查实际地址及路由。

IA_TA 是 DHCPv6 临时地址类型，与 SLAAC 隐私地址不同。当前配套 Kea 服务端不分配 IA_TA；需要自动地址或前缀委派时使用 IA_NA/IA_PD，见[DHCPv6 租约](../dhcp/leases.md)。