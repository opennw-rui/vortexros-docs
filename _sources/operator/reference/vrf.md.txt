# VPN 实例

[配置指南](../vrf.md)

## `display ip vpn-instance`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VPN-instance information
- 合法语法：

  ```text
  display ip vpn-instance [NAME | interface | verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VRF` | VPN instance name | 输入值、可选 |
| 命令后 | `interface` | show interface binding | 可选 |
| 命令后 | `verbose` | show verbose information | 可选 |

## `display ip vpn-instance interface`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display interfaces bound to VPN instances
- 合法语法：

  ```text
  display ip vpn-instance interface
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display ip vpn-instance verbose`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display verbose VPN-instance information
- 合法语法：

  ```text
  display ip vpn-instance verbose
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `ip binding vpn-instance`

把接口划入指定 VPN 的路由域。调整前规划该实例的地址、网关和路由，调整后从同一 VPN 验证连通性。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind the interface to a VPN instance
- 合法语法：

  ```text
  ip binding vpn-instance NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VRF` | VPN instance name | 输入值 |

## `ip vpn-instance`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a VPN instance and enter its view
- 合法语法：

  ```text
  ip vpn-instance NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VRF` | VPN instance name | 输入值 |

## `ipv4-family`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`
- 用途（设备帮助）：enter the IPv4 address-family view
- 合法语法：

  ```text
  ipv4-family
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `ipv6-family`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`
- 用途（设备帮助）：enter the IPv6 address-family view
- 合法语法：

  ```text
  ipv6-family
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `route-distinguisher`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：configure the route distinguisher；set the EVPN route distinguisher
- 合法语法：

  ```text
  route-distinguisher RD
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`bridge-domain-evpn`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `RD` | route distinguisher | 输入值 |

**适用视图：`vpn-instance, vpn-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `RD` | route distinguisher (A:B) | 输入值 |

## `undo ip binding vpn-instance`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind the interface from a VPN instance
- 合法语法：

  ```text
  undo ip binding vpn-instance
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo ip vpn-instance`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a VPN instance
- 合法语法：

  ```text
  undo ip vpn-instance NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VRF` | VPN instance name | 输入值 |

## `undo ipv4-family`

- 类别：配置命令
- 视图：`VPN实例视图`
- 用途（设备帮助）：delete the IPv4 address-family
- 合法语法：

  ```text
  undo ipv4-family
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6-family`

- 类别：配置命令
- 视图：`VPN实例视图`
- 用途（设备帮助）：delete the IPv6 address-family
- 合法语法：

  ```text
  undo ipv6-family
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo route-distinguisher`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：clear the EVPN route distinguisher；delete the route distinguisher
- 合法语法：

  ```text
  undo route-distinguisher
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`bridge-domain-evpn`**

此形式没有额外参数。

**适用视图：`vpn-instance, vpn-family`**

此形式没有额外参数。

## `undo vpn-target`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：configure an EVPN route target；delete a VPN target
- 合法语法：

  ```text
  undo vpn-target RT [ export-extcommunity | import-extcommunity | both ]
  ```
  ```text
  undo vpn-target RT { export-extcommunity | import-extcommunity }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`bridge-domain-evpn`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `RT` | route target | 输入值 |
| RT | `export-extcommunity` | export route target | 关键字 |
| RT | `import-extcommunity` | import route target | 关键字 |

**适用视图：`vpn-instance, vpn-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `RT` | VPN target (A:B) | 输入值 |
| RT | `export-extcommunity` | export route target | 可选 |
| RT | `import-extcommunity` | import route target | 可选 |
| RT | `both` | both import and export | 可选 |

## `vpn-target`

- 类别：配置命令
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- 用途（设备帮助）：configure a VPN target；configure an EVPN route target
- 合法语法：

  ```text
  vpn-target RT { export-extcommunity | import-extcommunity | both }
  ```
  ```text
  vpn-target RT { export-extcommunity | import-extcommunity }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`bridge-domain-evpn`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `RT` | route target | 输入值 |
| RT | `export-extcommunity` | export route target | 关键字 |
| RT | `import-extcommunity` | import route target | 关键字 |

**适用视图：`vpn-instance, vpn-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `RT` | VPN target (A:B) | 输入值 |
| RT | `export-extcommunity` | export route target | 关键字 |
| RT | `import-extcommunity` | import route target | 关键字 |
| RT | `both` | both import and export | 关键字 |
