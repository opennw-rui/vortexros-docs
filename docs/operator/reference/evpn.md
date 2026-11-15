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

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `esi`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure the Ethernet segment identifier
- 合法语法：

  ```text
  esi XXXX.XXXX.XXXX.XXXX.XXXX
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Eth-Trunk
接口类别：Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `XXXX.XXXX.XXXX.XXXX.XXXX` | Ethernet segment identifier | 输入值 |

## `evpn`

- 类别：配置命令
- 视图：`BD视图`
- 用途（设备帮助）：enter the EVPN view for this bridge-domain
- 合法语法：

  ```text
  evpn
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `evpn-overlay`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable EVPN as the VXLAN overlay control plane
- 合法语法：

  ```text
  evpn-overlay enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `enable` | enable the EVPN overlay | 关键字 |

## `l2vpn-family evpn`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：enter the BGP EVPN address family
- 合法语法：

  ```text
  l2vpn-family evpn
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo advertise l2vpn evpn`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：export VPN routes to the EVPN address family
- 合法语法：

  ```text
  undo advertise l2vpn evpn
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo esi`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove the Ethernet segment identifier
- 合法语法：

  ```text
  undo esi
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Eth-Trunk
接口类别：Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk

此形式没有额外参数。

## `undo evpn-overlay`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable EVPN as the VXLAN overlay control plane
- 合法语法：

  ```text
  undo evpn-overlay enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `enable` | disable the EVPN overlay | 关键字 |

## `undo l2vpn-family evpn`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：remove the BGP EVPN address family
- 合法语法：

  ```text
  undo l2vpn-family evpn
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
