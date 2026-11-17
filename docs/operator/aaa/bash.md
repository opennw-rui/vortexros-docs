# Bash 与 sudo

只有system-admin可使用`run bash`进入系统Shell，并可按账号策略使用sudo。network-admin负责设备配置，network-operator只读；角色权限见[角色与入口](../aaa.md)。

在受管SSH终端中执行：

~~~text
run bash
~~~

进入后由Bash处理路径补全、编辑键和Ctrl+C。执行`exit`或按Ctrl+D返回VortexROS CLI。Bash中输入不存在的命令会由Bash报告错误，不改变CLI权限。

网络接口、地址、路由和服务配置仍应通过VortexROS CLI完成，避免系统Shell中的临时修改与设备配置不一致。Bash适合系统维护和故障信息收集，不是网络配置的第二入口。

[账号命令](../reference/aaa.md)

## 密码与撤销

sudo 需要该账号的当前本地密码；首次改密后应输入新密码。公钥用于 SSH 认证，不替代 sudo 的密码校验。仅公钥、未设置本地密码的账号不能据此认为 sudo 可以完成认证。

管理员可在用户视图执行 `undo shell-access`、提交，单独撤销系统管理员的 Bash 入口；恢复使用 `shell-access enable`。停用或删除账号同时撤销其受管会话与 sudo 授权。修改角色或凭据后，旧 CLI 会话失效，应重新登录。

真实验证已覆盖：系统管理员进入 Bash 后 sudo 返回 root 身份；Bash 中输入不存在的命令再退出，只显示 Bash 自身错误，不在 CLI 追加 `exit status 127`。撤销 Bash 后，公钥仍可登录 CLI，但 `run bash` 被拒绝。


重启控制服务后，旧管理会话也可能失效。出现 local management session expired or invalid 时，应退出当前 CLI 并重新登录或重新进入 CLI；不要把管理会话失效当成数据面转发停止。未提交或未保存的配置按相应配置生命周期处理。
