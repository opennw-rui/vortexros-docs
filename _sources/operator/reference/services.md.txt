# DHCP、LLDP 与 SNMP


## `address prefix`

- 类别：配置命令
- 视图：`DHCPv6地址池视图`
- 用途（设备帮助）：configure a stateful IPv6 allocation prefix
- 合法语法：

  ```text
  address prefix X:X::X/M [life-time VALID PREFERRED]
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

## `display snmp-agent community`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display SNMPv2c read communities
- 合法语法：

  ```text
  display snmp-agent community
  ```

## `display snmp-agent sys-info`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display SNMP system information
- 合法语法：

  ```text
  display snmp-agent sys-info
  ```

## `display snmp-agent target-host`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display SNMP trap receivers
- 合法语法：

  ```text
  display snmp-agent target-host
  ```

## `display snmp-agent usm-user`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display SNMPv3 users
- 合法语法：

  ```text
  display snmp-agent usm-user
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

## `lease`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：configure the IPv4 lease time
- 合法语法：

  ```text
  lease { unlimited | day DAYS [hour HOURS [minute MINUTES]] }
  ```

## `network`

- 类别：配置命令
- 视图：`BGP地址族视图`、`IPv4地址池视图`、`OSPF Area视图`、`RIPng视图`、`RIP视图`
- 用途（设备帮助）：add an OSPF network；advertise a RIPng network；advertise a classful RIP network；configure the IPv4 pool network；originate a BGP network
- 合法语法：

  ```text
  network ADDRESS MASK [route-policy NAME]
  ```
  ```text
  network X.X.X.X
  ```
  ```text
  network X.X.X.X X.X.X.X [description TEXT]
  ```
  ```text
  network X.X.X.X mask { X.X.X.X | INTEGER<0-32> }
  ```
  ```text
  network X:X::X/M
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

## `snmp-agent`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable the SNMP agent
- 合法语法：

  ```text
  snmp-agent
  ```

## `snmp-agent community read`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure an SNMPv2c read community
- 合法语法：

  ```text
  snmp-agent community read COMMUNITY
  ```

## `snmp-agent protocol source-interface`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：bind the SNMP agent to an interface address
- 合法语法：

  ```text
  snmp-agent protocol source-interface { all-interface | IFNAME | vpn-instance VPN IFNAME }
  ```

## `snmp-agent protocol source-status all-interface`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：listen on all IPv4 interfaces in public and VPN instances
- 合法语法：

  ```text
  snmp-agent protocol source-status all-interface
  ```

## `snmp-agent sys-info contact`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set SNMP system contact
- 合法语法：

  ```text
  snmp-agent sys-info contact TEXT
  ```

## `snmp-agent sys-info location`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set SNMP system location
- 合法语法：

  ```text
  snmp-agent sys-info location TEXT
  ```

## `snmp-agent sys-info version v2c`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable SNMP v2c
- 合法语法：

  ```text
  snmp-agent sys-info version v2c
  ```

## `snmp-agent sys-info version v3`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable SNMP v3
- 合法语法：

  ```text
  snmp-agent sys-info version v3
  ```

## `snmp-agent target-host trap address udp-domain`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure an SNMP trap receiver
- 合法语法：

  ```text
  snmp-agent target-host trap address udp-domain ADDRESS udp-port PORT params securityname NAME { v2c | v3 }
  ```

## `snmp-agent trap enable standard`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable standard startup and interface traps
- 合法语法：

  ```text
  snmp-agent trap enable standard
  ```

## `snmp-agent trap source`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：select the trap source interface
- 合法语法：

  ```text
  snmp-agent trap source IFNAME
  ```

## `snmp-agent usm-user v3`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure an SNMPv3 authPriv user
- 合法语法：

  ```text
  snmp-agent usm-user v3 USER authentication-mode sha2-256 AUTH privacy-mode aes128 PRIV
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

## `undo lease`

- 类别：配置命令
- 视图：`IPv4地址池视图`
- 用途（设备帮助）：restore the default lease time
- 合法语法：

  ```text
  undo lease
  ```

## `undo network`

- 类别：配置命令
- 视图：`BGP地址族视图`、`IPv4地址池视图`、`OSPF Area视图`、`RIPng视图`、`RIP视图`
- 用途（设备帮助）：remove a BGP network；remove a RIP network；remove a RIPng network；remove an OSPF network；remove the IPv4 pool network
- 合法语法：

  ```text
  undo network
  ```
  ```text
  undo network ADDRESS MASK
  ```
  ```text
  undo network X.X.X.X
  ```
  ```text
  undo network X.X.X.X X.X.X.X
  ```
  ```text
  undo network X:X::X/M
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

## `undo snmp-agent`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：remove all SNMP configuration and stop the agent
- 合法语法：

  ```text
  undo snmp-agent
  ```

## `undo snmp-agent community read`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an SNMPv2c read community
- 合法语法：

  ```text
  undo snmp-agent community read COMMUNITY
  ```

## `undo snmp-agent protocol source-interface`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：remove the SNMP source interface
- 合法语法：

  ```text
  undo snmp-agent protocol source-interface
  ```

## `undo snmp-agent sys-info contact`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：clear SNMP system contact
- 合法语法：

  ```text
  undo snmp-agent sys-info contact
  ```

## `undo snmp-agent sys-info location`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：clear SNMP system location
- 合法语法：

  ```text
  undo snmp-agent sys-info location
  ```

## `undo snmp-agent sys-info version v2c`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable SNMP v2c
- 合法语法：

  ```text
  undo snmp-agent sys-info version v2c
  ```

## `undo snmp-agent sys-info version v3`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable SNMP v3
- 合法语法：

  ```text
  undo snmp-agent sys-info version v3
  ```

## `undo snmp-agent target-host trap address udp-domain`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete all trap targets at an address
- 合法语法：

  ```text
  undo snmp-agent target-host trap address udp-domain ADDRESS
  ```

## `undo snmp-agent trap enable standard`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable standard traps
- 合法语法：

  ```text
  undo snmp-agent trap enable standard
  ```

## `undo snmp-agent trap source`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：remove the trap source interface
- 合法语法：

  ```text
  undo snmp-agent trap source
  ```

## `undo snmp-agent usm-user v3`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an SNMPv3 user
- 合法语法：

  ```text
  undo snmp-agent usm-user v3 USER
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
