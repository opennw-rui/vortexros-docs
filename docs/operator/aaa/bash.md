# Bash 与 sudo


进入 run bash 后，空回车、Tab、方向键、退格及 Ctrl-C 由 Bash 处理；Ctrl-D 或 exit 返回 VortexROS CLI。Bash 执行期间不应穿插设备CLI提示符。非零命令状态本身不应在正常退出Bash时产生额外的 exit status127。

开发服务器使用当前未发布工作树的真实 SSH 补验：连续20次空回车时同一个Bash进程保持前台，原始PTY字节中没有穿插设备提示符；路径Tab、编辑键、Ctrl-C、窗口大小变更、密码sudo及Ctrl-D均正常。该结果对应已有终端所有权修复，不代表对旧发布标签完成重新部署。

管理员撤销 shell-access 后，旧会话可能提示身份已改变；重新登录仍可使用本角色允许的CLI，但 run bash 会被拒绝。需要恢复时，由管理员在对应user视图恢复 shell-access 并提交，再重新登录。不要把保留CLI登录权限与仍有Bash权限混为一谈。

[角色与入口](../aaa.md) · [命令参考](../reference/aaa.md)
