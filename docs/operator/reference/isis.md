# IS-IS

[配置指南](../isis.md)

共用命令：[`import-route`](dynamic-routing.md#cmd-import-route)。

## `cost-style`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set IS-IS metric style
- 合法语法：

  ```text
  cost-style {narrow|wide|transition}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `narrow` | narrow metrics | 关键字 |
| 命令后 | `wide` | wide metrics | 关键字 |
| 命令后 | `transition` | transition metrics | 关键字 |

## `display isis`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IS-IS information
- 合法语法：

  ```text
  display isis [process-id] [brief|peer|lsdb|route|interface|spf-delay|traffic-eng]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值、可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `brief` | Active configuration in brief | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `peer` | IS-IS neighbors | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `lsdb` | IS-IS link-state database | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `route` | IS-IS routing table | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `spf-delay` | IS-IS SPF backoff state | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `interface` | IS-IS interface information | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `traffic-eng` | IS-IS traffic engineering information | 可选 |
| traffic-eng | `database` | Traffic engineering database | 关键字 |
| traffic-eng | `interface` | Traffic engineering interface | 关键字 |
| traffic-eng | `router` | Traffic engineering router | 关键字 |
| 命令后 | `vpn-instance` | VPN instance | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |

## `hostname dynamic`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：enable the IS-IS dynamic hostname
- 合法语法：

  ```text
  hostname dynamic
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `ipv6 import-route`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：redistribute IPv6 routes into IS-IS
- 合法语法：

  ```text
  ipv6 import-route {direct|static|ospfv3|bgp}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct | 关键字 |
| 命令后 | `static` | static | 关键字 |
| 命令后 | `ospfv3` | OSPFv3 | 关键字 |
| 命令后 | `bgp` | BGP | 关键字 |

## `is-level`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set IS-IS level
- 合法语法：

  ```text
  is-level {level-1|level-2|level-1-2}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `level-1` | level-1 | 关键字 |
| 命令后 | `level-2` | level-2 | 关键字 |
| 命令后 | `level-1-2` | level-1-2 | 关键字 |

## `isis`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an IS-IS process and enter process view
- 合法语法：

  ```text
  isis INTEGER<1-65535> [vpn-instance NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值 |
| INTEGER<1-65535> | `vpn-instance` | VPN instance | 可选、可组合 |
| vpn-instance | `VPN` | VPN instance name | 输入值 |

## `isis bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure ISIS BFD timers
- 合法语法：

  ```text
  isis bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
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

## `isis bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable ISIS BFD on this interface
- 合法语法：

  ```text
  isis bfd enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `isis circuit-level`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the IS-IS circuit level
- 合法语法：

  ```text
  isis circuit-level {level-1|level-1-2|level-2}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `level-1` | Level-1 only | 关键字 |
| 命令后 | `level-1-2` | Level-1-2 | 关键字 |
| 命令后 | `level-2` | Level-2 only | 关键字 |

## `isis circuit-type p2p`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the IS-IS link to point-to-point
- 合法语法：

  ```text
  isis circuit-type p2p
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `isis cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set IS-IS interface metric
- 合法语法：

  ```text
  isis cost INTEGER<1-16777215>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-16777215>` | metric | 输入值 |

## `isis enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable IS-IS on an interface
- 合法语法：

  ```text
  isis enable INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值 |

## `isis ipv6-enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable IPv6 IS-IS on an interface
- 合法语法：

  ```text
  isis ipv6-enable INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值 |

## `isis passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：make IS-IS interface passive
- 合法语法：

  ```text
  isis passive
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `isis priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set IS-IS interface priority
- 合法语法：

  ```text
  isis priority INTEGER<0-127>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-127>` | priority | 输入值 |

## `network-entity`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set an IS-IS network entity title
- 合法语法：

  ```text
  network-entity NET
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NET` | NSAP network entity title | 输入值 |

## `reset service isis`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed isis routing service
- 合法语法：

  ```text
  reset service isis
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `set-overload-bit`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set the IS-IS overload bit
- 合法语法：

  ```text
  set-overload-bit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `spf-delay-ietf`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：configure IETF SPF backoff timers
- 合法语法：

  ```text
  spf-delay-ietf init-delay MS short-delay MS long-delay MS holddown MS time-to-learn MS
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `init-delay` | SPF backoff timer | 关键字 |
| holddown / init-delay / long-delay / short-delay / time-to-learn | `INTEGER<0-60000>` | Milliseconds | 输入值 |
| INTEGER<0-60000> | `short-delay` | SPF backoff timer | 关键字 |
| INTEGER<0-60000> | `long-delay` | SPF backoff timer | 关键字 |
| INTEGER<0-60000> | `holddown` | SPF backoff timer | 关键字 |
| INTEGER<0-60000> | `time-to-learn` | SPF backoff timer | 关键字 |

## `undo hostname`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：restore the default IS-IS hostname
- 合法语法：

  ```text
  undo hostname
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6 import-route`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：stop redistributing IPv6 routes into IS-IS
- 合法语法：

  ```text
  undo ipv6 import-route PROTOCOL
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct | 关键字 |
| 命令后 | `static` | static | 关键字 |
| 命令后 | `ospfv3` | OSPFv3 | 关键字 |
| 命令后 | `bgp` | BGP | 关键字 |

## `undo is-level`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：restore IS-IS level
- 合法语法：

  ```text
  undo is-level
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo isis`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an IS-IS process
- 合法语法：

  ```text
  undo isis INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值 |

## `undo isis bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore ISIS BFD timers
- 合法语法：

  ```text
  undo isis bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
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

## `undo isis bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ISIS BFD on this interface
- 合法语法：

  ```text
  undo isis bfd enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo isis circuit-level`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the IS-IS circuit level
- 合法语法：

  ```text
  undo isis circuit-level
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo isis circuit-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the IS-IS link type
- 合法语法：

  ```text
  undo isis circuit-type
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo isis cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore IS-IS interface metric
- 合法语法：

  ```text
  undo isis cost
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo isis enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable IS-IS on an interface
- 合法语法：

  ```text
  undo isis enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo isis ipv6-enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable IPv6 IS-IS on an interface
- 合法语法：

  ```text
  undo isis ipv6-enable INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值 |

## `undo isis passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore IS-IS interface
- 合法语法：

  ```text
  undo isis passive
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo isis priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore IS-IS interface priority
- 合法语法：

  ```text
  undo isis priority
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo network-entity`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：remove an IS-IS network entity title
- 合法语法：

  ```text
  undo network-entity NET
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NET` | NSAP network entity title | 输入值 |

## `undo set-overload-bit`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：clear the IS-IS overload bit
- 合法语法：

  ```text
  undo set-overload-bit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo spf-delay-ietf`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：disable IETF SPF backoff timers
- 合法语法：

  ```text
  undo spf-delay-ietf
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
