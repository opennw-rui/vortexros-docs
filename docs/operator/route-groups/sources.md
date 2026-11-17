# 文件与 URL

## 文件成员与URL成员

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


[功能目录](../route-groups.md) · [命令参数](../reference/route-groups.md)

## 更新结果与失败处理

IPv4、IPv6 列表可以同时使用。一次检查中的实际结果如下：

| 列表内容和操作 | 组与路由结果 |
|---|---|
| 单个合法前缀，提交或手动刷新 | `manual 0 external 1 effective 1`，对应路由存在 |
| 第二行含非法 CIDR，手动刷新 | 返回具体行号错误，保留上一份有效路由 |
| 仅含注释的合法空列表 | `effective 0`，该组成员路由撤销 |
| 周期 5 分钟，服务端改为空列表 | 周期下载后两族精确路由查询均为 0 条 |
| 撤销来源和自动刷新，改用手工成员 | `manual 1 external 0 effective 1`，不再显示 URL 或刷新计划 |

下载错误不会把无法读取的列表当成空表。恢复来源后可以手动刷新，也可以等候下一次自动尝试；用组详情、告警和实际路由共同确认恢复。删除最后一个成员、解除绑定和删除组是三个不同操作。
