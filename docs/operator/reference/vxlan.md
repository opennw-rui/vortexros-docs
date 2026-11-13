# VXLAN

[配置指南](../vxlan.md)

## `display vxlan statistics`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VXLAN tunnel traffic statistics
- 合法语法：

  ```text
  display vxlan statistics source IP peer IP [vni VNI]
  ```

## `display vxlan tunnel`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display static VXLAN tunnels (from NVE peer-list)
- 合法语法：

  ```text
  display vxlan tunnel [ID]
  ```

## `undo vni`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove head-end peer(s) for a VNI
- 合法语法：

  ```text
  undo vni VNI [head-end peer-list PEER]
  ```

## `undo vxlan anycast-gateway enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable the distributed VXLAN anycast gateway
- 合法语法：

  ```text
  undo vxlan anycast-gateway enable
  ```

## `undo vxlan vni`

- 类别：配置命令
- 视图：`BD视图`、`VPN实例视图`
- 用途（设备帮助）：clear the VXLAN VNI；remove the L3VNI from the VPN instance
- 合法语法：

  ```text
  undo vxlan vni
  ```

## `vni`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：add a head-end peer for a VNI
- 合法语法：

  ```text
  vni VNI head-end peer-list PEER
  ```

## `vxlan anycast-gateway enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable the distributed VXLAN anycast gateway
- 合法语法：

  ```text
  vxlan anycast-gateway enable
  ```

## `vxlan vni`

- 类别：配置命令
- 视图：`BD视图`、`VPN实例视图`
- 用途（设备帮助）：bind an L3VNI to the VPN instance；set the VXLAN VNI for this bridge-domain
- 合法语法：

  ```text
  vxlan vni VNI
  ```
