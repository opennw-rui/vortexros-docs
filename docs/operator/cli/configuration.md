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

每个会话有独立的 Candidate。提交失败时先读返回信息。若配置校验被拒绝，修正 Candidate。若提示配置已接受但运行状态未收敛，用 display health verbose 和 display alarm active 查原因，再根据实际业务状态决定是否保存。


## 试用一次编辑

在示例接口上暂存描述，查看差异后清除：

~~~text
system-view
interface Ethernet 1
description LAB-UPLINK
quit
display configuration candidate
clear configuration candidate
~~~

按提示确认清除。description 只修改接口说明文本，本例没有执行 commit。实际配置地址和转发见[静态路由案例](../../examples/static-route.md)。


## 提交等待提示

普通交互式 `commit` 等待约 1 秒后显示 `Committing.`，随后每秒追加一点，单行最多 12 点。完成后换行显示原有结果。Ctrl+C 停止进度显示，已经发出的提交请求继续执行；重新查询 Candidate、Running 和健康状态确认结果。快速提交和脚本调用不显示通用进度，数据面接管和远程路由列表保留各自阶段提示。


[目录](../01-cli.md)
