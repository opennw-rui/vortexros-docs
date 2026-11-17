# 创建与管理


出厂配置没有受管用户。通过 Linux 救援入口执行 `sudo vortexros`，创建首个管理员。
如需首次登录改密，用 `password PASSWORD` 设置临时密码后使用 `password change-required`，再提交并保存。

```text
system-view
```

配置清单：

```text
user opsadmin
 role system-admin
 password TEMPORARY-PASSWORD
 password change-required
#
```

CLI 操作：

```text
commit
return
save
```

使用临时密码登录时，CLI 会要求输入新密码。此时普通 CLI、Bash 和 sudo 均不可用。
改密会更新当前启动文件中的账号，成功后重新连接。未设置 `password change-required`
的账号直接进入 CLI。若提示改密已接受但启动文件持久性不确定，先用新密码重新连接，
并由管理员确认存储恢复后重新保存。

`password PASSWORD` 在终端内遮蔽密码输入，也可输入 `password` 后按提示设置并确认。也可以用 `ssh-public-key laptop ssh-ed25519 KEY`
配置公钥。SSH 公钥认证不提供 sudo 的密码。需要运行 sudo 的管理员请设置本机密码。
退出 Bash 后返回当前 CLI。

```text
display aaa users
display current-configuration configuration users
display aaa user opsadmin verbose
display aaa authentication
display users
run bash
```

账号修改进入 Candidate。提交后才投影到 Linux，保存后按启动配置恢复。root 与 system-admin 的配置显示使用 `password` 加 yescrypt 哈希。导出的配置含密码验证器，须按私密配置保管。新建账号默认处于 active 状态，提交前须配置密码或公钥。用 `undo active` 停用，`active` 恢复。默认角色和 active 状态在配置中省略。

用 `undo user NAME` 删除账号。管理员可用 `reset aaa user NAME sessions` 断开该账号的现有 CLI 会话。普通运行配置重置保留账号，恢复出厂清除受管账号。
账号投影失败时，可从救援入口检查 `display alarm active` 和
`journalctl -u vortexros-aaa-apply.service`。恢复出厂会等待受管账号清理；若清理失败，CLI 会显示待完成，健康检查保留 AAA 告警。
受管 CLI 在 Linux 凭据尚未同步完成时拒绝登录。独立 Linux 救援入口仍可使用。
故障解除后，控制进程会重新投影已提交的账号配置，成功后清除告警。首次改密已接受时，请等待投影恢复，然后使用新密码重新登录。与已有 Linux 用户同名时，请使用其他名称。
如果宿主 OpenSSH 配置了 `AllowUsers`，请将需要登录的受管用户名加入现有名单。先执行 `sshd -t` 验证配置，再重新加载 SSH 服务。


[角色与入口](../aaa.md) · [命令参考](../reference/aaa.md)
