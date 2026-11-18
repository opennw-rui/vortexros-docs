# 命令行

Linux 救援账号在终端执行 `sudo vortexros`；受管账号通过 SSH 直接进入 CLI。可执行的查询和配置由[AAA 角色](aaa.md)决定，网络配置从 `system-view` 开始。

| 提示符示例 | 位置 | 常用操作 |
| --- | --- | --- |
| &lt;VortexROS&gt; | 用户视图 | 查询、诊断、保存 |
| [~VortexROS] | 系统视图，无待提交改动 | 创建接口、路由或协议配置 |
| [*VortexROS-Ethernet1] | 接口视图，有待提交改动 | 配置当前接口，用 quit 返回上一层 |

输入 ? 查询当前位置允许的命令、参数和范围。输入当前词的前缀后，Tab 补全并循环候选；空行和空格后的空参数不触发补全。缩写必须能在当前位置唯一匹配。return 返回用户视图；如有待提交配置，按提示选择提交、丢弃或取消退出。

~~~{toctree}
:maxdepth: 2

cli/configuration
cli/help
cli/startup
~~~
