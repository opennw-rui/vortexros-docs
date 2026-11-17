# VXLAN

[配置指南](../vxlan.md)

## `display vxlan statistics`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VXLAN tunnel traffic statistics
- 合法语法：

  ```text
  display vxlan statistics source IP peer IP [vni VNI]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `source` | local VTEP | 关键字 |
| source | `SRC` | source IP | 输入值 |
| SRC | `peer` | remote VTEP | 关键字 |
| peer | `DST` | peer IP | 输入值 |
| DST | `vni` | filter by VNI | 可选 |
| vni | `VNI` | VXLAN network identifier | 输入值 |

## `display vxlan tunnel`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display static VXLAN tunnels (from NVE peer-list)
- 合法语法：

  ```text
  display vxlan tunnel [ID]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ID` | tunnel id (sw_if_index) | 输入值、可选 |

## `undo vni`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove a VNI or selected head-end peers
- 合法语法：

  ```text
  undo vni VNI [head-end peer-list PEER]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：NVE
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VNI` | VXLAN VNI | 输入值 |
| VNI | `head-end` | head-end replication | 可选 |
| head-end | `peer-list` | remote VTEP | 关键字 |
| peer-list | `PEER` | Remote VTEP IP address | 输入值 |
| peer-list | `protocol` | dynamic peer discovery | 关键字 |
| protocol | `bgp` | BGP EVPN | 关键字 |

## `undo vxlan anycast-gateway enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the distributed VXLAN anycast gateway
- 合法语法：

  ```text
  undo vxlan anycast-gateway enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：vbdif
接口类别：Vbdif

此形式没有额外参数。

## `undo vxlan vni`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BD视图`、`VPN实例视图`
- CLI 帮助：clear the VXLAN VNI；remove the L3VNI from the VPN instance
- 合法语法：

  ```text
  undo vxlan vni
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`bridge-domain`**

此形式没有额外参数。

**适用视图：`vpn-instance`**

此形式没有额外参数。

## `vni`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：add a head-end peer for a VNI
- 合法语法：

  ```text
  vni VNI head-end peer-list PEER
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：NVE
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VNI` | VXLAN VNI | 输入值 |
| VNI | `head-end` | head-end replication | 关键字 |
| head-end | `peer-list` | remote VTEP list | 关键字 |
| peer-list | `PEER` | Remote VTEP IP address | 输入值 |
| peer-list | `protocol` | dynamic peer discovery | 关键字 |
| protocol | `bgp` | BGP EVPN | 关键字 |

## `vxlan anycast-gateway enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable the distributed VXLAN anycast gateway
- 合法语法：

  ```text
  vxlan anycast-gateway enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：vbdif
接口类别：Vbdif

此形式没有额外参数。

## `vxlan vni`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BD视图`、`VPN实例视图`
- CLI 帮助：bind an L3VNI to the VPN instance；set the VXLAN VNI for this bridge-domain
- 合法语法：

  ```text
  vxlan vni VNI
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`bridge-domain`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VNI` | VXLAN network identifier | 输入值 |

**适用视图：`vpn-instance`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-16777215>` | VXLAN network identifier | 输入值 |
