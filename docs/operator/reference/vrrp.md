# VRRP

[配置指南](../vrrp.md)

## `display vrrp`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv4 VRRPv3 information
- 合法语法：

  ```text
  display vrrp [brief|interface INTERFACE|statistics|protocol-information|VRID]
  ```

## `display vrrp6`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 VRRPv3 information
- 合法语法：

  ```text
  display vrrp6 [brief|interface INTERFACE|statistics|protocol-information|VRID]
  ```

## `undo vrrp vrid`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete or reset an IPv4 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp vrid INTEGER<1-255> [...]
  ```

## `undo vrrp6 vrid`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete or reset an IPv6 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp6 vrid INTEGER<1-255> [...]
  ```

## `vrrp vrid`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv4 VRRPv3 group
- 合法语法：

  ```text
  vrrp vrid INTEGER<1-255> ...
  ```

## `vrrp6 vrid`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv6 VRRPv3 group
- 合法语法：

  ```text
  vrrp6 vrid INTEGER<1-255> ...
  ```
