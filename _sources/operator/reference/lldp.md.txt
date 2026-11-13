# LLDP

[配置指南](../lldp.md)

## `display lldp local`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display local LLDP information
- 合法语法：

  ```text
  display lldp local
  ```

## `display lldp neighbor brief`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display LLDP neighbor brief information
- 合法语法：

  ```text
  display lldp neighbor brief
  ```

## `display lldp neighbor interface`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display LLDP neighbor information on an interface
- 合法语法：

  ```text
  display lldp neighbor interface IF
  ```

## `enable lldp`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable LLDP globally and on all physical interfaces
- 合法语法：

  ```text
  enable lldp
  ```

## `lldp enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable LLDP on this physical interface
- 合法语法：

  ```text
  lldp enable
  ```

## `undo enable lldp`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable LLDP globally
- 合法语法：

  ```text
  undo enable lldp
  ```

## `undo lldp enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable LLDP on this physical interface
- 合法语法：

  ```text
  undo lldp enable
  ```
