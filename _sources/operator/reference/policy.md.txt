# 策略通用命令

(cmd-apply-config)=
## `apply config`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：restart VPP and apply the saved config.cfg configuration
- 合法语法：

  ```text
  apply config
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `deny`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：deny matching packets
- 合法语法：

  ```text
  deny
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `permit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：permit matching packets
- 合法语法：

  ```text
  permit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

(cmd-rule)=
## `rule`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`ACL视图`、`NAT策略视图`、`acl6`
- CLI 帮助：configure an ACL rule；create/enter a NAT rule
- 合法语法：

  ```text
  rule ID
  ```
  ```text
  rule [ID] permit|deny PROTO [source ...] [destination ...] [protocol fields]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`nat-policy`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ID` | rule ID | 输入值 |

**适用视图：`acl`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-4294967294>` | rule ID | 输入值、可选 |
| INTEGER<0-4294967294> / 命令后 | `permit` | permit matching packets | 关键字 |
| deny / permit | `1-255` | Protocol number 1-255 | 输入值 |
| 1-255=1 / 1-255=10…99 / 1-255=17 / 1-255=6 / ah / eigrp / esp / gre / icmp / igmp / ip / ipinip / ospf / sctp / tcp / udp | `source` | source address match | 可选、可组合 |
| source | `any` | match any source | 关键字 |
| source | `SRC` | source IPv4 host or prefix | 输入值 |
| DST / SRC | `WILDCARD` | Wildcard mask (e.g. 0 or 0.0.0.255) | 输入值、可选 |
| 1-255=1 / 1-255=10…99 / 1-255=17 / 1-255=6 / ah / eigrp / esp / gre / icmp / igmp / ip / ipinip / ospf / sctp / tcp / udp | `destination` | destination address match | 可选、可组合 |
| destination | `any` | match any destination | 关键字 |
| destination | `DST` | destination IPv4 host or prefix | 输入值 |
| 1-255=1 / icmp | `icmp-type` | ICMP type and optional code | 可选、可组合 |
| icmp-type | `TYPE<0-255>` | numeric ICMP type | 输入值 |
| TYPE<0-255> | `CODE<0-255>` | numeric ICMP code | 输入值、可选 |
| icmp-type | `echo` | echo request | 关键字 |
| icmp-type | `echo-reply` | echo reply | 关键字 |
| icmp-type | `fragmentneed-dfset` | fragmentation needed and DF set | 关键字 |
| icmp-type | `host-redirect` | redirect for host | 关键字 |
| icmp-type | `host-tos-redirect` | redirect for TOS and host | 关键字 |
| icmp-type | `host-unreachable` | host unreachable | 关键字 |
| icmp-type | `information-reply` | information reply | 关键字 |
| icmp-type | `information-request` | information request | 关键字 |
| icmp-type | `net-redirect` | redirect for network | 关键字 |
| icmp-type | `net-tos-redirect` | redirect for TOS and network | 关键字 |
| icmp-type | `net-unreachable` | network unreachable | 关键字 |
| icmp-type | `parameter-problem` | parameter problem | 关键字 |
| icmp-type | `port-unreachable` | port unreachable | 关键字 |
| icmp-type | `protocol-unreachable` | protocol unreachable | 关键字 |
| icmp-type | `reassembly-timeout` | fragment reassembly timeout | 关键字 |
| icmp-type | `source-quench` | source quench | 关键字 |
| icmp-type | `source-route-failed` | source route failed | 关键字 |
| icmp-type | `timestamp-reply` | timestamp reply | 关键字 |
| icmp-type | `timestamp-request` | timestamp request | 关键字 |
| icmp-type | `ttl-exceeded` | TTL exceeded | 关键字 |
| 1-255=17 / 1-255=6 / tcp / udp | `source-port` | source L4 port (TCP/UDP only) | 可选、可组合 |
| source-port | `any` | any source port | 关键字 |
| source-port | `eq` | match one source port | 关键字 |
| eq | `PORT` | source port | 输入值 |
| source-port | `range` | match a source port range | 关键字 |
| range | `START` | first source port | 输入值 |
| START | `END` | last source port | 输入值 |
| source-port | `SPORT` | Source port or range (80 or 80-100) | 输入值 |
| 1-255=17 / 1-255=6 / tcp / udp | `destination-port` | destination L4 port (TCP/UDP only) | 可选、可组合 |
| destination-port | `any` | any destination port | 关键字 |
| destination-port | `eq` | match one destination port | 关键字 |
| eq | `PORT` | destination port | 输入值 |
| destination-port | `range` | match a destination port range | 关键字 |
| range | `START` | first destination port | 输入值 |
| START | `END` | last destination port | 输入值 |
| destination-port | `DPORT` | Destination port or range (80 or 80-100) | 输入值 |
| 1-255=6 / tcp | `tcp-flag` | match TCP control flags | 可选、可组合 |
| tcp-flag | `TCP-FLAG` | TCP flag | 输入值 |
| TCP-FLAG | `TCP-FLAG` | additional TCP flag | 输入值、可选、可重复 |
| deny / permit | `ip` | any IPv4 protocol | 关键字 |
| deny / permit | `icmp` | ICMP (1) | 关键字 |
| deny / permit | `igmp` | IGMP (2) | 关键字 |
| deny / permit | `ipinip` | IP-in-IP (4) | 关键字 |
| deny / permit | `tcp` | TCP (6) | 关键字 |
| deny / permit | `udp` | UDP (17) | 关键字 |
| deny / permit | `gre` | GRE (47) — outer IP only | 关键字 |
| deny / permit | `esp` | ESP (50) — outer IP only | 关键字 |
| deny / permit | `ah` | AH (51) — outer IP only | 关键字 |
| deny / permit | `eigrp` | EIGRP (88) | 关键字 |
| deny / permit | `ospf` | OSPF (89) | 关键字 |
| deny / permit | `sctp` | SCTP (132) | 关键字 |
| INTEGER<0-4294967294> / 命令后 | `deny` | deny matching packets | 关键字 |

**适用视图：`acl6`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-4294967294>` | rule ID | 输入值、可选 |
| INTEGER<0-4294967294> / 命令后 | `permit` | permit matching packets | 关键字 |
| deny / permit | `1-255` | Protocol number 1-255 | 输入值 |
| 1-255=17 / 1-255=1…99 / 1-255=58 / 1-255=6 / ah / esp / gre / icmpv6 / ipv6 / ospf / sctp / tcp / udp | `source` | source IPv6 address match | 可选、可组合 |
| source | `any` | match any source | 关键字 |
| source | `SRC` | source IPv6 host or prefix | 输入值 |
| 1-255=17 / 1-255=1…99 / 1-255=58 / 1-255=6 / ah / esp / gre / icmpv6 / ipv6 / ospf / sctp / tcp / udp | `destination` | destination IPv6 address match | 可选、可组合 |
| destination | `any` | match any destination | 关键字 |
| destination | `DST` | destination IPv6 host or prefix | 输入值 |
| 1-255=17 / 1-255=6 / tcp / udp | `source-port` | source L4 port (TCP/UDP only) | 可选、可组合 |
| source-port | `any` | any source port | 关键字 |
| source-port | `eq` | match one source port | 关键字 |
| eq | `PORT` | source port | 输入值 |
| source-port | `range` | match a source port range | 关键字 |
| range | `START` | first source port | 输入值 |
| START | `END` | last source port | 输入值 |
| source-port | `SPORT` | Source port or range (80 or 80-100) | 输入值 |
| 1-255=17 / 1-255=6 / tcp / udp | `destination-port` | destination L4 port (TCP/UDP only) | 可选、可组合 |
| destination-port | `any` | any destination port | 关键字 |
| destination-port | `eq` | match one destination port | 关键字 |
| eq | `PORT` | destination port | 输入值 |
| destination-port | `range` | match a destination port range | 关键字 |
| range | `START` | first destination port | 输入值 |
| START | `END` | last destination port | 输入值 |
| destination-port | `DPORT` | Destination port or range (80 or 80-100) | 输入值 |
| 1-255=58 / icmpv6 | `icmp6-type` | ICMPv6 type and optional code | 可选、可组合 |
| icmp6-type | `TYPE<0-255>` | numeric ICMP type | 输入值 |
| TYPE<0-255> | `CODE<0-255>` | numeric ICMP code | 输入值、可选 |
| icmp6-type | `echo-request` | echo request | 关键字 |
| icmp6-type | `echo-reply` | echo reply | 关键字 |
| icmp6-type | `err-header-field` | erroneous header field | 关键字 |
| icmp6-type | `frag-time-exceeded` | fragment reassembly timeout | 关键字 |
| icmp6-type | `hop-limit-exceeded` | hop limit exceeded | 关键字 |
| icmp6-type | `host-admin-prohib` | administratively prohibited | 关键字 |
| icmp6-type | `host-unreachable` | address unreachable | 关键字 |
| icmp6-type | `neighbor-advertisement` | neighbor advertisement | 关键字 |
| icmp6-type | `neighbor-solicitation` | neighbor solicitation | 关键字 |
| icmp6-type | `network-unreachable` | no route to destination | 关键字 |
| icmp6-type | `packet-too-big` | packet too big | 关键字 |
| icmp6-type | `port-unreachable` | port unreachable | 关键字 |
| icmp6-type | `redirect` | redirect | 关键字 |
| icmp6-type | `router-advertisement` | router advertisement | 关键字 |
| icmp6-type | `router-solicitation` | router solicitation | 关键字 |
| icmp6-type | `unknown-ipv6-opt` | unrecognized IPv6 option | 关键字 |
| icmp6-type | `unknown-next-hdr` | unrecognized next header | 关键字 |
| 1-255=6 / tcp | `tcp-flag` | match TCP control flags | 可选、可组合 |
| tcp-flag | `TCP-FLAG` | TCP flag | 输入值 |
| TCP-FLAG | `TCP-FLAG` | additional TCP flag | 输入值、可选、可重复 |
| deny / permit | `ipv6` | any IPv6 next header | 关键字 |
| deny / permit | `tcp` | TCP (6) | 关键字 |
| deny / permit | `udp` | UDP (17) | 关键字 |
| deny / permit | `gre` | GRE (47) — outer IPv6 only | 关键字 |
| deny / permit | `esp` | ESP (50) — outer IPv6 only | 关键字 |
| deny / permit | `ah` | AH (51) — outer IPv6 only | 关键字 |
| deny / permit | `icmpv6` | ICMPv6 (58) | 关键字 |
| deny / permit | `ospf` | OSPF (89) | 关键字 |
| deny / permit | `sctp` | SCTP (132) | 关键字 |
| INTEGER<0-4294967294> / 命令后 | `deny` | deny matching packets | 关键字 |

## `undo deny`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：undo deny
- 合法语法：

  ```text
  undo deny
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo permit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：undo permit
- 合法语法：

  ```text
  undo permit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo precedence`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流策略视图`
- CLI 帮助：remove classifier precedence from the policy
- 合法语法：

  ```text
  undo precedence
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

(cmd-undo-rule)=
## `undo rule`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`ACL视图`、`NAT策略视图`、`acl6`
- CLI 帮助：delete a NAT rule；delete an ACL rule
- 合法语法：

  ```text
  undo rule ID
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`nat-policy`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ID` | rule ID | 输入值 |

**适用视图：`acl`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-4294967294>` | rule ID | 输入值 |

**适用视图：`acl6`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-4294967294>` | rule ID | 输入值 |
