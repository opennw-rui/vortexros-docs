# 首次改密与恢复


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

已有包级验收在QEMU中验证了准备文件写入失败、chpasswd 失败和部分执行后失败的恢复，以及公钥登录、保存和控制服务重启。详见[发布验证](../../release/vortexros.md)。


[角色与入口](../aaa.md) · [命令参考](../reference/aaa.md)
