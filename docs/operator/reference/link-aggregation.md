# 链路聚合

[配置指南](../link-aggregation.md)

共用命令：[`mode`](interfaces.md#cmd-mode)。

## `display eth-trunk`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display aggregate interface state
- 合法语法：

  ```text
  display eth-trunk [INTEGER<0-63>]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-63>` | Eth-Trunk interface number | 输入值、可选 |

## `eth-trunk`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：join an aggregate interface
- 合法语法：

  ```text
  eth-trunk INTEGER<0-63>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet
接口类别：Ethernet（未选择二/三层）

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-63>` | Eth-Trunk interface number | 输入值 |

## `trunkport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：add physical member ports
- 合法语法：

  ```text
  trunkport INTERFACE [to INTERFACE]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Eth-Trunk
接口类别：Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PHYS-IF` | physical Ethernet interface | 输入值 |
| PHYS-IF | `to` | range link symbol | 可选 |
| to | `PHYS-IF` | last physical Ethernet interface | 输入值 |

## `undo eth-trunk`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：leave the aggregate interface
- 合法语法：

  ```text
  undo eth-trunk [INTEGER<0-63>]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet
接口类别：聚合成员口

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-63>` | Eth-Trunk interface number | 输入值、可选 |

## `undo trunkport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove physical member ports
- 合法语法：

  ```text
  undo trunkport INTERFACE [to INTERFACE]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Eth-Trunk
接口类别：Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PHYS-IF` | physical Ethernet interface | 输入值 |
| PHYS-IF | `to` | range link symbol | 可选 |
| to | `PHYS-IF` | last physical Ethernet interface | 输入值 |
