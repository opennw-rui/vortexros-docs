# 管理会话

使用`display users`查看已登录用户、角色和会话状态：

~~~text
display users
~~~

需要断开某个受管账号的会话时执行：

~~~text
reset aaa user admin sessions
~~~

按提示确认后，该账号当前的受管SSH/CLI会话关闭。此操作不删除账号或密码；账号仍为活跃状态时可重新登录。需要禁止再次登录，在账号视图配置`undo active`并提交。

执行前确认目标账号，避免关闭自己的唯一管理连接。root救援入口不作为普通受管账号会话清理对象。

[账号管理](../aaa.md) · [命令参数](../reference/aaa.md)
