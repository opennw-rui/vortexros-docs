# 公钥与启停


仅需要查询权限的账号可以只配置 Ed25519 公钥，不设置密码。以下 KEY 替换成用户自己的公钥内容，私钥留在客户端：

```text
system-view
user auditread
 ssh-public-key laptop ssh-ed25519 KEY
 quit
commit
save
```

默认角色为 network-operator，默认 active，配置中省略这两个默认项。使用客户端私钥连接后，以 `display users` 核对用户名、角色和 Read-only；不要用 root 的登录结果代替受管账号验证。

停用：

```text
system-view
user auditread
 undo active
 quit
commit
```

在本轮开发服务器 QEMU 的真实 OpenSSH 验证中，未设置密码的公钥账号成功进入 CLI，`display users` 显示 network-operator / Read-only。提交 `undo active` 后，原 SSH 会话由服务端关闭；再次只使用该公钥连接，返回 `Permission denied (publickey,password)`。配置中显示 `undo active`，不会显示默认的 `active`。

恢复时进入相同用户视图执行 `active`、提交并保存。撤销单把公钥使用 `undo ssh-public-key laptop`；如果该账号不再使用，执行 `undo user auditread` 并提交、保存。不要撤销自己唯一的管理凭据。



[角色与入口](../aaa.md) · [命令参考](../reference/aaa.md)
