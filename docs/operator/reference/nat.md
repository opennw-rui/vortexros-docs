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

## `action no-nat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：permit matching flows without translation
- 合法语法：

  ```text
  action no-nat
  ```

## `action snat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：set SNAT action
- 合法语法：

  ```text
  action snat { pat | no-pat } { interface | address-pool NAME }
  ```

## `action static-nat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：set static prefix translation
- 合法语法：

  ```text
  action static-nat PREFIX
  ```

## `action twice-nat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：translate both source and destination
- 合法语法：

  ```text
  action twice-nat source IP [port PORT] destination IP [port PORT]
  ```

## `address`

- 类别：配置命令
- 视图：`NAT地址池视图`、`NAT地址集视图`
- 用途（设备帮助）：add an IPv4 prefix to this NAT address-pool；add an IPv4 prefix to this NAT address-set
- 合法语法：

  ```text
  address { IP | IP/LEN | IP MASK }
  ```

## `clear nat-policy counters`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：clear nat-policy runtime counters without removing sessions
- 合法语法：

  ```text
  clear nat-policy counters
  ```

## `clear nat-policy sessions`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：clear nat-policy sessions
- 合法语法：

  ```text
  clear nat-policy sessions [name POLICY [rule RULE-ID]]
  ```

## `destination address`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match destination address
- 合法语法：

  ```text
  destination address { IP MASK | IP/LEN | IP }
  ```

## `destination address-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a reusable NAT address-set
- 合法语法：

  ```text
  destination address-set name NAME
  ```

## `destination port`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a transport port or range
- 合法语法：

  ```text
  destination port { PORT | LOW-HIGH }
  ```

## `destination port-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a reusable NAT port-set
- 合法语法：

  ```text
  destination port-set name NAME
  ```

## `destination vpn-instance`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match an exact source/destination VPN instance
- 合法语法：

  ```text
  destination vpn-instance NAME
  ```

## `display nat-policy`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display NAT policy configuration and runtime state
- 合法语法：

  ```text
  display nat-policy { all | name NAME | address-set [NAME] | port-set [NAME] | address-pool [NAME] | runtime | objects | interfaces | statistics [name POLICY] | sessions [FILTERS] | configuration | workers }
  ```

## `hairpin enable`

- 类别：配置命令
- 视图：`NAT策略视图`
- 用途（设备帮助）：allow this policy's published mappings to be used for NAT hairpin
- 合法语法：

  ```text
  hairpin enable
  ```

## `nat-policy`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind a NAT policy to this interface
- 合法语法：

  ```text
  nat-policy NAME { inbound | outbound }
  ```

## `nat-policy address-pool name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create/enter a NAT address-pool
- 合法语法：

  ```text
  nat-policy address-pool name NAME
  ```

## `nat-policy address-set name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create/enter a NAT address-set
- 合法语法：

  ```text
  nat-policy address-set name NAME
  ```

## `nat-policy hairpin enable`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable NAT hairpin translations
- 合法语法：

  ```text
  nat-policy hairpin enable
  ```

## `nat-policy interface-pat-range`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the interface-source PAT port range
- 合法语法：

  ```text
  nat-policy interface-pat-range LOW-HIGH
  ```

## `nat-policy name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create/enter a NAT policy
- 合法语法：

  ```text
  nat-policy name NAME
  ```

## `nat-policy port-set name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create/enter a NAT port-set
- 合法语法：

  ```text
  nat-policy port-set name NAME
  ```

## `nat-policy sessions-per-worker`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the per-worker session capacity
- 合法语法：

  ```text
  nat-policy sessions-per-worker NUMBER
  ```

## `nat-policy timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set a nat-policy session timeout
- 合法语法：

  ```text
  nat-policy timeout CLASS SECONDS
  ```

## `nat-policy x86-tune expire-check-ms`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set nat-policy maintenance interval
- 合法语法：

  ```text
  nat-policy x86-tune expire-check-ms 10..1000
  ```

## `nat-policy x86-tune lru-refresh-ms`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set nat-policy maintenance interval
- 合法语法：

  ```text
  nat-policy x86-tune lru-refresh-ms 10..1000
  ```

## `pat-port-range`

- 类别：配置命令
- 视图：`NAT地址池视图`
- 用途（设备帮助）：set the address-pool PAT allocation range
- 合法语法：

  ```text
  pat-port-range LOW-HIGH
  ```

## `port`

- 类别：配置命令
- 视图：`NAT端口集视图`
- 用途（设备帮助）：add a port or inclusive range to this NAT port-set
- 合法语法：

  ```text
  port { PORT | LOW-HIGH }
  ```

## `priority`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：set rule priority; lower values run first
- 合法语法：

  ```text
  priority 0..9998
  ```

## `protocol`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match an IP protocol
- 合法语法：

  ```text
  protocol { any | tcp | udp | icmp | NUMBER }
  ```

## `session-limit`

- 类别：配置命令
- 视图：`NAT策略视图`
- 用途（设备帮助）：set this policy's session quota
- 合法语法：

  ```text
  session-limit { unlimited | NUMBER }
  ```

## `source address`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match source address
- 合法语法：

  ```text
  source address { IP MASK | IP/LEN | IP }
  ```

## `source address-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a reusable NAT address-set
- 合法语法：

  ```text
  source address-set name NAME
  ```

## `source port`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a transport port or range
- 合法语法：

  ```text
  source port { PORT | LOW-HIGH }
  ```

## `source port-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match a reusable NAT port-set
- 合法语法：

  ```text
  source port-set name NAME
  ```

## `source vpn-instance`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：match an exact source/destination VPN instance
- 合法语法：

  ```text
  source vpn-instance NAME
  ```

## `undo action`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：remove the translation action
- 合法语法：

  ```text
  undo action
  ```

## `undo action snat`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：remove SNAT action
- 合法语法：

  ```text
  undo action snat
  ```

## `undo address`

- 类别：配置命令
- 视图：`NAT地址池视图`、`NAT地址集视图`
- 用途（设备帮助）：remove an IPv4 prefix from this NAT address-pool；remove an IPv4 prefix from this NAT address-set
- 合法语法：

  ```text
  undo address { IP | IP/LEN | IP MASK }
  ```

## `undo destination address`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear destination address match
- 合法语法：

  ```text
  undo destination address
  ```

## `undo destination address-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the reusable NAT address-set match
- 合法语法：

  ```text
  undo destination address-set name
  ```

## `undo destination port`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the transport port match
- 合法语法：

  ```text
  undo destination port
  ```

## `undo destination port-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the reusable NAT port-set match
- 合法语法：

  ```text
  undo destination port-set name
  ```

## `undo destination vpn-instance`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：restore ANY VPN match
- 合法语法：

  ```text
  undo destination vpn-instance
  ```

## `undo hairpin enable`

- 类别：配置命令
- 视图：`NAT策略视图`
- 用途（设备帮助）：prevent this policy's mappings from being used for NAT hairpin
- 合法语法：

  ```text
  undo hairpin enable
  ```

## `undo nat-policy`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind a NAT policy from this interface
- 合法语法：

  ```text
  undo nat-policy [NAME] [{ inbound | outbound }]
  ```

## `undo nat-policy address-pool name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a NAT address-pool
- 合法语法：

  ```text
  undo nat-policy address-pool name NAME
  ```

## `undo nat-policy address-set name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a NAT address-set
- 合法语法：

  ```text
  undo nat-policy address-set name NAME
  ```

## `undo nat-policy hairpin enable`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable NAT hairpin translations
- 合法语法：

  ```text
  undo nat-policy hairpin enable
  ```

## `undo nat-policy interface-pat-range`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default interface PAT range
- 合法语法：

  ```text
  undo nat-policy interface-pat-range
  ```

## `undo nat-policy name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a NAT policy
- 合法语法：

  ```text
  undo nat-policy name NAME
  ```

## `undo nat-policy port-set name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a NAT port-set
- 合法语法：

  ```text
  undo nat-policy port-set name NAME
  ```

## `undo nat-policy sessions-per-worker`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default per-worker session capacity
- 合法语法：

  ```text
  undo nat-policy sessions-per-worker
  ```

## `undo nat-policy timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore one nat-policy session timeout
- 合法语法：

  ```text
  undo nat-policy timeout CLASS
  ```

## `undo nat-policy x86-tune expire-check-ms`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default maintenance interval
- 合法语法：

  ```text
  undo nat-policy x86-tune expire-check-ms
  ```

## `undo nat-policy x86-tune lru-refresh-ms`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default maintenance interval
- 合法语法：

  ```text
  undo nat-policy x86-tune lru-refresh-ms
  ```

## `undo pat-port-range`

- 类别：配置命令
- 视图：`NAT地址池视图`
- 用途（设备帮助）：restore the default address-pool PAT range
- 合法语法：

  ```text
  undo pat-port-range
  ```

## `undo port`

- 类别：配置命令
- 视图：`NAT端口集视图`
- 用途（设备帮助）：remove a port or range from this NAT port-set
- 合法语法：

  ```text
  undo port { PORT | LOW-HIGH }
  ```

## `undo priority`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：derive priority from rule ID
- 合法语法：

  ```text
  undo priority
  ```

## `undo protocol`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：restore ANY protocol match
- 合法语法：

  ```text
  undo protocol
  ```

## `undo session-limit`

- 类别：配置命令
- 视图：`NAT策略视图`
- 用途（设备帮助）：remove this policy's session quota
- 合法语法：

  ```text
  undo session-limit
  ```

## `undo source address`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear source address match
- 合法语法：

  ```text
  undo source address
  ```

## `undo source address-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the reusable NAT address-set match
- 合法语法：

  ```text
  undo source address-set name
  ```

## `undo source port`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the transport port match
- 合法语法：

  ```text
  undo source port
  ```

## `undo source port-set name`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：clear the reusable NAT port-set match
- 合法语法：

  ```text
  undo source port-set name
  ```

## `undo source vpn-instance`

- 类别：配置命令
- 视图：`NAT规则视图`
- 用途（设备帮助）：restore ANY VPN match
- 合法语法：

  ```text
  undo source vpn-instance
  ```
