# Candidate、提交与保存

## 从编辑到生效

| 命令 | 作用和影响 |
| --- | --- |
| display configuration candidate | 查看本会话待提交的变更 |
| refresh configuration candidate | 将本会话变更合并到最新 Running；若有冲突，按提示检查具体对象 |
| commit | 检查依赖并接受配置，可能改变接口、路由或转发策略 |
| display current-configuration | 查看已提交的 Running；接口视图可用 display this 查看对应范围 |
| display health | 查看后端收敛状态 |
| save | 把 Running 保存为启动配置，按提示确认 |
| clear configuration candidate | 只清除本会话未提交的修改，按提示确认 |

交互式 CLI 需要先建立管理会话；控制服务尚未就绪时会提示退出，待服务恢复后重新进入。服务重启后，已有会话若提示令牌失效，也需要重新进入，不会自动重发未完成的配置命令。

每个会话有独立的 Candidate。提交失败时先读返回信息。若配置校验被拒绝，修正 Candidate。若提示配置已接受但运行状态未收敛，用 display health verbose 和 display alarm active 查原因，再根据实际业务状态决定是否保存。


## 试用一次编辑

在示例接口上暂存描述，查看差异后清除：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 1
 description LAB-UPLINK
#
~~~

CLI 操作：

~~~text
display configuration candidate
clear configuration candidate
~~~

按提示确认清除。description 只修改接口说明文本，本例没有执行 commit。实际配置地址和转发见[静态路由案例](../../examples/static-route.md)。


## 提交等待提示

普通交互式 `commit` 等待约 1 秒后显示 `Committing.`，随后每秒追加一点，单行最多 12 点。完成后换行显示原有结果。Ctrl+C 停止进度显示，已经发出的提交请求继续执行；重新查询 Candidate、Running 和健康状态确认结果。快速提交和脚本调用不显示通用进度，数据面接管和远程路由列表保留各自阶段提示。


[目录](../01-cli.md)

## 导出与重新导入

```text
export configuration backup.cfg
load configuration backup.cfg
display configuration candidate
commit
save
```

导出的是受保护的已提交配置。相对文件名在当前实例的配置目录中解析，重新导入相同文件名也使用该目录；使用自定义配置位置时，不会转向默认目录或另一实例寻找同名文件。越出配置目录的相对路径会被拒绝，显式绝对路径导入仍可用。导入只替换本会话的Candidate，检查差异后再提交、保存；不要在没有确认差异时用备份覆盖其他会话的新配置。

实际导出后重新导入未变化的配置，差异查询显示 `No unmatched configurations.`。接口视图的 `display this` 查看Running，未提交的内容使用Candidate查询。

## Running 与启动配置

`display current-configuration`（可缩写为 `display cu`）读取最新已提交的 Running；其他会话的提交也应在下一次查询中可见。它不显示本会话尚未提交的 Candidate。

`display saved-configuration`（可缩写为 `display saved`）每次读取当前选定的启动文件；追加文件名时读取指定 CFG。磁盘文件被修改后，下次查询读取新配置，不沿用之前的显示缓存。手工编辑启动文件不会直接修改 Running；需要按导入、检查差异和提交的流程使配置生效。文件缺失或不能解析时报告错误。

配置显示只列出配置命令及 `#` 层级分隔符，不额外插入文件路径、格式版本或内部运行状态的注释说明。复制显示内容重新导入时，DHCP 客户端和中继保持其显式配置；角色的显式暂停由 `dhcp client-relay shutdown` 控制，不能因为没有版本注释或未启用 DHCP Server 而被停用。

## 按功能和视图查看配置

`display current-configuration configuration` 后选择功能名称。它只显示所选功能，便于检查和备份；不代表后端已收敛。接口参数使用类型加编号：

```text
display current-configuration configuration vpn-instance
display current-configuration configuration bridge-domain 460
display current-configuration configuration bgp
display current-configuration interface Ethernet 1
```

`display this` 查看所在视图的已提交配置。例如进入 VPN 的 IPv6 地址族后，只显示该地址族；返回 VPN 视图则可查看两族和共享属性。以下为已配置 RD、RT 的 IPv6 地址族输出：

```text
#
 ipv6-family
  route-distinguisher 65000:1803
  vpn-target 65000:50081 export-extcommunity
  vpn-target 65000:50081 import-extcommunity
#
return
```

需要查看未提交编辑时使用 `display configuration candidate`。输出中的 `#` 是配置层级分隔符；`return` 结束配置清单。
