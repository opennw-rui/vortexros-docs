# OSPFv3

[配置指南](../ospfv3.md)

共用命令：[`abr-summary`](dynamic-routing.md#cmd-abr-summary)、[`area`](dynamic-routing.md#cmd-area)、[`import-route`](dynamic-routing.md#cmd-import-route)、[`router-id`](dynamic-routing.md#cmd-router-id)。

## `display ospfv3`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display OSPFv3 information
- 合法语法：

  ```text
  display ospfv3 [process-id|vpn-instance NAME] [brief|peer|interface|lsdb|routing]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值、可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `brief` | brief OSPFv3 process information | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `peer` | OSPFv3 neighbors | 可选 |
| peer | `brief` | brief neighbor information | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `interface` | OSPFv3 interfaces | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `lsdb` | OSPFv3 link-state database | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `routing` | OSPFv3 routing table | 可选 |
| 命令后 | `vpn-instance` | VPN instance | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |

## `ospfv3`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：create an OSPFv3 process and enter its view；enable OSPFv3 on an interface
- 合法语法：

  ```text
  ospfv3 INTEGER<1-65535> [router-id X.X.X.X] [vpn-instance NAME]
  ```
  ```text
  ospfv3 INTEGER<1-65535> area X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`system`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPFv3 process ID | 输入值 |
| INTEGER<1-65535> | `router-id` | OSPF private router ID value | 可选、可组合 |
| router-id | `X.X.X.X` | OSPF Private router ID value | 输入值 |
| INTEGER<1-65535> | `vpn-instance` | VPN instance name | 可选、可组合 |
| vpn-instance | `VPN` | VPN instance name | 输入值 |

**适用视图：`interface`**
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPFv3 process ID | 输入值 |
| INTEGER<1-65535> | `area` | OSPFv3 area | 关键字 |
| area | `X.X.X.X` | area ID | 输入值 |

## `ospfv3 bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure OSPFV3 BFD timers
- 合法语法：

  ```text
  ospfv3 bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `min-tx-interval` | Minimum transmit interval in milliseconds | 关键字 |
| min-tx-interval | `INTEGER<100-1000>` | Minimum transmit interval in milliseconds | 输入值 |
| INTEGER<100-1000> / INTEGER<3-50> | `min-rx-interval` | Minimum receive interval in milliseconds | 可选、可组合 |
| min-rx-interval | `INTEGER<100-1000>` | Minimum receive interval in milliseconds | 输入值 |
| INTEGER<100-1000> | `detect-multiplier` | BFD detection multiplier | 可选、可组合 |
| detect-multiplier | `INTEGER<3-50>` | Detection multiplier | 输入值 |
| 命令后 | `min-rx-interval` | Minimum receive interval in milliseconds | 关键字 |
| INTEGER<100-1000> / INTEGER<3-50> | `min-tx-interval` | Minimum transmit interval in milliseconds | 可选、可组合 |
| 命令后 | `detect-multiplier` | BFD detection multiplier | 关键字 |

## `ospfv3 bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable OSPFV3 BFD on this interface
- 合法语法：

  ```text
  ospfv3 bfd enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `ospfv3 cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFv3 interface cost
- 合法语法：

  ```text
  ospfv3 cost INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPFv3 cost | 输入值 |

## `ospfv3 dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFv3 interface router priority
- 合法语法：

  ```text
  ospfv3 dr-priority INTEGER<0-255>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-255>` | router priority | 输入值 |

## `ospfv3 network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFv3 interface network type
- 合法语法：

  ```text
  ospfv3 network-type {broadcast|p2p|p2mp}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `broadcast` | broadcast network | 关键字 |
| 命令后 | `p2p` | point-to-point network | 关键字 |
| 命令后 | `p2mp` | point-to-multipoint network | 关键字 |

## `ospfv3 timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFV3 interface dead
- 合法语法：

  ```text
  ospfv3 timer dead INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | dead seconds | 输入值 |

## `ospfv3 timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFV3 interface hello
- 合法语法：

  ```text
  ospfv3 timer hello INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | hello seconds | 输入值 |

## `ospfv3 timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFV3 interface retransmit
- 合法语法：

  ```text
  ospfv3 timer retransmit INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | retransmit seconds | 输入值 |

## `ospfv3 timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFV3 interface transmit-delay
- 合法语法：

  ```text
  ospfv3 timer transmit-delay INTEGER<1-3600>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-3600>` | transmit-delay seconds | 输入值 |

## `reset ospfv3`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：reset one ospfv3 process so pending runtime settings take effect
- 合法语法：

  ```text
  reset ospfv3 INTEGER<1-65535> process
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | ospfv3 process ID | 输入值 |
| INTEGER<1-65535> | `process` | reset this routing process | 关键字 |

## `undo ospfv3`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：delete an OSPFv3 process；disable OSPFv3 on an interface
- 合法语法：

  ```text
  undo ospfv3 INTEGER<1-65535>
  ```
  ```text
  undo ospfv3 INTEGER<1-65535> area X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`system`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPFv3 process ID | 输入值 |

**适用视图：`interface`**
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPFv3 process ID | 输入值 |
| INTEGER<1-65535> | `area` | OSPFv3 area | 关键字 |
| area | `X.X.X.X` | area ID | 输入值 |

## `undo ospfv3 bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPFV3 BFD timers
- 合法语法：

  ```text
  undo ospfv3 bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `min-tx-interval` | Minimum transmit interval in milliseconds | 关键字 |
| detect-multiplier / min-tx-interval | `min-rx-interval` | Minimum receive interval in milliseconds | 可选、可组合 |
| min-rx-interval / min-tx-interval | `detect-multiplier` | BFD detection multiplier | 可选、可组合 |
| 命令后 | `min-rx-interval` | Minimum receive interval in milliseconds | 关键字 |
| detect-multiplier / min-rx-interval | `min-tx-interval` | Minimum transmit interval in milliseconds | 可选、可组合 |
| 命令后 | `detect-multiplier` | BFD detection multiplier | 关键字 |

## `undo ospfv3 bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable OSPFV3 BFD on this interface
- 合法语法：

  ```text
  undo ospfv3 bfd enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo ospfv3 cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPFv3 interface cost
- 合法语法：

  ```text
  undo ospfv3 cost
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo ospfv3 dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPFv3 interface router priority
- 合法语法：

  ```text
  undo ospfv3 dr-priority
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo ospfv3 network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPFv3 interface network type
- 合法语法：

  ```text
  undo ospfv3 network-type
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo ospfv3 timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPFV3 interface dead
- 合法语法：

  ```text
  undo ospfv3 timer dead
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo ospfv3 timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPFV3 interface hello
- 合法语法：

  ```text
  undo ospfv3 timer hello
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo ospfv3 timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPFV3 interface retransmit
- 合法语法：

  ```text
  undo ospfv3 timer retransmit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo ospfv3 timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPFV3 interface transmit-delay
- 合法语法：

  ```text
  undo ospfv3 timer transmit-delay
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。
