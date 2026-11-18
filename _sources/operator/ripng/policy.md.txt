# 汇总与度量偏移

在 RIPng 进程视图用 `aggregate-address 2001:db8:100::/48` 配置汇总。
提交后可在邻居的 `display ripng <进程号> route` 核对收到的前缀。
用 `undo aggregate-address 2001:db8:100::/48` 并提交撤销。

`offset-list <IPv6 ACL> in 4 interface <接口>` 可调整匹配入向路由的度量，
`out` 用于出向，省略接口时应用于该进程。ACL 规则只可用 permit 或 deny 匹配
IPv6 源前缀，该前缀在这里对应路由目的前缀。已引用的 ACL 须保留至少一条规则。用
`undo offset-list in interface <接口>` 撤销，提交后在 RIPng 路由表核对度量。


[完整双端案例](../../examples/ripng.md) · [参数参考](../reference/ripng.md)

## 度量计算与上限

默认接口接收代价为 1。出向 offset 增加发送度量；入向 ACL 匹配时，配置的 offset 作为该次接收的接口代价，替代通常的接口加 1，不能再重复加一次默认代价。未匹配 ACL 的路由仍按普通接口代价处理。

实际结果中，重分发默认度量 4、出向偏移 2，接收端 Cost 为 7。出向偏移 1、入向偏移 3 时为 8；把入向偏移改为 5 时为 10。度量达到 16 表示不可达，对应前缀退出有效路由选择；若仍有默认路由，目的地址查询可能返回默认路由，不表示该精确前缀仍然存在。

## 完整配置与撤销

两端先按[基础案例](../../examples/ripng.md)建立 RIPng，接口以下用 Ethernet0 表示。在发送端，为希望调整的路由前缀配置 ACL：

```text
acl ipv6 name RIP-OUT
 rule 5 permit ipv6 source 2001:db8:249:99::/64
#
ripng 1
 offset-list RIP-OUT out 2 interface Ethernet0
#
```

在接收端配置入向偏移时，同样先建立仅匹配路由前缀的 IPv6 ACL，再进入 RIPng 视图：

```text
acl ipv6 name RIP-IN
 rule 5 permit ipv6 source 2001:db8:249:99::/64
#
ripng 1
 offset-list RIP-IN in 3
#
```

每端提交后查询，等待正常更新到达：

```text
display ripng 1 route
display ipv6 routing-table protocol ripng
display acl ipv6 name RIP-IN
```

删除时先解除引用，再删 ACL。发送端：

```text
ripng 1
 undo offset-list out interface Ethernet0
#
undo acl ipv6 name RIP-OUT
```

接收端：

```text
ripng 1
 undo offset-list in
#
undo acl ipv6 name RIP-IN
```

引用中的 ACL 不允许直接删除，也不能改成匹配 UDP、TCP 等报文条件的规则；这里过滤的是路由前缀。实际尝试这些操作时均被拒绝，候选配置保持原样。
