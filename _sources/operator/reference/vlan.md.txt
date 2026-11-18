# VLAN

[配置指南](../vlan.md)

## `display vlan`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VLAN information
- 合法语法：

  ```text
  display vlan [VLAN-ID | summary]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `summary` | VLAN summary | 可选 |
| 命令后 | `ID` | VLAN ID | 输入值、可选 |

## `display vlan summary`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VLAN summary
- 合法语法：

  ```text
  display vlan summary
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `enable switch`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable the L2 switch instance
- 合法语法：

  ```text
  enable switch
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `port default vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the access port default VLAN
- 合法语法：

  ```text
  port default vlan VLAN-ID
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：二层 Ethernet、二层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VID` | VLAN ID 1-4095 | 输入值 |

## `port link-type`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the L2 port link type
- 合法语法：

  ```text
  port link-type { access | dot1q-tunnel | hybrid | trunk }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：二层 Ethernet、二层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `access` | Access port | 关键字 |
| 命令后 | `dot1q-tunnel` | QinQ port | 关键字 |
| 命令后 | `trunk` | Trunk port | 关键字 |

## `port trunk allow-pass vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：allow VLANs on a trunk port
- 合法语法：

  ```text
  port trunk allow-pass vlan { VLAN-LIST | all }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：二层 Ethernet、二层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `all` | all VLANs | 关键字 |
| 命令后 | `VLAN-ID` | VLAN ID | 输入值 |
| VLAN-ID | `to VLAN-ID` | VLAN range；VLAN ID | 可选、可重复 |
| VLAN-ID | `VLAN-ID` | VLAN ID | 输入值、可选、可重复 |

## `port trunk pvid vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the trunk native VLAN
- 合法语法：

  ```text
  port trunk pvid vlan VLAN-ID
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：二层 Ethernet、二层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VID` | VLAN ID | 输入值 |

## `portswitch`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：switch the aggregate to Layer 2 mode；switch the interface to L2 mode
- 合法语法：

  ```text
  portswitch
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Eth-Trunk
接口类别：Ethernet（未选择二/三层）、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk

此形式没有额外参数。

**适用视图：`interface`**
接口类别：Ethernet
接口类别：Ethernet（未选择二/三层）、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk

此形式没有额外参数。

## `switchport`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：switch the interface to L2 mode
- 合法语法：

  ```text
  switchport
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：Ethernet（未选择二/三层）

此形式没有额外参数。

## `undo enable switch`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable the L2 switch instance
- 合法语法：

  ```text
  undo enable switch
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo port default vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the access port default VLAN to 1
- 合法语法：

  ```text
  undo port default vlan
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：二层 Ethernet、二层 Eth-Trunk

此形式没有额外参数。

## `undo port link-type`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore portswitch-only L2 mode (access VLAN 1)
- 合法语法：

  ```text
  undo port link-type
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：二层 Ethernet、二层 Eth-Trunk

此形式没有额外参数。

## `undo port trunk allow-pass vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove allowed VLANs from a trunk port
- 合法语法：

  ```text
  undo port trunk allow-pass vlan { VLAN-LIST | all }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：二层 Ethernet、二层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `all` | all VLANs | 关键字 |
| 命令后 | `VLAN-ID` | VLAN ID | 输入值 |
| VLAN-ID | `to VLAN-ID` | VLAN range；VLAN ID | 可选、可重复 |
| VLAN-ID | `VLAN-ID` | VLAN ID | 输入值、可选、可重复 |

## `undo port trunk pvid vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the trunk native VLAN to 1
- 合法语法：

  ```text
  undo port trunk pvid vlan [VLAN-ID]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：二层 Ethernet、二层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VID` | VLAN ID | 输入值、可选 |

## `undo portswitch`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：return the aggregate to Layer 3 mode；return the interface to L3 mode
- 合法语法：

  ```text
  undo portswitch
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Eth-Trunk
接口类别：二层 Ethernet、二层 Eth-Trunk

此形式没有额外参数。

**适用视图：`interface`**
接口类别：Ethernet
接口类别：二层 Ethernet、二层 Eth-Trunk

此形式没有额外参数。

## `undo switchport`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：return the interface to L3 mode
- 合法语法：

  ```text
  undo switchport
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet、Eth-Trunk
接口类别：二层 Ethernet

此形式没有额外参数。

## `undo vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a VLAN
- 合法语法：

  ```text
  undo vlan VLAN-ID [to VLAN-ID]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ID` | VLAN ID | 输入值 |
| ID | `to` | end of range | 可选 |
| to | `ID` | end VLAN ID | 输入值 |

## `undo vlan batch`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete VLANs in a batch
- 合法语法：

  ```text
  undo vlan batch { VLAN-ID [to VLAN-ID] } *
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VLAN-ID` | VLAN ID | 输入值 |
| VLAN-ID | `to VLAN-ID` | VLAN range；VLAN ID | 可选、可重复 |
| VLAN-ID | `VLAN-ID` | VLAN ID | 输入值、可选、可重复 |

## `undo vlan-type`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove the sub-interface VLAN binding
- 合法语法：

  ```text
  undo vlan-type
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：子接口
接口类别：三层子接口
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a VLAN and enter VLAN view
- 合法语法：

  ```text
  vlan VLAN-ID [to VLAN-ID]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ID` | VLAN ID 1-4095 | 输入值 |
| ID | `to` | end of range | 可选 |
| to | `ID` | end VLAN ID | 输入值 |

## `vlan batch`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：create VLANs in a batch
- 合法语法：

  ```text
  vlan batch { VLAN-ID [to VLAN-ID] } *
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VLAN-ID` | VLAN ID | 输入值 |
| VLAN-ID | `to VLAN-ID` | VLAN range；VLAN ID | 可选、可重复 |
| VLAN-ID | `VLAN-ID` | VLAN ID | 输入值、可选、可重复 |

## `vlan-type dot1q`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind the sub-interface to a VLAN (dot1q)
- 合法语法：

  ```text
  vlan-type dot1q VLAN-ID [inner VLAN-ID]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：子接口
接口类别：三层子接口
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VID` | VLAN ID 1-4095 | 输入值 |
| VID | `inner` | QinQ inner VLAN | 可选 |
| inner | `VID` | inner VLAN ID | 输入值 |

## `port hybrid pvid vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set Hybrid PVID
- 合法语法：

  ```text
  port hybrid pvid vlan VLAN-ID
  ```


## `port hybrid tagged vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure Hybrid VLAN membership and egress tag mode
- 合法语法：

  ```text
  port hybrid tagged vlan VLAN-LIST
  ```


## `port hybrid untagged vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure Hybrid VLAN membership and egress tag mode
- 合法语法：

  ```text
  port hybrid untagged vlan VLAN-LIST
  ```


## `undo port hybrid pvid vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set Hybrid PVID
- 合法语法：

  ```text
  undo port hybrid pvid vlan
  ```


## `undo port hybrid tagged vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure Hybrid VLAN membership and egress tag mode
- 合法语法：

  ```text
  undo port hybrid tagged vlan VLAN-LIST
  ```


## `undo port hybrid untagged vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure Hybrid VLAN membership and egress tag mode
- 合法语法：

  ```text
  undo port hybrid untagged vlan VLAN-LIST
  ```
