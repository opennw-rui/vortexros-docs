# Bash 与 sudo

只有system-admin可使用`run bash`进入系统Shell，并可按账号策略使用sudo。network-admin负责设备配置，network-operator只读；角色权限见[角色与入口](../aaa.md)。

在受管SSH终端中执行：

~~~text
run bash
~~~

进入后由Bash处理路径补全、编辑键和Ctrl+C。执行`exit`或按Ctrl+D返回VortexROS CLI。Bash中输入不存在的命令会由Bash报告错误，不改变CLI权限。

网络接口、地址、路由和服务配置仍应通过VortexROS CLI完成，避免系统Shell中的临时修改与设备配置不一致。Bash适合系统维护和故障信息收集，不是网络配置的第二入口。

[账号命令](../reference/aaa.md)
