# WireGuard

[配置指南](../wireguard.md)

共用命令：[`allowd-ip`](tunnels.md#cmd-allowd-ip)、[`keepalive`](tunnels.md#cmd-keepalive)、[`peer`](tunnels.md#cmd-peer)、[`presharedkey`](tunnels.md#cmd-presharedkey)、[`publickey`](tunnels.md#cmd-publickey)、[`privatekey`](tunnels.md#cmd-privatekey)、[`source-port`](tunnels.md#cmd-source-port)。

## `display wireguard`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display WireGuard configuration and runtime
- 合法语法：

  ```text
  display wireguard { profile [NAME] | peer [PROFILE [PEER]] | interface [TUNNEL] }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `profile` | profiles | 关键字 |
| peer / profile | `WIREGUARD-PROFILE` | WireGuard profile name | 输入值、可选 |
| 命令后 | `peer` | peers | 关键字 |
| WIREGUARD-PROFILE | `WIREGUARD-PEER` | WireGuard peer name | 输入值、可选 |
| 命令后 | `interface` | interfaces | 关键字 |
| interface | `TUNNEL-IF` | Tunnel interface | 输入值、可选 |

## `undo wireguard profile`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a WireGuard profile
- 合法语法：

  ```text
  undo wireguard profile NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `WIREGUARD-PROFILE` | WireGuard profile name | 输入值 |

## `undo wireguard-profile`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind a WireGuard profile
- 合法语法：

  ```text
  undo wireguard-profile
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：隧道
接口类别：WireGuard 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `wireguard profile`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter a WireGuard profile
- 合法语法：

  ```text
  wireguard profile NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `WIREGUARD-PROFILE` | WireGuard profile name | 输入值 |

## `wireguard-profile`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind a WireGuard profile
- 合法语法：

  ```text
  wireguard-profile NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：隧道
接口类别：WireGuard 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `WIREGUARD-PROFILE` | WireGuard profile name | 输入值 |
