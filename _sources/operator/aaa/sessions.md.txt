# 会话管理


开发服务器中，公钥账号 cli-active 以 system-admin 登录，实际进入 Bash 后 exit 返回 CLI。另一 root 终端的 display users 同时显示两个会话；执行 reset aaa user cli-active sessions 并确认后，返回 Closed 1 management sessions，受管 SSH 连接实际断开，root 救援会话保留。公钥登录不等于已验证需要密码的 sudo；密码与 sudo 的既有验收另行保留。



[角色与入口](../aaa.md) · [命令参考](../reference/aaa.md)
