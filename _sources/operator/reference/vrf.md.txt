# VPN 实例

[配置指南](../vrf.md)

## `display ip vpn-instance`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VPN-instance information
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
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display interfaces bound to VPN instances
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
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display verbose VPN-instance information
- 合法语法：

  ```text
  display ip vpn-instance verbose
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `ip binding vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind the interface to a VPN instance
- 合法语法：

  ```text
  ip binding vpn-instance NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VRF` | VPN instance name | 输入值 |

## `ip vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a VPN instance and enter its view
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`
- CLI 帮助：enter the IPv4 address-family view
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`
- CLI 帮助：enter the IPv6 address-family view
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- CLI 帮助：configure the route distinguisher；set the EVPN route distinguisher
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：unbind the interface from a VPN instance
- 合法语法：

  ```text
  undo ip binding vpn-instance
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ip vpn-instance`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a VPN instance
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VPN实例视图`
- CLI 帮助：delete the IPv4 address-family
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VPN实例视图`
- CLI 帮助：delete the IPv6 address-family
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- CLI 帮助：clear the EVPN route distinguisher；delete the route distinguisher
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
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- CLI 帮助：configure an EVPN route target；delete a VPN target
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- CLI 帮助：configure a VPN target；configure an EVPN route target
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

### 读取结果

摘要中的 RD 按已启用的地址族分别列出。`display ip vpn-instance NAME` 选择单个实例；`display ip vpn-instance interface` 和 `display ip vpn-instance verbose` 显示全部实例，不附加实例名。

详细信息包括运行表号、接口归属、各族 RD/RT 及已配置的 EVPN VNI。共享 L3VNI50081 的双栈实例在两族下均显示 `EVPN VNI : 50081`；没有配置 L3VNI 时显示 `-`。该字段表示实例配置，实际 EVPN 路由及隧道状态继续使用 `display bgp evpn` 和 `display vxlan tunnel` 检查。
