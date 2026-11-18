# SNMP

[配置指南](../snmp.md)

## `display snmp-agent community`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display SNMPv2c read communities
- 合法语法：

  ```text
  display snmp-agent community
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Running（已接受配置）。

此形式没有额外参数。

## `display snmp-agent sys-info`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display SNMP system information
- 合法语法：

  ```text
  display snmp-agent sys-info
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Running（已接受配置）。

此形式没有额外参数。

## `display snmp-agent target-host`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display SNMP trap receivers
- 合法语法：

  ```text
  display snmp-agent target-host
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Running（已接受配置）。

此形式没有额外参数。

## `display snmp-agent usm-user`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display SNMPv3 users
- 合法语法：

  ```text
  display snmp-agent usm-user
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Running（已接受配置）。

此形式没有额外参数。

## `snmp-agent`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable the SNMP agent
- 合法语法：

  ```text
  snmp-agent
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `<cr>` | execute command | 可选 |

## `snmp-agent community read`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure an SNMPv2c read community
- 合法语法：

  ```text
  snmp-agent community read COMMUNITY
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `COMMUNITY` | read community | 输入值 |

## `snmp-agent protocol source-interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：bind the SNMP agent to an interface address
- 合法语法：

  ```text
  snmp-agent protocol source-interface { all-interface | IFNAME | vpn-instance VPN IFNAME }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `all-interface` | listen on all interfaces in public and VPN instances | 关键字 |
| 命令后 | `vpn-instance` | select a VPN instance | 关键字 |
| vpn-instance | `VRF` | VPN instance | 输入值 |
| VRF | `IF` | interface in the VPN instance | 输入值 |
| 命令后 | `IF` | public-network interface | 输入值 |

## `snmp-agent protocol source-status all-interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：listen on all IPv4 interfaces in public and VPN instances
- 合法语法：

  ```text
  snmp-agent protocol source-status all-interface
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `snmp-agent sys-info contact`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set SNMP system contact
- 合法语法：

  ```text
  snmp-agent sys-info contact TEXT
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | system contact | 输入值、后续文本 |

## `snmp-agent sys-info location`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set SNMP system location
- 合法语法：

  ```text
  snmp-agent sys-info location TEXT
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | system location | 输入值、后续文本 |

## `snmp-agent sys-info version v2c`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable SNMP v2c
- 合法语法：

  ```text
  snmp-agent sys-info version v2c
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `snmp-agent sys-info version v3`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable SNMP v3
- 合法语法：

  ```text
  snmp-agent sys-info version v3
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `snmp-agent target-host trap address udp-domain`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure an SNMP trap receiver
- 合法语法：

  ```text
  snmp-agent target-host trap address udp-domain ADDRESS udp-port PORT params securityname NAME { v2c | v3 }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PARAMETERS` | receiver, port and security parameters | 输入值、后续文本 |

## `snmp-agent trap enable standard`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable standard startup and interface traps
- 合法语法：

  ```text
  snmp-agent trap enable standard
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `snmp-agent trap source`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：select the trap source interface
- 合法语法：

  ```text
  snmp-agent trap source IFNAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | interface | 输入值 |

## `snmp-agent usm-user v3`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure an SNMPv3 authPriv user
- 合法语法：

  ```text
  snmp-agent usm-user v3 USER authentication-mode sha2-256 AUTH privacy-mode aes128 PRIV
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PARAMETERS` | user, authentication and privacy parameters | 输入值、后续文本 |

## `undo snmp-agent`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：remove all SNMP configuration and stop the agent
- 合法语法：

  ```text
  undo snmp-agent
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo snmp-agent community read`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an SNMPv2c read community
- 合法语法：

  ```text
  undo snmp-agent community read COMMUNITY
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `COMMUNITY` | read community | 输入值 |

## `undo snmp-agent protocol source-interface`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：remove the SNMP source interface
- 合法语法：

  ```text
  undo snmp-agent protocol source-interface
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo snmp-agent sys-info contact`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：clear SNMP system contact
- 合法语法：

  ```text
  undo snmp-agent sys-info contact
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo snmp-agent sys-info location`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：clear SNMP system location
- 合法语法：

  ```text
  undo snmp-agent sys-info location
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo snmp-agent sys-info version v2c`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable SNMP v2c
- 合法语法：

  ```text
  undo snmp-agent sys-info version v2c
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo snmp-agent sys-info version v3`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable SNMP v3
- 合法语法：

  ```text
  undo snmp-agent sys-info version v3
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo snmp-agent target-host trap address udp-domain`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete all trap targets at an address
- 合法语法：

  ```text
  undo snmp-agent target-host trap address udp-domain ADDRESS
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ADDRESS` | receiver address | 输入值 |

## `undo snmp-agent trap enable standard`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable standard traps
- 合法语法：

  ```text
  undo snmp-agent trap enable standard
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo snmp-agent trap source`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：remove the trap source interface
- 合法语法：

  ```text
  undo snmp-agent trap source
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo snmp-agent usm-user v3`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an SNMPv3 user
- 合法语法：

  ```text
  undo snmp-agent usm-user v3 USER
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `USER` | USM user | 输入值 |
