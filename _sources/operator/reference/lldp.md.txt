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

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display lldp neighbor brief`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display LLDP neighbor brief information
- 合法语法：

  ```text
  display lldp neighbor brief
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display lldp neighbor interface`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display LLDP neighbor information on an interface
- 合法语法：

  ```text
  display lldp neighbor interface IF
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | interface name | 输入值 |

## `enable lldp`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable LLDP globally and on all physical interfaces
- 合法语法：

  ```text
  enable lldp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `lldp enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable LLDP on this physical interface
- 合法语法：

  ```text
  lldp enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、聚合成员口、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk

此形式没有额外参数。

## `undo enable lldp`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable LLDP globally
- 合法语法：

  ```text
  undo enable lldp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo lldp enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable LLDP on this physical interface
- 合法语法：

  ```text
  undo lldp enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet

此形式没有额外参数。
