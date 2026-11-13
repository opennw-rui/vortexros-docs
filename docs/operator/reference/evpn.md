# EVPN

[配置指南](../11-vxlan-evpn.md)

## `advertise l2vpn evpn`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：export VPN routes to the EVPN address family
- 合法语法：

  ```text
  advertise l2vpn evpn
  ```

## `esi`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure the Ethernet segment identifier
- 合法语法：

  ```text
  esi XXXX.XXXX.XXXX.XXXX.XXXX
  ```

## `evpn`

- 类别：配置命令
- 视图：`BD视图`
- 用途（设备帮助）：enter the EVPN view for this bridge-domain
- 合法语法：

  ```text
  evpn
  ```

## `evpn-overlay`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable EVPN as the VXLAN overlay control plane
- 合法语法：

  ```text
  evpn-overlay enable
  ```

## `l2vpn-family evpn`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the BGP EVPN address family
- 合法语法：

  ```text
  l2vpn-family evpn
  ```

## `undo advertise l2vpn evpn`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：export VPN routes to the EVPN address family
- 合法语法：

  ```text
  undo advertise l2vpn evpn
  ```

## `undo esi`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove the Ethernet segment identifier
- 合法语法：

  ```text
  undo esi
  ```

## `undo evpn-overlay`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable EVPN as the VXLAN overlay control plane
- 合法语法：

  ```text
  undo evpn-overlay enable
  ```

## `undo l2vpn-family evpn`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove the BGP EVPN address family
- 合法语法：

  ```text
  undo l2vpn-family evpn
  ```
