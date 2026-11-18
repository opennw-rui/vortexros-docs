# uRPF

[配置指南](../urpf.md)

## `display ipv6 urpf`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 URPF information
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
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：show per-interface uRPF mode
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
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure ip uRPF on the interface
- 合法语法：

  ```text
  ip urpf { loose | strict | disable }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `loose` | loose mode | 关键字 |
| 命令后 | `strict` | strict mode | 关键字 |
| 命令后 | `disable` | disable uRPF | 关键字 |

## `ipv6 urpf`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure ipv6 uRPF on the interface
- 合法语法：

  ```text
  ipv6 urpf { loose | strict | disable }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `loose` | loose mode | 关键字 |
| 命令后 | `strict` | strict mode | 关键字 |
| 命令后 | `disable` | disable uRPF | 关键字 |

## `undo ip urpf`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable ip uRPF on the interface
- 合法语法：

  ```text
  undo ip urpf
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ipv6 urpf`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable ipv6 uRPF on the interface
- 合法语法：

  ```text
  undo ipv6 urpf
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。
