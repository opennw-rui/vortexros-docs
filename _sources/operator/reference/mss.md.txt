# TCP MSS

[配置指南](../mss.md)

## `tcp mss`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clamp TCP SYN MSS on this L3 interface
- 合法语法：

  ```text
  tcp mss { clamp | MSS }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `clamp` | clamp SYN MSS to MTU-40 (IPv4) / MTU-60 (IPv6) | 关键字 |
| 命令后 | `MSS` | MSS value in bytes | 输入值 |

## `undo tcp mss`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove TCP MSS clamping from the interface
- 合法语法：

  ```text
  undo tcp mss
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。
