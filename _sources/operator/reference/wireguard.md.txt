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

## `undo wireguard profile`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a WireGuard profile
- 合法语法：

  ```text
  undo wireguard profile NAME
  ```

## `undo wireguard-profile`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind a WireGuard profile
- 合法语法：

  ```text
  undo wireguard-profile
  ```

## `wireguard profile`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter a WireGuard profile
- 合法语法：

  ```text
  wireguard profile NAME
  ```

## `wireguard-profile`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind a WireGuard profile
- 合法语法：

  ```text
  wireguard-profile NAME
  ```
