# 组合与清理

`ipv6 address auto global default` 同时启用 SLAAC 与默认路由接收。撤销全部 RA 意图后，清理 RA 路由和 SLAAC 地址；独立 DHCPv6 地址不受影响。

## 地址共存与选择

同一接口可以同时使用 SLAAC 地址和 DHCPv6 地址。两者的前缀长度不必相同，例如 SLAAC 的 `/64` 与 DHCPv6 IA_NA 的 `/128` 可以并存。链路本地地址另计；这三种地址同时出现不等于生成了隐私地址，临时隐私地址默认关闭。

已验证的地址组合如下。DHCPv6 地址和委派前缀由服务器分配，不能把示例中的具体数值当作固定分配承诺。

| 地址 | 来源 | 用途 |
|---|---|---|
| `2001:db8:229:0:fe:dfff:fec3:cf22/64` | SLAAC | 全局通信 |
| `2001:db8:229::123/128` | DHCPv6 IA_NA | 全局通信 |
| `fe80::fe:dfff:fec3:cf22/64` | 链路本地地址 | 邻居发现与链路本地通信 |

`display ipv6 interface` 显示实际地址及 SLAAC、默认路由学习状态；`display dhcpv6 client` 显示 DHCPv6 获取结果，`display dhcpv6 client prefix` 显示委派前缀。DHCPv6 地址提示（hint）只是向服务器提出建议，不保证分配该地址；显示结果和源地址选择应使用实际取得的租约。检查实际地址后，可使用 `ping ipv6 -a SOURCE DESTINATION` 明确选择源地址。

不需要 SLAAC 地址而只使用 DHCPv6 地址时，撤销 SLAAC 配置；DHCPv6 不提供 IPv6 默认网关，需要单独保留 RA 默认路由学习或配置静态路由。撤销 DHCPv6 地址获取则保留 SLAAC 地址。撤销 `ipv6 address auto global default` 同时清理 SLAAC 地址和 RA 默认路由，不会删除独立的 DHCPv6 IA_NA 地址及前缀委派配置。

## 接口恢复

接口或数据面重建后，系统会重新发现上游路由器，恢复 SLAAC 地址；配置了默认路由学习时也会恢复 RA 默认路由，无需手动关闭、再打开接口。上游必须持续提供有效 RA，前缀需允许自主配置，地址通过 DAD 后才能使用。动态地址及默认路由不作为静态配置保存。

## 配置

以下为功能片段，接口、引用对象及对端须先按[完整案例](../../examples/ipv6-ra.md)准备。未创建的依赖会被拒绝。

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 1
 ipv6 enable
 ipv6 address auto global default
#
~~~

CLI 操作：

~~~text
commit
~~~

## 查询与实际效果

~~~text
display ipv6 interface brief
display ipv6 routing-table
~~~

[完整配置、检查与撤销](../../examples/ipv6-ra.md)；本节说明单项参数，完整组网请按案例的前置条件执行。

## 撤销

先解除消费者引用，再按以下片段撤销当前对象或开关；不要删除仍被其他业务使用的共享对象。

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 1
 undo ipv6 address auto global default
#
~~~

CLI 操作：

~~~text
commit
~~~

再次查询实际状态和新业务，确认后执行save。只提交未保存的变化不会在重启后作为启动配置恢复。

[逐条参数和限制](../reference/ipv6-autoconfig.md) · [功能目录](../ipv6-autoconfig.md)

## 修改与前缀委派

SLAAC 与 DHCPv6 地址获取可以先后启用。单独撤销任一获取方式，不会删除另一方式保留的地址；客户端重新申请期间，使用其动态地址的业务可能短暂中断。

前缀委派还包含两个独立对象：上游客户端请求，以及下游接口对命名前缀的引用。撤销时先删除下游引用，再撤销客户端请求；恢复后以 `display dhcpv6 client prefix` 的当前前缀为准。重新申请可能取得不同前缀，下游派生地址会随之更新，不能把动态委派值当作固定网段。
