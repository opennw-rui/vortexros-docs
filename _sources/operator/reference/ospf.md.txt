# OSPF

[配置指南](../ospf.md)

共用命令：[`abr-summary`](dynamic-routing.md#cmd-abr-summary)、[`area`](dynamic-routing.md#cmd-area)、[`import-route`](dynamic-routing.md#cmd-import-route)、[`network`](dynamic-routing.md#cmd-network)、[`router-id`](dynamic-routing.md#cmd-router-id)。

## `bandwidth-reference`

- 类别：配置命令
- 视图：`ospfv3`
- 用途（设备帮助）：set the OSPFv3 reference bandwidth
- 合法语法：

  ```text
  bandwidth-reference INTEGER<1-4294967>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4294967>` | reference bandwidth in Mbit/s | 输入值 |

## `display ospf`

peer 查询邻接，routing 查询协议路由，lsdb 查询链路状态数据库。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display OSPF information
- 合法语法：

  ```text
  display ospf [process-id] lsdb [{router|network|summary|asbr|ase|nssa|opaque-*} [link-state-id]] [originate-router router-id|self-originate] [age {min-value|max-value} seconds]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | Process ID | 输入值、可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `abr-asbr` | Information of the OSPF ABR and ASBR | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `asbr-summary` | Information of aggregate addresses for OSPF | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `brief` | Brief information of OSPF processes | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `graceful-restart` | Display GR information | 可选 |
| graceful-restart | `helper` | Helper details in the router | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `interface` | Interface information | 可选 |
| interface | `traffic` | OSPF interface packet counters | 可选 |
| interface / peer / traffic | `INTERFACE` | Interface name | 输入值、可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `lsdb` | Link state database | 可选 |
| lsdb | `router` | Router link states | 可选 |
| asbr / ase / lsdb / network / nssa / opaque-area / opaque-as / opaque-link / router / summary | `X.X.X.X` | Link state ID | 输入值、可选 |
| X.X.X.X / asbr / ase / lsdb / network / nssa / opaque-area / opaque-as / opaque-link / router / summary | `originate-router` | Advertising router link states | 可选 |
| originate-router | `X.X.X.X` | Advertising router ID | 输入值 |
| X.X.X.X / asbr / ase / lsdb / network / nssa / opaque-area / opaque-as / opaque-link / router / summary | `self-originate` | Self-originated link states | 可选 |
| X.X.X.X / asbr / ase / lsdb / network / nssa / opaque-area / opaque-as / opaque-link / router / summary | `age` | Only display LSAs in the age scope | 可选 |
| age | `min-value` | Minimum LSA age | 关键字 |
| max-value / min-value | `INTEGER<0-3600>` | LSA age in seconds | 输入值 |
| INTEGER<0-3600> | `max-value` | Maximum LSA age | 可选 |
| age | `max-value` | Maximum LSA age | 关键字 |
| lsdb | `network` | Network link states | 可选 |
| lsdb | `ase` | AS external link states | 可选 |
| lsdb | `asbr` | ASBR summary link states | 可选 |
| lsdb | `summary` | Network summary link states | 可选 |
| lsdb | `nssa` | NSSA external link states | 可选 |
| lsdb | `opaque-area` | Opaque area link states | 可选 |
| lsdb | `opaque-as` | Opaque AS link states | 可选 |
| lsdb | `opaque-link` | Opaque link-local link states | 可选 |
| lsdb | `brief` | Database summary | 可选 |
| lsdb | `detail` | Detailed database information | 可选 |
| lsdb | `INTEGER<1-5>` | LSA type | 输入值、可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `mpls-te` | MPLS-TE information | 可选 |
| mpls-te | `database` | MPLS-TE database | 关键字 |
| mpls-te | `interface` | Interface information | 关键字 |
| mpls-te | `router` | MPLS-TE router parameters | 关键字 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `peer` | A neighbor router | 可选 |
| peer | `X.X.X.X` | Neighbor router ID | 输入值、可选 |
| INTERFACE / X.X.X.X / peer | `brief` | Brief OSPF peer information | 可选 |
| peer | `last-nbr-down` | Information of last down peer | 可选 |
| DISPLAY-VRF / INTEGER<1-65535> / 命令后 | `routing` | OSPF route table | 可选 |
| 命令后 | `vpn-instance` | VPN instance | 可选 |
| vpn-instance | `DISPLAY-VRF` | VPN instance name | 输入值 |

## `nssa`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：configure a not-so-stubby area；configure an OSPFv3 nssa area
- 合法语法：

  ```text
  nssa [no-summary]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `no-summary` | do not advertise inter-area summaries | 可选 |

**适用视图：`ospfv3-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `no-summary` | suppress inter-area summaries | 可选 |

## `opaque-capability enable`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：enable OSPF opaque LSA capability
- 合法语法：

  ```text
  opaque-capability enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `ospf`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an OSPF process and enter OSPF view
- 合法语法：

  ```text
  ospf INTEGER<1-65535> [router-id X.X.X.X] [vpn-instance NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPF process 1-65535 | 输入值 |
| INTEGER<1-65535> | `router-id` | OSPF private router ID value | 可选、可组合 |
| router-id | `X.X.X.X` | OSPF Private router ID value | 输入值 |
| INTEGER<1-65535> | `vpn-instance` | VPN instance name | 可选、可组合 |
| vpn-instance | `VPN` | VPN instance name | 输入值 |

## `ospf bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure OSPF BFD timers
- 合法语法：

  ```text
  ospf bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

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

## `ospf bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable OSPF BFD on this interface
- 合法语法：

  ```text
  ospf bfd enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `ospf cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface cost
- 合法语法：

  ```text
  ospf cost INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPF cost 1-65535 | 输入值 |

## `ospf dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface router priority
- 合法语法：

  ```text
  ospf dr-priority INTEGER<0-255>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-255>` | Router priority value | 输入值 |

## `ospf enable`

在接口激活进程和区域，提交后发送 Hello。见[OSPF 案例](../../examples/ospf.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable OSPF on an interface
- 合法语法：

  ```text
  ospf enable INTEGER<1-65535> area X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPF process ID | 输入值 |
| INTEGER<1-65535> | `area` | OSPF area | 关键字 |
| area | `X.X.X.X` | area ID | 输入值 |

## `ospf network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface network type
- 合法语法：

  ```text
  ospf network-type {broadcast|nbma|p2p|p2mp}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `broadcast` | broadcast network | 关键字 |
| 命令后 | `nbma` | non-broadcast multi-access network | 关键字 |
| 命令后 | `p2p` | point-to-point network | 关键字 |
| 命令后 | `p2mp` | point-to-multipoint network | 关键字 |

## `ospf passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：suppress OSPF Hellos on this interface
- 合法语法：

  ```text
  ospf passive
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `ospf timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface dead
- 合法语法：

  ```text
  ospf timer dead INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | dead seconds | 输入值 |

## `ospf timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface hello
- 合法语法：

  ```text
  ospf timer hello INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | hello seconds | 输入值 |

## `ospf timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface retransmit
- 合法语法：

  ```text
  ospf timer retransmit INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | retransmit seconds | 输入值 |

## `ospf timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface transmit-delay
- 合法语法：

  ```text
  ospf timer transmit-delay INTEGER<1-3600>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-3600>` | transmit-delay seconds | 输入值 |

## `reset ospf`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：reset one ospf process so pending runtime settings take effect
- 合法语法：

  ```text
  reset ospf INTEGER<1-65535> process
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | ospf process ID | 输入值 |
| INTEGER<1-65535> | `process` | reset this routing process | 关键字 |

## `reset service ospf`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed ospf routing service
- 合法语法：

  ```text
  reset service ospf [ipv4|ipv6|all]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ipv4` | restart the IPv4 protocol daemon | 可选 |
| 命令后 | `ipv6` | restart the IPv6 protocol daemon | 可选 |
| 命令后 | `all` | restart both address-family daemons | 可选 |

## `stub`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：configure a stub area；configure an OSPFv3 stub area
- 合法语法：

  ```text
  stub [no-summary]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `no-summary` | do not advertise inter-area summaries | 可选 |

**适用视图：`ospfv3-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `no-summary` | suppress inter-area summaries | 可选 |

## `undo bandwidth-reference`

- 类别：配置命令
- 视图：`ospfv3`
- 用途（设备帮助）：restore the OSPFv3 reference bandwidth
- 合法语法：

  ```text
  undo bandwidth-reference
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo nssa`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：restore a normal OSPF area；restore a normal OSPFv3 area
- 合法语法：

  ```text
  undo nssa
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf-area`**

此形式没有额外参数。

**适用视图：`ospfv3-area`**

此形式没有额外参数。

## `undo opaque-capability enable`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：disable OSPF opaque LSA capability
- 合法语法：

  ```text
  undo opaque-capability enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ospf`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an OSPF process
- 合法语法：

  ```text
  undo ospf INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPF process ID | 输入值 |

## `undo ospf bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPF BFD timers
- 合法语法：

  ```text
  undo ospf bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `min-tx-interval` | Minimum transmit interval in milliseconds | 关键字 |
| detect-multiplier / min-tx-interval | `min-rx-interval` | Minimum receive interval in milliseconds | 可选、可组合 |
| min-rx-interval / min-tx-interval | `detect-multiplier` | BFD detection multiplier | 可选、可组合 |
| 命令后 | `min-rx-interval` | Minimum receive interval in milliseconds | 关键字 |
| detect-multiplier / min-rx-interval | `min-tx-interval` | Minimum transmit interval in milliseconds | 可选、可组合 |
| 命令后 | `detect-multiplier` | BFD detection multiplier | 关键字 |

## `undo ospf bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable OSPF BFD on this interface
- 合法语法：

  ```text
  undo ospf bfd enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ospf cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPF interface cost
- 合法语法：

  ```text
  undo ospf cost
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ospf dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface router priority
- 合法语法：

  ```text
  undo ospf dr-priority
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ospf enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable OSPF on an interface
- 合法语法：

  ```text
  undo ospf enable INTEGER<1-65535>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | OSPF process ID | 输入值 |

## `undo ospf network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface network type
- 合法语法：

  ```text
  undo ospf network-type
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ospf passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPF Hellos on this interface
- 合法语法：

  ```text
  undo ospf passive
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ospf timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface dead
- 合法语法：

  ```text
  undo ospf timer dead
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ospf timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface hello
- 合法语法：

  ```text
  undo ospf timer hello
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ospf timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface retransmit
- 合法语法：

  ```text
  undo ospf timer retransmit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo ospf timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface transmit-delay
- 合法语法：

  ```text
  undo ospf timer transmit-delay
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：Ethernet（未选择二/三层）、三层 Ethernet、三层子接口、Eth-Trunk（未选择二/三层）、三层 Eth-Trunk、尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道、LoopBack、Vlanif、Vbdif

此形式没有额外参数。

## `undo stub`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：restore a normal OSPF area；restore a normal OSPFv3 area
- 合法语法：

  ```text
  undo stub
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf-area`**

此形式没有额外参数。

**适用视图：`ospfv3-area`**

此形式没有额外参数。
