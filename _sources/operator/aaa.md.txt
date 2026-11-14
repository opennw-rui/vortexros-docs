# 本地账号与 SSH

## 管理入口和角色

现有 Linux 救援账号仍使用 OpenSSH 登录，再执行 `sudo vortexros`。受管账号使用
`ssh 用户名@设备` 直接进入 VortexROS CLI。SSH 需要交互终端，受管账号不开放远程执行、文件传输或 SSH 转发。

| 角色 | 权限 |
| --- | --- |
| `network-operator` | 查询接口、协议、路由和系统健康等运行状态 |
| `network-admin` | 网络配置、提交、保存和网络运维 |
| `system-admin` | 网络与系统配置、账号管理；默认可运行 Bash 和 sudo，可用 `undo shell-access` 单独撤销 |

## 初始化本地管理员

出厂配置没有受管用户。通过 Linux 救援入口执行 `sudo vortexros`，创建首个管理员。
如需首次登录改密，用 `password PASSWORD` 设置临时密码后使用 `password change-required`，再提交并保存。

```text
system-view
user opsadmin
 role system-admin
 password TEMPORARY-PASSWORD
 password change-required
quit
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


## 首次改密失败恢复

首次改密只保存该账号的凭据变更，不会把其他尚未保存的网络配置一起写入启动 CFG。命令失败时，需要区分“尚未接受”和“已经接受、后续持久化或 Linux 投影未完成”。

| 失败阶段 | 状态与处理 |
| --- | --- |
| 启动 CFG 替换前失败 | 新密码未被接受；先恢复存储，再使用临时密码重试首次改密 |
| CFG 已替换，父目录同步失败 | 回读确认后继续发布 Running，并报告持久性不确定；确认存储恢复后由管理员重新保存 |
| CFG 和 Running 已接受，但 Linux 账号投影失败 | 保留新配置，产生 `LOCAL_ACCOUNTS_FAILED`；受管 CLI 拒绝授权，等待投影恢复后用新密码连接 |
| Linux 操作已部分完成，但投影服务最终失败 | 即使 Linux 已接受新密码，完整投影成功前仍不开放受管 CLI |

从独立 Linux 救援入口检查：

~~~bash
sudo vortexros --no-pager display alarm active
sudo vortexros health check --json --require-saved
sudo journalctl -u vortexros-aaa-apply.service -u vortexrosd.service --since '-10 minutes' --no-pager
~~~

按错误内容恢复 `/VortexROS/run/aaa-apply.json` 的写入条件、账号工具执行条件或存储故障。控制进程沿用现有自动收敛重新应用 Running，完整成功后清除告警。无需为重试再修改一次账号。

**登录限制以完整投影结果为准。** OpenSSH 的 Linux 密码认证与 VortexROS 的 CLI 授权是两个阶段。旧 shadow 尚未更新时，旧临时密码可能通过前者，但不能借此进入普通 CLI；部分操作后新密码已经可认证，也仍须等待完整投影成功。新 sudo 授权同样在成功后发布。root 救援入口保持可用。

当告警清除、严格健康恢复，并确认 Linux 已同步后，用新密码重新 SSH 登录。正常完成会显示：

~~~text
Password changed and saved. Reconnect using the new password.
~~~

Debug 9 最终包在 QEMU 中已验证准备文件写入失败、chpasswd 失败和部分执行后失败的恢复，以及公钥登录、保存和控制服务重启。详见[发布验证](../release/vortexros.md)。
