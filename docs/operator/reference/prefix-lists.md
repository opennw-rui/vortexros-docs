# 前缀列表

[配置指南](../prefix-lists.md)

## `display ip ip-prefix`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IP prefix lists
- 合法语法：

  ```text
  display ip ip-prefix [NAME [verbose|first-match PREFIX]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP-PREFIX` | Prefix list name | 输入值、可选 |
| IP-PREFIX | `verbose` | Backend rule counters | 可选 |
| IP-PREFIX | `first-match` | First rule that matches a prefix | 可选 |
| first-match | `X.X.X.X/M` | Prefix to test | 输入值 |

## `display ip ipv6-prefix`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 prefix lists
- 合法语法：

  ```text
  display ip ipv6-prefix [NAME [verbose|first-match PREFIX]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IPV6-PREFIX` | Prefix list name | 输入值、可选 |
| IPV6-PREFIX | `verbose` | Backend rule counters | 可选 |
| IPV6-PREFIX | `first-match` | First rule that matches a prefix | 可选 |
| first-match | `X:X::X/M` | Prefix to test | 输入值 |

## `display ipv6 prefix`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 prefix-list information
- 合法语法：

  ```text
  display ipv6 prefix [NAME [verbose|first-match PREFIX]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IPV6-PREFIX` | Prefix list name | 输入值、可选 |
| IPV6-PREFIX | `verbose` | Backend rule counters | 可选 |
| IPV6-PREFIX | `first-match` | First rule that matches a prefix | 可选 |
| first-match | `X:X::X/M` | Prefix to test | 输入值 |

## `ip ip-prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：configure an IP prefix list entry
- 合法语法：

  ```text
  ip ip-prefix NAME [index SEQ] {permit|deny} IP MASK [greater-equal GE] [less-equal LE]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP-PREFIX` | Specify a prefix list name | 输入值 |
| IP-PREFIX | `index` | Set the sequence number of this entry for IP prefix-list | 可选 |
| index | `INTEGER<1-65535>` | sequence number | 输入值 |
| INTEGER<1-65535> / IP-PREFIX | `permit` | Specify a permit rule | 关键字 |
| deny / permit | `IP` | prefix address | 输入值 |
| IP | `MASK` | mask length or dotted mask | 输入值、可选 |
| IP / MASK | `greater-equal` | minimum prefix length | 可选、可组合 |
| greater-equal | `INTEGER<0-32>` | minimum prefix length | 输入值 |
| IP / MASK | `less-equal` | maximum prefix length | 可选、可组合 |
| less-equal | `INTEGER<0-32>` | maximum prefix length | 输入值 |
| INTEGER<1-65535> / IP-PREFIX | `deny` | Specify a deny rule | 关键字 |

## `ip ipv6-prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：configure an IPv6 prefix list entry
- 合法语法：

  ```text
  ip ipv6-prefix NAME [index SEQ] {permit|deny} IPV6 PREFIX-LENGTH [greater-equal GE] [less-equal LE]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IPV6-PREFIX` | Specify a prefix list name | 输入值 |
| IPV6-PREFIX | `index` | Set the sequence number of this entry for IP prefix-list | 可选 |
| index | `INTEGER<1-65535>` | sequence number | 输入值 |
| INTEGER<1-65535> / IPV6-PREFIX | `permit` | Specify a permit rule | 关键字 |
| deny / permit | `X:X::X` | IPv6 prefix address | 输入值 |
| X:X::X | `MASK` | mask length or dotted mask | 输入值、可选 |
| MASK / X:X::X | `greater-equal` | minimum prefix length | 可选、可组合 |
| greater-equal | `INTEGER<0-128>` | minimum prefix length | 输入值 |
| MASK / X:X::X | `less-equal` | maximum prefix length | 可选、可组合 |
| less-equal | `INTEGER<0-128>` | maximum prefix length | 输入值 |
| INTEGER<1-65535> / IPV6-PREFIX | `deny` | Specify a deny rule | 关键字 |

## `undo ip ip-prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an IP prefix list entry or list
- 合法语法：

  ```text
  undo ip ip-prefix NAME [index SEQ]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP-PREFIX` | Specify a prefix list name | 输入值 |
| IP-PREFIX | `index` | sequence | 可选 |
| index | `SEQ` | sequence | 输入值 |

## `undo ip ipv6-prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an IPv6 prefix list entry or list
- 合法语法：

  ```text
  undo ip ipv6-prefix NAME [index SEQ]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IPV6-PREFIX` | Specify an IPv6 prefix list name | 输入值 |
| IPV6-PREFIX | `index` | sequence | 可选 |
| index | `SEQ` | sequence | 输入值 |
