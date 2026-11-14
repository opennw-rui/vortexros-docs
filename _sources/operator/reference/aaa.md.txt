# 本地账号

[配置指南](../aaa.md)

## `active`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：enable SSH login

## `display aaa authentication`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the local login authentication policy

## `display aaa user`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display details for a local AAA account

## `display aaa users`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display local AAA accounts

## `display users`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display active management sessions

## `password`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：set local password

## `password change-required`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：require a password change on the next login

## `reset aaa user`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：disconnect sessions for a managed user

## `role`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：set local user role

## `run bash`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：open the managed administrator's Linux shell

## `shell-access enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：allow system-admin to enter Bash

## `ssh-public-key`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：set an Ed25519 SSH public key

## `undo active`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：disable SSH login

## `undo password`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：remove local password

## `undo shell-access`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：revoke Bash access

## `undo ssh-public-key`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`local-user`
- CLI 帮助：remove an SSH public key

## `undo user`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：remove local user

## `user`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter local user view
