# ACL

[配置指南](../acl.md)

共用命令：[`rule`](policy.md#cmd-rule)、[`undo rule`](policy.md#cmd-undo-rule)。

## `acl ipv6 name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an IPv6 ACL and enter ACL view
- 合法语法：

  ```text
  acl ipv6 name NAME [advance]
  ```

## `acl name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an IPv4 ACL and enter ACL view
- 合法语法：

  ```text
  acl name NAME [advance]
  ```

## `display acl`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：list ACLs and their rules (name-based)
- 合法语法：

  ```text
  display acl [ipv6] [all | name NAME]
  ```

## `traffic-filter`

在指定方向挂载 ACL。同地址族未匹配流量默认丢弃。见[ACL 案例](../../examples/acl.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：apply an ACL to interface traffic
- 合法语法：

  ```text
  traffic-filter { inbound | outbound } acl NAME
  ```

## `undo acl ipv6 name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an ACL
- 合法语法：

  ```text
  undo acl ipv6 name NAME
  ```

## `undo acl name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an ACL
- 合法语法：

  ```text
  undo acl name NAME
  ```

## `undo traffic-filter`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove an ACL from the interface
- 合法语法：

  ```text
  undo traffic-filter { inbound | outbound }
  ```
