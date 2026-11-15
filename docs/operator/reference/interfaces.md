# Ethernet 与接口

[配置指南](../ethernet.md)

## `description`

- 类别：配置命令
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- 用途（设备帮助）：NVE interface description；bridge-domain description；configure ACL description；configure group description；configure the VLAN description；configure the VPN instance description；configure the interface description；set NAT policy description；set NAT rule description
- 合法语法：

  ```text
  description TEXT
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif, interface/ethernet-aggregate-member

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description string | 输入值、后续文本 |

**适用视图：`bridge-domain`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `TEXT` | description text | 输入值、后续文本 |

**适用视图：`interface`**
适用分区：interface/nve
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
- 视图：`任意允许视图`
- 用途（设备帮助）：display interface flow-steering configuration and runtime
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
- 视图：`任意允许视图`
- 用途（设备帮助）：display interface information
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
- 视图：`任意允许视图`
- 用途（设备帮助）：display brief interface list
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
- 视图：`任意允许视图`
- 用途（设备帮助）：display interface descriptions
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
- 视图：`任意允许视图`
- 用途（设备帮助）：display physical interface hardware offload capabilities and state
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
- 视图：`任意允许视图`
- 用途（设备帮助）：per-interface counters
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
- 视图：`任意允许视图`
- 用途（设备帮助）：show Linux Control Plane interface pairs
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
- 视图：`接口视图`
- 用途（设备帮助）：configure sub-interface encapsulation
- 合法语法：

  ```text
  encapsulation { dot1q | dot1ad } vid VLAN-ID | encapsulation qinq vid PE-VID ce-vid CE-VID
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：subif
适用分区：interface/subif-l2
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
- 视图：`接口视图`
- 用途（设备帮助）：enable tunnel-aware ingress worker steering
- 合法语法：

  ```text
  flow-steering enable
  ```


<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：ethernet

此形式没有额外参数。

(cmd-hardware-offload)=
## `hardware offload`

- 类别：配置命令
- 视图：`dataplane-if`、`接口视图`
- 用途（设备帮助）：restore default hardware offload use
- 合法语法：

  ```text
  hardware offload OFFLOAD [OFFLOAD ...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：ethernet

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
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter the interface view
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
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter a batch interface view
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
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：Preconfigure an interface before it is present
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

为三层接口设置地址。提交后形成直连网段，修改已有地址可能影响 SSH、邻居和路由。见[静态路由案例](../../examples/static-route.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv4 address
- 合法语法：

  ```text
  ip address IP MASK [sub]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 address (X.X.X.X) | 输入值 |
| IP | `MASK` | mask or prefix length | 输入值 |
| MASK | `sub` | secondary address | 可选 |

## `ipv6 address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv6 address
- 合法语法：

  ```text
  ipv6 address IP PREFIXLEN
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv6 address (X:X::X:X) | 输入值 |
| IP | `PREFIXLEN` | prefix length | 输入值 |

## `lcp host`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：create a same-name Linux control-plane interface mapping
- 合法语法：

  ```text
  lcp host HOST-IF [tap|tun]
  ```


<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `HOST-IF` | Linux host interface name (must equal the VPP interface name) | 输入值 |
| HOST-IF | `tap` | TAP device | 可选 |
| HOST-IF | `tun` | TUN device | 可选 |

(cmd-mode)=
## `mode`

- 类别：配置命令
- 视图：`dataplane-if`、`接口视图`
- 用途（设备帮助）：Select the physical port driver；set the aggregate working mode
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
接口类别：eth-trunk
适用分区：interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `lacp-static` | Static LACP working mode | 关键字 |
| 命令后 | `manual` | Manual working mode | 关键字 |

## `mtu`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the interface MTU
- 合法语法：

  ```text
  mtu N
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `N` | MTU in bytes | 输入值 |

## `shutdown`

- 类别：配置命令
- 视图：`BFD会话视图`、`接口视图`
- 用途（设备帮助）：shut down the interface；shutdown
- 合法语法：

  ```text
  shutdown
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif, interface/ethernet-aggregate-member

此形式没有额外参数。

**适用视图：`bfd-session`**

此形式没有额外参数。

## `statistic enable`

- 类别：配置命令
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- 用途（设备帮助）：enable counters for this NAT policy；enable counters for this NAT rule；enable detailed interface packet statistics
- 合法语法：

  ```text
  statistic enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：ethernet

此形式没有额外参数。

**适用视图：`nat-policy`**

此形式没有额外参数。

**适用视图：`nat-rule`**

此形式没有额外参数。

## `undo description`

- 类别：配置命令
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- 用途（设备帮助）：clear ACL description；clear NAT policy description；clear NAT rule description；clear NVE description；clear bridge-domain description；delete group description；delete the VLAN description；delete the VPN instance description；delete the interface description
- 合法语法：

  ```text
  undo description
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif, interface/ethernet-aggregate-member

此形式没有额外参数。

**适用视图：`bridge-domain`**

此形式没有额外参数。

**适用视图：`interface`**
适用分区：interface/nve
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
- 视图：`接口视图`
- 用途（设备帮助）：remove the sub-interface encapsulation
- 合法语法：

  ```text
  undo encapsulation
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：subif
适用分区：interface/subif-l2
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `undo flow-steering enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ingress worker steering on the interface
- 合法语法：

  ```text
  undo flow-steering enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：ethernet

此形式没有额外参数。

## `undo hardware offload`

- 类别：配置命令
- 视图：`dataplane-if`、`接口视图`
- 用途（设备帮助）：disable hardware offload use
- 合法语法：

  ```text
  undo hardware offload OFFLOAD [OFFLOAD ...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：ethernet

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
- 视图：`系统视图`
- 用途（设备帮助）：delete an interface
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
- 视图：`接口视图`
- 用途（设备帮助）：delete an IPv4 address
- 合法语法：

  ```text
  undo ip address [IP MASK]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 address (X.X.X.X) | 输入值、可选 |
| IP | `MASK` | mask or prefix length | 输入值 |

## `undo ipv6 address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete an IPv6 address
- 合法语法：

  ```text
  undo ipv6 address [IP PREFIXLEN]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv6 address (X:X::X:X) | 输入值、可选 |
| IP | `PREFIXLEN` | prefix length | 输入值 |

## `undo lcp host`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete the Linux control-plane interface mapping
- 合法语法：

  ```text
  undo lcp host
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo mode`

- 类别：配置命令
- 视图：`dataplane-if`、`接口视图`
- 用途（设备帮助）：Restore Linux kernel mode；restore manual aggregate mode
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
接口类别：eth-trunk
适用分区：interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3

此形式没有额外参数。

## `undo mtu`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default interface MTU
- 合法语法：

  ```text
  undo mtu
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

此形式没有额外参数。

## `undo shutdown`

- 类别：配置命令
- 视图：`BFD会话视图`、`接口视图`
- 用途（设备帮助）：bring the interface up；undo shutdown
- 合法语法：

  ```text
  undo shutdown
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
适用分区：interface/ethernet-neutral, interface/ethernet-l2, interface/ethernet-l3, interface/eth-trunk-neutral, interface/eth-trunk-l2, interface/eth-trunk-l3, interface/subif-l2, interface/subif-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif, interface/ethernet-aggregate-member

此形式没有额外参数。

**适用视图：`bfd-session`**

此形式没有额外参数。

## `undo statistic enable`

- 类别：配置命令
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- 用途（设备帮助）：disable counters for this NAT policy；disable counters for this NAT rule；disable detailed interface packet statistics
- 合法语法：

  ```text
  undo statistic enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：ethernet

此形式没有额外参数。

**适用视图：`nat-policy`**

此形式没有额外参数。

**适用视图：`nat-rule`**

此形式没有额外参数。
