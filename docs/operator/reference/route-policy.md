# 路由策略

[配置指南](../route-policy.md)

## `apply as-path`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：prepend AS numbers to the BGP AS path
- 合法语法：

  ```text
  apply as-path ASNUM [ASNUM ...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ASNUM` | one or more AS numbers | 输入值、后续文本 |

## `apply community`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set BGP community values
- 合法语法：

  ```text
  apply community VALUE [VALUE ...] [additive]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | community values and optional additive | 输入值、后续文本 |

## `apply cost`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set route metric
- 合法语法：

  ```text
  apply cost VALUE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | route metric | 输入值 |

## `apply ip-address next-hop`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set an IPv4 next hop
- 合法语法：

  ```text
  apply ip-address next-hop X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 next hop | 输入值 |

## `apply ipv6 next-hop`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set an IPv6 next hop
- 合法语法：

  ```text
  apply ipv6 next-hop X:X::X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X` | IPv6 next hop | 输入值 |

## `apply large-community`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set BGP large-community values
- 合法语法：

  ```text
  apply large-community VALUE [VALUE ...] [additive]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | large-community values and optional additive | 输入值、后续文本 |

## `apply local-preference`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set local preference
- 合法语法：

  ```text
  apply local-preference VALUE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | local preference | 输入值 |

## `apply origin`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set the BGP origin attribute
- 合法语法：

  ```text
  apply origin {igp|egp|incomplete}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `igp` | IGP origin | 关键字 |
| 命令后 | `egp` | EGP origin | 关键字 |
| 命令后 | `incomplete` | incomplete origin | 关键字 |

## `apply tag`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set route tag
- 合法语法：

  ```text
  apply tag INTEGER<0-4294967295>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-4294967295>` | route tag | 输入值 |

## `continue node`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：continue evaluation at a later route-policy node
- 合法语法：

  ```text
  continue node INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | target node | 输入值 |

## `display route-policy`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display route policies
- 合法语法：

  ```text
  display route-policy [NAME [verbose]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ROUTE-POLICY` | Name of the route policy | 输入值、可选 |
| ROUTE-POLICY | `verbose` | Backend policy counters | 可选 |

## `if-match cost`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set route metric
- 合法语法：

  ```text
  if-match cost INTEGER<0-4294967295>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-4294967295>` | route metric | 输入值 |

## `if-match ip-prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：match an IP prefix list
- 合法语法：

  ```text
  if-match ip-prefix NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP-PREFIX` | Specify a prefix list name | 输入值 |

## `if-match ipv6 address prefix-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：match an IPv6 prefix list
- 合法语法：

  ```text
  if-match ipv6 address prefix-list NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IPV6-PREFIX` | Specify an IPv6 prefix list name | 输入值 |

## `if-match protocol`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：match the route source protocol
- 合法语法：

  ```text
  if-match protocol {direct|static|ospf|ospfv3|isis|rip|ripng|bgp}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | DIRECT routes | 关键字 |
| 命令后 | `static` | STATIC routes | 关键字 |
| 命令后 | `ospf` | OSPF routes | 关键字 |
| 命令后 | `ospfv3` | OSPFV3 routes | 关键字 |
| 命令后 | `isis` | ISIS routes | 关键字 |
| 命令后 | `rip` | RIP routes | 关键字 |
| 命令后 | `ripng` | RIPNG routes | 关键字 |
| 命令后 | `bgp` | BGP routes | 关键字 |

## `if-match tag`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set route tag
- 合法语法：

  ```text
  if-match tag INTEGER<0-4294967295>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-4294967295>` | route tag | 输入值 |

## `route-policy`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a route policy node and enter its view
- 合法语法：

  ```text
  route-policy NAME {permit|deny} node INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ROUTE-POLICY` | Name of the route policy | 输入值 |
| ROUTE-POLICY | `permit` | permit node | 关键字 |
| deny / permit | `node` | Specify a route-policy node | 关键字 |
| node | `INTEGER<1-65535>` | Node number | 输入值 |
| ROUTE-POLICY | `deny` | deny node | 关键字 |

## `undo apply as-path`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the AS-path prepend action
- 合法语法：

  ```text
  undo apply as-path
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo apply community`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the BGP community action
- 合法语法：

  ```text
  undo apply community
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo apply cost`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：restore default route metric
- 合法语法：

  ```text
  undo apply cost
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo apply ip-address next-hop`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the IPv4 next-hop action
- 合法语法：

  ```text
  undo apply ip-address next-hop
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo apply ipv6 next-hop`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the IPv6 next-hop action
- 合法语法：

  ```text
  undo apply ipv6 next-hop
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo apply large-community`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the BGP large-community action
- 合法语法：

  ```text
  undo apply large-community
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo apply local-preference`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：restore default local preference
- 合法语法：

  ```text
  undo apply local-preference
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo apply origin`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the BGP origin action
- 合法语法：

  ```text
  undo apply origin
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo apply tag`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove route tag
- 合法语法：

  ```text
  undo apply tag
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo continue`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：stop evaluation after this route-policy node
- 合法语法：

  ```text
  undo continue
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo if-match cost`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove route metric
- 合法语法：

  ```text
  undo if-match cost
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo if-match ip-prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove an IP prefix match
- 合法语法：

  ```text
  undo if-match ip-prefix NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP-PREFIX` | Specify a prefix list name | 输入值 |

## `undo if-match ipv6 address prefix-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove an IPv6 prefix match
- 合法语法：

  ```text
  undo if-match ipv6 address prefix-list NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IPV6-PREFIX` | Specify an IPv6 prefix list name | 输入值 |

## `undo if-match protocol`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the route source protocol match
- 合法语法：

  ```text
  undo if-match protocol
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo if-match tag`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove route tag
- 合法语法：

  ```text
  undo if-match tag
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo route-policy`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a route policy
- 合法语法：

  ```text
  undo route-policy NAME [permit|deny node INTEGER<1-65535>]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ROUTE-POLICY` | Name of the route policy | 输入值 |
| ROUTE-POLICY | `permit` | delete a permit node | 可选 |
| deny / permit | `node` | Specify a route-policy node | 关键字 |
| node | `INTEGER<1-65535>` | Node number | 输入值 |
| ROUTE-POLICY | `deny` | delete a deny node | 可选 |
