# Ethernet 与接口

[配置指南](../ethernet.md)

## `description`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- CLI 帮助：NVE interface description；bridge-domain description；configure ACL description；configure group description；configure the VLAN description；configure the VPN instance description；configure the interface description；set NAT policy description；set NAT rule description
- 合法语法：

  ```text
  description TEXT
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif、聚合成员口

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description string | 输入值、后续文本 |

**适用视图：`bridge-domain`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description text | 输入值、后续文本 |

**适用视图：`interface`**
接口类别：NVE
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description text | 输入值、后续文本 |

**适用视图：`vpn-instance`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description string | 输入值、后续文本 |

**适用视图：`nat-policy`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description | 输入值、后续文本 |

**适用视图：`nat-rule`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description | 输入值、后续文本 |

**适用视图：`vlan`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description string | 输入值、后续文本 |

**适用视图：`route-static-group`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description | 输入值、后续文本 |

**适用视图：`acl, acl6`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description string | 输入值、后续文本 |

## `display flow-steering`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display interface flow-steering configuration and runtime
- 合法语法：

  ```text
  display flow-steering [interface IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `interface` | select an interface | 可选 |
| interface | `IF` | interface name | 输入值 |

## `display interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display interface information
- 合法语法：

  ```text
  display interface [IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | interface name or TYPE | 输入值、可选 |
| IF | `N` | interface number when TYPE and NUMBER are split | 输入值、可选 |

## `display interface brief`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display brief interface list
- 合法语法：

  ```text
  display interface brief
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display interface description`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display interface descriptions
- 合法语法：

  ```text
  display interface description [IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | interface name or TYPE | 输入值、可选 |
| IF | `N` | interface number | 输入值、可选 |

## `display interface hardware offload`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display physical interface hardware offload capabilities and state
- 合法语法：

  ```text
  display interface hardware offload [IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PHYS-IF` | physical Ethernet interface | 输入值、可选 |

## `display interface statistics`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：per-interface counters
- 合法语法：

  ```text
  display interface statistics [IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | interface name or TYPE | 输入值、可选 |
| IF | `N` | interface number | 输入值、可选 |

## `display lcp`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：show Linux Control Plane interface pairs
- 合法语法：

  ```text
  display lcp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `encapsulation`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure sub-interface encapsulation
- 合法语法：

  ```text
  encapsulation { dot1q | dot1ad } vid VLAN-ID [ce-vid { VID [to VID] ... | any }] | encapsulation qinq vid PE-VID ce-vid { VID [to VID] ... | any }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：子接口
接口类别：二层子接口
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `dot1q` | IEEE 802.1Q | 关键字 |
| dot1ad / dot1q | `vid` | VLAN ID | 关键字 |
| vid | `VID` | VLAN ID | 输入值 |
| 命令后 | `dot1ad` | IEEE 802.1ad | 关键字 |
| 命令后 | `qinq` | QinQ | 关键字 |
| qinq | `vid` | outer VLAN ID | 关键字 |
| vid | `VID` | outer VLAN ID | 输入值 |
| VID | `ce-vid` | inner VLAN ID | 关键字 |
| ce-vid | `CE-VID` | inner VLAN ID | 输入值 |

## `flow-steering enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable tunnel-aware ingress worker steering
- 合法语法：

  ```text
  flow-steering enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet

此形式没有额外参数。

(cmd-hardware-offload)=
## `hardware offload`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane-if`、`接口视图`
- CLI 帮助：restore default hardware offload use
- 合法语法：

  ```text
  hardware offload OFFLOAD [OFFLOAD ...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `gso` | Generic segmentation offload | 关键字 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `gso` | Generic segmentation offload | 可选、可组合 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `rx-checksum` | Receive TCP/UDP checksum offload | 可选、可组合 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `tx-checksum` | Transmit TCP/UDP checksum offload | 可选、可组合 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `tso` | TCP segmentation offload | 可选、可组合 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `multi-segs` | Multi-segment transmit and receive scatter | 可选、可组合 |
| 命令后 | `rx-checksum` | Receive TCP/UDP checksum offload | 关键字 |
| 命令后 | `tx-checksum` | Transmit TCP/UDP checksum offload | 关键字 |
| 命令后 | `tso` | TCP segmentation offload | 关键字 |
| 命令后 | `multi-segs` | Multi-segment transmit and receive scatter | 关键字 |

## `interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter the interface view
- 合法语法：

  ```text
  interface { Eth-Trunk N | LoopBack N | Tunnel N | Vlanif N | Vbdif N | eth N | IFNAME }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `Eth-Trunk` | Ethernet-Trunk interface | 关键字 |
| Eth-Trunk | `INTEGER<0-63>` | Eth-Trunk interface number | 输入值 |
| 命令后 | `loopback` | LoopBack interface | 关键字 |
| 100GE / 10GE / 25GE / 40GE / GigabitEthernet / XGigabitEthernet / eth / loopback / nve / vbdif / vlanif | `N` | interface locator | 输入值 |
| 命令后 | `tunnel` | Tunnel interface | 关键字 |
| tunnel | `INTEGER<0-4294967295>` | Tunnel interface number | 输入值 |
| 命令后 | `vlanif` | Vlanif interface (BVI) | 关键字 |
| 命令后 | `vbdif` | Vbdif interface (service BD BVI) | 关键字 |
| 命令后 | `nve` | NVE interface | 关键字 |
| 命令后 | `eth` | Ethernet interface | 关键字 |
| 命令后 | `GigabitEthernet` | Gigabit Ethernet interface | 关键字 |
| 命令后 | `XGigabitEthernet` | 10 Gigabit Ethernet interface | 关键字 |
| 命令后 | `10GE` | 10 Gigabit Ethernet interface | 关键字 |
| 命令后 | `25GE` | 25 Gigabit Ethernet interface | 关键字 |
| 命令后 | `40GE` | 40 Gigabit Ethernet interface | 关键字 |
| 命令后 | `100GE` | 100 Gigabit Ethernet interface | 关键字 |
| 命令后 | `IFNAME` | interface name | 输入值 |

## `interface range`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter a batch interface view
- 合法语法：

  ```text
  interface range IF1 to IF2
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF1` | first interface | 输入值 |
| IF1 | `to` | last interface in the range | 关键字 |
| to | `IF2` | last interface | 输入值 |

## `interface user-defined`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：Preconfigure an interface before it is present
- 合法语法：

  ```text
  interface user-defined NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | Linux-compatible interface name | 输入值 |

## `ip address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure an IPv4 address
- 合法语法：

  ```text
  ip address IP MASK [sub]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 address (X.X.X.X) | 输入值 |
| IP | `MASK` | mask or prefix length | 输入值 |
| MASK | `sub` | secondary address | 可选 |

## `ipv6 address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure an IPv6 address
- 合法语法：

  ```text
  ipv6 address IP PREFIXLEN
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv6 address (X:X::X:X) | 输入值 |
| IP | `PREFIXLEN` | prefix length | 输入值 |

## `lcp host`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：create a same-name Linux control-plane interface mapping
- 合法语法：

  ```text
  lcp host HOST-IF [tap|tun]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `HOST-IF` | Linux host interface name (must equal the VPP interface name) | 输入值 |
| HOST-IF | `tap` | TAP device | 可选 |
| HOST-IF | `tun` | TUN device | 可选 |

(cmd-mode)=
## `mode`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane-if`、`接口视图`
- CLI 帮助：Select the physical port driver；set the aggregate working mode
- 合法语法：

  ```text
  mode { kernel | dpdk }
  ```
  ```text
  mode { lacp-static | manual }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`dataplane-if`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `kernel` | Linux kernel driver | 关键字 |
| 命令后 | `dpdk` | VPP DPDK driver | 关键字 |

**适用视图：`interface`**
接口类别：Eth-Trunk
接口类别：Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `lacp-static` | Static LACP working mode | 关键字 |
| 命令后 | `manual` | Manual working mode | 关键字 |

## `mtu`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the interface MTU
- 合法语法：

  ```text
  mtu N
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `N` | MTU in bytes | 输入值 |

## `shutdown`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`、`接口视图`
- CLI 帮助：shut down the interface；shutdown
- 合法语法：

  ```text
  shutdown
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif、聚合成员口

此形式没有额外参数。

**适用视图：`bfd-session`**

此形式没有额外参数。

## `statistic enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- CLI 帮助：enable counters for this NAT policy；enable counters for this NAT rule；enable detailed interface packet statistics
- 合法语法：

  ```text
  statistic enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Ethernet

此形式没有额外参数。

**适用视图：`nat-policy`**

此形式没有额外参数。

**适用视图：`nat-rule`**

此形式没有额外参数。

## `undo description`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- CLI 帮助：clear ACL description；clear NAT policy description；clear NAT rule description；clear NVE description；clear bridge-domain description；delete group description；delete the VLAN description；delete the VPN instance description；delete the interface description
- 合法语法：

  ```text
  undo description
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif、聚合成员口

此形式没有额外参数。

**适用视图：`bridge-domain`**

此形式没有额外参数。

**适用视图：`interface`**
接口类别：NVE
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

**适用视图：`vpn-instance`**

此形式没有额外参数。

**适用视图：`nat-policy`**

此形式没有额外参数。

**适用视图：`nat-rule`**

此形式没有额外参数。

**适用视图：`vlan`**

此形式没有额外参数。

**适用视图：`route-static-group`**

此形式没有额外参数。

**适用视图：`acl, acl6`**

此形式没有额外参数。

## `undo encapsulation`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove the sub-interface encapsulation
- 合法语法：

  ```text
  undo encapsulation
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：子接口
接口类别：二层子接口
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `undo flow-steering enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable ingress worker steering on the interface
- 合法语法：

  ```text
  undo flow-steering enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet

此形式没有额外参数。

## `undo hardware offload`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane-if`、`接口视图`
- CLI 帮助：disable hardware offload use
- 合法语法：

  ```text
  undo hardware offload OFFLOAD [OFFLOAD ...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `gso` | Generic segmentation offload | 关键字 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `gso` | Generic segmentation offload | 可选、可组合 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `rx-checksum` | Receive TCP/UDP checksum offload | 可选、可组合 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `tx-checksum` | Transmit TCP/UDP checksum offload | 可选、可组合 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `tso` | TCP segmentation offload | 可选、可组合 |
| gso / multi-segs / rx-checksum / tso / tx-checksum | `multi-segs` | Multi-segment transmit and receive scatter | 可选、可组合 |
| 命令后 | `rx-checksum` | Receive TCP/UDP checksum offload | 关键字 |
| 命令后 | `tx-checksum` | Transmit TCP/UDP checksum offload | 关键字 |
| 命令后 | `tso` | TCP segmentation offload | 关键字 |
| 命令后 | `multi-segs` | Multi-segment transmit and receive scatter | 关键字 |

## `undo interface`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an interface
- 合法语法：

  ```text
  undo interface IFNAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | interface | 输入值 |

## `undo ip address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete an IPv4 address
- 合法语法：

  ```text
  undo ip address [IP MASK]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 address (X.X.X.X) | 输入值、可选 |
| IP | `MASK` | mask or prefix length | 输入值 |

## `undo ipv6 address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete an IPv6 address
- 合法语法：

  ```text
  undo ipv6 address [IP PREFIXLEN]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv6 address (X:X::X:X) | 输入值、可选 |
| IP | `PREFIXLEN` | prefix length | 输入值 |

## `undo lcp host`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete the Linux control-plane interface mapping
- 合法语法：

  ```text
  undo lcp host
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo mode`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane-if`、`接口视图`
- CLI 帮助：Restore Linux kernel mode；restore manual aggregate mode
- 合法语法：

  ```text
  undo mode
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`dataplane-if`**

此形式没有额外参数。

**适用视图：`interface`**
接口类别：Eth-Trunk
接口类别：Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk

此形式没有额外参数。

## `undo mtu`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default interface MTU
- 合法语法：

  ```text
  undo mtu
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo shutdown`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`、`接口视图`
- CLI 帮助：bring the interface up；undo shutdown
- 合法语法：

  ```text
  undo shutdown
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Ethernet（未选择二/三层）、二层 Ethernet、三层 Ethernet、Eth-Trunk（未选择二/三层）、二层 Eth-Trunk、三层 Eth-Trunk、二层子接口、三层子接口、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif、聚合成员口

此形式没有额外参数。

**适用视图：`bfd-session`**

此形式没有额外参数。

## `undo statistic enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- CLI 帮助：disable counters for this NAT policy；disable counters for this NAT rule；disable detailed interface packet statistics
- 合法语法：

  ```text
  undo statistic enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：Ethernet

此形式没有额外参数。

**适用视图：`nat-policy`**

此形式没有额外参数。

**适用视图：`nat-rule`**

此形式没有额外参数。

## 批量接口编辑

interface range Ethernet 97 to Ethernet 98 进入连续接口视图。description、mtu、shutdown 等支持的接口命令作用于整个范围，commit 后统一生效。例如：

```text
interface range Ethernet 97 to Ethernet 98
 description RANGE-TEST
 mtu 1400
 shutdown
#
commit
```

两接口的实测结果均为管理 Down、MTU 1400，描述均为 RANGE-TEST。使用同一范围的 undo description、undo mtu、undo shutdown 并提交后，描述清空、MTU 恢复 1500、管理状态恢复 Up。实际链路与协议状态仍取决于各接口本身。

不能向多个接口批量配置同一个本机 IP 地址：命令会因地址冲突拒绝整个地址编辑，不会只为第一个接口写入。此前已暂存的其他编辑继续保留。用 display configuration candidate 检查待提交配置；display this 显示该范围已经提交的配置。


显式 lcp host 配置撤销后，物理接口以及 LoopBack、Vlanif、Vbdif 等由功能管理的逻辑接口恢复自动同名控制端点，原接口地址和 VPN 绑定保留。显式参数与默认相同时，撤销不会重建端点；需要替换端点时可能短暂丢包。提交完成后检查 display lcp、接口地址及连通性。display current-configuration configuration lcp 只列显式声明，不把自动端点显示为额外配置。


VPP数据面中，同一VPN内不同三层接口的IPv4子网不能相互覆盖，LoopBack的/32也受此限制。例如，Ethernet0配置198.19.196.2/24后，不能在同VPN的LoopBack上配置198.19.196.33/32。不同VPN相互独立；同一接口上相同掩码的不同主、从地址仍可使用。选择LoopBack地址时，应使用独立主机前缀，避免落入其他接口已配置的子网。

## `rewrite pop`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：select symmetric VLAN tag removal
- 合法语法：

  ```text
  rewrite pop { single | double | none }
  ```


配置对称标签处理。`single` 移除、恢复外层标签；`double` 移除、恢复固定双层标签；VortexROS 扩展 `none` 保留标签。多内层集合或 `any` 只能选择 `single` 或 `none`，不能用 `double`。详见 [L2 子接口](../subinterfaces-l2.md)。

## `undo rewrite pop`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the legacy default VLAN rewrite
- 合法语法：

  ```text
  undo rewrite pop
  ```


恢复原有默认：单标签 pop1、固定双标签 pop2。多内层或 `any` 撤销后不可直接提交，需显式补齐支持的动作。
