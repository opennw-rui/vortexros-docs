# MQC

[配置指南](../mqc.md)

共用命令：[`apply config`](policy.md#cmd-apply-config)。

## `car`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：configure traffic policing (CAR)
- 合法语法：

  ```text
  car cir CIR [kbps|mbps] [pir PIR [kbps|mbps]] [cbs CBS [pbs PBS]] [green|yellow|red pass|discard|remark dscp DSCP]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `cir` | committed information rate | 关键字 |
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

## `classifier`

- 类别：配置命令
- 视图：`流策略视图`
- 用途（设备帮助）：bind a classifier to a behavior
- 合法语法：

  ```text
  classifier C behavior B [precedence N]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `CLASSIFIER` | classifier name | 输入值 |
| CLASSIFIER | `behavior` | behavior | 关键字 |
| behavior | `BEHAVIOR` | behavior name | 输入值 |
| BEHAVIOR | `precedence` | bind precedence | 可选 |
| precedence | `N` | precedence | 输入值 |

## `display traffic behavior`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display MQC traffic behaviors
- 合法语法：

  ```text
  display traffic behavior [user-defined [NAME]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：配置与运行态，按子命令区分。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `user-defined` | user-defined behavior | 可选 |
| user-defined | `BEHAVIOR` | behavior name | 输入值、可选 |

## `display traffic classifier`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display MQC traffic classifiers
- 合法语法：

  ```text
  display traffic classifier [user-defined [NAME]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Running（已接受配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `user-defined` | user-defined classifier | 可选 |
| user-defined | `CLASSIFIER` | classifier name | 输入值、可选 |

## `display traffic policy`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display MQC traffic policies
- 合法语法：

  ```text
  display traffic policy [user-defined [NAME]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Running（已接受配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `user-defined` | user-defined policy | 可选 |
| user-defined | `POLICY` | policy name | 输入值、可选 |

## `if-match`

- 类别：配置命令
- 视图：`流分类器视图`
- 用途（设备帮助）：configure a classifier match rule
- 合法语法：

  ```text
  if-match [not] CONDITION
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| not / 命令后 | `any` | match any packet | 关键字 |
| not / 命令后 | `acl` | match ACL | 关键字 |
| acl | `ACL` | ACL name | 输入值 |
| not / 命令后 | `dscp` | match DSCP | 关键字 |
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
| not / 命令后 | `vlan-id` | match VLAN ID | 关键字 |
| vlan-id | `INTEGER<1-4094>` | VLAN ID | 输入值 |
| not / 命令后 | `protocol` | match network protocol | 关键字 |
| protocol | `ip` | IPv4 | 关键字 |
| protocol | `ipv6` | IPv6 | 关键字 |
| not / 命令后 | `protocol-number` | match IP protocol number | 关键字 |
| protocol-number | `INTEGER<0-255>` | IP protocol number | 输入值 |
| not / 命令后 | `source-ip` | match source prefix | 关键字 |
| destination-ip / source-ip | `PREFIX` | IPv4 or IPv6 prefix | 输入值 |
| not / 命令后 | `destination-ip` | match destination prefix | 关键字 |
| not / 命令后 | `source-port` | match source port | 关键字 |
| destination-port / source-port | `INTEGER<0-65535>` | first port | 输入值 |
| INTEGER<0-4294967295> / INTEGER<0-65535> | `to` | range end | 可选 |
| to | `INTEGER<0-65535>` | last port | 输入值 |
| not / 命令后 | `destination-port` | match destination port | 关键字 |
| not / 命令后 | `packet-length` | match packet length | 关键字 |
| packet-length | `INTEGER<0-4294967295>` | minimum length | 输入值 |
| to | `INTEGER<0-4294967295>` | maximum length | 输入值 |
| not / 命令后 | `tcp` | match TCP fields | 关键字 |
| tcp | `syn-flag` | TCP SYN flag | 关键字 |
| not / 命令后 | `tcp-flags` | match TCP flag value and mask | 关键字 |
| tcp-flags | `VALUE` | hex flag value | 输入值 |
| VALUE | `mask` | flag mask | 关键字 |
| mask | `MASK` | hex flag mask | 输入值 |
| not / 命令后 | `vxlan-vni` | match VXLAN VNI | 关键字 |
| vxlan-vni | `INTEGER<0-16777215>` | VXLAN VNI | 输入值 |
| not / 命令后 | `inbound-interface` | match input interface | 关键字 |
| inbound-interface / outbound-interface | `IF` | interface | 输入值 |
| not / 命令后 | `outbound-interface` | match output interface | 关键字 |
| 命令后 | `not` | invert a condition | 关键字 |

## `if-match any`

- 类别：配置命令
- 视图：`流分类器视图`
- 用途（设备帮助）：match any packet
- 合法语法：

  ```text
  if-match any
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `redirect`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：configure PBR redirect
- 合法语法：

  ```text
  redirect ip-nexthop IP | ipv6-nexthop IPv6 [interface IF] [vpn-instance VRF] | interface IF | vpn-instance VRF
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ip-nexthop` | next-hop IP | 关键字 |
| ip-nexthop | `IP` | next-hop | 输入值 |
| IP / IPv6 | `interface IF` | outgoing interface；interface | 可选、可组合 |
| IP / IPv6 | `vpn-instance VRF` | next-hop VPN instance；VPN instance | 可选、可组合 |
| 命令后 | `ipv6-nexthop` | next-hop IPv6 | 关键字 |
| ipv6-nexthop | `IPv6` | next-hop | 输入值 |
| 命令后 | `interface` | outgoing interface | 关键字 |
| interface | `IF` | interface | 输入值 |
| 命令后 | `vpn-instance` | look up the packet destination in a VPN routing table | 关键字 |
| vpn-instance | `VRF` | VPN instance name | 输入值 |

## `remark dscp`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：remark packet DSCP
- 合法语法：

  ```text
  remark dscp DSCP
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `cs0` | CS0 / default (0) | 关键字 |
| 命令后 | `cs1` | CS1 (8) | 关键字 |
| 命令后 | `af11` | AF11 (10) | 关键字 |
| 命令后 | `af12` | AF12 (12) | 关键字 |
| 命令后 | `af13` | AF13 (14) | 关键字 |
| 命令后 | `cs2` | CS2 (16) | 关键字 |
| 命令后 | `af21` | AF21 (18) | 关键字 |
| 命令后 | `af22` | AF22 (20) | 关键字 |
| 命令后 | `af23` | AF23 (22) | 关键字 |
| 命令后 | `cs3` | CS3 (24) | 关键字 |
| 命令后 | `af31` | AF31 (26) | 关键字 |
| 命令后 | `af32` | AF32 (28) | 关键字 |
| 命令后 | `af33` | AF33 (30) | 关键字 |
| 命令后 | `cs4` | CS4 (32) | 关键字 |
| 命令后 | `af41` | AF41 (34) | 关键字 |
| 命令后 | `af42` | AF42 (36) | 关键字 |
| 命令后 | `af43` | AF43 (38) | 关键字 |
| 命令后 | `cs5` | CS5 (40) | 关键字 |
| 命令后 | `ef` | EF (46) | 关键字 |
| 命令后 | `cs6` | CS6 (48) | 关键字 |
| 命令后 | `cs7` | CS7 (56) | 关键字 |
| 命令后 | `DSCP` | DSCP value 0-63 | 输入值 |

## `traffic behavior`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a traffic behavior and enter its view
- 合法语法：

  ```text
  traffic behavior NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `STRING<1-31>` | Name of behavior | 输入值 |

## `traffic classifier`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a traffic classifier and enter its view
- 合法语法：

  ```text
  traffic classifier NAME [operator and|or]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `STRING<1-31>` | Name of classifier | 输入值 |
| STRING<1-31> | `operator` | match operator | 可选 |
| operator | `and` | and | 关键字 |
| operator | `or` | or | 关键字 |

## `traffic policy`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a traffic policy and enter its view
- 合法语法：

  ```text
  traffic policy NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `STRING<1-31>` | Name of Traffic policy | 输入值 |

## `traffic-policy`

- 类别：配置命令
- 视图：`VLAN视图`、`接口视图`
- 用途（设备帮助）：apply an MQC policy to traffic in this VLAN；apply an MQC traffic policy
- 合法语法：

  ```text
  traffic-policy NAME inbound
  ```
  ```text
  traffic-policy NAME { inbound | outbound }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif, interface/ethernet-aggregate-member

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `POLICY` | policy name | 输入值 |
| POLICY | `inbound` | inbound | 关键字 |
| POLICY | `outbound` | outbound | 关键字 |

**适用视图：`vlan`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `POLICY` | policy name | 输入值 |
| POLICY | `inbound` | inbound | 关键字 |
| POLICY | `outbound` | outbound | 关键字 |

## `undo car`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：remove traffic policing (CAR)
- 合法语法：

  ```text
  undo car
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo classifier`

- 类别：配置命令
- 视图：`流策略视图`
- 用途（设备帮助）：unbind a classifier from the policy
- 合法语法：

  ```text
  undo classifier [NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `CLASSIFIER` | classifier name | 输入值、可选 |

## `undo if-match`

- 类别：配置命令
- 视图：`流分类器视图`
- 用途（设备帮助）：remove the classifier match rule
- 合法语法：

  ```text
  undo if-match [TYPE]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `any` | undo match-any rule | 可选 |
| 命令后 | `acl` | undo ACL match | 可选 |
| 命令后 | `dscp` | undo DSCP match | 可选 |
| 命令后 | `vlan-id` | undo VLAN ID match | 可选 |
| 命令后 | `protocol` | undo network protocol match | 可选 |
| 命令后 | `protocol-number` | undo IP protocol-number match | 可选 |
| 命令后 | `source-ip` | undo source prefix match | 可选 |
| 命令后 | `destination-ip` | undo destination prefix match | 可选 |
| 命令后 | `source-port` | undo source-port match | 可选 |
| 命令后 | `destination-port` | undo destination-port match | 可选 |
| 命令后 | `packet-length` | undo packet-length match | 可选 |
| 命令后 | `tcp` | undo TCP match | 可选 |
| 命令后 | `tcp-flags` | undo TCP-flags match | 可选 |
| 命令后 | `vxlan-vni` | undo VXLAN VNI match | 可选 |
| 命令后 | `inbound-interface` | undo input-interface match | 可选 |
| 命令后 | `outbound-interface` | undo output-interface match | 可选 |

## `undo redirect`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：remove PBR redirect
- 合法语法：

  ```text
  undo redirect
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo remark dscp`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：remove DSCP remarking
- 合法语法：

  ```text
  undo remark dscp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo traffic behavior`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a traffic behavior
- 合法语法：

  ```text
  undo traffic behavior NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `BEHAVIOR` | behavior name | 输入值 |

## `undo traffic classifier`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a traffic classifier
- 合法语法：

  ```text
  undo traffic classifier NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `CLASSIFIER` | classifier name | 输入值 |

## `undo traffic policy`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a traffic policy
- 合法语法：

  ```text
  undo traffic policy NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `POLICY` | policy name | 输入值 |

## `undo traffic-policy`

- 类别：配置命令
- 视图：`VLAN视图`、`接口视图`
- 用途（设备帮助）：remove an MQC traffic policy from the interface；remove the shared MQC policy from this VLAN
- 合法语法：

  ```text
  undo traffic-policy [inbound]
  ```
  ```text
  undo traffic-policy [inbound|outbound]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif, interface/ethernet-aggregate-member

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `inbound` | inbound | 可选 |
| 命令后 | `outbound` | outbound | 可选 |

**适用视图：`vlan`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `inbound` | inbound | 可选 |
| 命令后 | `outbound` | outbound | 可选 |
