# 桥域

[配置指南](../bridge-domains.md)

## `bridge-domain`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：add the interface to a bridge-domain；create a bridge-domain and enter its view
- 合法语法：

  ```text
  bridge-domain ID
  ```
  ```text
  bridge-domain ID [bvi]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Ethernet、Eth-Trunk、子接口、LoopBack、隧道
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、二层子接口、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ID` | bridge-domain ID | 输入值 |
| ID | `bvi` | bridged virtual interface | 可选 |

**适用视图：`system, interface, vpn-instance, acl, acl6, bridge-domain, vlan, classifier, behavior, policy, nat-policy, nat-address-set, nat-port-set, nat-address-pool, ospf, ospfv3, bgp, route-policy, wireguard-profile, amneziawg-profile, bfd, route-static-group, ip-pool, dhcpv6-pool, mpls, dataplane, local-user, bridge-domain-evpn, nat-rule, vpn-family, ospf-area, ospfv3-area, bgp-family, rip, ripng, isis, wireguard-peer, amneziawg-peer, bfd-session, dataplane-if`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ID` | bridge-domain ID | 输入值 |
| ID | `flood` | enable flooding | 可选、可组合 |
| ID | `no-flood` | disable flooding | 可选、可组合 |
| ID | `forward` | enable forwarding | 可选、可组合 |
| ID | `no-forward` | disable forwarding | 可选、可组合 |
| ID | `learn` | enable MAC learning | 可选、可组合 |
| ID | `no-learn` | disable MAC learning | 可选、可组合 |
| ID | `uu-flood` | enable unknown-unicast flooding | 可选、可组合 |
| ID | `no-uu-flood` | disable unknown-unicast flooding | 可选、可组合 |
| ID | `arp-term` | enable ARP termination | 可选、可组合 |
| ID | `no-arp-term` | disable ARP termination | 可选、可组合 |
| ID | `arp-ufwd` | enable ARP unicast forwarding | 可选、可组合 |
| ID | `no-arp-ufwd` | disable ARP unicast forwarding | 可选、可组合 |
| ID | `mac-age SECONDS` | set MAC aging time；aging time | 可选、可组合 |
| ID | `tag TEXT` | set bridge-domain tag；tag text | 可选、可组合 |

## `display bridge-domain`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display bridge-domains (service BD + VLAN domains)
- 合法语法：

  ```text
  display bridge-domain [ID]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ID` | bridge-domain ID (user-facing for service BD) | 输入值、可选 |

## `display mac-address`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the MAC address table
- 合法语法：

  ```text
  display mac-address [MAC | vlan VLAN-ID | bridge-domain BD | interface IF | static | dynamic]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vlan` | filter by VLAN | 可选 |
| vlan | `VLAN-ID` | VLAN ID | 输入值 |
| 命令后 | `bridge-domain` | filter by service bridge-domain | 可选 |
| bridge-domain | `BD` | bridge-domain ID | 输入值 |
| 命令后 | `interface` | filter by interface | 可选 |
| interface | `IF` | interface name | 输入值 |
| 命令后 | `static` | static entries | 可选 |
| 命令后 | `dynamic` | dynamic entries | 可选 |
| 命令后 | `MAC` | MAC address | 输入值、可选 |

## `l2 binding vlan`

- 类别：配置命令
- 视图：`BD视图`
- 用途（设备帮助）：bind a local VLAN into this bridge-domain
- 合法语法：

  ```text
  l2 binding vlan VLAN-ID
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VLAN-ID` | VLAN ID 1-4095 | 输入值 |

## `mac-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the interface MAC address
- 合法语法：

  ```text
  mac-address MAC
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `MAC` | MAC address | 输入值 |

## `mac-address aging-time`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the dynamic MAC address aging time
- 合法语法：

  ```text
  mac-address aging-time INTEGER<60-15300>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<60-15300>` | aging time in seconds (whole minutes) | 输入值 |

## `mac-address static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static MAC address
- 合法语法：

  ```text
  mac-address static MAC IF bridge-domain BD
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `MAC` | MAC address | 输入值 |
| MAC | `IF` | outgoing interface | 输入值 |
| IF | `bridge-domain` | bridge-domain | 关键字 |
| bridge-domain | `ID` | bridge-domain ID | 输入值 |

## `reset mac-address`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reset dynamically learned MAC addresses
- 合法语法：

  ```text
  reset mac-address [interface TYPE N] [mac-address H-H-H]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `H-H-H` | learned MAC address | 输入值、可选、可组合 |
| 命令后 | `interface` | select a Layer 2 interface | 可选、可组合 |
| interface | `IF` | interface name or TYPE N | 输入值 |
| 命令后 | `mac-address` | select one learned MAC address | 可选、可组合 |
| mac-address | `H-H-H` | learned MAC address | 输入值 |

## `undo bridge-domain`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：delete a bridge-domain；remove the interface from a bridge-domain
- 合法语法：

  ```text
  undo bridge-domain
  ```
  ```text
  undo bridge-domain ID
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Ethernet、Eth-Trunk、子接口、LoopBack、隧道
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、二层子接口、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk

此形式没有额外参数。

**适用视图：`system`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ID` | bridge-domain ID | 输入值 |

## `undo l2 binding vlan`

- 类别：配置命令
- 视图：`BD视图`
- 用途（设备帮助）：remove VLAN binding from this bridge-domain
- 合法语法：

  ```text
  undo l2 binding vlan
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo mac-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default interface MAC address
- 合法语法：

  ```text
  undo mac-address
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo mac-address aging-time`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default dynamic MAC address aging time
- 合法语法：

  ```text
  undo mac-address aging-time
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo mac-address static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static MAC address
- 合法语法：

  ```text
  undo mac-address static MAC IF bridge-domain BD
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `MAC` | MAC address | 输入值 |
| MAC | `IF` | outgoing interface | 输入值 |
| IF | `bridge-domain` | bridge-domain | 关键字 |
| bridge-domain | `ID` | bridge-domain ID | 输入值 |
