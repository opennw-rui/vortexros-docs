# MPLS LDP 与 L3VPN


## `display mpls forwarding-table`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the VPP MPLS forwarding table
- 合法语法：

  ```text
  display mpls forwarding-table
  ```

## `display mpls interface`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display MPLS-enabled interfaces
- 合法语法：

  ```text
  display mpls interface
  ```

## `display mpls ldp binding`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display LDP label bindings
- 合法语法：

  ```text
  display mpls ldp binding
  ```

## `display mpls ldp interface`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display LDP interface state
- 合法语法：

  ```text
  display mpls ldp interface
  ```

## `display mpls ldp peer`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display LDP peers
- 合法语法：

  ```text
  display mpls ldp peer
  ```

## `display mpls lsp`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the Zebra MPLS forwarding table
- 合法语法：

  ```text
  display mpls lsp
  ```

## `mpls`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：enable MPLS and enter the MPLS view；enable MPLS forwarding on the interface
- 合法语法：

  ```text
  mpls
  ```

## `mpls ldp`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：enable LDP discovery on the interface；enable MPLS LDP globally
- 合法语法：

  ```text
  mpls ldp
  ```

## `mpls lsr-id`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure the MPLS label switching router ID
- 合法语法：

  ```text
  mpls lsr-id A.B.C.D
  ```

## `ttl propagate`

- 类别：配置命令
- 视图：`mpls`
- 用途（设备帮助）：use uniform MPLS TTL propagation
- 合法语法：

  ```text
  ttl propagate
  ```

## `undo mpls`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：disable MPLS forwarding on the interface；disable MPLS globally
- 合法语法：

  ```text
  undo mpls
  ```

## `undo mpls ldp`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：disable LDP discovery on the interface；disable MPLS LDP globally
- 合法语法：

  ```text
  undo mpls ldp
  ```

## `undo mpls lsr-id`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：remove the MPLS label switching router ID
- 合法语法：

  ```text
  undo mpls lsr-id
  ```

## `undo ttl propagate`

- 类别：配置命令
- 视图：`mpls`
- 用途（设备帮助）：use pipe mode and hide MPLS transit hops
- 合法语法：

  ```text
  undo ttl propagate
  ```
