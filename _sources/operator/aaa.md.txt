# 本地账号与 SSH


现有 Linux 救援账号仍使用 OpenSSH 登录，再执行 `sudo vortexros`。受管账号使用
`ssh 用户名@设备` 直接进入 VortexROS CLI。SSH 需要交互终端，受管账号不开放远程执行、文件传输或 SSH 转发。

| 角色 | 权限 |
| --- | --- |
| `network-operator` | 查询接口、协议、路由和系统健康等运行状态 |
| `network-admin` | 网络配置、提交、保存和网络运维 |
| `system-admin` | 网络与系统配置、账号管理；默认可运行 Bash 和 sudo，可用 `undo shell-access` 单独撤销 |


默认不内置受管用户或密码。受管 SSH 与独立 Linux 救援入口分开；账号修改先提交，保存后才进入启动 CFG。

## 账号、认证与授权

本地账号配置决定谁可进入受管 CLI，以及进入后能执行哪些操作。密码和公钥用于身份认证，角色用于授权；拥有有效 Linux 认证信息不等于已完成受管账号的权限更新。

按最小实际职责选择角色，首次改密、账号启停和 Bash 权限分别配置。首次改密只保存该账号所需的凭据变化，不替用户保存其他尚未保存的网络配置。账号投影尚未完成时的登录限制和自动恢复见密码页面。

宿主 OpenSSH 的 AllowUsers 等既有策略由系统管理员维护，不由 VortexROS 擅自放宽。账号存在、密码正确而 SSH 被宿主拒绝时，应检查对应策略；保留独立 Linux 救援入口，避免只依赖即将修改的受管账号。

~~~{toctree}
:maxdepth: 2

aaa/accounts
aaa/password
aaa/keys
aaa/sessions
aaa/bash
~~~

[命令参数](reference/aaa.md)
