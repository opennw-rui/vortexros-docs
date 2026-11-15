# uRPF

[配置指南](../urpf.md)

## `display ipv6 urpf`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 URPF information
- 合法语法：

  ```text
  display ipv6 urpf
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display urpf`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：show per-interface uRPF mode
- 合法语法：

  ```text
  display urpf
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `ip urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure ip uRPF on the interface
- 合法语法：

  ```text
  ip urpf { loose | strict | disable }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `loose` | loose mode | 关键字 |
| 命令后 | `strict` | strict mode | 关键字 |
| 命令后 | `disable` | disable uRPF | 关键字 |

## `ipv6 urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure ipv6 uRPF on the interface
- 合法语法：

  ```text
  ipv6 urpf { loose | strict | disable }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `loose` | loose mode | 关键字 |
| 命令后 | `strict` | strict mode | 关键字 |
| 命令后 | `disable` | disable uRPF | 关键字 |

## `undo ip urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ip uRPF on the interface
- 合法语法：

  ```text
  undo ip urpf
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo ipv6 urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ipv6 uRPF on the interface
- 合法语法：

  ```text
  undo ipv6 urpf
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。
