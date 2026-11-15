# 汇总与度量偏移

在 RIPng 进程视图用 `aggregate-address 2001:db8:100::/48` 配置汇总。
提交后可在邻居的 `display ripng <进程号> route` 核对收到的前缀。
用 `undo aggregate-address 2001:db8:100::/48` 并提交撤销。

`offset-list <IPv6 ACL> in 4 interface <接口>` 可调整匹配入向路由的度量，
`out` 用于出向，省略接口时应用于该进程。ACL 规则只可用 permit 或 deny 匹配
IPv6 源前缀，该前缀在这里对应路由目的前缀。已引用的 ACL 须保留至少一条规则。用
`undo offset-list in interface <接口>` 撤销，提交后在 RIPng 路由表核对度量。


[完整双端案例与实测](../../examples/ripng.md) · [参数参考](../reference/ripng.md)
