# 静态路由组

为大量前缀共用下一跳与路由属性。

[命令参考](reference/route-groups.md) · [配置案例](../examples/route-group.md)

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

### 文件成员与URL成员

路由组的外部列表统一存放在：

```text
/VortexROS/route-static-groupd
```

管理员可先把每行一个CIDR的文件放到该目录，再在路由组视图中选择。`?`和Tab只列出目录顶层的普通文件，不接受子目录、符号链接或包含路径分隔符的名称：

```text
route-static group name CDN
 source file cdn-v4.txt
```

首次`commit`会解析、规范化并生成不可变运行快照。之后直接修改原文件不会绕过配置事务改变现网；执行下面的命令才会重新读取、显示进度并增量更新路由：

```text
reset route-static group name CDN
```

URL与本地文件互斥。URL下载后的原始物化结果和元数据也由系统存放在同一目录的受管子目录中：

```text
route-static group name CDN
 source url https://lists.example.net/cdn-v4.txt vpn-instance BLUE
 auto-refresh enable
 auto-refresh interval 4320
```

URL默认必须使用HTTPS。只有明确接受明文传输的受控环境才可配置
`source url http://192.0.2.10/routes.txt insecure`；HTTPS来源不允许经重定向降级为HTTP。

两种来源的内容均为每行一个CIDR，空行和整行`#`注释跳过；任一非法行使新版本整体失效。手工与外部成员取并集。本地文件不支持`auto-refresh`；URL可按配置定时刷新。

首次配置URL后，执行全局 `commit` 会显示连接、下载、检查、应用和完成等进度；只有文件下载并检查成功后配置才会生效。后续普通commit不会重复下载：

```text
reset route-static group name CDN
display route-static group name CDN verbose
display ip routing-table-group name CDN verbose
```

Ctrl+C只停止当前终端的进度显示，不取消设备正在执行的更新，也不关闭SSH。

## 路由组增量修改

- 一个成员变化只影响“该前缀×引用该组的绑定”；
- 一个绑定变化只处理该组成员；
- 普通静态路由和多个路由组产生完全相同的路径和属性时，设备只保留一条有效路由；
- 路径相同但Preference、Tag等不同会报告冲突；
- 增加或删除单个成员时，只更新该成员所影响的路由，不重新加载整个路由组。
