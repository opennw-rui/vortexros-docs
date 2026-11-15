# NAT

[配置指南](../nat.md)

共用命令：[`rule`](policy.md#cmd-rule)、[`undo rule`](policy.md#cmd-undo-rule)、[`apply config`](policy.md#cmd-apply-config)。

## `action dnat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：set DNAT action
- 合法语法：

  ```text
  action dnat IP [port PORT]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | translated destination host | 输入值 |
| IP | `port` | translated destination port | 可选 |
| port | `PORT` | 1..65535 | 输入值 |

## `action no-nat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：permit matching flows without translation
- 合法语法：

  ```text
  action no-nat
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `action snat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：set SNAT action
- 合法语法：

  ```text
  action snat { pat | no-pat } { interface | address-pool NAME }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `pat` | source NAT with port translation | 关键字 |
| no-pat / pat | `interface` | use the egress interface address | 关键字 |
| no-pat / pat | `address-pool` | use a named address pool | 关键字 |
| address-pool | `NAME` | NAT address-pool name | 输入值 |
| 命令后 | `no-pat` | source NAT without port translation | 关键字 |

## `action static-nat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：set static prefix translation
- 合法语法：

  ```text
  action static-nat PREFIX
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PREFIX` | translated IPv4 prefix | 输入值 |

## `action twice-nat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：translate both source and destination
- 合法语法：

  ```text
  action twice-nat source IP [port PORT] destination IP [port PORT]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `source` | translated source | 关键字 |
| source | `SRC-IP` | translated source host | 输入值 |
| SRC-IP | `port` | translated source port | 可选 |
| port | `SRC-PORT` | 1..65535 | 输入值 |
| SRC-IP | `destination` | translated destination | 关键字 |
| destination | `DST-IP` | translated destination host | 输入值 |
| DST-IP | `port` | translated destination port | 可选 |
| port | `DST-PORT` | 1..65535 | 输入值 |

## `address`

- 类别：配置命令
- 视图：`NAT地址池视图`、`NAT地址集视图`
- 用途（设备帮助）：add an IPv4 prefix to this NAT address-pool；add an IPv4 prefix to this NAT address-set
- 合法语法：

  ```text
  address { IP | IP/LEN | IP MASK }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`nat-address-pool`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ADDR` | IPv4 pool prefix | 输入值 |
| ADDR | `MASK` | netmask or prefix length | 输入值、可选 |

**适用视图：`nat-address-set`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ADDR` | IPv4 prefix or host | 输入值 |
| ADDR | `MASK` | netmask or prefix length | 输入值、可选 |

## `clear nat-policy counters`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：clear nat-policy runtime counters without removing sessions
- 合法语法：

  ```text
  clear nat-policy counters
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `clear nat-policy sessions`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：clear nat-policy sessions
- 合法语法：

  ```text
  clear nat-policy sessions [name POLICY [rule RULE-ID]]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | limit to one policy | 可选 |
| name | `POLICY` | policy name | 输入值 |
| POLICY | `rule` | limit to one rule | 可选 |
| rule | `RULE-ID` | 0..9998 | 输入值 |

## `destination address`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match destination address
- 合法语法：

  ```text
  destination address { IP MASK | IP/LEN | IP }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ADDR` | IP address (host or X.X.X.X/M) | 输入值 |
| ADDR | `MASK` | Netmask or prefix length | 输入值、可选 |

## `destination address-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a reusable NAT address-set
- 合法语法：

  ```text
  destination address-set name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAT-ADDRESS-SET` | address-set name | 输入值 |

## `destination port`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a transport port or range
- 合法语法：

  ```text
  destination port { PORT | LOW-HIGH }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PORT-RANGE` | 1..65535 or LOW-HIGH | 输入值 |

## `destination port-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a reusable NAT port-set
- 合法语法：

  ```text
  destination port-set name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAT-PORT-SET` | port-set name | 输入值 |

## `destination vpn-instance`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match an exact source/destination VPN instance
- 合法语法：

  ```text
  destination vpn-instance NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VRF` | vpn-instance name or default | 输入值 |

## `display nat-policy`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display NAT policy configuration and runtime state
- 合法语法：

  ```text
  display nat-policy { all | name NAME | address-set [NAME] | port-set [NAME] | address-pool [NAME] | runtime | objects | interfaces | statistics [name POLICY] | sessions [FILTERS] | configuration | workers }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：配置与运行态，按子命令区分。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `all` | all NAT policies | 关键字 |
| 命令后 | `name` | one NAT policy | 关键字 |
| name | `NAT-POLICY` | policy name | 输入值 |
| 命令后 | `address-set` | NAT address-sets | 关键字 |
| address-set | `NAT-ADDRESS-SET` | address-set name | 输入值、可选 |
| 命令后 | `port-set` | NAT port-sets | 关键字 |
| port-set | `NAT-PORT-SET` | port-set name | 输入值、可选 |
| 命令后 | `address-pool` | NAT address-pools | 关键字 |
| address-pool | `NAT-ADDRESS-POOL` | address-pool name | 输入值、可选 |
| 命令后 | `sessions` | nat-policy runtime sessions | 关键字 |
| sessions | `protocol PROTOCOL` | filter by original IP protocol；tcp, udp, icmp, sctp or 0..255 | 可选、可组合 |
| sessions | `source-ip IPV4` | filter by original source IPv4 address；source IPv4 host address | 可选、可组合 |
| sessions | `destination-ip IPV4` | filter by original destination IPv4 address；destination IPv4 host address | 可选、可组合 |
| sessions | `source-port PORT` | filter by original source port；0..65535 | 可选、可组合 |
| sessions | `destination-port PORT` | filter by original destination port；0..65535 | 可选、可组合 |
| sessions | `worker INDEX` | filter by VPP thread index；VPP worker thread index | 可选、可组合 |
| sessions | `core CPU-ID` | filter by CPU core；logical CPU identifier | 可选、可组合 |
| sessions | `name POLICY` | filter by NAT policy；case-sensitive policy name | 可选、可组合 |
| sessions | `rule RULE-ID` | filter by rule identifier；NAT policy rule identifier | 可选、可组合 |
| sessions | `action` | filter by NAT action | 可选、可组合 |
| action | `no-nat` | no translation | 关键字 |
| action | `static-nat` | static NAT | 关键字 |
| action | `snat-no-pat` | source NAT without PAT | 关键字 |
| action | `snat-pat` | source NAT with PAT | 关键字 |
| action | `dnat` | destination NAT | 关键字 |
| action | `twice-nat` | source and destination NAT | 关键字 |
| sessions | `hairpin` | filter by NAT hairpin state | 可选、可组合 |
| hairpin | `enable` | hairpin sessions only | 关键字 |
| hairpin | `disable` | non-hairpin sessions only | 关键字 |
| 命令后 | `runtime` | runtime policy state and quotas | 关键字 |
| 命令后 | `objects` | runtime sets, pools, members and reference counts | 关键字 |
| 命令后 | `interfaces` | runtime interface attachments | 关键字 |
| 命令后 | `statistics` | per-rule packet and byte statistics | 关键字 |
| statistics | `name` | one policy | 可选 |
| name | `POLICY` | policy name | 输入值 |
| 命令后 | `configuration` | nat-policy runtime configuration | 关键字 |
| 命令后 | `workers` | nat-policy per-worker counters | 关键字 |

## `hairpin enable`

- 类别：配置命令
- 视图：`NAT策略视图`
- 用途（设备帮助）：allow this policy's published mappings to be used for NAT hairpin
- 合法语法：

  ```text
  hairpin enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `nat-policy`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind a NAT policy to this interface
- 合法语法：

  ```text
  nat-policy NAME { inbound | outbound }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
适用分区：interface/ethernet-neutral, interface/ethernet-l3, interface/subif-l3, interface/eth-trunk-neutral, interface/eth-trunk-l3, interface/tunnel-pending, interface/tunnel-gre, interface/tunnel-wireguard, interface/tunnel-amneziawg, interface/loopback, interface/vlanif, interface/vbdif

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAT-POLICY` | NAT policy name | 输入值 |
| NAT-POLICY | `inbound` | inside / ingress | 关键字 |
| NAT-POLICY | `outbound` | outside / egress | 关键字 |

## `nat-policy address-pool name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create/enter a NAT address-pool
- 合法语法：

  ```text
  nat-policy address-pool name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | NAT address-pool name | 输入值 |

## `nat-policy address-set name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create/enter a NAT address-set
- 合法语法：

  ```text
  nat-policy address-set name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | NAT address-set name | 输入值 |

## `nat-policy hairpin enable`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable NAT hairpin translations
- 合法语法：

  ```text
  nat-policy hairpin enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `nat-policy interface-pat-range`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the interface-source PAT port range
- 合法语法：

  ```text
  nat-policy interface-pat-range LOW-HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `LOW-HIGH` | inclusive range; lowest port is 1024 | 输入值 |

## `nat-policy name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create/enter a NAT policy
- 合法语法：

  ```text
  nat-policy name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | NAT policy name | 输入值 |

## `nat-policy port-set name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create/enter a NAT port-set
- 合法语法：

  ```text
  nat-policy port-set name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | NAT port-set name | 输入值 |

## `nat-policy sessions-per-worker`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the per-worker session capacity
- 合法语法：

  ```text
  nat-policy sessions-per-worker NUMBER
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NUMBER` | maximum sessions per worker | 输入值 |

## `nat-policy timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set a nat-policy session timeout
- 合法语法：

  ```text
  nat-policy timeout CLASS SECONDS
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `udp` | udp session timeout | 关键字 |
| icmp / other / tcp-close / tcp-established / tcp-transitory / udp | `SECONDS` | timeout in seconds | 输入值 |
| 命令后 | `tcp-established` | tcp-established session timeout | 关键字 |
| 命令后 | `tcp-transitory` | tcp-transitory session timeout | 关键字 |
| 命令后 | `icmp` | icmp session timeout | 关键字 |
| 命令后 | `other` | other session timeout | 关键字 |
| 命令后 | `tcp-close` | tcp-close session timeout | 关键字 |

## `nat-policy x86-tune expire-check-ms`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set nat-policy maintenance interval
- 合法语法：

  ```text
  nat-policy x86-tune expire-check-ms 10..1000
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `MILLISECONDS` | 10..1000 | 输入值 |

## `nat-policy x86-tune lru-refresh-ms`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set nat-policy maintenance interval
- 合法语法：

  ```text
  nat-policy x86-tune lru-refresh-ms 10..1000
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `MILLISECONDS` | 10..1000 | 输入值 |

## `pat-port-range`

- 类别：配置命令
- 视图：`NAT地址池视图`
- 用途（设备帮助）：set the address-pool PAT allocation range
- 合法语法：

  ```text
  pat-port-range LOW-HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `LOW-HIGH` | inclusive port range; lowest port is 1024 | 输入值 |

## `port`

- 类别：配置命令
- 视图：`NAT端口集视图`
- 用途（设备帮助）：add a port or inclusive range to this NAT port-set
- 合法语法：

  ```text
  port { PORT | LOW-HIGH }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PORT-RANGE` | 1..65535 or LOW-HIGH | 输入值 |

## `priority`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：set rule priority; lower values run first
- 合法语法：

  ```text
  priority 0..9998
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NUMBER` | 0..9998 | 输入值 |

## `protocol`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match an IP protocol
- 合法语法：

  ```text
  protocol { any | tcp | udp | icmp | NUMBER }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `any` | any IP protocol | 关键字 |
| 命令后 | `tcp` | TCP | 关键字 |
| 命令后 | `udp` | UDP | 关键字 |
| 命令后 | `icmp` | ICMP | 关键字 |
| 命令后 | `NUMBER` | IP protocol 0..255 | 输入值 |

## `session-limit`

- 类别：配置命令
- 视图：`NAT策略视图`
- 用途（设备帮助）：set this policy's session quota
- 合法语法：

  ```text
  session-limit { unlimited | NUMBER }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `unlimited` | no per-policy quota | 关键字 |
| 命令后 | `NUMBER` | maximum active sessions | 输入值 |

## `source address`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match source address
- 合法语法：

  ```text
  source address { IP MASK | IP/LEN | IP }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ADDR` | IP address (host or X.X.X.X/M) | 输入值 |
| ADDR | `MASK` | Netmask or prefix length | 输入值、可选 |

## `source address-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a reusable NAT address-set
- 合法语法：

  ```text
  source address-set name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAT-ADDRESS-SET` | address-set name | 输入值 |

## `source port`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a transport port or range
- 合法语法：

  ```text
  source port { PORT | LOW-HIGH }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PORT-RANGE` | 1..65535 or LOW-HIGH | 输入值 |

## `source port-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a reusable NAT port-set
- 合法语法：

  ```text
  source port-set name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAT-PORT-SET` | port-set name | 输入值 |

## `source vpn-instance`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match an exact source/destination VPN instance
- 合法语法：

  ```text
  source vpn-instance NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VRF` | vpn-instance name or default | 输入值 |

## `undo action`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：remove the translation action
- 合法语法：

  ```text
  undo action
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo action snat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：remove SNAT action
- 合法语法：

  ```text
  undo action snat
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo address`

- 类别：配置命令
- 视图：`NAT地址池视图`、`NAT地址集视图`
- 用途（设备帮助）：remove an IPv4 prefix from this NAT address-pool；remove an IPv4 prefix from this NAT address-set
- 合法语法：

  ```text
  undo address { IP | IP/LEN | IP MASK }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`nat-address-pool`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ADDR` | IPv4 pool prefix | 输入值 |
| ADDR | `MASK` | netmask or prefix length | 输入值、可选 |

**适用视图：`nat-address-set`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ADDR` | IPv4 prefix or host | 输入值 |
| ADDR | `MASK` | netmask or prefix length | 输入值、可选 |

## `undo destination address`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear destination address match
- 合法语法：

  ```text
  undo destination address
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo destination address-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the reusable NAT address-set match
- 合法语法：

  ```text
  undo destination address-set name
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo destination port`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the transport port match
- 合法语法：

  ```text
  undo destination port
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo destination port-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the reusable NAT port-set match
- 合法语法：

  ```text
  undo destination port-set name
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo destination vpn-instance`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：restore ANY VPN match
- 合法语法：

  ```text
  undo destination vpn-instance
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo hairpin enable`

- 类别：配置命令
- 视图：`NAT策略视图`
- 用途（设备帮助）：prevent this policy's mappings from being used for NAT hairpin
- 合法语法：

  ```text
  undo hairpin enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo nat-policy`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind a NAT policy from this interface
- 合法语法：

  ```text
  undo nat-policy [NAME] [{ inbound | outbound }]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAT-POLICY\|DIRECTION` | NAT policy name or inbound/outbound | 输入值、可选 |
| NAT-POLICY\|DIRECTION | `DIRECTION` | inbound or outbound | 输入值、可选 |

## `undo nat-policy address-pool name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a NAT address-pool
- 合法语法：

  ```text
  undo nat-policy address-pool name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | NAT address-pool name | 输入值 |

## `undo nat-policy address-set name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a NAT address-set
- 合法语法：

  ```text
  undo nat-policy address-set name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | NAT address-set name | 输入值 |

## `undo nat-policy hairpin enable`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable NAT hairpin translations
- 合法语法：

  ```text
  undo nat-policy hairpin enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo nat-policy interface-pat-range`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default interface PAT range
- 合法语法：

  ```text
  undo nat-policy interface-pat-range
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo nat-policy name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a NAT policy
- 合法语法：

  ```text
  undo nat-policy name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | NAT policy name | 输入值 |

## `undo nat-policy port-set name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a NAT port-set
- 合法语法：

  ```text
  undo nat-policy port-set name NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `NAME` | NAT port-set name | 输入值 |

## `undo nat-policy sessions-per-worker`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default per-worker session capacity
- 合法语法：

  ```text
  undo nat-policy sessions-per-worker
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo nat-policy timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore one nat-policy session timeout
- 合法语法：

  ```text
  undo nat-policy timeout CLASS
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `udp` | UDP | 关键字 |
| 命令后 | `tcp-established` | established TCP | 关键字 |
| 命令后 | `tcp-transitory` | transitory TCP | 关键字 |
| 命令后 | `icmp` | ICMP | 关键字 |
| 命令后 | `other` | other protocols | 关键字 |
| 命令后 | `tcp-close` | TCP close | 关键字 |

## `undo nat-policy x86-tune expire-check-ms`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default maintenance interval
- 合法语法：

  ```text
  undo nat-policy x86-tune expire-check-ms
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo nat-policy x86-tune lru-refresh-ms`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default maintenance interval
- 合法语法：

  ```text
  undo nat-policy x86-tune lru-refresh-ms
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo pat-port-range`

- 类别：配置命令
- 视图：`NAT地址池视图`
- 用途（设备帮助）：restore the default address-pool PAT range
- 合法语法：

  ```text
  undo pat-port-range
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo port`

- 类别：配置命令
- 视图：`NAT端口集视图`
- 用途（设备帮助）：remove a port or range from this NAT port-set
- 合法语法：

  ```text
  undo port { PORT | LOW-HIGH }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PORT-RANGE` | 1..65535 or LOW-HIGH | 输入值 |

## `undo priority`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：derive priority from rule ID
- 合法语法：

  ```text
  undo priority
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo protocol`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：restore ANY protocol match
- 合法语法：

  ```text
  undo protocol
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo session-limit`

- 类别：配置命令
- 视图：`NAT策略视图`
- 用途（设备帮助）：remove this policy's session quota
- 合法语法：

  ```text
  undo session-limit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo source address`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear source address match
- 合法语法：

  ```text
  undo source address
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo source address-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the reusable NAT address-set match
- 合法语法：

  ```text
  undo source address-set name
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo source port`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the transport port match
- 合法语法：

  ```text
  undo source port
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo source port-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the reusable NAT port-set match
- 合法语法：

  ```text
  undo source port-set name
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo source vpn-instance`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：restore ANY VPN match
- 合法语法：

  ```text
  undo source vpn-instance
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
