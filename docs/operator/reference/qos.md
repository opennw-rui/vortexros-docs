# QoS

[配置指南](../qos.md)

## `qos lr`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VLAN视图`、`接口视图`
- CLI 帮助：configure interface or VLAN rate limit (2-rate 3-color)
- 合法语法：

  ```text
  qos lr { inbound | outbound } cir CIR [pir PIR] [cbs CBS] [pbs PBS] [green|yellow|red pass|discard]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif、聚合成员口

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `inbound` | inbound | 关键字 |
| inbound / outbound | `cir` | committed information rate | 关键字 |
| cir | `CIR` | CIR value (default kbps) | 输入值 |
| CIR | `kbps` | kilobits per second | 可选、可组合 |
| CIR | `mbps` | megabits per second | 可选、可组合 |
| CIR | `pir PIR` | peak information rate；PIR value | 可选、可组合 |
| CIR | `cbs CBS` | committed burst size (bytes)；CBS in bytes | 可选、可组合 |
| CIR | `pbs PBS` | peak burst size (bytes)；PBS in bytes | 可选、可组合 |
| CIR | `green` | green packets | 可选、可组合 |
| green / red / yellow | `pass` | forward packets | 关键字 |
| green / red / yellow | `discard` | drop packets | 关键字 |
| green / red / yellow | `remark` | remark a color's DSCP | 关键字 |
| remark | `dscp` | DSCP value | 关键字 |
| dscp | `cs0` | CS0 / default (0) | 关键字 |
| dscp | `cs1` | CS1 (8) | 关键字 |
| dscp | `af11` | AF11 (10) | 关键字 |
| dscp | `af12` | AF12 (12) | 关键字 |
| dscp | `af13` | AF13 (14) | 关键字 |
| dscp | `cs2` | CS2 (16) | 关键字 |
| dscp | `af21` | AF21 (18) | 关键字 |
| dscp | `af22` | AF22 (20) | 关键字 |
| dscp | `af23` | AF23 (22) | 关键字 |
| dscp | `cs3` | CS3 (24) | 关键字 |
| dscp | `af31` | AF31 (26) | 关键字 |
| dscp | `af32` | AF32 (28) | 关键字 |
| dscp | `af33` | AF33 (30) | 关键字 |
| dscp | `cs4` | CS4 (32) | 关键字 |
| dscp | `af41` | AF41 (34) | 关键字 |
| dscp | `af42` | AF42 (36) | 关键字 |
| dscp | `af43` | AF43 (38) | 关键字 |
| dscp | `cs5` | CS5 (40) | 关键字 |
| dscp | `ef` | EF (46) | 关键字 |
| dscp | `cs6` | CS6 (48) | 关键字 |
| dscp | `cs7` | CS7 (56) | 关键字 |
| dscp | `DSCP` | DSCP value 0-63 | 输入值 |
| CIR | `yellow` | yellow packets | 可选、可组合 |
| CIR | `red` | red packets | 可选、可组合 |
| 命令后 | `outbound` | outbound | 关键字 |

## `undo qos lr`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VLAN视图`、`接口视图`
- CLI 帮助：remove interface or VLAN rate limit
- 合法语法：

  ```text
  undo qos lr { inbound | outbound }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif、聚合成员口

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `inbound` | inbound | 关键字 |
| 命令后 | `outbound` | outbound | 关键字 |
