# BFD

[配置指南](../bfd.md)

## `bfd`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enable BFD or configure a static session
- 合法语法：

  ```text
  bfd [NAME bind peer-ip PEER ...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | Static BFD session name | 输入值、可选 |
| NAME | `bind` | Bind a static BFD session | 关键字 |
| bind | `peer-ip` | Set the IPv4 peer address | 关键字 |
| peer-ip | `X.X.X.X` | Peer IPv4 address | 输入值 |
| X.X.X.X / X:X::X | `source-ip IP-ADDRESS` | Set the source IP address；Source IP address | 可选、可组合 |
| X.X.X.X / X:X::X | `interface INTERFACE` | Bind the outgoing interface；Interface name | 可选、可组合 |
| X.X.X.X / X:X::X | `vpn-instance VPN` | Bind a VPN instance；VPN instance name | 可选、可组合 |
| X.X.X.X / X:X::X | `multi-hop` | Use a multi-hop BFD session | 可选、可组合 |
| bind | `peer-ipv6` | Set the IPv6 peer address | 关键字 |
| peer-ipv6 | `X:X::X` | Peer IPv6 address | 输入值 |

## `detect-multiplier`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：Detect multiplier
- 合法语法：

  ```text
  detect-multiplier INTEGER
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<3-50>` | Detect multiplier | 输入值 |

## `display bfd`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display BFD information
- 合法语法：

  ```text
  display bfd [configuration|session [all|NAME]|statistics]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `configuration` | BFD configuration | 可选 |
| 命令后 | `session` | BFD session information | 可选 |
| session | `all` | All BFD sessions | 可选 |
| session | `NAME` | Static BFD session name | 输入值、可选 |
| 命令后 | `statistics` | BFD session statistics | 可选 |

## `log-session-changes`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：log-session-changes
- 合法语法：

  ```text
  log-session-changes
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `min-rx-interval`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：Minimum receive interval in milliseconds
- 合法语法：

  ```text
  min-rx-interval INTEGER
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<100-1000>` | Minimum receive interval in milliseconds | 输入值 |

## `min-tx-interval`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：Minimum transmit interval in milliseconds
- 合法语法：

  ```text
  min-tx-interval INTEGER
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<100-1000>` | Minimum transmit interval in milliseconds | 输入值 |

## `reset service bfd`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart the managed bfd routing service
- 合法语法：

  ```text
  reset service bfd
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `undo bfd`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：delete a BFD session or disable BFD
- 合法语法：

  ```text
  undo bfd [NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | Static BFD session name | 输入值、可选 |

## `undo detect-multiplier`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：restore the default Detect multiplier
- 合法语法：

  ```text
  undo detect-multiplier
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo log-session-changes`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：undo log-session-changes
- 合法语法：

  ```text
  undo log-session-changes
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo min-rx-interval`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：restore the default Minimum receive interval in milliseconds
- 合法语法：

  ```text
  undo min-rx-interval
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo min-tx-interval`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：restore the default Minimum transmit interval in milliseconds
- 合法语法：

  ```text
  undo min-tx-interval
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
