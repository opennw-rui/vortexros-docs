# 本地账号与 SSH


现有 Linux 救援账号仍使用 OpenSSH 登录，再执行 `sudo vortexros`。受管账号使用
`ssh 用户名@设备` 直接进入 VortexROS CLI。SSH 需要交互终端，受管账号不开放远程执行、文件传输或 SSH 转发。

| 角色 | 权限 |
| --- | --- |
| `network-operator` | 查询接口、协议、路由和系统健康等运行状态 |
| `network-admin` | 网络配置、提交、保存和网络运维 |
| `system-admin` | 网络与系统配置、账号管理；默认可运行 Bash 和 sudo，可用 `undo shell-access` 单独撤销 |


默认不内置受管用户或密码。受管 SSH 与独立 Linux 救援入口分开；账号修改先提交，保存后才进入启动 CFG。

~~~{toctree}
:maxdepth: 2

aaa/accounts
aaa/password
aaa/keys
aaa/sessions
aaa/bash
~~~

[命令参数](reference/aaa.md)
