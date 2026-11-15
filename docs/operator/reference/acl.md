# ACL

[配置指南](../acl.md)

共用命令：[`rule`](policy.md#cmd-rule)、[`undo rule`](policy.md#cmd-undo-rule)。

## `acl ipv6 name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an IPv6 ACL and enter ACL view
- 合法语法：

  ```text
  acl ipv6 name NAME [advance]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ACL` | Name of ACL | 输入值 |
| ACL | `advance` | advanced ACL | 可选 |
| ACL | `advanced` | legacy advanced ACL spelling | 可选 |

## `acl name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an IPv4 ACL and enter ACL view
- 合法语法：

  ```text
  acl name NAME [advance]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ACL` | Name of ACL | 输入值 |
| ACL | `advance` | advanced ACL | 可选 |
| ACL | `advanced` | legacy advanced ACL spelling | 可选 |

## `display acl`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：list ACLs and their rules (name-based)
- 合法语法：

  ```text
  display acl [ipv6] [all | name NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ipv6` | display IPv6 ACLs | 可选 |
| ipv6 | `all` | all IPv6 ACLs | 可选 |
| ipv6 / 命令后 | `name` | ACL name keyword | 可选 |
| name | `ACL` | ACL name | 输入值 |
| 命令后 | `all` | all ACLs | 可选 |

## `traffic-filter`

在指定方向挂载 ACL。同地址族未匹配流量默认丢弃。见[ACL 案例](../../examples/acl.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：apply an ACL to interface traffic
- 合法语法：

  ```text
  traffic-filter { inbound | outbound } acl NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif, interface/ethernet-aggregate-member

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `inbound` | inbound | 关键字 |
| inbound / outbound | `acl` | ACL | 关键字 |
| acl | `ACL` | ACL name | 输入值 |
| 命令后 | `outbound` | outbound | 关键字 |

## `undo acl ipv6 name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an ACL
- 合法语法：

  ```text
  undo acl ipv6 name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ACL` | ACL name | 输入值 |

## `undo acl name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an ACL
- 合法语法：

  ```text
  undo acl name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ACL` | ACL name | 输入值 |

## `undo traffic-filter`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove an ACL from the interface
- 合法语法：

  ```text
  undo traffic-filter { inbound | outbound }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif, interface/ethernet-aggregate-member

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `inbound` | inbound | 关键字 |
| 命令后 | `outbound` | outbound | 关键字 |
