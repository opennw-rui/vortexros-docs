# 策略通用命令

(cmd-apply-config)=
## `apply config`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：restart VPP and apply the saved config.cfg configuration
- 合法语法：

  ```text
  apply config
  ```

## `deny`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：deny matching packets
- 合法语法：

  ```text
  deny
  ```

## `permit`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：permit matching packets
- 合法语法：

  ```text
  permit
  ```

(cmd-rule)=
## `rule`

- 类别：配置命令
- 视图：`ACL视图`、`NAT策略视图`、`acl6`
- 用途（设备帮助）：configure an ACL rule；create/enter a NAT rule
- 合法语法：

  ```text
  rule ID
  ```
  ```text
  rule [ID] permit|deny PROTO [source ...] [destination ...] [protocol fields]
  ```

## `undo deny`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：undo deny
- 合法语法：

  ```text
  undo deny
  ```

## `undo permit`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：undo permit
- 合法语法：

  ```text
  undo permit
  ```

## `undo precedence`

- 类别：配置命令
- 视图：`流策略视图`
- 用途（设备帮助）：remove classifier precedence from the policy
- 合法语法：

  ```text
  undo precedence
  ```

(cmd-undo-rule)=
## `undo rule`

- 类别：配置命令
- 视图：`ACL视图`、`NAT策略视图`、`acl6`
- 用途（设备帮助）：delete a NAT rule；delete an ACL rule
- 合法语法：

  ```text
  undo rule ID
  ```
