# 命令行

Linux 救援账号在终端执行 `sudo vortexros`；受管账号通过 SSH 直接进入 CLI。可执行的查询和配置由[AAA 角色](aaa.md)决定，网络配置从 `system-view` 开始。

| 提示符示例 | 位置 | 常用操作 |
| --- | --- | --- |
| &lt;VortexROS&gt; | 用户视图 | 查询、诊断、保存 |
| [~VortexROS] | 系统视图，无待提交改动 | 创建接口、路由或协议配置 |
| [*VortexROS-Ethernet1] | 接口视图，有待提交改动 | 配置当前接口，用 quit 返回上一层 |

输入 ? 查询当前位置允许的命令、参数和范围。输入当前词的前缀后，Tab 补全并循环候选；空行和空格后的空参数不触发补全。缩写必须能在当前位置唯一匹配。return 返回用户视图；如有待提交配置，按提示选择提交、丢弃或取消退出。

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

## 帮助、过滤与分页

~~~text
display interface brief
display current-configuration interface Ethernet 1
display ip routing-table protocol static
display ip fib | include 203.0.113
~~~

先用接口、协议或 VPN 参数缩小范围。include 过滤显示行，表头或总计可能保留。分页时按空格翻页、Enter 看下一行、q 结束显示。

## 试用一次编辑

在实验接口上暂存描述，查看差异后清除：

~~~text
system-view
interface Ethernet 1
description LAB-UPLINK
quit
display configuration candidate
clear configuration candidate
~~~

按提示确认清除。description 只修改接口说明文本，本例没有执行 commit。实际配置地址和转发见[静态路由案例](../examples/static-route.md)。

## 提交等待提示

普通交互式 `commit` 等待约 1 秒后显示 `Committing.`，随后每秒追加一点，单行最多 12 点。完成后换行显示原有结果。Ctrl+C 停止进度显示，已经发出的提交请求继续执行；重新查询 Candidate、Running 和健康状态确认结果。快速提交和脚本调用不显示通用进度，数据面接管和远程路由列表保留各自阶段提示。

## 启动配置片段

以下片段仅修改设备名称，可用于 CFG 解析和保存回放的语义校验；不代表网络拓扑验收。

```vortexros-config
#
sysname Manual-Test
#
return
```
