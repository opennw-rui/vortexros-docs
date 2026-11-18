# MPLS 与 LDP

[配置指南](../ldp.md)

## `display mpls forwarding-table`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the VPP MPLS forwarding table
- 合法语法：

  ```text
  display mpls forwarding-table
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display mpls interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display MPLS-enabled interfaces
- 合法语法：

  ```text
  display mpls interface
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display mpls ldp binding`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display LDP label bindings
- 合法语法：

  ```text
  display mpls ldp binding
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display mpls ldp interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display LDP interface state
- 合法语法：

  ```text
  display mpls ldp interface
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display mpls ldp peer`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display LDP peers
- 合法语法：

  ```text
  display mpls ldp peer
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display mpls lsp`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the Zebra MPLS forwarding table
- 合法语法：

  ```text
  display mpls lsp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `mpls`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：enable MPLS and enter the MPLS view；enable MPLS forwarding on the interface
- 合法语法：

  ```text
  mpls
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`system`**

此形式没有额外参数。

**适用视图：`interface`**

此形式没有额外参数。

## `mpls ldp`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：enable LDP discovery on the interface；enable MPLS LDP globally
- 合法语法：

  ```text
  mpls ldp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`system`**

此形式没有额外参数。

**适用视图：`interface`**

此形式没有额外参数。

## `mpls lsr-id`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure the MPLS label switching router ID
- 合法语法：

  ```text
  mpls lsr-id A.B.C.D
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `A.B.C.D` | MPLS LSR ID | 输入值 |

## `ttl propagate`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`mpls`
- CLI 帮助：use uniform MPLS TTL propagation
- 合法语法：

  ```text
  ttl propagate
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo mpls`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：disable MPLS forwarding on the interface；disable MPLS globally
- 合法语法：

  ```text
  undo mpls
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`system`**

此形式没有额外参数。

**适用视图：`interface`**

此形式没有额外参数。

## `undo mpls ldp`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：disable LDP discovery on the interface；disable MPLS LDP globally
- 合法语法：

  ```text
  undo mpls ldp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`system`**

此形式没有额外参数。

**适用视图：`interface`**

此形式没有额外参数。

## `undo mpls lsr-id`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：remove the MPLS label switching router ID
- 合法语法：

  ```text
  undo mpls lsr-id
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ttl propagate`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`mpls`
- CLI 帮助：use pipe mode and hide MPLS transit hops
- 合法语法：

  ```text
  undo ttl propagate
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
