# RIPng

使用 RIPng 在 IPv6 网络交换路由。路由使用后端默认优先级 120。

[命令参考](reference/ripng.md)

## 配置


```text
ripng 2 vpn-instance BLUE
 network 2001:db8:100::/64
 import-route static
 default-route originate
```

RIPng视图中的`import-route ospf`表示导入OSPFv3路由，系统会映射到后端的IPv6协议名称。

在 RIPng 进程视图用 `aggregate-address 2001:db8:100::/48` 配置汇总。
提交后可在邻居的 `display ripng <进程号> route` 核对收到的前缀。
用 `undo aggregate-address 2001:db8:100::/48` 并提交撤销。

`offset-list <IPv6 ACL> in 4 interface <接口>` 可调整匹配入向路由的度量，
`out` 用于出向，省略接口时应用于该进程。ACL 规则只可用 permit 或 deny 匹配
IPv6 源前缀，该前缀在这里对应路由目的前缀。已引用的 ACL 须保留至少一条规则。用
`undo offset-list in interface <接口>` 撤销，提交后在 RIPng 路由表核对度量。

## 验证与撤销

```text
display ripng 2 interface
display ripng 2 route
```

执行 `undo ripng 2 vpn-instance BLUE` 并提交会删除该进程。
