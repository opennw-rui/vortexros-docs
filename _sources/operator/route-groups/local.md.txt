# 本地路由组

## 配置

静态路由组用于让大量前缀共用相同的下一跳、出接口、VPN、Preference和Tag。配置中只保留路由组及其绑定关系，不会把十万条成员展开成同样数量的普通静态路由命令。

```text
route-static group name CDN
 description CDN-PREFIXES
 route 198.18.0.0/24
 route 198.18.1.1
#
ip route-static-group CDN 192.0.2.1 preference 60 tag 100
```

裸IPv4规范为`/32`，裸IPv6规范为`/128`，输入掩码后配置统一显示CIDR。手工成员自动去重。


[功能目录](../route-groups.md) · [命令参数](../reference/route-groups.md)
