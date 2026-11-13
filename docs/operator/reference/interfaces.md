# 接口、二层与邻居


## `acl ipv6 name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an IPv6 ACL and enter ACL view
- 合法语法：

  ```text
  acl ipv6 name NAME [advance]
  ```

## `acl name`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an IPv4 ACL and enter ACL view
- 合法语法：

  ```text
  acl name NAME [advance]
  ```

## `amneziawg profile`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter an AmneziaWG profile
- 合法语法：

  ```text
  amneziawg profile NAME
  ```

## `amneziawg-profile`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind an AmneziaWG profile
- 合法语法：

  ```text
  amneziawg-profile NAME
  ```

## `arp proxy`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a Linux proxy-neighbour address range
- 合法语法：

  ```text
  arp proxy X.X.X.X X.X.X.X interface IFNAME
  ```

## `arp static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static ARP entry in a bridge-domain
- 合法语法：

  ```text
  arp static IP MAC bridge-domain BD
  ```

## `arp timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the dynamic IPv4 neighbor aging time
- 合法语法：

  ```text
  arp timeout INTEGER<60-86400>
  ```

## `bfd`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enable BFD or configure a static session
- 合法语法：

  ```text
  bfd [NAME bind peer-ip PEER ...]
  ```

## `bgp`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a BGP instance and enter BGP view
- 合法语法：

  ```text
  bgp ASNUM
  ```

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

## `cpu isolation enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Isolate VPP CPUs at Linux boot
- 合法语法：

  ```text
  cpu isolation enable
  ```

## `cpu main-core`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Pin the VPP main thread
- 合法语法：

  ```text
  cpu main-core NUMBER
  ```

## `cpu worker-cores`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Pin VPP worker threads
- 合法语法：

  ```text
  cpu worker-cores CPU-LIST
  ```

## `dataplane`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：Configure dataplane startup
- 合法语法：

  ```text
  dataplane
  ```

## `description`

- 类别：配置命令
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- 用途（设备帮助）：NVE interface description；bridge-domain description；configure ACL description；configure group description；configure the VLAN description；configure the VPN instance description；configure the interface description；set NAT policy description；set NAT rule description
- 合法语法：

  ```text
  description TEXT
  ```

## `descriptors`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Set RX and TX descriptors
- 合法语法：

  ```text
  descriptors rx COUNT tx COUNT
  ```

## `destination`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：set the peer endpoint and outer VPN；set the tunnel destination and optional underlay VPN
- 合法语法：

  ```text
  destination IP [vpn-instance NAME]
  ```
  ```text
  destination [vpn-instance VPN] [IP port PORT]
  ```

## `device`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Assign a physical PCI port to an Ethernet interface
- 合法语法：

  ```text
  device PCI-BDF name Ethernet NUMBER
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

## `display arp`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the ARP table
- 合法语法：

  ```text
  display arp [all | interface IF | vpn-instance VRF | static | dynamic]
  ```

## `display arp proxy`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display configured proxy-neighbour entries and Linux state
- 合法语法：

  ```text
  display arp proxy
  ```

## `display bridge-domain`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display bridge-domains (service BD + VLAN domains)
- 合法语法：

  ```text
  display bridge-domain [ID]
  ```

## `display dataplane`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：Display active dataplane resources
- 合法语法：

  ```text
  display dataplane [verbose|interfaces|cpu|memory|iommu|tables]
  ```

## `display eth-trunk`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display aggregate interface state
- 合法语法：

  ```text
  display eth-trunk [INTEGER<0-63>]
  ```

## `display flow-steering`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display interface flow-steering configuration and runtime
- 合法语法：

  ```text
  display flow-steering [interface IF]
  ```

## `display interface`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display interface information
- 合法语法：

  ```text
  display interface [IF]
  ```

## `display interface brief`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display brief interface list
- 合法语法：

  ```text
  display interface brief
  ```

## `display interface description`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display interface descriptions
- 合法语法：

  ```text
  display interface description [IF]
  ```

## `display interface hardware offload`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display physical interface hardware offload capabilities and state
- 合法语法：

  ```text
  display interface hardware offload [IF]
  ```

## `display interface statistics`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：per-interface counters
- 合法语法：

  ```text
  display interface statistics [IF]
  ```

## `display lcp`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：show Linux Control Plane interface pairs
- 合法语法：

  ```text
  display lcp
  ```

## `display lldp local`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display local LLDP information
- 合法语法：

  ```text
  display lldp local
  ```

## `display lldp neighbor brief`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display LLDP neighbor brief information
- 合法语法：

  ```text
  display lldp neighbor brief
  ```

## `display lldp neighbor interface`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display LLDP neighbor information on an interface
- 合法语法：

  ```text
  display lldp neighbor interface IF
  ```

## `display mac-address`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the MAC address table
- 合法语法：

  ```text
  display mac-address [MAC | vlan VLAN-ID | bridge-domain BD | interface IF | static | dynamic]
  ```

## `display vlan`

查询成员、链路和标签处理。U/D 表示端口状态，TG/UT 表示带标签或不带标签。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VLAN information
- 合法语法：

  ```text
  display vlan [VLAN-ID | summary]
  ```

## `display vlan summary`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VLAN summary
- 合法语法：

  ```text
  display vlan summary
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

## `encapsulation`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure sub-interface encapsulation
- 合法语法：

  ```text
  encapsulation { dot1q | dot1ad } vid VLAN-ID | encapsulation qinq vid PE-VID ce-vid CE-VID
  ```

## `esi`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure the Ethernet segment identifier
- 合法语法：

  ```text
  esi XXXX.XXXX.XXXX.XXXX.XXXX
  ```

## `eth-trunk`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：join an aggregate interface
- 合法语法：

  ```text
  eth-trunk INTEGER<0-63>
  ```

## `evpn`

- 类别：配置命令
- 视图：`BD视图`
- 用途（设备帮助）：enter the EVPN view for this bridge-domain
- 合法语法：

  ```text
  evpn
  ```

## `flow-steering enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable tunnel-aware ingress worker steering
- 合法语法：

  ```text
  flow-steering enable
  ```

## `gre key`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the GRE key (optional)
- 合法语法：

  ```text
  gre key KEY
  ```

## `hardware offload`

- 类别：配置命令
- 视图：`dataplane-if`、`接口视图`
- 用途（设备帮助）：restore default hardware offload use
- 合法语法：

  ```text
  hardware offload OFFLOAD [OFFLOAD ...]
  ```

## `interface`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter the interface view
- 合法语法：

  ```text
  interface { Eth-Trunk N | LoopBack N | Tunnel N | Vlanif N | Vbdif N | eth N | IFNAME }
  ```

## `interface range`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter a batch interface view
- 合法语法：

  ```text
  interface range IF1 to IF2
  ```

## `interface user-defined`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：Preconfigure an interface before it is present
- 合法语法：

  ```text
  interface user-defined NAME
  ```

## `iommu enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Enable IOMMU at Linux boot
- 合法语法：

  ```text
  iommu enable
  ```

## `ip address`

为三层接口设置地址。提交后形成直连网段，修改已有地址可能影响 SSH、邻居和路由。见[静态路由案例](../../examples/static-route.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv4 address
- 合法语法：

  ```text
  ip address IP MASK [sub]
  ```

## `ip address dhcp-alloc`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：obtain the IPv4 address by DHCP
- 合法语法：

  ```text
  ip address dhcp-alloc
  ```

## `ip binding vpn-instance`

把接口划入指定 VPN 的路由域。调整前规划该实例的地址、网关和路由，调整后从同一 VPN 验证连通性。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind the interface to a VPN instance
- 合法语法：

  ```text
  ip binding vpn-instance NAME
  ```

## `ip ip-prefix`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：configure an IP prefix list entry
- 合法语法：

  ```text
  ip ip-prefix NAME [index SEQ] {permit|deny} IP MASK [greater-equal GE] [less-equal LE]
  ```

## `ip ipv6-prefix`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：configure an IPv6 prefix list entry
- 合法语法：

  ```text
  ip ipv6-prefix NAME [index SEQ] {permit|deny} IPV6 PREFIX-LENGTH [greater-equal GE] [less-equal LE]
  ```

## `ip pool`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create or enter an IPv4 pool
- 合法语法：

  ```text
  ip pool NAME
  ```

## `ip urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure ip uRPF on the interface
- 合法语法：

  ```text
  ip urpf { loose | strict | disable }
  ```

## `ip vpn-instance`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a VPN instance and enter its view
- 合法语法：

  ```text
  ip vpn-instance NAME
  ```

## `ipv6 address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv6 address
- 合法语法：

  ```text
  ipv6 address IP PREFIXLEN
  ```

## `ipv6 address auto dhcp`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：obtain an IPv6 address by stateful DHCPv6
- 合法语法：

  ```text
  ipv6 address auto dhcp [hint X:X::X]
  ```

## `ipv6 address auto global default`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：derive global IPv6 addresses and the default route from router advertisements
- 合法语法：

  ```text
  ipv6 address auto global default
  ```

## `ipv6 address auto slaac`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：derive IPv6 addresses from router advertisements
- 合法语法：

  ```text
  ipv6 address auto slaac
  ```

## `ipv6 address dhcpv6-prefix`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：derive an interface address from a delegated prefix
- 合法语法：

  ```text
  ipv6 address dhcpv6-prefix PREFIX-NAME SUFFIX/PREFIXLEN
  ```

## `ipv6 nd ra default-route enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：install default routes learned from router advertisements
- 合法语法：

  ```text
  ipv6 nd ra default-route enable
  ```

## `ipv6 route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter an IPv6 static route group
- 合法语法：

  ```text
  ipv6 route-static group name GROUP
  ```

## `ipv6 urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure ipv6 uRPF on the interface
- 合法语法：

  ```text
  ipv6 urpf { loose | strict | disable }
  ```

## `isis`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an IS-IS process and enter process view
- 合法语法：

  ```text
  isis INTEGER<1-65535> [vpn-instance NAME]
  ```

## `isis bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure ISIS BFD timers
- 合法语法：

  ```text
  isis bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

## `isis bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable ISIS BFD on this interface
- 合法语法：

  ```text
  isis bfd enable
  ```

## `isis circuit-level`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the IS-IS circuit level
- 合法语法：

  ```text
  isis circuit-level {level-1|level-1-2|level-2}
  ```

## `isis circuit-type p2p`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the IS-IS link to point-to-point
- 合法语法：

  ```text
  isis circuit-type p2p
  ```

## `isis cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set IS-IS interface metric
- 合法语法：

  ```text
  isis cost INTEGER<1-16777215>
  ```

## `isis enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable IS-IS on an interface
- 合法语法：

  ```text
  isis enable INTEGER<1-65535>
  ```

## `isis ipv6-enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable IPv6 IS-IS on an interface
- 合法语法：

  ```text
  isis ipv6-enable INTEGER<1-65535>
  ```

## `isis passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：make IS-IS interface passive
- 合法语法：

  ```text
  isis passive
  ```

## `isis priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set IS-IS interface priority
- 合法语法：

  ```text
  isis priority INTEGER<0-127>
  ```

## `l2 binding vlan`

- 类别：配置命令
- 视图：`BD视图`
- 用途（设备帮助）：bind a local VLAN into this bridge-domain
- 合法语法：

  ```text
  l2 binding vlan VLAN-ID
  ```

## `lcp host`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：create a same-name Linux control-plane interface mapping
- 合法语法：

  ```text
  lcp host HOST-IF [tap|tun]
  ```

## `lldp enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable LLDP on this physical interface
- 合法语法：

  ```text
  lldp enable
  ```

## `mac-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the interface MAC address
- 合法语法：

  ```text
  mac-address MAC
  ```

## `mac-address aging-time`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the dynamic MAC address aging time
- 合法语法：

  ```text
  mac-address aging-time INTEGER<60-15300>
  ```

## `mac-address learn-limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Set the VPP global dynamic MAC learning limit
- 合法语法：

  ```text
  mac-address learn-limit INTEGER<1-2147483647>
  ```

## `mac-address static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static MAC address
- 合法语法：

  ```text
  mac-address static MAC IF bridge-domain BD
  ```

## `memory hugepages`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Reserve huge pages at boot
- 合法语法：

  ```text
  memory hugepages size { 2M | 1G } count NUMBER
  ```

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

## `mtu`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the interface MTU
- 合法语法：

  ```text
  mtu N
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

## `neighbor ipv4 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Set the Linux and VPP IPv4 neighbor limit
- 合法语法：

  ```text
  neighbor ipv4 limit INTEGER<4-2147483647>
  ```

## `neighbor ipv6 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Set the Linux and VPP IPv6 neighbor limit
- 合法语法：

  ```text
  neighbor ipv6 limit INTEGER<4-2147483647>
  ```

## `ospf`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an OSPF process and enter OSPF view
- 合法语法：

  ```text
  ospf INTEGER<1-65535> [router-id X.X.X.X] [vpn-instance NAME]
  ```

## `ospf bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure OSPF BFD timers
- 合法语法：

  ```text
  ospf bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

## `ospf bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable OSPF BFD on this interface
- 合法语法：

  ```text
  ospf bfd enable
  ```

## `ospf cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface cost
- 合法语法：

  ```text
  ospf cost INTEGER<1-65535>
  ```

## `ospf dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface router priority
- 合法语法：

  ```text
  ospf dr-priority INTEGER<0-255>
  ```

## `ospf enable`

在接口激活进程和区域，提交后发送 Hello。见[OSPF 案例](../../examples/ospf.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable OSPF on an interface
- 合法语法：

  ```text
  ospf enable INTEGER<1-65535> area X.X.X.X
  ```

## `ospf network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface network type
- 合法语法：

  ```text
  ospf network-type {broadcast|nbma|p2p|p2mp}
  ```

## `ospf passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：suppress OSPF Hellos on this interface
- 合法语法：

  ```text
  ospf passive
  ```

## `ospf timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface dead
- 合法语法：

  ```text
  ospf timer dead INTEGER<1-65535>
  ```

## `ospf timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface hello
- 合法语法：

  ```text
  ospf timer hello INTEGER<1-65535>
  ```

## `ospf timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface retransmit
- 合法语法：

  ```text
  ospf timer retransmit INTEGER<1-65535>
  ```

## `ospf timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface transmit-delay
- 合法语法：

  ```text
  ospf timer transmit-delay INTEGER<1-3600>
  ```

## `ospfv3`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：create an OSPFv3 process and enter its view；enable OSPFv3 on an interface
- 合法语法：

  ```text
  ospfv3 INTEGER<1-65535> [router-id X.X.X.X] [vpn-instance NAME]
  ```
  ```text
  ospfv3 INTEGER<1-65535> area X.X.X.X
  ```

## `ospfv3 bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure OSPFV3 BFD timers
- 合法语法：

  ```text
  ospfv3 bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

## `ospfv3 bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable OSPFV3 BFD on this interface
- 合法语法：

  ```text
  ospfv3 bfd enable
  ```

## `ospfv3 cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFv3 interface cost
- 合法语法：

  ```text
  ospfv3 cost INTEGER<1-65535>
  ```

## `ospfv3 dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFv3 interface router priority
- 合法语法：

  ```text
  ospfv3 dr-priority INTEGER<0-255>
  ```

## `ospfv3 network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFv3 interface network type
- 合法语法：

  ```text
  ospfv3 network-type {broadcast|p2p|p2mp}
  ```

## `ospfv3 timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFV3 interface dead
- 合法语法：

  ```text
  ospfv3 timer dead INTEGER<1-65535>
  ```

## `ospfv3 timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFV3 interface hello
- 合法语法：

  ```text
  ospfv3 timer hello INTEGER<1-65535>
  ```

## `ospfv3 timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFV3 interface retransmit
- 合法语法：

  ```text
  ospfv3 timer retransmit INTEGER<1-65535>
  ```

## `ospfv3 timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPFV3 interface transmit-delay
- 合法语法：

  ```text
  ospfv3 timer transmit-delay INTEGER<1-3600>
  ```

## `port default vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the access port default VLAN
- 合法语法：

  ```text
  port default vlan VLAN-ID
  ```

## `port link-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the L2 port link type
- 合法语法：

  ```text
  port link-type { access | dot1q-tunnel | trunk }
  ```

## `port trunk allow-pass vlan`

为当前 trunk 放行指定 VLAN。对端也须允许该 VLAN。撤销会中断相应 VLAN 经此口的转发。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：allow VLANs on a trunk port
- 合法语法：

  ```text
  port trunk allow-pass vlan { VLAN-LIST | all }
  ```

## `port trunk pvid vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the trunk native VLAN
- 合法语法：

  ```text
  port trunk pvid vlan VLAN-ID
  ```

## `portswitch`

把接口设为二层交换口。先处理已有三层地址及依赖。见[VLAN 网关案例](../../examples/vlan-gateway.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：switch the aggregate to Layer 2 mode；switch the interface to L2 mode
- 合法语法：

  ```text
  portswitch
  ```

## `privatekey`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set or generate the AmneziaWG private key；set or generate the WireGuard private key
- 合法语法：

  ```text
  privatekey { STRING<44> | auto | cipher CIPHERTEXT }
  ```

## `qos lr`

- 类别：配置命令
- 视图：`VLAN视图`、`接口视图`
- 用途（设备帮助）：configure interface or VLAN rate limit (2-rate 3-color)
- 合法语法：

  ```text
  qos lr { inbound | outbound } cir CIR [pir PIR] [cbs CBS] [pbs PBS] [green|yellow|red pass|discard]
  ```

## `queues`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Set RX and TX queues
- 合法语法：

  ```text
  queues rx COUNT tx COUNT
  ```

## `rip`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a RIP process and enter process view
- 合法语法：

  ```text
  rip INTEGER<1-65535> [vpn-instance NAME]
  ```

## `rip bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure RIP BFD timers
- 合法语法：

  ```text
  rip bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

## `rip bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable RIP BFD on this interface
- 合法语法：

  ```text
  rip bfd enable
  ```

## `ripng`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a RIP process and enter process view
- 合法语法：

  ```text
  ripng INTEGER<1-65535> [vpn-instance NAME]
  ```

## `route-policy`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a route policy node and enter its view
- 合法语法：

  ```text
  route-policy NAME {permit|deny} node INTEGER<1-65535>
  ```

## `route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter an IPv4 static route group
- 合法语法：

  ```text
  route-static group name GROUP
  ```

## `shutdown`

- 类别：配置命令
- 视图：`BFD会话视图`、`接口视图`
- 用途（设备帮助）：shut down the interface；shutdown
- 合法语法：

  ```text
  shutdown
  ```

## `source`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：pin the peer outer source address；set AmneziaWG source and underlay VPN；set NVE source VTEP address and optional underlay VPN；set WireGuard source and underlay VPN；set the tunnel source IP address
- 合法语法：

  ```text
  source IP
  ```
  ```text
  source IP [vpn-instance NAME]
  ```
  ```text
  source vpn-instance NAME [IP]
  ```

## `source-port`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set fixed AmneziaWG server listen port；set fixed WireGuard server listen port
- 合法语法：

  ```text
  source-port PORT
  ```

## `statistic enable`

- 类别：配置命令
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- 用途（设备帮助）：enable counters for this NAT policy；enable counters for this NAT rule；enable detailed interface packet statistics
- 合法语法：

  ```text
  statistic enable
  ```

## `switchport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：switch the interface to L2 mode
- 合法语法：

  ```text
  switchport
  ```

## `tcp mss`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clamp TCP SYN MSS on this L3 interface
- 合法语法：

  ```text
  tcp mss { clamp | MSS }
  ```

## `traffic behavior`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a traffic behavior and enter its view
- 合法语法：

  ```text
  traffic behavior NAME
  ```

## `traffic classifier`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a traffic classifier and enter its view
- 合法语法：

  ```text
  traffic classifier NAME [operator and|or]
  ```

## `traffic policy`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a traffic policy and enter its view
- 合法语法：

  ```text
  traffic policy NAME
  ```

## `traffic-filter`

在指定方向挂载 ACL。同地址族未匹配流量默认丢弃。见[ACL 案例](../../examples/acl.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：apply an ACL to interface traffic
- 合法语法：

  ```text
  traffic-filter { inbound | outbound } acl NAME
  ```

## `traffic-policy`

- 类别：配置命令
- 视图：`VLAN视图`、`接口视图`
- 用途（设备帮助）：apply an MQC policy to traffic in this VLAN；apply an MQC traffic policy
- 合法语法：

  ```text
  traffic-policy NAME inbound
  ```
  ```text
  traffic-policy NAME { inbound | outbound }
  ```

## `trunkport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：add physical member ports
- 合法语法：

  ```text
  trunkport INTERFACE [to INTERFACE]
  ```

## `tunnel-protocol`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the tunnel encapsulation protocol
- 合法语法：

  ```text
  tunnel-protocol { gre | ipv4-ipv4 | ipv6-ipv4 | ipv4-ipv6 | ipv6-ipv6 | wireguard | amneziawg }
  ```

## `undo amneziawg-profile`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind an AmneziaWG profile
- 合法语法：

  ```text
  undo amneziawg-profile
  ```

## `undo arp proxy`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a Linux proxy-neighbour address range
- 合法语法：

  ```text
  undo arp proxy X.X.X.X X.X.X.X interface IFNAME
  ```

## `undo arp static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static ARP entry
- 合法语法：

  ```text
  undo arp static IP MAC bridge-domain BD
  ```

## `undo arp timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default IPv4 neighbor aging time
- 合法语法：

  ```text
  undo arp timeout
  ```

## `undo bfd`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete a BFD session or disable BFD
- 合法语法：

  ```text
  undo bfd [NAME]
  ```

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

## `undo cpu isolation enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu isolation enable
  ```

## `undo cpu main-core`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu main-core
  ```

## `undo cpu worker-cores`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu worker-cores
  ```

## `undo description`

- 类别：配置命令
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- 用途（设备帮助）：clear ACL description；clear NAT policy description；clear NAT rule description；clear NVE description；clear bridge-domain description；delete group description；delete the VLAN description；delete the VPN instance description；delete the interface description
- 合法语法：

  ```text
  undo description
  ```

## `undo descriptors`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Restore default descriptors
- 合法语法：

  ```text
  undo descriptors
  ```

## `undo destination`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：clear the peer endpoint；clear the tunnel destination IP address
- 合法语法：

  ```text
  undo destination
  ```

## `undo device`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove a PCI port assignment
- 合法语法：

  ```text
  undo device PCI-BDF
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

## `undo enable dhcp server`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：disable DHCP servers
- 合法语法：

  ```text
  undo enable dhcp server
  ```

## `undo encapsulation`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove the sub-interface encapsulation
- 合法语法：

  ```text
  undo encapsulation
  ```

## `undo esi`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove the Ethernet segment identifier
- 合法语法：

  ```text
  undo esi
  ```

## `undo eth-trunk`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：leave the aggregate interface
- 合法语法：

  ```text
  undo eth-trunk [INTEGER<0-63>]
  ```

## `undo flow-steering enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ingress worker steering on the interface
- 合法语法：

  ```text
  undo flow-steering enable
  ```

## `undo gre key`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clear the GRE key
- 合法语法：

  ```text
  undo gre key
  ```

## `undo hardware offload`

- 类别：配置命令
- 视图：`dataplane-if`、`接口视图`
- 用途（设备帮助）：disable hardware offload use
- 合法语法：

  ```text
  undo hardware offload OFFLOAD [OFFLOAD ...]
  ```

## `undo interface`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an interface
- 合法语法：

  ```text
  undo interface IFNAME
  ```

## `undo iommu enable`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo iommu enable
  ```

## `undo ip address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete an IPv4 address
- 合法语法：

  ```text
  undo ip address [IP MASK]
  ```

## `undo ip address dhcp-alloc`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable the DHCPv4 client
- 合法语法：

  ```text
  undo ip address dhcp-alloc
  ```

## `undo ip binding vpn-instance`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind the interface from a VPN instance
- 合法语法：

  ```text
  undo ip binding vpn-instance
  ```

## `undo ip pool`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete an IPv4 address pool
- 合法语法：

  ```text
  undo ip pool NAME
  ```

## `undo ip urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ip uRPF on the interface
- 合法语法：

  ```text
  undo ip urpf
  ```

## `undo ipv6 address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete an IPv6 address
- 合法语法：

  ```text
  undo ipv6 address [IP PREFIXLEN]
  ```

## `undo ipv6 address auto dhcp`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable the stateful DHCPv6 client
- 合法语法：

  ```text
  undo ipv6 address auto dhcp
  ```

## `undo ipv6 address auto global default`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable automatic global IPv6 addresses and RA default routes
- 合法语法：

  ```text
  undo ipv6 address auto global default
  ```

## `undo ipv6 address auto slaac`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable derive IPv6 addresses from router advertisements
- 合法语法：

  ```text
  undo ipv6 address auto slaac
  ```

## `undo ipv6 address dhcpv6-prefix`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove an address derived from a delegated prefix
- 合法语法：

  ```text
  undo ipv6 address dhcpv6-prefix PREFIX-NAME
  ```

## `undo ipv6 nd ra default-route enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable install default routes learned from router advertisements
- 合法语法：

  ```text
  undo ipv6 nd ra default-route enable
  ```

## `undo ipv6 route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete an IPv6 static route group
- 合法语法：

  ```text
  undo ipv6 route-static group name GROUP
  ```

## `undo ipv6 urpf`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ipv6 uRPF on the interface
- 合法语法：

  ```text
  undo ipv6 urpf
  ```

## `undo isis bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore ISIS BFD timers
- 合法语法：

  ```text
  undo isis bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

## `undo isis bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ISIS BFD on this interface
- 合法语法：

  ```text
  undo isis bfd enable
  ```

## `undo isis circuit-level`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the IS-IS circuit level
- 合法语法：

  ```text
  undo isis circuit-level
  ```

## `undo isis circuit-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the IS-IS link type
- 合法语法：

  ```text
  undo isis circuit-type
  ```

## `undo isis cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore IS-IS interface metric
- 合法语法：

  ```text
  undo isis cost
  ```

## `undo isis enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable IS-IS on an interface
- 合法语法：

  ```text
  undo isis enable
  ```

## `undo isis ipv6-enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable IPv6 IS-IS on an interface
- 合法语法：

  ```text
  undo isis ipv6-enable INTEGER<1-65535>
  ```

## `undo isis passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore IS-IS interface
- 合法语法：

  ```text
  undo isis passive
  ```

## `undo isis priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore IS-IS interface priority
- 合法语法：

  ```text
  undo isis priority
  ```

## `undo l2 binding vlan`

- 类别：配置命令
- 视图：`BD视图`
- 用途（设备帮助）：remove VLAN binding from this bridge-domain
- 合法语法：

  ```text
  undo l2 binding vlan
  ```

## `undo lcp host`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete the Linux control-plane interface mapping
- 合法语法：

  ```text
  undo lcp host
  ```

## `undo lldp enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable LLDP on this physical interface
- 合法语法：

  ```text
  undo lldp enable
  ```

## `undo mac-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default interface MAC address
- 合法语法：

  ```text
  undo mac-address
  ```

## `undo mac-address aging-time`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default dynamic MAC address aging time
- 合法语法：

  ```text
  undo mac-address aging-time
  ```

## `undo mac-address learn-limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Restore the default table limit
- 合法语法：

  ```text
  undo mac-address learn-limit
  ```

## `undo mac-address static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static MAC address
- 合法语法：

  ```text
  undo mac-address static MAC IF bridge-domain BD
  ```

## `undo memory hugepages`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Remove this dataplane setting
- 合法语法：

  ```text
  undo memory hugepages
  ```

## `undo mode`

- 类别：配置命令
- 视图：`dataplane-if`、`接口视图`
- 用途（设备帮助）：Restore Linux kernel mode；restore manual aggregate mode
- 合法语法：

  ```text
  undo mode
  ```

## `undo mtu`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default interface MTU
- 合法语法：

  ```text
  undo mtu
  ```

## `undo nat-policy`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind a NAT policy from this interface
- 合法语法：

  ```text
  undo nat-policy [NAME] [{ inbound | outbound }]
  ```

## `undo neighbor ipv4 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Restore the default table limit
- 合法语法：

  ```text
  undo neighbor ipv4 limit
  ```

## `undo neighbor ipv6 limit`

- 类别：配置命令
- 视图：`dataplane`
- 用途（设备帮助）：Restore the default table limit
- 合法语法：

  ```text
  undo neighbor ipv6 limit
  ```

## `undo ospf bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPF BFD timers
- 合法语法：

  ```text
  undo ospf bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

## `undo ospf bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable OSPF BFD on this interface
- 合法语法：

  ```text
  undo ospf bfd enable
  ```

## `undo ospf cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPF interface cost
- 合法语法：

  ```text
  undo ospf cost
  ```

## `undo ospf dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface router priority
- 合法语法：

  ```text
  undo ospf dr-priority
  ```

## `undo ospf enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable OSPF on an interface
- 合法语法：

  ```text
  undo ospf enable INTEGER<1-65535>
  ```

## `undo ospf network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface network type
- 合法语法：

  ```text
  undo ospf network-type
  ```

## `undo ospf passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPF Hellos on this interface
- 合法语法：

  ```text
  undo ospf passive
  ```

## `undo ospf timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface dead
- 合法语法：

  ```text
  undo ospf timer dead
  ```

## `undo ospf timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface hello
- 合法语法：

  ```text
  undo ospf timer hello
  ```

## `undo ospf timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface retransmit
- 合法语法：

  ```text
  undo ospf timer retransmit
  ```

## `undo ospf timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface transmit-delay
- 合法语法：

  ```text
  undo ospf timer transmit-delay
  ```

## `undo ospfv3`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：delete an OSPFv3 process；disable OSPFv3 on an interface
- 合法语法：

  ```text
  undo ospfv3 INTEGER<1-65535>
  ```
  ```text
  undo ospfv3 INTEGER<1-65535> area X.X.X.X
  ```

## `undo ospfv3 bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPFV3 BFD timers
- 合法语法：

  ```text
  undo ospfv3 bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

## `undo ospfv3 bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable OSPFV3 BFD on this interface
- 合法语法：

  ```text
  undo ospfv3 bfd enable
  ```

## `undo ospfv3 cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPFv3 interface cost
- 合法语法：

  ```text
  undo ospfv3 cost
  ```

## `undo ospfv3 dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPFv3 interface router priority
- 合法语法：

  ```text
  undo ospfv3 dr-priority
  ```

## `undo ospfv3 network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPFv3 interface network type
- 合法语法：

  ```text
  undo ospfv3 network-type
  ```

## `undo ospfv3 timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPFV3 interface dead
- 合法语法：

  ```text
  undo ospfv3 timer dead
  ```

## `undo ospfv3 timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPFV3 interface hello
- 合法语法：

  ```text
  undo ospfv3 timer hello
  ```

## `undo ospfv3 timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPFV3 interface retransmit
- 合法语法：

  ```text
  undo ospfv3 timer retransmit
  ```

## `undo ospfv3 timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPFV3 interface transmit-delay
- 合法语法：

  ```text
  undo ospfv3 timer transmit-delay
  ```

## `undo port default vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the access port default VLAN to 1
- 合法语法：

  ```text
  undo port default vlan
  ```

## `undo port link-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore portswitch-only L2 mode (access VLAN 1)
- 合法语法：

  ```text
  undo port link-type
  ```

## `undo port trunk allow-pass vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove allowed VLANs from a trunk port
- 合法语法：

  ```text
  undo port trunk allow-pass vlan { VLAN-LIST | all }
  ```

## `undo port trunk pvid vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the trunk native VLAN to 1
- 合法语法：

  ```text
  undo port trunk pvid vlan [VLAN-ID]
  ```

## `undo portswitch`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：return the aggregate to Layer 3 mode；return the interface to L3 mode
- 合法语法：

  ```text
  undo portswitch
  ```

## `undo privatekey`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clear AmneziaWG key；clear WireGuard key
- 合法语法：

  ```text
  undo privatekey
  ```

## `undo qos lr`

- 类别：配置命令
- 视图：`VLAN视图`、`接口视图`
- 用途（设备帮助）：remove interface or VLAN rate limit
- 合法语法：

  ```text
  undo qos lr { inbound | outbound }
  ```

## `undo queues`

- 类别：配置命令
- 视图：`dataplane-if`
- 用途（设备帮助）：Restore default queues
- 合法语法：

  ```text
  undo queues
  ```

## `undo rip bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore RIP BFD timers
- 合法语法：

  ```text
  undo rip bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

## `undo rip bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable RIP BFD on this interface
- 合法语法：

  ```text
  undo rip bfd enable
  ```

## `undo route-static group`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：delete an IPv4 static route group
- 合法语法：

  ```text
  undo route-static group name GROUP
  ```

## `undo shutdown`

- 类别：配置命令
- 视图：`BFD会话视图`、`接口视图`
- 用途（设备帮助）：bring the interface up；undo shutdown
- 合法语法：

  ```text
  undo shutdown
  ```

## `undo source`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：clear AmneziaWG source；clear NVE source address；clear WireGuard source；clear the tunnel source IP address；use automatic peer source selection
- 合法语法：

  ```text
  undo source
  ```

## `undo source-port`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：use a dynamic AmneziaWG client source port；use a dynamic WireGuard client source port
- 合法语法：

  ```text
  undo source-port
  ```

## `undo statistic enable`

- 类别：配置命令
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- 用途（设备帮助）：disable counters for this NAT policy；disable counters for this NAT rule；disable detailed interface packet statistics
- 合法语法：

  ```text
  undo statistic enable
  ```

## `undo switchport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：return the interface to L3 mode
- 合法语法：

  ```text
  undo switchport
  ```

## `undo tcp mss`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove TCP MSS clamping from the interface
- 合法语法：

  ```text
  undo tcp mss
  ```

## `undo traffic-filter`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove an ACL from the interface
- 合法语法：

  ```text
  undo traffic-filter { inbound | outbound }
  ```

## `undo traffic-policy`

- 类别：配置命令
- 视图：`VLAN视图`、`接口视图`
- 用途（设备帮助）：remove an MQC traffic policy from the interface；remove the shared MQC policy from this VLAN
- 合法语法：

  ```text
  undo traffic-policy [inbound]
  ```
  ```text
  undo traffic-policy [inbound|outbound]
  ```

## `undo trunkport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove physical member ports
- 合法语法：

  ```text
  undo trunkport INTERFACE [to INTERFACE]
  ```

## `undo tunnel-protocol`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clear the tunnel encapsulation protocol
- 合法语法：

  ```text
  undo tunnel-protocol
  ```

## `undo vlan`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a VLAN
- 合法语法：

  ```text
  undo vlan VLAN-ID [to VLAN-ID]
  ```

## `undo vlan batch`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete VLANs in a batch
- 合法语法：

  ```text
  undo vlan batch { VLAN-ID [to VLAN-ID] } *
  ```

## `undo vlan-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove the sub-interface VLAN binding
- 合法语法：

  ```text
  undo vlan-type
  ```

## `undo vni`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove head-end peer(s) for a VNI
- 合法语法：

  ```text
  undo vni VNI [head-end peer-list PEER]
  ```

## `undo vrrp vrid`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete or reset an IPv4 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp vrid INTEGER<1-255> [...]
  ```

## `undo vrrp6 vrid`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete or reset an IPv6 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp6 vrid INTEGER<1-255> [...]
  ```

## `undo vxlan anycast-gateway enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable the distributed VXLAN anycast gateway
- 合法语法：

  ```text
  undo vxlan anycast-gateway enable
  ```

## `undo vxlan vni`

- 类别：配置命令
- 视图：`BD视图`、`VPN实例视图`
- 用途（设备帮助）：clear the VXLAN VNI；remove the L3VNI from the VPN instance
- 合法语法：

  ```text
  undo vxlan vni
  ```

## `undo wireguard-profile`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：unbind a WireGuard profile
- 合法语法：

  ```text
  undo wireguard-profile
  ```

## `vlan`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a VLAN and enter VLAN view
- 合法语法：

  ```text
  vlan VLAN-ID [to VLAN-ID]
  ```

## `vlan batch`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：create VLANs in a batch
- 合法语法：

  ```text
  vlan batch { VLAN-ID [to VLAN-ID] } *
  ```

## `vlan-type dot1q`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind the sub-interface to a VLAN (dot1q)
- 合法语法：

  ```text
  vlan-type dot1q VLAN-ID [inner VLAN-ID]
  ```

## `vni`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：add a head-end peer for a VNI
- 合法语法：

  ```text
  vni VNI head-end peer-list PEER
  ```

## `vrrp vrid`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv4 VRRPv3 group
- 合法语法：

  ```text
  vrrp vrid INTEGER<1-255> ...
  ```

## `vrrp6 vrid`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv6 VRRPv3 group
- 合法语法：

  ```text
  vrrp6 vrid INTEGER<1-255> ...
  ```

## `vxlan anycast-gateway enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable the distributed VXLAN anycast gateway
- 合法语法：

  ```text
  vxlan anycast-gateway enable
  ```

## `vxlan vni`

- 类别：配置命令
- 视图：`BD视图`、`VPN实例视图`
- 用途（设备帮助）：bind an L3VNI to the VPN instance；set the VXLAN VNI for this bridge-domain
- 合法语法：

  ```text
  vxlan vni VNI
  ```

## `wireguard profile`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：enter a WireGuard profile
- 合法语法：

  ```text
  wireguard profile NAME
  ```

## `wireguard-profile`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind a WireGuard profile
- 合法语法：

  ```text
  wireguard-profile NAME
  ```
