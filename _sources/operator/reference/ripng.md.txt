# RIPng

[配置指南](../ripng.md)

共用命令：[`network`](dynamic-routing.md#cmd-network)、[`import-route`](dynamic-routing.md#cmd-import-route)。

## `aggregate-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`
- CLI 帮助：advertise a RIPng aggregate
- 合法语法：

  ```text
  aggregate-address X:X::X/M
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X/M` | IPv6 aggregate prefix | 输入值 |

## `display ripng`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display RIPng information
- 合法语法：

  ```text
  display ripng [process-id] [database|route|interface|statistics]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值、可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `database` | Database information | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `interface` | Interface information | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `route` | Route information | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `statistics` | Statistical information | 可选 |
| 命令后 | `vpn-instance` | VPN instance | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |

## `offset-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`
- CLI 帮助：adjust RIPng route metrics selected by an IPv6 ACL
- 合法语法：

  ```text
  offset-list ACL {in|out} INTEGER<0-16> [interface IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ACL` | IPv6 ACL name | 输入值 |
| ACL | `in` | Incoming updates | 关键字 |
| in / out | `INTEGER<0-16>` | Metric offset | 输入值 |
| INTEGER<0-16> | `interface` | Limit to one RIPng interface | 可选 |
| interface | `INTERFACE` | Interface name | 输入值 |
| ACL | `out` | Outgoing updates | 关键字 |

## `ripng`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a RIP process and enter process view
- 合法语法：

  ```text
  ripng INTEGER<1-65535> [vpn-instance NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值 |
| INTEGER<1-65535> | `vpn-instance` | VPN instance | 可选、可组合 |
| vpn-instance | `VPN` | VPN instance name | 输入值 |

## `undo aggregate-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`
- CLI 帮助：withdraw a RIPng aggregate
- 合法语法：

  ```text
  undo aggregate-address X:X::X/M
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X/M` | IPv6 aggregate prefix | 输入值 |

## `undo offset-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`
- CLI 帮助：remove a RIPng metric offset
- 合法语法：

  ```text
  undo offset-list {in|out} [interface IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `in` | Incoming updates | 关键字 |
| in / out | `interface` | Limit to one RIPng interface | 可选 |
| interface | `INTERFACE` | Interface name | 输入值 |
| 命令后 | `out` | Outgoing updates | 关键字 |

## `undo ripng`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a RIP process
- 合法语法：

  ```text
  undo ripng INTEGER<1-65535> [vpn-instance NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ARGS` | process id and optional vpn-instance | 输入值、后续文本 |
