# ACL、QoS、MQC、MSS 与 NAT


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

## `apply config`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：restart VPP and apply the saved config.cfg configuration
- 合法语法：

  ```text
  apply config
  ```

## `car`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：configure traffic policing (CAR)
- 合法语法：

  ```text
  car cir CIR [kbps|mbps] [pir PIR [kbps|mbps]] [cbs CBS [pbs PBS]] [green|yellow|red pass|discard|remark dscp DSCP]
  ```

## `classifier`

- 类别：配置命令
- 视图：`流策略视图`
- 用途（设备帮助）：bind a classifier to a behavior
- 合法语法：

  ```text
  classifier C behavior B [precedence N]
  ```

## `deny`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：deny matching packets
- 合法语法：

  ```text
  deny
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

## `display acl`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：list ACLs and their rules (name-based)
- 合法语法：

  ```text
  display acl [ipv6] [all | name NAME]
  ```

## `display nat-policy`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display NAT policy configuration and runtime state
- 合法语法：

  ```text
  display nat-policy { all | name NAME | address-set [NAME] | port-set [NAME] | address-pool [NAME] | runtime | objects | interfaces | statistics [name POLICY] | sessions [FILTERS] | configuration | workers }
  ```

## `display traffic behavior`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display MQC traffic behaviors
- 合法语法：

  ```text
  display traffic behavior [user-defined [NAME]]
  ```

## `display traffic classifier`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display MQC traffic classifiers
- 合法语法：

  ```text
  display traffic classifier [user-defined [NAME]]
  ```

## `display traffic policy`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display MQC traffic policies
- 合法语法：

  ```text
  display traffic policy [user-defined [NAME]]
  ```

## `hairpin enable`

- 类别：配置命令
- 视图：`NAT策略视图`
- 用途（设备帮助）：allow this policy's published mappings to be used for NAT hairpin
- 合法语法：

  ```text
  hairpin enable
  ```

## `if-match`

- 类别：配置命令
- 视图：`流分类器视图`
- 用途（设备帮助）：configure a classifier match rule
- 合法语法：

  ```text
  if-match [not] CONDITION
  ```

## `if-match any`

- 类别：配置命令
- 视图：`流分类器视图`
- 用途（设备帮助）：match any packet
- 合法语法：

  ```text
  if-match any
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

## `permit`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：permit matching packets
- 合法语法：

  ```text
  permit
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

## `redirect`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：configure PBR redirect
- 合法语法：

  ```text
  redirect ip-nexthop IP | ipv6-nexthop IPv6 [interface IF] [vpn-instance VRF] | interface IF | vpn-instance VRF
  ```

## `remark dscp`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：remark packet DSCP
- 合法语法：

  ```text
  remark dscp DSCP
  ```

## `rule`

- 类别：配置命令
- 视图：`ACL视图`、`NAT策略视图`、`acl6`
- 用途（设备帮助）：configure an ACL rule；create/enter a NAT rule
- 合法语法：

  ```text
  rule ID
  ```
  ```text
  rule [ID] permit|deny PROTO [source ...] [destination ...] [protocol fields]
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

## `undo acl ipv6 name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an ACL
- 合法语法：

  ```text
  undo acl ipv6 name NAME
  ```

## `undo acl name`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an ACL
- 合法语法：

  ```text
  undo acl name NAME
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

## `undo car`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：remove traffic policing (CAR)
- 合法语法：

  ```text
  undo car
  ```

## `undo classifier`

- 类别：配置命令
- 视图：`流策略视图`
- 用途（设备帮助）：unbind a classifier from the policy
- 合法语法：

  ```text
  undo classifier [NAME]
  ```

## `undo deny`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：undo deny
- 合法语法：

  ```text
  undo deny
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

## `undo if-match`

- 类别：配置命令
- 视图：`流分类器视图`
- 用途（设备帮助）：remove the classifier match rule
- 合法语法：

  ```text
  undo if-match [TYPE]
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

## `undo permit`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：undo permit
- 合法语法：

  ```text
  undo permit
  ```

## `undo port`

- 类别：配置命令
- 视图：`NAT端口集视图`
- 用途（设备帮助）：remove a port or range from this NAT port-set
- 合法语法：

  ```text
  undo port { PORT | LOW-HIGH }
  ```

## `undo precedence`

- 类别：配置命令
- 视图：`流策略视图`
- 用途（设备帮助）：remove classifier precedence from the policy
- 合法语法：

  ```text
  undo precedence
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

## `undo redirect`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：remove PBR redirect
- 合法语法：

  ```text
  undo redirect
  ```

## `undo remark dscp`

- 类别：配置命令
- 视图：`流行为视图`
- 用途（设备帮助）：remove DSCP remarking
- 合法语法：

  ```text
  undo remark dscp
  ```

## `undo rule`

- 类别：配置命令
- 视图：`ACL视图`、`NAT策略视图`、`acl6`
- 用途（设备帮助）：delete a NAT rule；delete an ACL rule
- 合法语法：

  ```text
  undo rule ID
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

## `undo traffic behavior`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a traffic behavior
- 合法语法：

  ```text
  undo traffic behavior NAME
  ```

## `undo traffic classifier`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a traffic classifier
- 合法语法：

  ```text
  undo traffic classifier NAME
  ```

## `undo traffic policy`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a traffic policy
- 合法语法：

  ```text
  undo traffic policy NAME
  ```
