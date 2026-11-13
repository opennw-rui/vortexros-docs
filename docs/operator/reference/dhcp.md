# DHCP

[配置指南](../dhcp.md)

共用命令：[`network`](dynamic-routing.md#cmd-network)。

## `address prefix`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：configure a stateful IPv6 allocation prefix
- 合法语法：

  ```text
  address prefix X:X::X/M [life-time VALID PREFERRED]
  ```

## `dhcp client classless-route enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：install learned classless routes
- 合法语法：

  ```text
  dhcp client classless-route enable
  ```

## `dhcp client default-route enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：install the learned default route
- 合法语法：

  ```text
  dhcp client default-route enable
  ```

## `dhcp client default-route preference`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the DHCP default route preference
- 合法语法：

  ```text
  dhcp client default-route preference INTEGER<1-255>
  ```

## `dhcp client-relay shutdown`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：Suspend DHCP client and relay on this interface
- 合法语法：

  ```text
  dhcp client-relay shutdown
  ```

## `dhcp relay server-ip`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：add a DHCPv4 relay server
- 合法语法：

  ```text
  dhcp relay server-ip X.X.X.X
  ```

## `dhcp select`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：select the DHCPv4 interface role
- 合法语法：

  ```text
  dhcp select { global | interface | relay }
  ```

## `dhcp server dns-list`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure interface-pool DNS servers
- 合法语法：

  ```text
  dhcp server dns-list X.X.X.X [X.X.X.X]
  ```

## `dhcp server domain-name`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure the interface-pool domain name
- 合法语法：

  ```text
  dhcp server domain-name DOMAIN
  ```

## `dhcp server excluded-ip-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：exclude addresses from the interface pool
- 合法语法：

  ```text
  dhcp server excluded-ip-address START [END]
  ```

## `dhcp server gateway-list`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure interface-pool gateway addresses
- 合法语法：

  ```text
  dhcp server gateway-list { X.X.X.X [X.X.X.X] | disable }
  ```

## `dhcp server ip-range`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure the allocatable interface-pool range
- 合法语法：

  ```text
  dhcp server ip-range START END
  ```

## `dhcp server lease`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure the interface-pool lease time
- 合法语法：

  ```text
  dhcp server lease { unlimited | day DAYS [hour HOURS [minute MINUTES]] }
  ```

## `dhcp server static-bind ip-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind an interface-pool address to a client MAC
- 合法语法：

  ```text
  dhcp server static-bind ip-address X.X.X.X mac-address H-H-H
  ```

## `dhcpv6 client information-request`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：obtain non-address information by DHCPv6
- 合法语法：

  ```text
  dhcpv6 client information-request
  ```

## `dhcpv6 client pd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：request an IPv6 delegated prefix
- 合法语法：

  ```text
  dhcpv6 client pd PREFIX-NAME
  ```

## `dhcpv6 client renew`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`接口视图`
- 用途（设备帮助）：renew the DHCPv6 client lease now
- 合法语法：

  ```text
  dhcpv6 client renew
  ```

## `dhcpv6 duid`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：configure the DHCPv6 server identifier type
- 合法语法：

  ```text
  dhcpv6 duid { ll | llt }
  ```

## `dhcpv6 pool`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create or enter an IPv6 address pool
- 合法语法：

  ```text
  dhcpv6 pool NAME
  ```

## `dhcpv6 relay destination`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：add a DHCPv6 relay destination
- 合法语法：

  ```text
  dhcpv6 relay destination X:X::X
  ```

## `dhcpv6 relay interface`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the DHCPv6 relay upper interface
- 合法语法：

  ```text
  dhcpv6 relay interface IF
  ```

## `dhcpv6 server`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable the DHCPv6 server on an interface
- 合法语法：

  ```text
  dhcpv6 server POOL
  ```

## `display dhcp client`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display DHCPv4 client state
- 合法语法：

  ```text
  display dhcp client [interface IF]
  ```

## `display dhcp configuration`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display DHCP configuration summary
- 合法语法：

  ```text
  display dhcp configuration
  ```

## `display dhcp relay`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display DHCPv4 relay state
- 合法语法：

  ```text
  display dhcp relay [interface IF]
  ```

## `display dhcp service`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display DHCP service status
- 合法语法：

  ```text
  display dhcp service [verbose]
  ```

## `display dhcpv6 client`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display DHCPv6 client state
- 合法语法：

  ```text
  display dhcpv6 client [interface IF]
  ```

## `display dhcpv6 client prefix`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display DHCPv6 delegated-prefix state
- 合法语法：

  ```text
  display dhcpv6 client prefix [name PREFIX-NAME]
  ```

## `display dhcpv6 pool`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display IPv6 address pools and server leases
- 合法语法：

  ```text
  display dhcpv6 pool [name NAME] [all | used] [verbose]
  ```

## `display dhcpv6 relay`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display DHCPv6 relay state
- 合法语法：

  ```text
  display dhcpv6 relay [interface IF]
  ```

## `display ip pool`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display IPv4 address pools and server leases
- 合法语法：

  ```text
  display ip pool [name NAME | interface TYPE N] [all | used] [verbose]
  ```

## `display ipv6 pool`

- 类别：只读显示命令
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：display IPv6 pool information and server leases
- 合法语法：

  ```text
  display ipv6 pool [name NAME] [all | used] [verbose]
  ```

## `dns-domain-name`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：configure DNS domain name
- 合法语法：

  ```text
  dns-domain-name VALUE
  ```

## `dns-list`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：configure IPv4 DNS server
- 合法语法：

  ```text
  dns-list X.X.X.X [X.X.X.X ...]
  ```

## `dns-server`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：configure IPv6 DNS server
- 合法语法：

  ```text
  dns-server VALUE
  ```

## `domain-name`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：configure the DHCP domain name
- 合法语法：

  ```text
  domain-name DOMAIN
  ```

## `enable dhcp server`

允许 IPv4/IPv6 DHCP 服务端运行，客户端和中继按接口配置。见[DHCP 案例](../../examples/dhcp.md)。

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enable DHCP servers
- 合法语法：

  ```text
  enable dhcp server
  ```

## `excluded-address`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：exclude an IPv6 address or range from allocation
- 合法语法：

  ```text
  excluded-address START [END]
  ```

## `excluded-ip-address`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：exclude an IPv4 address or range from allocation
- 合法语法：

  ```text
  excluded-ip-address START [END]
  ```

## `gateway-list`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：configure IPv4 gateway address
- 合法语法：

  ```text
  gateway-list X.X.X.X [X.X.X.X ...]
  ```

## `information-refresh`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：set the DHCPv6 information refresh interval
- 合法语法：

  ```text
  information-refresh INTEGER<600-4294967295>
  ```

## `ip address dhcp-alloc`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：obtain the IPv4 address by DHCP
- 合法语法：

  ```text
  ip address dhcp-alloc
  ```

## `ip pool`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create or enter an IPv4 pool
- 合法语法：

  ```text
  ip pool NAME
  ```

## `ipv6 address auto dhcp`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：obtain an IPv6 address by stateful DHCPv6
- 合法语法：

  ```text
  ipv6 address auto dhcp [hint X:X::X]
  ```

## `ipv6 address dhcpv6-prefix`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：derive an interface address from a delegated prefix
- 合法语法：

  ```text
  ipv6 address dhcpv6-prefix PREFIX-NAME SUFFIX/PREFIXLEN
  ```

## `lease`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：configure the IPv4 lease time
- 合法语法：

  ```text
  lease { unlimited | day DAYS [hour HOURS [minute MINUTES]] }
  ```

## `prefix-delegation`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：configure an IPv6 delegated-prefix pool
- 合法语法：

  ```text
  prefix-delegation X:X::X/M INTEGER<1-128> [life-time VALID PREFERRED]
  ```

## `section`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：configure an allocatable IPv4 address range
- 合法语法：

  ```text
  section INTEGER<0-255> START [END]
  ```

## `static-bind ip-address`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：bind an IPv4 address to a client MAC
- 合法语法：

  ```text
  static-bind ip-address X.X.X.X mac-address H-H-H
  ```

## `undo address prefix`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：remove a stateful IPv6 allocation prefix
- 合法语法：

  ```text
  undo address prefix X:X::X/M
  ```

## `undo dhcp client classless-route enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：do not install learned classless routes
- 合法语法：

  ```text
  undo dhcp client classless-route enable
  ```

## `undo dhcp client default-route enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：do not install the learned default route
- 合法语法：

  ```text
  undo dhcp client default-route enable
  ```

## `undo dhcp client-relay shutdown`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：Resume configured DHCP client and relay on this interface
- 合法语法：

  ```text
  undo dhcp client-relay shutdown
  ```

## `undo dhcp relay server-ip`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove a DHCPv4 relay server
- 合法语法：

  ```text
  undo dhcp relay server-ip X.X.X.X
  ```

## `undo dhcp select`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable the DHCPv4 server or relay role
- 合法语法：

  ```text
  undo dhcp select
  ```

## `undo dhcp server dns-list`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove interface-pool DNS servers
- 合法语法：

  ```text
  undo dhcp server dns-list [X.X.X.X]
  ```

## `undo dhcp server domain-name`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove the interface-pool domain name
- 合法语法：

  ```text
  undo dhcp server domain-name
  ```

## `undo dhcp server excluded-ip-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove an interface-pool exclusion
- 合法语法：

  ```text
  undo dhcp server excluded-ip-address START [END]
  ```

## `undo dhcp server gateway-list`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the interface-address gateway default
- 合法语法：

  ```text
  undo dhcp server gateway-list [X.X.X.X]
  ```

## `undo dhcp server ip-range`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore allocation from the interface primary subnet
- 合法语法：

  ```text
  undo dhcp server ip-range
  ```

## `undo dhcp server lease`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default interface-pool lease
- 合法语法：

  ```text
  undo dhcp server lease
  ```

## `undo dhcp server static-bind ip-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove an interface-pool static binding
- 合法语法：

  ```text
  undo dhcp server static-bind ip-address X.X.X.X
  ```

## `undo dhcpv6 client information-request`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable DHCPv6 information requests
- 合法语法：

  ```text
  undo dhcpv6 client information-request
  ```

## `undo dhcpv6 client pd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable DHCPv6 prefix delegation
- 合法语法：

  ```text
  undo dhcpv6 client pd
  ```

## `undo dhcpv6 duid`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：restore the default DHCPv6 server identifier
- 合法语法：

  ```text
  undo dhcpv6 duid
  ```

## `undo dhcpv6 pool`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete an IPv6 address pool
- 合法语法：

  ```text
  undo dhcpv6 pool NAME
  ```

## `undo dhcpv6 relay destination`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove a DHCPv6 relay destination
- 合法语法：

  ```text
  undo dhcpv6 relay destination X:X::X
  ```

## `undo dhcpv6 relay interface`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove a DHCPv6 relay upper interface
- 合法语法：

  ```text
  undo dhcpv6 relay interface IF
  ```

## `undo dhcpv6 server`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable the DHCPv6 server
- 合法语法：

  ```text
  undo dhcpv6 server
  ```

## `undo dns-domain-name`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：remove DNS domain name
- 合法语法：

  ```text
  undo dns-domain-name VALUE
  ```

## `undo dns-list`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：remove IPv4 DNS server
- 合法语法：

  ```text
  undo dns-list [VALUE]
  ```

## `undo dns-server`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：remove IPv6 DNS server
- 合法语法：

  ```text
  undo dns-server VALUE
  ```

## `undo domain-name`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：remove the DHCP domain name
- 合法语法：

  ```text
  undo domain-name
  ```

## `undo enable dhcp server`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：disable DHCP servers
- 合法语法：

  ```text
  undo enable dhcp server
  ```

## `undo excluded-address`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：remove an excluded address or range
- 合法语法：

  ```text
  undo excluded-address START [END]
  ```

## `undo excluded-ip-address`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：remove an excluded address or range
- 合法语法：

  ```text
  undo excluded-ip-address START [END]
  ```

## `undo gateway-list`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：remove IPv4 gateway address
- 合法语法：

  ```text
  undo gateway-list [VALUE]
  ```

## `undo information-refresh`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：restore the default DHCPv6 information refresh interval
- 合法语法：

  ```text
  undo information-refresh
  ```

## `undo ip address dhcp-alloc`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable the DHCPv4 client
- 合法语法：

  ```text
  undo ip address dhcp-alloc
  ```

## `undo ip pool`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete an IPv4 address pool
- 合法语法：

  ```text
  undo ip pool NAME
  ```

## `undo ipv6 address auto dhcp`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable the stateful DHCPv6 client
- 合法语法：

  ```text
  undo ipv6 address auto dhcp
  ```

## `undo ipv6 address dhcpv6-prefix`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove an address derived from a delegated prefix
- 合法语法：

  ```text
  undo ipv6 address dhcpv6-prefix PREFIX-NAME
  ```

## `undo lease`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：restore the default lease time
- 合法语法：

  ```text
  undo lease
  ```

## `undo prefix-delegation`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：remove an IPv6 delegated-prefix pool
- 合法语法：

  ```text
  undo prefix-delegation X:X::X/M INTEGER<1-128>
  ```

## `undo section`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：remove an allocatable IPv4 address range
- 合法语法：

  ```text
  undo section INTEGER<0-255>
  ```

## `undo static-bind ip-address`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：remove a static IPv4 client binding
- 合法语法：

  ```text
  undo static-bind ip-address X.X.X.X
  ```

## `undo vpn-instance`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`、`IPv4地址池视图`、`OSPF视图`
- 用途（设备帮助）：bind the pool to the default network instance；remove OSPF VPN binding
- 合法语法：

  ```text
  undo vpn-instance
  ```

## `vpn-instance`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`、`IPv4地址池视图`、`OSPF视图`
- 用途（设备帮助）：bind OSPF process to a VPN instance；bind the pool to a VPN instance
- 合法语法：

  ```text
  vpn-instance NAME
  ```
