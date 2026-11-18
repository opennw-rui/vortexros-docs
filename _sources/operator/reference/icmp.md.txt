# ICMP 发送控制

[配置指南](../icmp-send.md)

## `display icmp interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display actual locally generated IPv4 ICMP send policy
- 合法语法：

  ```text
  display icmp interface IF | TYPE N
  ```

## `icmp`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure locally generated IPv4 ICMP suppression
- 合法语法：

  ```text
  icmp name NAME | type TYPE [code CODE]
  ```

## `undo icmp`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure locally generated IPv4 ICMP suppression
- 合法语法：

  ```text
  undo icmp name NAME | type TYPE [code CODE]
  ```

