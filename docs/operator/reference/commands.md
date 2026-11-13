# VortexROS 全命令参考

本页列出当前版本实际提供的CLI。每条命令路径只出现一次；同一命令在不同视图中的合法写法会合并展示。配置命令先保存在当前登录会话中，执行 `commit` 成功后生效；显示命令不会改变设备配置。

本参考包含 **806** 条规范命令路径。

## 阅读说明

- `视图`表示命令可以在哪些 CLI 视图中使用；`任意允许视图`表示命令可在多个合法视图中使用。
- 管理CLI仅允许root通过本地Unix Socket访问；远程认证和sudo授权由Linux负责。
- `CLI 帮助`保留设备实际的 `?` 提示文字。
- 完整配置步骤、输出样例和故障处理请进入对应配置指南章节。

## CLI、Candidate 与配置管理

### `commit`

- 类别：即时运维命令
- 执行效果：检查并应用当前登录会话中尚未提交的配置。
- 视图：`任意允许视图`
- CLI 帮助：validate and apply the current session configuration
- 合法语法：

  ```text
  commit
  ```

### `end`

- 类别：视图导航命令
- 执行效果：返回系统/用户视图；若存在未提交配置则按交互提示处理。
- 视图：`任意允许视图`
- CLI 帮助：return to the user view
- 合法语法：

  ```text
  end
  ```

### `export configuration`

- 类别：配置文件/恢复命令
- 执行效果：把已提交配置导出到指定文件，不改变设备状态。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：export protected committed configuration in CLI language
- 合法语法：

  ```text
  export configuration FILE
  ```

### `load configuration`

- 类别：Candidate管理命令
- 执行效果：检查配置文件并载入当前会话；执行 commit 前不会改变设备当前配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：parse CLI-language configuration into candidate
- 合法语法：

  ```text
  load configuration FILE
  ```

### `quit`

- 类别：视图导航命令
- 执行效果：退出当前视图或用户会话；不会进入Linux shell。
- 视图：`任意允许视图`
- CLI 帮助：return to the previous view
- 合法语法：

  ```text
  quit
  ```

### `refresh configuration candidate`

- 类别：Candidate管理命令
- 执行效果：在保留本会话修改的前提下同步其他会话已经提交的配置；发生冲突时提示具体对象。
- 视图：`任意允许视图`
- CLI 帮助：rebase the private candidate onto the latest running configuration
- 合法语法：

  ```text
  refresh configuration candidate
  ```

### `refresh nat-policy interface-pat`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`任意允许视图`
- CLI 帮助：refresh dynamic PAT state after an interface address change
- 合法语法：

  ```text
  refresh nat-policy interface-pat INTERFACE
  ```

### `restore factory-configuration`

- 类别：配置文件/恢复命令
- 执行效果：确认后恢复出厂配置并重启相关网络服务；业务和管理连接可能中断。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：erase running and saved configuration, reset managed services, then restart VPP
- 合法语法：

  ```text
  restore factory-configuration
  ```

### `return`

- 类别：视图导航命令
- 执行效果：返回系统/用户视图；若存在未提交配置则按交互提示处理。
- 视图：`任意允许视图`
- CLI 帮助：return to the user view
- 合法语法：

  ```text
  return
  ```

### `save`

- 类别：配置文件/恢复命令
- 执行效果：将已经提交并生效的配置保存为下次启动配置，不包含其他会话尚未提交的修改。
- 视图：`任意允许视图`
- CLI 帮助：render the committed running configuration to a .cfg file
- 合法语法：

  ```text
  save [FILE.cfg]
  ```

### `startup saved-configuration`

- 类别：配置文件/恢复命令
- 执行效果：选择设备下次启动时读取的配置文件，不改变当前运行配置。
- 视图：`任意允许视图`
- CLI 帮助：select a .cfg file as the next startup configuration
- 合法语法：

  ```text
  startup saved-configuration FILE.cfg
  ```

### `system-view`

- 类别：视图导航命令
- 执行效果：进入系统视图，本命令本身不修改配置。
- 视图：`用户视图`
- CLI 帮助：enter the system view
- 合法语法：

  ```text
  system-view
  ```

## 系统、健康与服务

### `display alarm active`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display active alarms
- 合法语法：

  ```text
  display alarm active
  ```

### `display alarm history`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display cleared alarm history
- 合法语法：

  ```text
  display alarm history [last N]
  ```

### `display configuration candidate`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display uncommitted candidate configuration
- 合法语法：

  ```text
  display configuration candidate [merge | sessions]
  ```

### `display configuration storage`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display running and saved configuration storage status
- 合法语法：

  ```text
  display configuration storage
  ```

### `display cpu-usage`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display CPU usage
- 合法语法：

  ```text
  display cpu-usage [verbose]
  ```

### `display current-configuration`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the current configuration
- 合法语法：

  ```text
  display current-configuration [configuration TYPE [name NAME] | interface [TYPE [N]] | all]
  ```

### `display health`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display control-plane health
- 合法语法：

  ```text
  display health [verbose]
  ```

### `display history`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display command history for this connection
- 合法语法：

  ```text
  display history
  ```

### `display memory-usage`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display memory usage
- 合法语法：

  ```text
  display memory-usage
  ```

### `display service`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display network service status
- 合法语法：

  ```text
  display service [verbose]
  ```

### `display vpp api compatibility`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VPP binary API compatibility
- 合法语法：

  ```text
  display vpp api compatibility [verbose]
  ```

### `display vpp interface-ownership`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display physical-interface dataplane ownership and recovery state
- 合法语法：

  ```text
  display vpp interface-ownership [verbose]
  ```

### `display vpp takeover transaction`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the current or most recent VPP takeover transaction
- 合法语法：

  ```text
  display vpp takeover transaction
  ```

### `enable lldp`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable LLDP globally and on all physical interfaces
- 合法语法：

  ```text
  enable lldp
  ```

### `enable switch`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable the L2 switch instance
- 合法语法：

  ```text
  enable switch
  ```

### `health check`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：strict machine-readable control-plane readiness gate
- 合法语法：

  ```text
  health check [--wait] [--timeout DURATION] [--json] [--allow-weak-vpp] [--require-saved]
  ```

### `sysname`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set the device name
- 合法语法：

  ```text
  sysname HOSTNAME
  ```

### `undo enable lldp`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable LLDP globally
- 合法语法：

  ```text
  undo enable lldp
  ```

### `undo enable switch`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable the L2 switch instance
- 合法语法：

  ```text
  undo enable switch
  ```

### `undo sysname`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the default device name
- 合法语法：

  ```text
  undo sysname
  ```

### `undo vpp startup-config`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore default VPP startup configuration path
- 合法语法：

  ```text
  undo vpp startup-config
  ```

### `vpp startup-config`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：VPP process startup configuration file (-c)
- 合法语法：

  ```text
  vpp startup-config PATH
  ```

## 接口、二层与邻居

### `acl ipv6 name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create an IPv6 ACL and enter ACL view
- 合法语法：

  ```text
  acl ipv6 name NAME [advance]
  ```

### `acl name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create an IPv4 ACL and enter ACL view
- 合法语法：

  ```text
  acl name NAME [advance]
  ```

### `amneziawg profile`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter an AmneziaWG profile
- 合法语法：

  ```text
  amneziawg profile NAME
  ```

### `amneziawg-profile`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind an AmneziaWG profile
- 合法语法：

  ```text
  amneziawg-profile NAME
  ```

### `arp proxy`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure a Linux proxy-neighbour address range
- 合法语法：

  ```text
  arp proxy X.X.X.X X.X.X.X interface IFNAME
  ```

### `arp static`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure a static ARP entry in a bridge-domain
- 合法语法：

  ```text
  arp static IP MAC bridge-domain BD
  ```

### `arp timeout`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set the dynamic IPv4 neighbor aging time
- 合法语法：

  ```text
  arp timeout INTEGER<60-86400>
  ```

### `bfd`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enable BFD or configure a static session
- 合法语法：

  ```text
  bfd [NAME bind peer-ip PEER ...]
  ```

### `bgp`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a BGP instance and enter BGP view
- 合法语法：

  ```text
  bgp ASNUM
  ```

### `bridge-domain`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：add the interface to a bridge-domain；create a bridge-domain and enter its view
- 合法语法：

  ```text
  bridge-domain ID
  ```
  ```text
  bridge-domain ID [bvi]
  ```

### `cpu isolation enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Isolate VPP CPUs at Linux boot
- 合法语法：

  ```text
  cpu isolation enable
  ```

### `cpu main-core`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Pin the VPP main thread
- 合法语法：

  ```text
  cpu main-core NUMBER
  ```

### `cpu worker-cores`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Pin VPP worker threads
- 合法语法：

  ```text
  cpu worker-cores CPU-LIST
  ```

### `dataplane`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：Configure dataplane startup
- 合法语法：

  ```text
  dataplane
  ```

### `description`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- CLI 帮助：NVE interface description；bridge-domain description；configure ACL description；configure group description；configure the VLAN description；configure the VPN instance description；configure the interface description；set NAT policy description；set NAT rule description
- 合法语法：

  ```text
  description TEXT
  ```

### `descriptors`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane-if`
- CLI 帮助：Set RX and TX descriptors
- 合法语法：

  ```text
  descriptors rx COUNT tx COUNT
  ```

### `destination`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- CLI 帮助：set the peer endpoint and outer VPN；set the tunnel destination and optional underlay VPN
- 合法语法：

  ```text
  destination IP [vpn-instance NAME]
  ```
  ```text
  destination [vpn-instance VPN] [IP port PORT]
  ```

### `device`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Assign a physical PCI port to an Ethernet interface
- 合法语法：

  ```text
  device PCI-BDF name Ethernet NUMBER
  ```

### `dhcp client classless-route enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：install learned classless routes
- 合法语法：

  ```text
  dhcp client classless-route enable
  ```

### `dhcp client default-route enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：install the learned default route
- 合法语法：

  ```text
  dhcp client default-route enable
  ```

### `dhcp client default-route preference`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the DHCP default route preference
- 合法语法：

  ```text
  dhcp client default-route preference INTEGER<1-255>
  ```

### `dhcp client-relay shutdown`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：Suspend DHCP client and relay on this interface
- 合法语法：

  ```text
  dhcp client-relay shutdown
  ```

### `dhcp relay server-ip`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：add a DHCPv4 relay server
- 合法语法：

  ```text
  dhcp relay server-ip X.X.X.X
  ```

### `dhcp select`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：select the DHCPv4 interface role
- 合法语法：

  ```text
  dhcp select { global | interface | relay }
  ```

### `dhcp server dns-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure interface-pool DNS servers
- 合法语法：

  ```text
  dhcp server dns-list X.X.X.X [X.X.X.X]
  ```

### `dhcp server domain-name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure the interface-pool domain name
- 合法语法：

  ```text
  dhcp server domain-name DOMAIN
  ```

### `dhcp server excluded-ip-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：exclude addresses from the interface pool
- 合法语法：

  ```text
  dhcp server excluded-ip-address START [END]
  ```

### `dhcp server gateway-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure interface-pool gateway addresses
- 合法语法：

  ```text
  dhcp server gateway-list { X.X.X.X [X.X.X.X] | disable }
  ```

### `dhcp server ip-range`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure the allocatable interface-pool range
- 合法语法：

  ```text
  dhcp server ip-range START END
  ```

### `dhcp server lease`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure the interface-pool lease time
- 合法语法：

  ```text
  dhcp server lease { unlimited | day DAYS [hour HOURS [minute MINUTES]] }
  ```

### `dhcp server static-bind ip-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind an interface-pool address to a client MAC
- 合法语法：

  ```text
  dhcp server static-bind ip-address X.X.X.X mac-address H-H-H
  ```

### `dhcpv6 client information-request`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：obtain non-address information by DHCPv6
- 合法语法：

  ```text
  dhcpv6 client information-request
  ```

### `dhcpv6 client pd`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：request an IPv6 delegated prefix
- 合法语法：

  ```text
  dhcpv6 client pd PREFIX-NAME
  ```

### `dhcpv6 client renew`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`接口视图`
- CLI 帮助：renew the DHCPv6 client lease now
- 合法语法：

  ```text
  dhcpv6 client renew
  ```

### `dhcpv6 duid`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：configure the DHCPv6 server identifier type
- 合法语法：

  ```text
  dhcpv6 duid { ll | llt }
  ```

### `dhcpv6 pool`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create or enter an IPv6 address pool
- 合法语法：

  ```text
  dhcpv6 pool NAME
  ```

### `dhcpv6 relay destination`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：add a DHCPv6 relay destination
- 合法语法：

  ```text
  dhcpv6 relay destination X:X::X
  ```

### `dhcpv6 relay interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the DHCPv6 relay upper interface
- 合法语法：

  ```text
  dhcpv6 relay interface IF
  ```

### `dhcpv6 server`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable the DHCPv6 server on an interface
- 合法语法：

  ```text
  dhcpv6 server POOL
  ```

### `display arp`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the ARP table
- 合法语法：

  ```text
  display arp [all | interface IF | vpn-instance VRF | static | dynamic]
  ```

### `display arp proxy`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display configured proxy-neighbour entries and Linux state
- 合法语法：

  ```text
  display arp proxy
  ```

### `display bridge-domain`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display bridge-domains (service BD + VLAN domains)
- 合法语法：

  ```text
  display bridge-domain [ID]
  ```

### `display dataplane`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：Display active dataplane resources
- 合法语法：

  ```text
  display dataplane [verbose|interfaces|cpu|memory|iommu|tables]
  ```

### `display eth-trunk`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display aggregate interface state
- 合法语法：

  ```text
  display eth-trunk [INTEGER<0-63>]
  ```

### `display flow-steering`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display interface flow-steering configuration and runtime
- 合法语法：

  ```text
  display flow-steering [interface IF]
  ```

### `display interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display interface information
- 合法语法：

  ```text
  display interface [IF]
  ```

### `display interface brief`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display brief interface list
- 合法语法：

  ```text
  display interface brief
  ```

### `display interface description`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display interface descriptions
- 合法语法：

  ```text
  display interface description [IF]
  ```

### `display interface hardware offload`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display physical interface hardware offload capabilities and state
- 合法语法：

  ```text
  display interface hardware offload [IF]
  ```

### `display interface statistics`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：per-interface counters
- 合法语法：

  ```text
  display interface statistics [IF]
  ```

### `display lcp`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：show Linux Control Plane interface pairs
- 合法语法：

  ```text
  display lcp
  ```

### `display lldp local`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display local LLDP information
- 合法语法：

  ```text
  display lldp local
  ```

### `display lldp neighbor brief`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display LLDP neighbor brief information
- 合法语法：

  ```text
  display lldp neighbor brief
  ```

### `display lldp neighbor interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display LLDP neighbor information on an interface
- 合法语法：

  ```text
  display lldp neighbor interface IF
  ```

### `display mac-address`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the MAC address table
- 合法语法：

  ```text
  display mac-address [MAC | vlan VLAN-ID | bridge-domain BD | interface IF | static | dynamic]
  ```

### `display vlan`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VLAN information
- 合法语法：

  ```text
  display vlan [VLAN-ID | summary]
  ```

### `display vlan summary`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VLAN summary
- 合法语法：

  ```text
  display vlan summary
  ```

### `enable dhcp server`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enable DHCP servers
- 合法语法：

  ```text
  enable dhcp server
  ```

### `encapsulation`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure sub-interface encapsulation
- 合法语法：

  ```text
  encapsulation { dot1q | dot1ad } vid VLAN-ID | encapsulation qinq vid PE-VID ce-vid CE-VID
  ```

### `esi`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure the Ethernet segment identifier
- 合法语法：

  ```text
  esi XXXX.XXXX.XXXX.XXXX.XXXX
  ```

### `eth-trunk`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：join an aggregate interface
- 合法语法：

  ```text
  eth-trunk INTEGER<0-63>
  ```

### `evpn`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BD视图`
- CLI 帮助：enter the EVPN view for this bridge-domain
- 合法语法：

  ```text
  evpn
  ```

### `flow-steering enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable tunnel-aware ingress worker steering
- 合法语法：

  ```text
  flow-steering enable
  ```

### `gre key`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the GRE key (optional)
- 合法语法：

  ```text
  gre key KEY
  ```

### `hardware offload`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane-if`、`接口视图`
- CLI 帮助：restore default hardware offload use
- 合法语法：

  ```text
  hardware offload OFFLOAD [OFFLOAD ...]
  ```

### `interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter the interface view
- 合法语法：

  ```text
  interface { Eth-Trunk N | LoopBack N | Tunnel N | Vlanif N | Vbdif N | eth N | IFNAME }
  ```

### `interface range`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter a batch interface view
- 合法语法：

  ```text
  interface range IF1 to IF2
  ```

### `interface user-defined`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：Preconfigure an interface before it is present
- 合法语法：

  ```text
  interface user-defined NAME
  ```

### `iommu enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Enable IOMMU at Linux boot
- 合法语法：

  ```text
  iommu enable
  ```

### `ip address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure an IPv4 address
- 合法语法：

  ```text
  ip address IP MASK [sub]
  ```

### `ip address dhcp-alloc`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：obtain the IPv4 address by DHCP
- 合法语法：

  ```text
  ip address dhcp-alloc
  ```

### `ip binding vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind the interface to a VPN instance
- 合法语法：

  ```text
  ip binding vpn-instance NAME
  ```

### `ip ip-prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：configure an IP prefix list entry
- 合法语法：

  ```text
  ip ip-prefix NAME [index SEQ] {permit|deny} IP MASK [greater-equal GE] [less-equal LE]
  ```

### `ip ipv6-prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：configure an IPv6 prefix list entry
- 合法语法：

  ```text
  ip ipv6-prefix NAME [index SEQ] {permit|deny} IPV6 PREFIX-LENGTH [greater-equal GE] [less-equal LE]
  ```

### `ip pool`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create or enter an IPv4 pool
- 合法语法：

  ```text
  ip pool NAME
  ```

### `ip urpf`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure ip uRPF on the interface
- 合法语法：

  ```text
  ip urpf { loose | strict | disable }
  ```

### `ip vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a VPN instance and enter its view
- 合法语法：

  ```text
  ip vpn-instance NAME
  ```

### `ipv6 address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure an IPv6 address
- 合法语法：

  ```text
  ipv6 address IP PREFIXLEN
  ```

### `ipv6 address auto dhcp`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：obtain an IPv6 address by stateful DHCPv6
- 合法语法：

  ```text
  ipv6 address auto dhcp [hint X:X::X]
  ```

### `ipv6 address auto global default`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：derive global IPv6 addresses and the default route from router advertisements
- 合法语法：

  ```text
  ipv6 address auto global default
  ```

### `ipv6 address auto slaac`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：derive IPv6 addresses from router advertisements
- 合法语法：

  ```text
  ipv6 address auto slaac
  ```

### `ipv6 address dhcpv6-prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：derive an interface address from a delegated prefix
- 合法语法：

  ```text
  ipv6 address dhcpv6-prefix PREFIX-NAME SUFFIX/PREFIXLEN
  ```

### `ipv6 nd ra default-route enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：install default routes learned from router advertisements
- 合法语法：

  ```text
  ipv6 nd ra default-route enable
  ```

### `ipv6 route-static group`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter an IPv6 static route group
- 合法语法：

  ```text
  ipv6 route-static group name GROUP
  ```

### `ipv6 urpf`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure ipv6 uRPF on the interface
- 合法语法：

  ```text
  ipv6 urpf { loose | strict | disable }
  ```

### `isis`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create an IS-IS process and enter process view
- 合法语法：

  ```text
  isis INTEGER<1-65535> [vpn-instance NAME]
  ```

### `isis bfd`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure ISIS BFD timers
- 合法语法：

  ```text
  isis bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

### `isis bfd enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable ISIS BFD on this interface
- 合法语法：

  ```text
  isis bfd enable
  ```

### `isis circuit-level`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the IS-IS circuit level
- 合法语法：

  ```text
  isis circuit-level {level-1|level-1-2|level-2}
  ```

### `isis circuit-type p2p`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the IS-IS link to point-to-point
- 合法语法：

  ```text
  isis circuit-type p2p
  ```

### `isis cost`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set IS-IS interface metric
- 合法语法：

  ```text
  isis cost INTEGER<1-16777215>
  ```

### `isis enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable IS-IS on an interface
- 合法语法：

  ```text
  isis enable INTEGER<1-65535>
  ```

### `isis ipv6-enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable IPv6 IS-IS on an interface
- 合法语法：

  ```text
  isis ipv6-enable INTEGER<1-65535>
  ```

### `isis passive`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：make IS-IS interface passive
- 合法语法：

  ```text
  isis passive
  ```

### `isis priority`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set IS-IS interface priority
- 合法语法：

  ```text
  isis priority INTEGER<0-127>
  ```

### `l2 binding vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BD视图`
- CLI 帮助：bind a local VLAN into this bridge-domain
- 合法语法：

  ```text
  l2 binding vlan VLAN-ID
  ```

### `lcp host`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：create a same-name Linux control-plane interface mapping
- 合法语法：

  ```text
  lcp host HOST-IF [tap|tun]
  ```

### `lldp enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable LLDP on this physical interface
- 合法语法：

  ```text
  lldp enable
  ```

### `mac-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the interface MAC address
- 合法语法：

  ```text
  mac-address MAC
  ```

### `mac-address aging-time`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set the dynamic MAC address aging time
- 合法语法：

  ```text
  mac-address aging-time INTEGER<60-15300>
  ```

### `mac-address learn-limit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Set the VPP global dynamic MAC learning limit
- 合法语法：

  ```text
  mac-address learn-limit INTEGER<1-2147483647>
  ```

### `mac-address static`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure a static MAC address
- 合法语法：

  ```text
  mac-address static MAC IF bridge-domain BD
  ```

### `memory hugepages`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Reserve huge pages at boot
- 合法语法：

  ```text
  memory hugepages size { 2M | 1G } count NUMBER
  ```

### `mode`

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

### `mtu`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the interface MTU
- 合法语法：

  ```text
  mtu N
  ```

### `nat-policy`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind a NAT policy to this interface
- 合法语法：

  ```text
  nat-policy NAME { inbound | outbound }
  ```

### `nat-policy address-pool name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create/enter a NAT address-pool
- 合法语法：

  ```text
  nat-policy address-pool name NAME
  ```

### `nat-policy address-set name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create/enter a NAT address-set
- 合法语法：

  ```text
  nat-policy address-set name NAME
  ```

### `nat-policy name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create/enter a NAT policy
- 合法语法：

  ```text
  nat-policy name NAME
  ```

### `nat-policy port-set name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create/enter a NAT port-set
- 合法语法：

  ```text
  nat-policy port-set name NAME
  ```

### `neighbor ipv4 limit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Set the Linux and VPP IPv4 neighbor limit
- 合法语法：

  ```text
  neighbor ipv4 limit INTEGER<4-2147483647>
  ```

### `neighbor ipv6 limit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Set the Linux and VPP IPv6 neighbor limit
- 合法语法：

  ```text
  neighbor ipv6 limit INTEGER<4-2147483647>
  ```

### `ospf`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create an OSPF process and enter OSPF view
- 合法语法：

  ```text
  ospf INTEGER<1-65535> [router-id X.X.X.X] [vpn-instance NAME]
  ```

### `ospf bfd`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure OSPF BFD timers
- 合法语法：

  ```text
  ospf bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

### `ospf bfd enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable OSPF BFD on this interface
- 合法语法：

  ```text
  ospf bfd enable
  ```

### `ospf cost`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPF interface cost
- 合法语法：

  ```text
  ospf cost INTEGER<1-65535>
  ```

### `ospf dr-priority`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPF interface router priority
- 合法语法：

  ```text
  ospf dr-priority INTEGER<0-255>
  ```

### `ospf enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable OSPF on an interface
- 合法语法：

  ```text
  ospf enable INTEGER<1-65535> area X.X.X.X
  ```

### `ospf network-type`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPF interface network type
- 合法语法：

  ```text
  ospf network-type {broadcast|nbma|p2p|p2mp}
  ```

### `ospf passive`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：suppress OSPF Hellos on this interface
- 合法语法：

  ```text
  ospf passive
  ```

### `ospf timer dead`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPF interface dead
- 合法语法：

  ```text
  ospf timer dead INTEGER<1-65535>
  ```

### `ospf timer hello`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPF interface hello
- 合法语法：

  ```text
  ospf timer hello INTEGER<1-65535>
  ```

### `ospf timer retransmit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPF interface retransmit
- 合法语法：

  ```text
  ospf timer retransmit INTEGER<1-65535>
  ```

### `ospf timer transmit-delay`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPF interface transmit-delay
- 合法语法：

  ```text
  ospf timer transmit-delay INTEGER<1-3600>
  ```

### `ospfv3`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：create an OSPFv3 process and enter its view；enable OSPFv3 on an interface
- 合法语法：

  ```text
  ospfv3 INTEGER<1-65535> [router-id X.X.X.X] [vpn-instance NAME]
  ```
  ```text
  ospfv3 INTEGER<1-65535> area X.X.X.X
  ```

### `ospfv3 bfd`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure OSPFV3 BFD timers
- 合法语法：

  ```text
  ospfv3 bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

### `ospfv3 bfd enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable OSPFV3 BFD on this interface
- 合法语法：

  ```text
  ospfv3 bfd enable
  ```

### `ospfv3 cost`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPFv3 interface cost
- 合法语法：

  ```text
  ospfv3 cost INTEGER<1-65535>
  ```

### `ospfv3 dr-priority`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPFv3 interface router priority
- 合法语法：

  ```text
  ospfv3 dr-priority INTEGER<0-255>
  ```

### `ospfv3 network-type`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPFv3 interface network type
- 合法语法：

  ```text
  ospfv3 network-type {broadcast|p2p|p2mp}
  ```

### `ospfv3 timer dead`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPFV3 interface dead
- 合法语法：

  ```text
  ospfv3 timer dead INTEGER<1-65535>
  ```

### `ospfv3 timer hello`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPFV3 interface hello
- 合法语法：

  ```text
  ospfv3 timer hello INTEGER<1-65535>
  ```

### `ospfv3 timer retransmit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPFV3 interface retransmit
- 合法语法：

  ```text
  ospfv3 timer retransmit INTEGER<1-65535>
  ```

### `ospfv3 timer transmit-delay`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set OSPFV3 interface transmit-delay
- 合法语法：

  ```text
  ospfv3 timer transmit-delay INTEGER<1-3600>
  ```

### `port default vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the access port default VLAN
- 合法语法：

  ```text
  port default vlan VLAN-ID
  ```

### `port link-type`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the L2 port link type
- 合法语法：

  ```text
  port link-type { access | dot1q-tunnel | trunk }
  ```

### `port trunk allow-pass vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：allow VLANs on a trunk port
- 合法语法：

  ```text
  port trunk allow-pass vlan { VLAN-LIST | all }
  ```

### `port trunk pvid vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the trunk native VLAN
- 合法语法：

  ```text
  port trunk pvid vlan VLAN-ID
  ```

### `portswitch`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：switch the aggregate to Layer 2 mode；switch the interface to L2 mode
- 合法语法：

  ```text
  portswitch
  ```

### `privatekey`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set or generate the AmneziaWG private key；set or generate the WireGuard private key
- 合法语法：

  ```text
  privatekey { STRING<44> | auto | cipher CIPHERTEXT }
  ```

### `qos lr`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VLAN视图`、`接口视图`
- CLI 帮助：configure interface or VLAN rate limit (2-rate 3-color)
- 合法语法：

  ```text
  qos lr { inbound | outbound } cir CIR [pir PIR] [cbs CBS] [pbs PBS] [green|yellow|red pass|discard]
  ```

### `queues`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`dataplane-if`
- CLI 帮助：Set RX and TX queues
- 合法语法：

  ```text
  queues rx COUNT tx COUNT
  ```

### `rip`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a RIP process and enter process view
- 合法语法：

  ```text
  rip INTEGER<1-65535> [vpn-instance NAME]
  ```

### `rip bfd`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure RIP BFD timers
- 合法语法：

  ```text
  rip bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

### `rip bfd enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable RIP BFD on this interface
- 合法语法：

  ```text
  rip bfd enable
  ```

### `ripng`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a RIP process and enter process view
- 合法语法：

  ```text
  ripng INTEGER<1-65535> [vpn-instance NAME]
  ```

### `route-policy`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a route policy node and enter its view
- 合法语法：

  ```text
  route-policy NAME {permit|deny} node INTEGER<1-65535>
  ```

### `route-static group`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter an IPv4 static route group
- 合法语法：

  ```text
  route-static group name GROUP
  ```

### `shutdown`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`、`接口视图`
- CLI 帮助：shut down the interface；shutdown
- 合法语法：

  ```text
  shutdown
  ```

### `source`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- CLI 帮助：pin the peer outer source address；set AmneziaWG source and underlay VPN；set NVE source VTEP address and optional underlay VPN；set WireGuard source and underlay VPN；set the tunnel source IP address
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

### `source-port`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set fixed AmneziaWG server listen port；set fixed WireGuard server listen port
- 合法语法：

  ```text
  source-port PORT
  ```

### `statistic enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- CLI 帮助：enable counters for this NAT policy；enable counters for this NAT rule；enable detailed interface packet statistics
- 合法语法：

  ```text
  statistic enable
  ```

### `switchport`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：switch the interface to L2 mode
- 合法语法：

  ```text
  switchport
  ```

### `tcp mss`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：clamp TCP SYN MSS on this L3 interface
- 合法语法：

  ```text
  tcp mss { clamp | MSS }
  ```

### `traffic behavior`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a traffic behavior and enter its view
- 合法语法：

  ```text
  traffic behavior NAME
  ```

### `traffic classifier`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a traffic classifier and enter its view
- 合法语法：

  ```text
  traffic classifier NAME [operator and|or]
  ```

### `traffic policy`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a traffic policy and enter its view
- 合法语法：

  ```text
  traffic policy NAME
  ```

### `traffic-filter`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：apply an ACL to interface traffic
- 合法语法：

  ```text
  traffic-filter { inbound | outbound } acl NAME
  ```

### `traffic-policy`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VLAN视图`、`接口视图`
- CLI 帮助：apply an MQC policy to traffic in this VLAN；apply an MQC traffic policy
- 合法语法：

  ```text
  traffic-policy NAME inbound
  ```
  ```text
  traffic-policy NAME { inbound | outbound }
  ```

### `trunkport`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：add physical member ports
- 合法语法：

  ```text
  trunkport INTERFACE [to INTERFACE]
  ```

### `tunnel-protocol`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the tunnel encapsulation protocol
- 合法语法：

  ```text
  tunnel-protocol { gre | ipv4-ipv4 | ipv6-ipv4 | ipv4-ipv6 | ipv6-ipv6 | wireguard | amneziawg }
  ```

### `undo amneziawg-profile`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：unbind an AmneziaWG profile
- 合法语法：

  ```text
  undo amneziawg-profile
  ```

### `undo arp proxy`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a Linux proxy-neighbour address range
- 合法语法：

  ```text
  undo arp proxy X.X.X.X X.X.X.X interface IFNAME
  ```

### `undo arp static`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a static ARP entry
- 合法语法：

  ```text
  undo arp static IP MAC bridge-domain BD
  ```

### `undo arp timeout`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the default IPv4 neighbor aging time
- 合法语法：

  ```text
  undo arp timeout
  ```

### `undo bfd`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：delete a BFD session or disable BFD
- 合法语法：

  ```text
  undo bfd [NAME]
  ```

### `undo bridge-domain`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：delete a bridge-domain；remove the interface from a bridge-domain
- 合法语法：

  ```text
  undo bridge-domain
  ```
  ```text
  undo bridge-domain ID
  ```

### `undo cpu isolation enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu isolation enable
  ```

### `undo cpu main-core`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu main-core
  ```

### `undo cpu worker-cores`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove this dataplane setting
- 合法语法：

  ```text
  undo cpu worker-cores
  ```

### `undo description`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- CLI 帮助：clear ACL description；clear NAT policy description；clear NAT rule description；clear NVE description；clear bridge-domain description；delete group description；delete the VLAN description；delete the VPN instance description；delete the interface description
- 合法语法：

  ```text
  undo description
  ```

### `undo descriptors`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane-if`
- CLI 帮助：Restore default descriptors
- 合法语法：

  ```text
  undo descriptors
  ```

### `undo destination`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- CLI 帮助：clear the peer endpoint；clear the tunnel destination IP address
- 合法语法：

  ```text
  undo destination
  ```

### `undo device`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove a PCI port assignment
- 合法语法：

  ```text
  undo device PCI-BDF
  ```

### `undo dhcp client classless-route enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：do not install learned classless routes
- 合法语法：

  ```text
  undo dhcp client classless-route enable
  ```

### `undo dhcp client default-route enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：do not install the learned default route
- 合法语法：

  ```text
  undo dhcp client default-route enable
  ```

### `undo dhcp client-relay shutdown`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：Resume configured DHCP client and relay on this interface
- 合法语法：

  ```text
  undo dhcp client-relay shutdown
  ```

### `undo dhcp relay server-ip`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove a DHCPv4 relay server
- 合法语法：

  ```text
  undo dhcp relay server-ip X.X.X.X
  ```

### `undo dhcp select`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the DHCPv4 server or relay role
- 合法语法：

  ```text
  undo dhcp select
  ```

### `undo dhcp server dns-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove interface-pool DNS servers
- 合法语法：

  ```text
  undo dhcp server dns-list [X.X.X.X]
  ```

### `undo dhcp server domain-name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove the interface-pool domain name
- 合法语法：

  ```text
  undo dhcp server domain-name
  ```

### `undo dhcp server excluded-ip-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove an interface-pool exclusion
- 合法语法：

  ```text
  undo dhcp server excluded-ip-address START [END]
  ```

### `undo dhcp server gateway-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the interface-address gateway default
- 合法语法：

  ```text
  undo dhcp server gateway-list [X.X.X.X]
  ```

### `undo dhcp server ip-range`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore allocation from the interface primary subnet
- 合法语法：

  ```text
  undo dhcp server ip-range
  ```

### `undo dhcp server lease`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default interface-pool lease
- 合法语法：

  ```text
  undo dhcp server lease
  ```

### `undo dhcp server static-bind ip-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove an interface-pool static binding
- 合法语法：

  ```text
  undo dhcp server static-bind ip-address X.X.X.X
  ```

### `undo dhcpv6 client information-request`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable DHCPv6 information requests
- 合法语法：

  ```text
  undo dhcpv6 client information-request
  ```

### `undo dhcpv6 client pd`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable DHCPv6 prefix delegation
- 合法语法：

  ```text
  undo dhcpv6 client pd
  ```

### `undo dhcpv6 duid`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：restore the default DHCPv6 server identifier
- 合法语法：

  ```text
  undo dhcpv6 duid
  ```

### `undo dhcpv6 pool`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：delete an IPv6 address pool
- 合法语法：

  ```text
  undo dhcpv6 pool NAME
  ```

### `undo dhcpv6 relay destination`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove a DHCPv6 relay destination
- 合法语法：

  ```text
  undo dhcpv6 relay destination X:X::X
  ```

### `undo dhcpv6 relay interface`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove a DHCPv6 relay upper interface
- 合法语法：

  ```text
  undo dhcpv6 relay interface IF
  ```

### `undo dhcpv6 server`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the DHCPv6 server
- 合法语法：

  ```text
  undo dhcpv6 server
  ```

### `undo enable dhcp server`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：disable DHCP servers
- 合法语法：

  ```text
  undo enable dhcp server
  ```

### `undo encapsulation`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove the sub-interface encapsulation
- 合法语法：

  ```text
  undo encapsulation
  ```

### `undo esi`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove the Ethernet segment identifier
- 合法语法：

  ```text
  undo esi
  ```

### `undo eth-trunk`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：leave the aggregate interface
- 合法语法：

  ```text
  undo eth-trunk [INTEGER<0-63>]
  ```

### `undo flow-steering enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable ingress worker steering on the interface
- 合法语法：

  ```text
  undo flow-steering enable
  ```

### `undo gre key`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：clear the GRE key
- 合法语法：

  ```text
  undo gre key
  ```

### `undo hardware offload`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane-if`、`接口视图`
- CLI 帮助：disable hardware offload use
- 合法语法：

  ```text
  undo hardware offload OFFLOAD [OFFLOAD ...]
  ```

### `undo interface`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an interface
- 合法语法：

  ```text
  undo interface IFNAME
  ```

### `undo iommu enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove this dataplane setting
- 合法语法：

  ```text
  undo iommu enable
  ```

### `undo ip address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete an IPv4 address
- 合法语法：

  ```text
  undo ip address [IP MASK]
  ```

### `undo ip address dhcp-alloc`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the DHCPv4 client
- 合法语法：

  ```text
  undo ip address dhcp-alloc
  ```

### `undo ip binding vpn-instance`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：unbind the interface from a VPN instance
- 合法语法：

  ```text
  undo ip binding vpn-instance
  ```

### `undo ip pool`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：delete an IPv4 address pool
- 合法语法：

  ```text
  undo ip pool NAME
  ```

### `undo ip urpf`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable ip uRPF on the interface
- 合法语法：

  ```text
  undo ip urpf
  ```

### `undo ipv6 address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete an IPv6 address
- 合法语法：

  ```text
  undo ipv6 address [IP PREFIXLEN]
  ```

### `undo ipv6 address auto dhcp`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the stateful DHCPv6 client
- 合法语法：

  ```text
  undo ipv6 address auto dhcp
  ```

### `undo ipv6 address auto global default`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable automatic global IPv6 addresses and RA default routes
- 合法语法：

  ```text
  undo ipv6 address auto global default
  ```

### `undo ipv6 address auto slaac`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable derive IPv6 addresses from router advertisements
- 合法语法：

  ```text
  undo ipv6 address auto slaac
  ```

### `undo ipv6 address dhcpv6-prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove an address derived from a delegated prefix
- 合法语法：

  ```text
  undo ipv6 address dhcpv6-prefix PREFIX-NAME
  ```

### `undo ipv6 nd ra default-route enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable install default routes learned from router advertisements
- 合法语法：

  ```text
  undo ipv6 nd ra default-route enable
  ```

### `undo ipv6 route-static group`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：delete an IPv6 static route group
- 合法语法：

  ```text
  undo ipv6 route-static group name GROUP
  ```

### `undo ipv6 urpf`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable ipv6 uRPF on the interface
- 合法语法：

  ```text
  undo ipv6 urpf
  ```

### `undo isis bfd`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore ISIS BFD timers
- 合法语法：

  ```text
  undo isis bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

### `undo isis bfd enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable ISIS BFD on this interface
- 合法语法：

  ```text
  undo isis bfd enable
  ```

### `undo isis circuit-level`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the IS-IS circuit level
- 合法语法：

  ```text
  undo isis circuit-level
  ```

### `undo isis circuit-type`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the IS-IS link type
- 合法语法：

  ```text
  undo isis circuit-type
  ```

### `undo isis cost`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore IS-IS interface metric
- 合法语法：

  ```text
  undo isis cost
  ```

### `undo isis enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable IS-IS on an interface
- 合法语法：

  ```text
  undo isis enable
  ```

### `undo isis ipv6-enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable IPv6 IS-IS on an interface
- 合法语法：

  ```text
  undo isis ipv6-enable INTEGER<1-65535>
  ```

### `undo isis passive`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore IS-IS interface
- 合法语法：

  ```text
  undo isis passive
  ```

### `undo isis priority`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore IS-IS interface priority
- 合法语法：

  ```text
  undo isis priority
  ```

### `undo l2 binding vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BD视图`
- CLI 帮助：remove VLAN binding from this bridge-domain
- 合法语法：

  ```text
  undo l2 binding vlan
  ```

### `undo lcp host`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete the Linux control-plane interface mapping
- 合法语法：

  ```text
  undo lcp host
  ```

### `undo lldp enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable LLDP on this physical interface
- 合法语法：

  ```text
  undo lldp enable
  ```

### `undo mac-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default interface MAC address
- 合法语法：

  ```text
  undo mac-address
  ```

### `undo mac-address aging-time`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the default dynamic MAC address aging time
- 合法语法：

  ```text
  undo mac-address aging-time
  ```

### `undo mac-address learn-limit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Restore the default table limit
- 合法语法：

  ```text
  undo mac-address learn-limit
  ```

### `undo mac-address static`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a static MAC address
- 合法语法：

  ```text
  undo mac-address static MAC IF bridge-domain BD
  ```

### `undo memory hugepages`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Remove this dataplane setting
- 合法语法：

  ```text
  undo memory hugepages
  ```

### `undo mode`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane-if`、`接口视图`
- CLI 帮助：Restore Linux kernel mode；restore manual aggregate mode
- 合法语法：

  ```text
  undo mode
  ```

### `undo mtu`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default interface MTU
- 合法语法：

  ```text
  undo mtu
  ```

### `undo nat-policy`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：unbind a NAT policy from this interface
- 合法语法：

  ```text
  undo nat-policy [NAME] [{ inbound | outbound }]
  ```

### `undo neighbor ipv4 limit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Restore the default table limit
- 合法语法：

  ```text
  undo neighbor ipv4 limit
  ```

### `undo neighbor ipv6 limit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane`
- CLI 帮助：Restore the default table limit
- 合法语法：

  ```text
  undo neighbor ipv6 limit
  ```

### `undo ospf bfd`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore OSPF BFD timers
- 合法语法：

  ```text
  undo ospf bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

### `undo ospf bfd enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable OSPF BFD on this interface
- 合法语法：

  ```text
  undo ospf bfd enable
  ```

### `undo ospf cost`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore OSPF interface cost
- 合法语法：

  ```text
  undo ospf cost
  ```

### `undo ospf dr-priority`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPF interface router priority
- 合法语法：

  ```text
  undo ospf dr-priority
  ```

### `undo ospf enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable OSPF on an interface
- 合法语法：

  ```text
  undo ospf enable INTEGER<1-65535>
  ```

### `undo ospf network-type`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPF interface network type
- 合法语法：

  ```text
  undo ospf network-type
  ```

### `undo ospf passive`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore OSPF Hellos on this interface
- 合法语法：

  ```text
  undo ospf passive
  ```

### `undo ospf timer dead`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPF interface dead
- 合法语法：

  ```text
  undo ospf timer dead
  ```

### `undo ospf timer hello`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPF interface hello
- 合法语法：

  ```text
  undo ospf timer hello
  ```

### `undo ospf timer retransmit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPF interface retransmit
- 合法语法：

  ```text
  undo ospf timer retransmit
  ```

### `undo ospf timer transmit-delay`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPF interface transmit-delay
- 合法语法：

  ```text
  undo ospf timer transmit-delay
  ```

### `undo ospfv3`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：delete an OSPFv3 process；disable OSPFv3 on an interface
- 合法语法：

  ```text
  undo ospfv3 INTEGER<1-65535>
  ```
  ```text
  undo ospfv3 INTEGER<1-65535> area X.X.X.X
  ```

### `undo ospfv3 bfd`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore OSPFV3 BFD timers
- 合法语法：

  ```text
  undo ospfv3 bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

### `undo ospfv3 bfd enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable OSPFV3 BFD on this interface
- 合法语法：

  ```text
  undo ospfv3 bfd enable
  ```

### `undo ospfv3 cost`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore OSPFv3 interface cost
- 合法语法：

  ```text
  undo ospfv3 cost
  ```

### `undo ospfv3 dr-priority`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore OSPFv3 interface router priority
- 合法语法：

  ```text
  undo ospfv3 dr-priority
  ```

### `undo ospfv3 network-type`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore OSPFv3 interface network type
- 合法语法：

  ```text
  undo ospfv3 network-type
  ```

### `undo ospfv3 timer dead`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPFV3 interface dead
- 合法语法：

  ```text
  undo ospfv3 timer dead
  ```

### `undo ospfv3 timer hello`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPFV3 interface hello
- 合法语法：

  ```text
  undo ospfv3 timer hello
  ```

### `undo ospfv3 timer retransmit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPFV3 interface retransmit
- 合法语法：

  ```text
  undo ospfv3 timer retransmit
  ```

### `undo ospfv3 timer transmit-delay`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default OSPFV3 interface transmit-delay
- 合法语法：

  ```text
  undo ospfv3 timer transmit-delay
  ```

### `undo port default vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the access port default VLAN to 1
- 合法语法：

  ```text
  undo port default vlan
  ```

### `undo port link-type`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore portswitch-only L2 mode (access VLAN 1)
- 合法语法：

  ```text
  undo port link-type
  ```

### `undo port trunk allow-pass vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove allowed VLANs from a trunk port
- 合法语法：

  ```text
  undo port trunk allow-pass vlan { VLAN-LIST | all }
  ```

### `undo port trunk pvid vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the trunk native VLAN to 1
- 合法语法：

  ```text
  undo port trunk pvid vlan [VLAN-ID]
  ```

### `undo portswitch`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：return the aggregate to Layer 3 mode；return the interface to L3 mode
- 合法语法：

  ```text
  undo portswitch
  ```

### `undo privatekey`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：clear AmneziaWG key；clear WireGuard key
- 合法语法：

  ```text
  undo privatekey
  ```

### `undo qos lr`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VLAN视图`、`接口视图`
- CLI 帮助：remove interface or VLAN rate limit
- 合法语法：

  ```text
  undo qos lr { inbound | outbound }
  ```

### `undo queues`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`dataplane-if`
- CLI 帮助：Restore default queues
- 合法语法：

  ```text
  undo queues
  ```

### `undo rip bfd`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore RIP BFD timers
- 合法语法：

  ```text
  undo rip bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

### `undo rip bfd enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable RIP BFD on this interface
- 合法语法：

  ```text
  undo rip bfd enable
  ```

### `undo route-static group`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：delete an IPv4 static route group
- 合法语法：

  ```text
  undo route-static group name GROUP
  ```

### `undo shutdown`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`、`接口视图`
- CLI 帮助：bring the interface up；undo shutdown
- 合法语法：

  ```text
  undo shutdown
  ```

### `undo source`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- CLI 帮助：clear AmneziaWG source；clear NVE source address；clear WireGuard source；clear the tunnel source IP address；use automatic peer source selection
- 合法语法：

  ```text
  undo source
  ```

### `undo source-port`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：use a dynamic AmneziaWG client source port；use a dynamic WireGuard client source port
- 合法语法：

  ```text
  undo source-port
  ```

### `undo statistic enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- CLI 帮助：disable counters for this NAT policy；disable counters for this NAT rule；disable detailed interface packet statistics
- 合法语法：

  ```text
  undo statistic enable
  ```

### `undo switchport`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：return the interface to L3 mode
- 合法语法：

  ```text
  undo switchport
  ```

### `undo tcp mss`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove TCP MSS clamping from the interface
- 合法语法：

  ```text
  undo tcp mss
  ```

### `undo traffic-filter`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove an ACL from the interface
- 合法语法：

  ```text
  undo traffic-filter { inbound | outbound }
  ```

### `undo traffic-policy`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VLAN视图`、`接口视图`
- CLI 帮助：remove an MQC traffic policy from the interface；remove the shared MQC policy from this VLAN
- 合法语法：

  ```text
  undo traffic-policy [inbound]
  ```
  ```text
  undo traffic-policy [inbound|outbound]
  ```

### `undo trunkport`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove physical member ports
- 合法语法：

  ```text
  undo trunkport INTERFACE [to INTERFACE]
  ```

### `undo tunnel-protocol`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：clear the tunnel encapsulation protocol
- 合法语法：

  ```text
  undo tunnel-protocol
  ```

### `undo vlan`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a VLAN
- 合法语法：

  ```text
  undo vlan VLAN-ID [to VLAN-ID]
  ```

### `undo vlan batch`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete VLANs in a batch
- 合法语法：

  ```text
  undo vlan batch { VLAN-ID [to VLAN-ID] } *
  ```

### `undo vlan-type`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove the sub-interface VLAN binding
- 合法语法：

  ```text
  undo vlan-type
  ```

### `undo vni`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove head-end peer(s) for a VNI
- 合法语法：

  ```text
  undo vni VNI [head-end peer-list PEER]
  ```

### `undo vrrp vrid`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete or reset an IPv4 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp vrid INTEGER<1-255> [...]
  ```

### `undo vrrp6 vrid`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：delete or reset an IPv6 VRRPv3 group
- 合法语法：

  ```text
  undo vrrp6 vrid INTEGER<1-255> [...]
  ```

### `undo vxlan anycast-gateway enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the distributed VXLAN anycast gateway
- 合法语法：

  ```text
  undo vxlan anycast-gateway enable
  ```

### `undo vxlan vni`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BD视图`、`VPN实例视图`
- CLI 帮助：clear the VXLAN VNI；remove the L3VNI from the VPN instance
- 合法语法：

  ```text
  undo vxlan vni
  ```

### `undo wireguard-profile`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：unbind a WireGuard profile
- 合法语法：

  ```text
  undo wireguard-profile
  ```

### `vlan`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create a VLAN and enter VLAN view
- 合法语法：

  ```text
  vlan VLAN-ID [to VLAN-ID]
  ```

### `vlan batch`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：create VLANs in a batch
- 合法语法：

  ```text
  vlan batch { VLAN-ID [to VLAN-ID] } *
  ```

### `vlan-type dot1q`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind the sub-interface to a VLAN (dot1q)
- 合法语法：

  ```text
  vlan-type dot1q VLAN-ID [inner VLAN-ID]
  ```

### `vni`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：add a head-end peer for a VNI
- 合法语法：

  ```text
  vni VNI head-end peer-list PEER
  ```

### `vrrp vrid`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure an IPv4 VRRPv3 group
- 合法语法：

  ```text
  vrrp vrid INTEGER<1-255> ...
  ```

### `vrrp6 vrid`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure an IPv6 VRRPv3 group
- 合法语法：

  ```text
  vrrp6 vrid INTEGER<1-255> ...
  ```

### `vxlan anycast-gateway enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable the distributed VXLAN anycast gateway
- 合法语法：

  ```text
  vxlan anycast-gateway enable
  ```

### `vxlan vni`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BD视图`、`VPN实例视图`
- CLI 帮助：bind an L3VNI to the VPN instance；set the VXLAN VNI for this bridge-domain
- 合法语法：

  ```text
  vxlan vni VNI
  ```

### `wireguard profile`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter a WireGuard profile
- 合法语法：

  ```text
  wireguard profile NAME
  ```

### `wireguard-profile`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind a WireGuard profile
- 合法语法：

  ```text
  wireguard-profile NAME
  ```

## IP、VPN 与静态路由

### `auto-refresh enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：enable automatic remote-list refresh
- 合法语法：

  ```text
  auto-refresh enable
  ```

### `auto-refresh interval`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：set the remote-list refresh interval
- 合法语法：

  ```text
  auto-refresh interval INTEGER<5-10080>
  ```

### `display ip fib`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the effective VPP IPv4 forwarding table
- 合法语法：

  ```text
  display ip fib [vpn-instance VRF]
  ```

### `display ip interface brief`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv4 interface brief
- 合法语法：

  ```text
  display ip interface brief
  ```

### `display ip ip-prefix`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IP prefix lists
- 合法语法：

  ```text
  display ip ip-prefix [NAME [verbose|first-match PREFIX]]
  ```

### `display ip ipv6-prefix`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 prefix lists
- 合法语法：

  ```text
  display ip ipv6-prefix [NAME [verbose|first-match PREFIX]]
  ```

### `display ip pool`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display IPv4 address pools and server leases
- 合法语法：

  ```text
  display ip pool [name NAME | interface TYPE N] [all | used] [verbose]
  ```

### `display ip routing-table`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the IPv4 routing table
- 合法语法：

  ```text
  display ip routing-table [X.X.X.X [INTEGER<0-32> | X.X.X.X] [longer-match] | vpn-instance NAME | all-vpn-instance | protocol PROTO [inactive | verbose] | statistics | route-number | verbose | all-routes | limit N]
  ```

### `display ip routing-table-group`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv4 static route group applications
- 合法语法：

  ```text
  display ip routing-table-group [name GROUP] [route PREFIX] [verbose]
  ```

### `display ip vpn-instance`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VPN-instance information
- 合法语法：

  ```text
  display ip vpn-instance [NAME | interface | verbose]
  ```

### `display ip vpn-instance interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display interfaces bound to VPN instances
- 合法语法：

  ```text
  display ip vpn-instance interface
  ```

### `display ip vpn-instance verbose`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display verbose VPN-instance information
- 合法语法：

  ```text
  display ip vpn-instance verbose
  ```

### `display ipv6 fib`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 FIB information
- 合法语法：

  ```text
  display ipv6 fib [vpn-instance VRF]
  ```

### `display ipv6 interface brief`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 interface brief
- 合法语法：

  ```text
  display ipv6 interface brief
  ```

### `display ipv6 nd`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 neighbor discovery information
- 合法语法：

  ```text
  display ipv6 nd
  ```

### `display ipv6 neighbors`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 neighbor information
- 合法语法：

  ```text
  display ipv6 neighbors [interface IF | vpn-instance VRF | static | dynamic]
  ```

### `display ipv6 pathmtu`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 path MTU information
- 合法语法：

  ```text
  display ipv6 pathmtu [vpn-instance VRF]
  ```

### `display ipv6 pool`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display IPv6 pool information and server leases
- 合法语法：

  ```text
  display ipv6 pool [name NAME] [all | used] [verbose]
  ```

### `display ipv6 prefix`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 prefix-list information
- 合法语法：

  ```text
  display ipv6 prefix [NAME [verbose|first-match PREFIX]]
  ```

### `display ipv6 route-static group`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 static route groups
- 合法语法：

  ```text
  display ipv6 route-static group [name GROUP] [verbose]
  ```

### `display ipv6 routing-table`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the IPv6 routing table
- 合法语法：

  ```text
  display ipv6 routing-table [X:X::X:X [INTEGER<0-128> | X:X::X:X] [longer-match] | vpn-instance NAME | all-vpn-instance | protocol PROTO [inactive | verbose] | statistics | route-number | verbose | all-routes | limit N]
  ```

### `display ipv6 routing-table-group`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 static route group applications
- 合法语法：

  ```text
  display ipv6 routing-table-group [name GROUP] [route PREFIX] [verbose]
  ```

### `display ipv6 urpf`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 URPF information
- 合法语法：

  ```text
  display ipv6 urpf
  ```

### `display route-static group`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv4 static route groups
- 合法语法：

  ```text
  display route-static group [name GROUP] [verbose]
  ```

### `ip route-static`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure a static IPv4 route
- 合法语法：

  ```text
  ip route-static [vpn-instance DEST-VPN] DEST MASK { NULL 0 | NH | TYPE N [NH] | vpn-instance NH-VRF [NH] } [preference PREF | tag TAG] * [description TEXT]
  ```

### `ip route-static-group`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：apply a static route group
- 合法语法：

  ```text
  ip route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

### `ipv4-family`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`
- CLI 帮助：enter the IPv4 address-family view
- 合法语法：

  ```text
  ipv4-family
  ```

### `ipv6 nd max-number`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set the IPv6 neighbor database capacity
- 合法语法：

  ```text
  ipv6 nd max-number INTEGER<1-4294967295>
  ```

### `ipv6 nd recycle`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure IPv6 neighbor recycling at capacity
- 合法语法：

  ```text
  ipv6 nd recycle { enable | disable }
  ```

### `ipv6 nd stale-timeout`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set the dynamic IPv6 neighbor stale aging time
- 合法语法：

  ```text
  ipv6 nd stale-timeout INTEGER<60-172800>
  ```

### `ipv6 neighbor`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure a static IPv6 neighbor
- 合法语法：

  ```text
  ipv6 neighbor IPV6 MAC interface IF
  ```

### `ipv6 route-static`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure a static IPv6 route
- 合法语法：

  ```text
  ipv6 route-static [vpn-instance DEST-VPN] DEST PREFIXLEN { NULL 0 | NH | TYPE N [NH] | vpn-instance NH-VRF [NH] } [preference PREF | tag TAG] * [description TEXT]
  ```

### `ipv6 route-static-group`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：apply a static route group
- 合法语法：

  ```text
  ipv6 route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

### `ipv6-family`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`
- CLI 帮助：enter the IPv6 address-family view
- 合法语法：

  ```text
  ipv6-family
  ```

### `route`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：add a route prefix
- 合法语法：

  ```text
  route PREFIX [MASK|PREFIXLEN]
  ```

### `route-distinguisher`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- CLI 帮助：configure the route distinguisher；set the EVPN route distinguisher
- 合法语法：

  ```text
  route-distinguisher RD
  ```

### `source file`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：use a CIDR-list file from /VortexROS/route-static-groupd
- 合法语法：

  ```text
  source file FILE
  ```

### `source url`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：set the remote CIDR-list source
- 合法语法：

  ```text
  source url URL [insecure] [vpn-instance NAME] [resolve-address IP]
  ```

### `undo auto-refresh enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：disable automatic remote-list refresh
- 合法语法：

  ```text
  undo auto-refresh enable
  ```

### `undo auto-refresh interval`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：restore the 4320-minute refresh interval
- 合法语法：

  ```text
  undo auto-refresh interval
  ```

### `undo ip ip-prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an IP prefix list entry or list
- 合法语法：

  ```text
  undo ip ip-prefix NAME [index SEQ]
  ```

### `undo ip ipv6-prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an IPv6 prefix list entry or list
- 合法语法：

  ```text
  undo ip ipv6-prefix NAME [index SEQ]
  ```

### `undo ip route-static`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a static IPv4 route
- 合法语法：

  ```text
  undo ip route-static [vpn-instance DEST-VPN] DEST MASK [NULL 0 | NH | TYPE N [NH] [vpn-instance NH-VRF] | vpn-instance NH-VRF [NH]]
  ```

### `undo ip route-static-group`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：apply a static route group
- 合法语法：

  ```text
  undo ip route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

### `undo ip vpn-instance`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a VPN instance
- 合法语法：

  ```text
  undo ip vpn-instance NAME
  ```

### `undo ipv4-family`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VPN实例视图`
- CLI 帮助：delete the IPv4 address-family
- 合法语法：

  ```text
  undo ipv4-family
  ```

### `undo ipv6 nd max-number`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the VPP default IPv6 neighbor capacity
- 合法语法：

  ```text
  undo ipv6 nd max-number
  ```

### `undo ipv6 nd recycle`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the VPP default IPv6 neighbor recycle policy
- 合法语法：

  ```text
  undo ipv6 nd recycle
  ```

### `undo ipv6 nd stale-timeout`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the default IPv6 neighbor stale aging time
- 合法语法：

  ```text
  undo ipv6 nd stale-timeout
  ```

### `undo ipv6 neighbor`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a static IPv6 neighbor
- 合法语法：

  ```text
  undo ipv6 neighbor IPV6 MAC interface IF
  ```

### `undo ipv6 route-static`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a static IPv6 route
- 合法语法：

  ```text
  undo ipv6 route-static [vpn-instance DEST-VPN] DEST PREFIXLEN [NULL 0 | NH | TYPE N [NH] [vpn-instance NH-VRF] | vpn-instance NH-VRF [NH]]
  ```

### `undo ipv6 route-static-group`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：apply a static route group
- 合法语法：

  ```text
  undo ipv6 route-static-group [vpn-instance DEST-VPN] GROUP PATH
  ```

### `undo ipv6-family`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VPN实例视图`
- CLI 帮助：delete the IPv6 address-family
- 合法语法：

  ```text
  undo ipv6-family
  ```

### `undo route`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：delete a route prefix
- 合法语法：

  ```text
  undo route PREFIX [MASK|PREFIXLEN]
  ```

### `undo route-distinguisher`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- CLI 帮助：clear the EVPN route distinguisher；delete the route distinguisher
- 合法语法：

  ```text
  undo route-distinguisher
  ```

### `undo source file`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：remove the local CIDR-list source
- 合法语法：

  ```text
  undo source file
  ```

### `undo source url`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`静态路由组视图`
- CLI 帮助：remove the remote CIDR-list source
- 合法语法：

  ```text
  undo source url
  ```

### `undo vpn-target`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- CLI 帮助：configure an EVPN route target；delete a VPN target
- 合法语法：

  ```text
  undo vpn-target RT [ export-extcommunity | import-extcommunity | both ]
  ```
  ```text
  undo vpn-target RT { export-extcommunity | import-extcommunity }
  ```

### `vpn-target`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`VPN地址族视图`、`VPN实例视图`、`bridge-domain-evpn`
- CLI 帮助：configure a VPN target；configure an EVPN route target
- 合法语法：

  ```text
  vpn-target RT { export-extcommunity | import-extcommunity | both }
  ```
  ```text
  vpn-target RT { export-extcommunity | import-extcommunity }
  ```

## 动态路由、策略路由、BFD 与 VRRP

### `abr-summary`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`ospfv3-area`
- CLI 帮助：configure an OSPFv3 area summary；configure an area summary
- 合法语法：

  ```text
  abr-summary X.X.X.X X.X.X.X [not-advertise]
  ```
  ```text
  abr-summary X:X::X:X INTEGER<0-128> [not-advertise]
  ```

### `advertise l2vpn evpn`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：export VPN routes to the EVPN address family
- 合法语法：

  ```text
  advertise l2vpn evpn
  ```

### `aggregate`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：configure a BGP aggregate route
- 合法语法：

  ```text
  aggregate ADDRESS MASK [as-set] [detail-suppressed]
  ```

### `aggregate-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`
- CLI 帮助：advertise a RIPng aggregate
- 合法语法：

  ```text
  aggregate-address X:X::X/M
  ```

### `apply as-path`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：prepend AS numbers to the BGP AS path
- 合法语法：

  ```text
  apply as-path ASNUM [ASNUM ...]
  ```

### `apply community`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set BGP community values
- 合法语法：

  ```text
  apply community VALUE [VALUE ...] [additive]
  ```

### `apply cost`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set route metric
- 合法语法：

  ```text
  apply cost VALUE
  ```

### `apply ip-address next-hop`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set an IPv4 next hop
- 合法语法：

  ```text
  apply ip-address next-hop X.X.X.X
  ```

### `apply ipv6 next-hop`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set an IPv6 next hop
- 合法语法：

  ```text
  apply ipv6 next-hop X:X::X
  ```

### `apply large-community`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set BGP large-community values
- 合法语法：

  ```text
  apply large-community VALUE [VALUE ...] [additive]
  ```

### `apply local-preference`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set local preference
- 合法语法：

  ```text
  apply local-preference VALUE
  ```

### `apply origin`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set the BGP origin attribute
- 合法语法：

  ```text
  apply origin {igp|egp|incomplete}
  ```

### `apply tag`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set route tag
- 合法语法：

  ```text
  apply tag INTEGER<0-4294967295>
  ```

### `area`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`OSPF视图`、`ospfv3-area`、`ospfv3`
- CLI 帮助：enter an OSPF area view；enter an OSPFv3 area view
- 合法语法：

  ```text
  area X.X.X.X
  ```

### `auto-cost reference-bandwidth`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`
- CLI 帮助：set the OSPF reference bandwidth
- 合法语法：

  ```text
  auto-cost reference-bandwidth INTEGER<1-4294967>
  ```

### `bandwidth-reference`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`ospfv3`
- CLI 帮助：set the OSPFv3 reference bandwidth
- 合法语法：

  ```text
  bandwidth-reference INTEGER<1-4294967>
  ```

### `continue node`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：continue evaluation at a later route-policy node
- 合法语法：

  ```text
  continue node INTEGER<1-65535>
  ```

### `cost-style`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：set IS-IS metric style
- 合法语法：

  ```text
  cost-style {narrow|wide|transition}
  ```

### `default ipv4-unicast`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：activate IPv4 unicast by default
- 合法语法：

  ```text
  default ipv4-unicast
  ```

### `default tcp-protected`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：protect the BGP TCP listener with configured peers
- 合法语法：

  ```text
  default tcp-protected
  ```

### `default-metric`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`
- CLI 帮助：set default metric；set the default metric for redistributed OSPF routes
- 合法语法：

  ```text
  default-metric INTEGER<1-16777214>
  ```
  ```text
  default-metric INTEGER<1-16>
  ```

### `default-route originate`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：originate a default route
- 合法语法：

  ```text
  default-route originate
  ```

### `default-route-advertise`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`ospfv3`
- CLI 帮助：originate a default route into OSPF；originate an IPv6 default route into OSPFv3
- 合法语法：

  ```text
  default-route-advertise [always]
  ```

### `detect-multiplier`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：Detect multiplier
- 合法语法：

  ```text
  detect-multiplier INTEGER
  ```

### `display bfd`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display BFD information
- 合法语法：

  ```text
  display bfd [configuration|session [all|NAME]|statistics]
  ```

### `display bgp`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display BGP information
- 合法语法：

  ```text
  display bgp {peer|routing-table|ipv6|vpnv4|vpnv6|...}
  ```

### `display bgp tcp-protection`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display BGP TCP listener source protection
- 合法语法：

  ```text
  display bgp tcp-protection [verbose]
  ```

### `display isis`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IS-IS information
- 合法语法：

  ```text
  display isis [process-id] [brief|peer|lsdb|route|interface|spf-delay|traffic-eng]
  ```

### `display ospf`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display OSPF information
- 合法语法：

  ```text
  display ospf [process-id] lsdb [{router|network|summary|asbr|ase|nssa|opaque-*} [link-state-id]] [originate-router router-id|self-originate] [age {min-value|max-value} seconds]
  ```

### `display ospfv3`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display OSPFv3 information
- 合法语法：

  ```text
  display ospfv3 [process-id|vpn-instance NAME] [brief|peer|interface|lsdb|routing]
  ```

### `display rip`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display RIP information
- 合法语法：

  ```text
  display rip [process-id] [database|route|interface|statistics]
  ```

### `display ripng`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display RIPng information
- 合法语法：

  ```text
  display ripng [process-id] [database|route|interface|statistics]
  ```

### `display route-policy`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display route policies
- 合法语法：

  ```text
  display route-policy [NAME [verbose]]
  ```

### `display vrrp`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv4 VRRPv3 information
- 合法语法：

  ```text
  display vrrp [brief|interface INTERFACE|statistics|protocol-information|VRID]
  ```

### `graceful-restart`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：set BGP graceful-restart role
- 合法语法：

  ```text
  graceful-restart {enable|helper-only|disable}
  ```

### `graceful-restart timer restart`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：set BGP graceful-restart restart timer
- 合法语法：

  ```text
  graceful-restart timer restart INTEGER<0-4095>
  ```

### `graceful-restart timer wait-for-rib`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：set BGP graceful-restart wait-for-rib timer
- 合法语法：

  ```text
  graceful-restart timer wait-for-rib INTEGER<1-4095>
  ```

### `group`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`
- CLI 帮助：create a case-sensitive BGP peer-group
- 合法语法：

  ```text
  group NAME [internal|external]
  ```

### `hostname dynamic`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：enable the IS-IS dynamic hostname
- 合法语法：

  ```text
  hostname dynamic
  ```

### `if-match cost`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set route metric
- 合法语法：

  ```text
  if-match cost INTEGER<0-4294967295>
  ```

### `if-match ip-prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：match an IP prefix list
- 合法语法：

  ```text
  if-match ip-prefix NAME
  ```

### `if-match ipv6 address prefix-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：match an IPv6 prefix list
- 合法语法：

  ```text
  if-match ipv6 address prefix-list NAME
  ```

### `if-match protocol`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：match the route source protocol
- 合法语法：

  ```text
  if-match protocol {direct|static|ospf|ospfv3|isis|rip|ripng|bgp}
  ```

### `if-match tag`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：set route tag
- 合法语法：

  ```text
  if-match tag INTEGER<0-4294967295>
  ```

### `import-route`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`IS-IS视图`、`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：redistribute IPv6 routes into OSPFv3；redistribute routes into BGP；redistribute routes into IS-IS；redistribute routes into OSPF；redistribute routes into RIP
- 合法语法：

  ```text
  import-route PROTOCOL [route-policy NAME] [cost COST]
  ```
  ```text
  import-route PROTOCOL [route-policy NAME] [cost COST] [type {1|2}]
  ```
  ```text
  import-route {direct|static|ospf|bgp|isis}
  ```
  ```text
  import-route {direct|static|ospf|bgp}
  ```

### `ipv4-family unicast`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：enter the IPv4 unicast address family
- 合法语法：

  ```text
  ipv4-family unicast
  ```

### `ipv4-family vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：enter the IPv4 VPN address family
- 合法语法：

  ```text
  ipv4-family vpn-instance VPN
  ```

### `ipv4-family vpnv4`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：enter the VPNv4 address family
- 合法语法：

  ```text
  ipv4-family vpnv4
  ```

### `ipv6 import-route`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：redistribute IPv6 routes into IS-IS
- 合法语法：

  ```text
  ipv6 import-route {direct|static|ospfv3|bgp}
  ```

### `ipv6-family unicast`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：enter the IPv6 unicast address family
- 合法语法：

  ```text
  ipv6-family unicast
  ```

### `ipv6-family vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：enter the IPv6 VPN address family
- 合法语法：

  ```text
  ipv6-family vpn-instance VPN
  ```

### `ipv6-family vpnv6`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：enter the VPNv6 address family
- 合法语法：

  ```text
  ipv6-family vpnv6
  ```

### `is-level`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：set IS-IS level
- 合法语法：

  ```text
  is-level {level-1|level-2|level-1-2}
  ```

### `l2vpn-family evpn`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：enter the BGP EVPN address family
- 合法语法：

  ```text
  l2vpn-family evpn
  ```

### `load-balancing as-path-ignore`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：allow equal-length different AS paths in BGP ECMP
- 合法语法：

  ```text
  load-balancing as-path-ignore
  ```

### `log-adjacency-changes`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`、`OSPF视图`
- CLI 帮助：log IS-IS adjacency changes；log OSPF adjacency changes
- 合法语法：

  ```text
  log-adjacency-changes
  ```
  ```text
  log-adjacency-changes [detail]
  ```

### `log-session-changes`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：log-session-changes
- 合法语法：

  ```text
  log-session-changes
  ```

### `maximum load-balancing`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：set the maximum OSPFv3 ECMP paths；set the maximum number of BGP equal-cost paths；set the maximum number of RIP equal-cost paths
- 合法语法：

  ```text
  maximum load-balancing INTEGER<1-32>
  ```
  ```text
  maximum load-balancing INTEGER<1-6>
  ```
  ```text
  maximum load-balancing [ebgp|ibgp] INTEGER<1-256>
  ```

### `maximum-paths`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`
- CLI 帮助：set the maximum OSPF ECMP paths
- 合法语法：

  ```text
  maximum-paths INTEGER<1-256>
  ```

### `min-rx-interval`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：Minimum receive interval in milliseconds
- 合法语法：

  ```text
  min-rx-interval INTEGER
  ```

### `min-tx-interval`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：Minimum transmit interval in milliseconds
- 合法语法：

  ```text
  min-tx-interval INTEGER
  ```

### `network-entity`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：set an IS-IS network entity title
- 合法语法：

  ```text
  network-entity NET
  ```

### `nssa`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`ospfv3-area`
- CLI 帮助：configure a not-so-stubby area；configure an OSPFv3 nssa area
- 合法语法：

  ```text
  nssa [no-summary]
  ```

### `offset-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`
- CLI 帮助：adjust RIPng route metrics selected by an IPv6 ACL
- 合法语法：

  ```text
  offset-list ACL {in|out} INTEGER<0-16> [interface IF]
  ```

### `opaque-capability enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`
- CLI 帮助：enable OSPF opaque LSA capability
- 合法语法：

  ```text
  opaque-capability enable
  ```

### `passive-interface default`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：make all RIP interfaces passive
- 合法语法：

  ```text
  passive-interface default
  ```

### `passive-mode`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：passive-mode
- 合法语法：

  ```text
  passive-mode
  ```

### `policy vpn-target`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：control VPN route-target filtering
- 合法语法：

  ```text
  policy vpn-target
  ```

### `preference`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIP视图`
- CLI 帮助：set RIP route preference
- 合法语法：

  ```text
  preference INTEGER<1-255>
  ```

### `reflect between-clients`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：allow route reflection between clients
- 合法语法：

  ```text
  reflect between-clients
  ```

### `reflector cluster-id`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：set the route-reflector cluster ID
- 合法语法：

  ```text
  reflector cluster-id X.X.X.X
  ```

### `router-id`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`OSPF视图`、`ospfv3`
- CLI 帮助：set BGP router ID；set OSPF router ID；set the OSPFv3 router ID
- 合法语法：

  ```text
  router-id X.X.X.X
  ```

### `set-overload-bit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：set the IS-IS overload bit
- 合法语法：

  ```text
  set-overload-bit
  ```

### `silent-interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：suppress OSPF Hellos on an interface；suppress OSPFv3 Hellos on an interface；suppress RIP updates on an interface
- 合法语法：

  ```text
  silent-interface INTERFACE
  ```

### `spf-delay-ietf`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：configure IETF SPF backoff timers
- 合法语法：

  ```text
  spf-delay-ietf init-delay MS short-delay MS long-delay MS holddown MS time-to-learn MS
  ```

### `stub`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`ospfv3-area`
- CLI 帮助：configure a stub area；configure an OSPFv3 stub area
- 合法语法：

  ```text
  stub [no-summary]
  ```

### `timer keepalive`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：set BGP keepalive and hold timers
- 合法语法：

  ```text
  timer keepalive INTEGER<0-21845> hold INTEGER<0-65535>
  ```

### `timers rip`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：set RIP update, timeout and garbage timers
- 合法语法：

  ```text
  timers rip INTEGER<1-32767> INTEGER<1-32767> INTEGER<1-32767>
  ```

### `undo abr-summary`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`ospfv3-area`
- CLI 帮助：delete an area summary；remove an OSPFv3 area summary
- 合法语法：

  ```text
  undo abr-summary X.X.X.X X.X.X.X
  ```
  ```text
  undo abr-summary X:X::X:X INTEGER<0-128>
  ```

### `undo advertise l2vpn evpn`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：export VPN routes to the EVPN address family
- 合法语法：

  ```text
  undo advertise l2vpn evpn
  ```

### `undo aggregate`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：delete a BGP aggregate route
- 合法语法：

  ```text
  undo aggregate ADDRESS MASK
  ```

### `undo aggregate-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`
- CLI 帮助：withdraw a RIPng aggregate
- 合法语法：

  ```text
  undo aggregate-address X:X::X/M
  ```

### `undo apply as-path`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the AS-path prepend action
- 合法语法：

  ```text
  undo apply as-path
  ```

### `undo apply community`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the BGP community action
- 合法语法：

  ```text
  undo apply community
  ```

### `undo apply cost`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：restore default route metric
- 合法语法：

  ```text
  undo apply cost
  ```

### `undo apply ip-address next-hop`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the IPv4 next-hop action
- 合法语法：

  ```text
  undo apply ip-address next-hop
  ```

### `undo apply ipv6 next-hop`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the IPv6 next-hop action
- 合法语法：

  ```text
  undo apply ipv6 next-hop
  ```

### `undo apply large-community`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the BGP large-community action
- 合法语法：

  ```text
  undo apply large-community
  ```

### `undo apply local-preference`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：restore default local preference
- 合法语法：

  ```text
  undo apply local-preference
  ```

### `undo apply origin`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the BGP origin action
- 合法语法：

  ```text
  undo apply origin
  ```

### `undo apply tag`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove route tag
- 合法语法：

  ```text
  undo apply tag
  ```

### `undo auto-cost reference-bandwidth`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`
- CLI 帮助：restore the OSPF reference bandwidth
- 合法语法：

  ```text
  undo auto-cost reference-bandwidth
  ```

### `undo bandwidth-reference`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`ospfv3`
- CLI 帮助：restore the OSPFv3 reference bandwidth
- 合法语法：

  ```text
  undo bandwidth-reference
  ```

### `undo bgp`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a BGP instance
- 合法语法：

  ```text
  undo bgp ASNUM
  ```

### `undo continue`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：stop evaluation after this route-policy node
- 合法语法：

  ```text
  undo continue
  ```

### `undo default ipv4-unicast`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`
- CLI 帮助：disable automatic IPv4-unicast peer activation
- 合法语法：

  ```text
  undo default ipv4-unicast
  ```

### `undo default tcp-protected`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：disable BGP TCP listener peer protection
- 合法语法：

  ```text
  undo default tcp-protected
  ```

### `undo default-metric`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`
- CLI 帮助：restore default metric；restore the default OSPF redistribution metric
- 合法语法：

  ```text
  undo default-metric
  ```

### `undo default-route originate`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：stop originating a default route
- 合法语法：

  ```text
  undo default-route originate
  ```

### `undo default-route-advertise`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`ospfv3`
- CLI 帮助：remove OSPF default route advertisement；stop originating an IPv6 default route
- 合法语法：

  ```text
  undo default-route-advertise
  ```

### `undo detect-multiplier`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：restore the default Detect multiplier
- 合法语法：

  ```text
  undo detect-multiplier
  ```

### `undo graceful-restart`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：restore the default BGP graceful-restart helper role
- 合法语法：

  ```text
  undo graceful-restart
  ```

### `undo graceful-restart timer restart`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：restore BGP graceful-restart restart timer
- 合法语法：

  ```text
  undo graceful-restart timer restart
  ```

### `undo graceful-restart timer wait-for-rib`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：restore BGP graceful-restart wait-for-rib timer
- 合法语法：

  ```text
  undo graceful-restart timer wait-for-rib
  ```

### `undo group`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`
- CLI 帮助：delete an unused BGP peer-group
- 合法语法：

  ```text
  undo group NAME
  ```

### `undo hostname`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：restore the default IS-IS hostname
- 合法语法：

  ```text
  undo hostname
  ```

### `undo if-match cost`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove route metric
- 合法语法：

  ```text
  undo if-match cost
  ```

### `undo if-match ip-prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove an IP prefix match
- 合法语法：

  ```text
  undo if-match ip-prefix NAME
  ```

### `undo if-match ipv6 address prefix-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove an IPv6 prefix match
- 合法语法：

  ```text
  undo if-match ipv6 address prefix-list NAME
  ```

### `undo if-match protocol`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove the route source protocol match
- 合法语法：

  ```text
  undo if-match protocol
  ```

### `undo if-match tag`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`路由策略视图`
- CLI 帮助：remove route tag
- 合法语法：

  ```text
  undo if-match tag
  ```

### `undo import-route`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`IS-IS视图`、`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：stop redistributing routes into BGP；stop redistributing routes into IS-IS；stop redistributing routes into OSPF；stop redistributing routes into OSPFv3；stop redistributing routes into RIP
- 合法语法：

  ```text
  undo import-route PROTOCOL
  ```

### `undo ipv4-family vpn-instance`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：remove an IPv4 VPN address family
- 合法语法：

  ```text
  undo ipv4-family vpn-instance VPN
  ```

### `undo ipv4-family vpnv4`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：remove the VPNv4 address family
- 合法语法：

  ```text
  undo ipv4-family vpnv4
  ```

### `undo ipv6 import-route`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：stop redistributing IPv6 routes into IS-IS
- 合法语法：

  ```text
  undo ipv6 import-route PROTOCOL
  ```

### `undo ipv6-family unicast`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：remove the IPv6 unicast address family
- 合法语法：

  ```text
  undo ipv6-family unicast
  ```

### `undo ipv6-family vpn-instance`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：remove an IPv6 VPN address family
- 合法语法：

  ```text
  undo ipv6-family vpn-instance VPN
  ```

### `undo ipv6-family vpnv6`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：remove the VPNv6 address family
- 合法语法：

  ```text
  undo ipv6-family vpnv6
  ```

### `undo is-level`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：restore IS-IS level
- 合法语法：

  ```text
  undo is-level
  ```

### `undo isis`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an IS-IS process
- 合法语法：

  ```text
  undo isis INTEGER<1-65535>
  ```

### `undo l2vpn-family evpn`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：remove the BGP EVPN address family
- 合法语法：

  ```text
  undo l2vpn-family evpn
  ```

### `undo load-balancing as-path-ignore`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：require identical AS paths for BGP ECMP
- 合法语法：

  ```text
  undo load-balancing as-path-ignore
  ```

### `undo log-adjacency-changes`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`、`OSPF视图`
- CLI 帮助：stop logging IS-IS adjacency changes；stop logging OSPF adjacency changes
- 合法语法：

  ```text
  undo log-adjacency-changes
  ```

### `undo log-session-changes`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：undo log-session-changes
- 合法语法：

  ```text
  undo log-session-changes
  ```

### `undo maximum load-balancing`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：restore RIP path default；restore the OSPFv3 ECMP path limit；restore the default BGP equal-cost path count
- 合法语法：

  ```text
  undo maximum load-balancing
  ```
  ```text
  undo maximum load-balancing [ebgp|ibgp]
  ```

### `undo maximum-paths`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`
- CLI 帮助：restore the default OSPF ECMP path count
- 合法语法：

  ```text
  undo maximum-paths
  ```

### `undo min-rx-interval`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：restore the default Minimum receive interval in milliseconds
- 合法语法：

  ```text
  undo min-rx-interval
  ```

### `undo min-tx-interval`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：restore the default Minimum transmit interval in milliseconds
- 合法语法：

  ```text
  undo min-tx-interval
  ```

### `undo network-entity`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：remove an IS-IS network entity title
- 合法语法：

  ```text
  undo network-entity NET
  ```

### `undo nssa`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`ospfv3-area`
- CLI 帮助：restore a normal OSPF area；restore a normal OSPFv3 area
- 合法语法：

  ```text
  undo nssa
  ```

### `undo offset-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`
- CLI 帮助：remove a RIPng metric offset
- 合法语法：

  ```text
  undo offset-list {in|out} [interface IF]
  ```

### `undo opaque-capability enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`
- CLI 帮助：disable OSPF opaque LSA capability
- 合法语法：

  ```text
  undo opaque-capability enable
  ```

### `undo ospf`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an OSPF process
- 合法语法：

  ```text
  undo ospf INTEGER<1-65535>
  ```

### `undo passive-interface default`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：restore passive interface default
- 合法语法：

  ```text
  undo passive-interface default
  ```

### `undo passive-mode`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：undo passive-mode
- 合法语法：

  ```text
  undo passive-mode
  ```

### `undo policy vpn-target`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：control VPN route-target filtering
- 合法语法：

  ```text
  undo policy vpn-target
  ```

### `undo preference`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIP视图`
- CLI 帮助：restore RIP route preference
- 合法语法：

  ```text
  undo preference
  ```

### `undo reflect between-clients`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：disable route reflection between clients
- 合法语法：

  ```text
  undo reflect between-clients
  ```

### `undo reflector cluster-id`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：restore the router ID as the cluster ID
- 合法语法：

  ```text
  undo reflector cluster-id
  ```

### `undo rip`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a RIP process
- 合法语法：

  ```text
  undo rip INTEGER<1-65535> [vpn-instance NAME]
  ```

### `undo ripng`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a RIP process
- 合法语法：

  ```text
  undo ripng INTEGER<1-65535> [vpn-instance NAME]
  ```

### `undo route-policy`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a route policy
- 合法语法：

  ```text
  undo route-policy NAME [permit|deny node INTEGER<1-65535>]
  ```

### `undo router-id`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`OSPF视图`、`ospfv3`
- CLI 帮助：remove BGP router ID；remove OSPF router ID；remove the OSPFv3 router ID
- 合法语法：

  ```text
  undo router-id
  ```

### `undo set-overload-bit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：clear the IS-IS overload bit
- 合法语法：

  ```text
  undo set-overload-bit
  ```

### `undo silent-interface`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：enable RIP updates on an interface；restore OSPF Hellos on an interface；restore OSPFv3 Hellos on an interface
- 合法语法：

  ```text
  undo silent-interface INTERFACE
  ```

### `undo spf-delay-ietf`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`
- CLI 帮助：disable IETF SPF backoff timers
- 合法语法：

  ```text
  undo spf-delay-ietf
  ```

### `undo stub`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`ospfv3-area`
- CLI 帮助：restore a normal OSPF area；restore a normal OSPFv3 area
- 合法语法：

  ```text
  undo stub
  ```

### `undo timer keepalive`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：restore BGP keepalive and hold timers
- 合法语法：

  ```text
  undo timer keepalive
  ```

### `undo timers rip`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：restore RIP timers
- 合法语法：

  ```text
  undo timers rip
  ```

### `version`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIP视图`
- CLI 帮助：set RIP version
- 合法语法：

  ```text
  version {1|2}
  ```

## MPLS LDP 与 L3VPN

### `display mpls forwarding-table`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the VPP MPLS forwarding table
- 合法语法：

  ```text
  display mpls forwarding-table
  ```

### `display mpls interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display MPLS-enabled interfaces
- 合法语法：

  ```text
  display mpls interface
  ```

### `display mpls ldp binding`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display LDP label bindings
- 合法语法：

  ```text
  display mpls ldp binding
  ```

### `display mpls ldp interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display LDP interface state
- 合法语法：

  ```text
  display mpls ldp interface
  ```

### `display mpls ldp peer`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display LDP peers
- 合法语法：

  ```text
  display mpls ldp peer
  ```

### `display mpls lsp`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the Zebra MPLS forwarding table
- 合法语法：

  ```text
  display mpls lsp
  ```

### `mpls`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：enable MPLS and enter the MPLS view；enable MPLS forwarding on the interface
- 合法语法：

  ```text
  mpls
  ```

### `mpls ldp`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：enable LDP discovery on the interface；enable MPLS LDP globally
- 合法语法：

  ```text
  mpls ldp
  ```

### `mpls lsr-id`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure the MPLS label switching router ID
- 合法语法：

  ```text
  mpls lsr-id A.B.C.D
  ```

### `ttl propagate`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`mpls`
- CLI 帮助：use uniform MPLS TTL propagation
- 合法语法：

  ```text
  ttl propagate
  ```

### `undo mpls`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：disable MPLS forwarding on the interface；disable MPLS globally
- 合法语法：

  ```text
  undo mpls
  ```

### `undo mpls ldp`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`、`系统视图`
- CLI 帮助：disable LDP discovery on the interface；disable MPLS LDP globally
- 合法语法：

  ```text
  undo mpls ldp
  ```

### `undo mpls lsr-id`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：remove the MPLS label switching router ID
- 合法语法：

  ```text
  undo mpls lsr-id
  ```

### `undo ttl propagate`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`mpls`
- CLI 帮助：use pipe mode and hide MPLS transit hops
- 合法语法：

  ```text
  undo ttl propagate
  ```

## GRE、IP-in-IP、VXLAN、WireGuard 与 AmneziaWG

### `allowd-ip`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- CLI 帮助：add an allowed IP selector (longest prefix selects the peer)
- 合法语法：

  ```text
  allowd-ip IP LENGTH
  ```

### `disable-cookies enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：enable cookie replies disabled
- 合法语法：

  ```text
  disable-cookies enable
  ```

### `display amneziawg`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display AmneziaWG configuration and runtime
- 合法语法：

  ```text
  display amneziawg { profile [NAME] | peer [PROFILE [PEER]] | interface [TUNNEL] }
  ```

### `display vxlan statistics`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display VXLAN tunnel traffic statistics
- 合法语法：

  ```text
  display vxlan statistics source IP peer IP [vni VNI]
  ```

### `display vxlan tunnel`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display static VXLAN tunnels (from NVE peer-list)
- 合法语法：

  ```text
  display vxlan tunnel [ID]
  ```

### `display wireguard`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display WireGuard configuration and runtime
- 合法语法：

  ```text
  display wireguard { profile [NAME] | peer [PROFILE [PEER]] | interface [TUNNEL] }
  ```

### `evpn-overlay`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable EVPN as the VXLAN overlay control plane
- 合法语法：

  ```text
  evpn-overlay enable
  ```

### `header cookie`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set cookie message header range
- 合法语法：

  ```text
  header cookie LOW HIGH
  ```

### `header init`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set init message header range
- 合法语法：

  ```text
  header init LOW HIGH
  ```

### `header response`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set response message header range
- 合法语法：

  ```text
  header response LOW HIGH
  ```

### `header transport`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set transport message header range
- 合法语法：

  ```text
  header transport LOW HIGH
  ```

### `header-protection`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：enable ChaCha20 message header protection
- 合法语法：

  ```text
  header-protection { KEY | cipher CIPHERTEXT }
  ```

### `junk count`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set random junk packet count
- 合法语法：

  ```text
  junk count INTEGER<0-128>
  ```

### `junk size`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set random junk packet size range
- 合法语法：

  ```text
  junk size MIN MAX
  ```

### `junk-packet`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set a raw or dynamic handshake signature packet
- 合法语法：

  ```text
  junk-packet SLOT { BASE64 | expression EXPRESSION }
  ```

### `keepalive`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- CLI 帮助：set persistent keepalive
- 合法语法：

  ```text
  keepalive SECONDS
  ```

### `padding content`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set decrypted content padding range
- 合法语法：

  ```text
  padding content MIN MAX
  ```

### `padding cookie`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set cookie reply fixed padding
- 合法语法：

  ```text
  padding cookie INTEGER<0-1024>
  ```

### `padding init`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set handshake initiation fixed padding
- 合法语法：

  ```text
  padding init INTEGER<0-1024>
  ```

### `padding response`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set handshake response fixed padding
- 合法语法：

  ```text
  padding response INTEGER<0-1024>
  ```

### `padding transport`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set transport packet fixed padding
- 合法语法：

  ```text
  padding transport INTEGER<0-1024>
  ```

### `peer`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`WireGuard Profile视图`、`amneziawg-profile`
- CLI 帮助：configure a BGP neighbor；enter a WireGuard peer；enter an AmneziaWG peer
- 合法语法：

  ```text
  peer NAME
  ```
  ```text
  peer X.X.X.X [option ...]
  ```

### `presharedkey`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- CLI 帮助：set AmneziaWG peer presharedkey；set WireGuard peer presharedkey
- 合法语法：

  ```text
  presharedkey { KEY | cipher CIPHERTEXT }
  ```

### `publickey`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- CLI 帮助：set AmneziaWG peer publickey；set WireGuard peer publickey；validate the derived AmneziaWG public key during configuration replay；validate the derived WireGuard public key during configuration replay
- 合法语法：

  ```text
  publickey KEY
  ```

### `random-trailers enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：enable random packet trailers
- 合法语法：

  ```text
  random-trailers enable
  ```

### `timing keepalive`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set keepalive random range
- 合法语法：

  ```text
  timing keepalive LOW HIGH
  ```

### `timing max-handshakes`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set max-handshakes random range
- 合法语法：

  ```text
  timing max-handshakes LOW HIGH
  ```

### `timing reject-after`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set reject-after random range
- 合法语法：

  ```text
  timing reject-after LOW HIGH
  ```

### `timing rekey-after`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set rekey-after random range
- 合法语法：

  ```text
  timing rekey-after LOW HIGH
  ```

### `timing rekey-timeout`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set rekey-timeout random range
- 合法语法：

  ```text
  timing rekey-timeout LOW HIGH
  ```

### `undo allowd-ip`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- CLI 帮助：remove an allowed IP selector
- 合法语法：

  ```text
  undo allowd-ip IP LENGTH
  ```

### `undo amneziawg profile`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an AmneziaWG profile
- 合法语法：

  ```text
  undo amneziawg profile NAME
  ```

### `undo disable-cookies enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：disable cookie replies disabled
- 合法语法：

  ```text
  undo disable-cookies enable
  ```

### `undo evpn-overlay`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable EVPN as the VXLAN overlay control plane
- 合法语法：

  ```text
  undo evpn-overlay enable
  ```

### `undo header cookie`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default cookie message header
- 合法语法：

  ```text
  undo header cookie
  ```

### `undo header init`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default init message header
- 合法语法：

  ```text
  undo header init
  ```

### `undo header response`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default response message header
- 合法语法：

  ```text
  undo header response
  ```

### `undo header transport`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default transport message header
- 合法语法：

  ```text
  undo header transport
  ```

### `undo header-protection`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：disable message header protection
- 合法语法：

  ```text
  undo header-protection
  ```

### `undo junk count`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default junk packet count
- 合法语法：

  ```text
  undo junk count
  ```

### `undo junk size`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default junk packet size
- 合法语法：

  ```text
  undo junk size
  ```

### `undo junk-packet`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：delete a raw junk UDP payload slot
- 合法语法：

  ```text
  undo junk-packet SLOT
  ```

### `undo keepalive`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- CLI 帮助：clear persistent keepalive
- 合法语法：

  ```text
  undo keepalive
  ```

### `undo padding content`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default content padding
- 合法语法：

  ```text
  undo padding content
  ```

### `undo padding cookie`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default cookie reply padding
- 合法语法：

  ```text
  undo padding cookie
  ```

### `undo padding init`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default handshake initiation padding
- 合法语法：

  ```text
  undo padding init
  ```

### `undo padding response`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default handshake response padding
- 合法语法：

  ```text
  undo padding response
  ```

### `undo padding transport`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default transport packet padding
- 合法语法：

  ```text
  undo padding transport
  ```

### `undo peer`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`WireGuard Profile视图`、`amneziawg-profile`
- CLI 帮助：delete a WireGuard peer；delete an AmneziaWG peer；remove or reset a BGP neighbor or peer-group
- 合法语法：

  ```text
  undo peer NAME
  ```
  ```text
  undo peer PEER [option]
  ```

### `undo presharedkey`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- CLI 帮助：clear AmneziaWG peer presharedkey；clear WireGuard peer presharedkey
- 合法语法：

  ```text
  undo presharedkey
  ```

### `undo publickey`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- CLI 帮助：clear AmneziaWG peer publickey；clear WireGuard peer publickey
- 合法语法：

  ```text
  undo publickey
  ```

### `undo random-trailers enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：disable random packet trailers
- 合法语法：

  ```text
  undo random-trailers enable
  ```

### `undo timing keepalive`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default keepalive timing
- 合法语法：

  ```text
  undo timing keepalive
  ```

### `undo timing max-handshakes`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default max-handshakes timing
- 合法语法：

  ```text
  undo timing max-handshakes
  ```

### `undo timing reject-after`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default reject-after timing
- 合法语法：

  ```text
  undo timing reject-after
  ```

### `undo timing rekey-after`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default rekey-after timing
- 合法语法：

  ```text
  undo timing rekey-after
  ```

### `undo timing rekey-timeout`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default rekey-timeout timing
- 合法语法：

  ```text
  undo timing rekey-timeout
  ```

### `undo wireguard profile`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a WireGuard profile
- 合法语法：

  ```text
  undo wireguard profile NAME
  ```

## ACL、QoS、MQC、MSS 与 NAT

### `action dnat`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：set DNAT action
- 合法语法：

  ```text
  action dnat IP [port PORT]
  ```

### `action no-nat`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：permit matching flows without translation
- 合法语法：

  ```text
  action no-nat
  ```

### `action snat`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：set SNAT action
- 合法语法：

  ```text
  action snat { pat | no-pat } { interface | address-pool NAME }
  ```

### `action static-nat`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：set static prefix translation
- 合法语法：

  ```text
  action static-nat PREFIX
  ```

### `action twice-nat`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：translate both source and destination
- 合法语法：

  ```text
  action twice-nat source IP [port PORT] destination IP [port PORT]
  ```

### `address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT地址池视图`、`NAT地址集视图`
- CLI 帮助：add an IPv4 prefix to this NAT address-pool；add an IPv4 prefix to this NAT address-set
- 合法语法：

  ```text
  address { IP | IP/LEN | IP MASK }
  ```

### `apply config`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：restart VPP and apply the saved config.cfg configuration
- 合法语法：

  ```text
  apply config
  ```

### `car`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：configure traffic policing (CAR)
- 合法语法：

  ```text
  car cir CIR [kbps|mbps] [pir PIR [kbps|mbps]] [cbs CBS [pbs PBS]] [green|yellow|red pass|discard|remark dscp DSCP]
  ```

### `classifier`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流策略视图`
- CLI 帮助：bind a classifier to a behavior
- 合法语法：

  ```text
  classifier C behavior B [precedence N]
  ```

### `deny`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：deny matching packets
- 合法语法：

  ```text
  deny
  ```

### `destination address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match destination address
- 合法语法：

  ```text
  destination address { IP MASK | IP/LEN | IP }
  ```

### `destination address-set name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match a reusable NAT address-set
- 合法语法：

  ```text
  destination address-set name NAME
  ```

### `destination port`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match a transport port or range
- 合法语法：

  ```text
  destination port { PORT | LOW-HIGH }
  ```

### `destination port-set name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match a reusable NAT port-set
- 合法语法：

  ```text
  destination port-set name NAME
  ```

### `destination vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match an exact source/destination VPN instance
- 合法语法：

  ```text
  destination vpn-instance NAME
  ```

### `display acl`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：list ACLs and their rules (name-based)
- 合法语法：

  ```text
  display acl [ipv6] [all | name NAME]
  ```

### `display nat-policy`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display NAT policy configuration and runtime state
- 合法语法：

  ```text
  display nat-policy { all | name NAME | address-set [NAME] | port-set [NAME] | address-pool [NAME] | runtime | objects | interfaces | statistics [name POLICY] | sessions [FILTERS] | configuration | workers }
  ```

### `display traffic behavior`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display MQC traffic behaviors
- 合法语法：

  ```text
  display traffic behavior [user-defined [NAME]]
  ```

### `display traffic classifier`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display MQC traffic classifiers
- 合法语法：

  ```text
  display traffic classifier [user-defined [NAME]]
  ```

### `display traffic policy`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display MQC traffic policies
- 合法语法：

  ```text
  display traffic policy [user-defined [NAME]]
  ```

### `hairpin enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT策略视图`
- CLI 帮助：allow this policy's published mappings to be used for NAT hairpin
- 合法语法：

  ```text
  hairpin enable
  ```

### `if-match`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流分类器视图`
- CLI 帮助：configure a classifier match rule
- 合法语法：

  ```text
  if-match [not] CONDITION
  ```

### `if-match any`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流分类器视图`
- CLI 帮助：match any packet
- 合法语法：

  ```text
  if-match any
  ```

### `nat-policy hairpin enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable NAT hairpin translations
- 合法语法：

  ```text
  nat-policy hairpin enable
  ```

### `nat-policy interface-pat-range`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set the interface-source PAT port range
- 合法语法：

  ```text
  nat-policy interface-pat-range LOW-HIGH
  ```

### `nat-policy sessions-per-worker`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set the per-worker session capacity
- 合法语法：

  ```text
  nat-policy sessions-per-worker NUMBER
  ```

### `nat-policy timeout`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set a nat-policy session timeout
- 合法语法：

  ```text
  nat-policy timeout CLASS SECONDS
  ```

### `nat-policy x86-tune expire-check-ms`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set nat-policy maintenance interval
- 合法语法：

  ```text
  nat-policy x86-tune expire-check-ms 10..1000
  ```

### `nat-policy x86-tune lru-refresh-ms`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set nat-policy maintenance interval
- 合法语法：

  ```text
  nat-policy x86-tune lru-refresh-ms 10..1000
  ```

### `pat-port-range`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT地址池视图`
- CLI 帮助：set the address-pool PAT allocation range
- 合法语法：

  ```text
  pat-port-range LOW-HIGH
  ```

### `permit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：permit matching packets
- 合法语法：

  ```text
  permit
  ```

### `port`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT端口集视图`
- CLI 帮助：add a port or inclusive range to this NAT port-set
- 合法语法：

  ```text
  port { PORT | LOW-HIGH }
  ```

### `priority`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：set rule priority; lower values run first
- 合法语法：

  ```text
  priority 0..9998
  ```

### `protocol`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match an IP protocol
- 合法语法：

  ```text
  protocol { any | tcp | udp | icmp | NUMBER }
  ```

### `redirect`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：configure PBR redirect
- 合法语法：

  ```text
  redirect ip-nexthop IP | ipv6-nexthop IPv6 [interface IF] [vpn-instance VRF] | interface IF | vpn-instance VRF
  ```

### `remark dscp`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：remark packet DSCP
- 合法语法：

  ```text
  remark dscp DSCP
  ```

### `rule`

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

### `session-limit`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT策略视图`
- CLI 帮助：set this policy's session quota
- 合法语法：

  ```text
  session-limit { unlimited | NUMBER }
  ```

### `source address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match source address
- 合法语法：

  ```text
  source address { IP MASK | IP/LEN | IP }
  ```

### `source address-set name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match a reusable NAT address-set
- 合法语法：

  ```text
  source address-set name NAME
  ```

### `source port`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match a transport port or range
- 合法语法：

  ```text
  source port { PORT | LOW-HIGH }
  ```

### `source port-set name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match a reusable NAT port-set
- 合法语法：

  ```text
  source port-set name NAME
  ```

### `source vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：match an exact source/destination VPN instance
- 合法语法：

  ```text
  source vpn-instance NAME
  ```

### `undo acl ipv6 name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an ACL
- 合法语法：

  ```text
  undo acl ipv6 name NAME
  ```

### `undo acl name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an ACL
- 合法语法：

  ```text
  undo acl name NAME
  ```

### `undo action`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：remove the translation action
- 合法语法：

  ```text
  undo action
  ```

### `undo action snat`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：remove SNAT action
- 合法语法：

  ```text
  undo action snat
  ```

### `undo address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT地址池视图`、`NAT地址集视图`
- CLI 帮助：remove an IPv4 prefix from this NAT address-pool；remove an IPv4 prefix from this NAT address-set
- 合法语法：

  ```text
  undo address { IP | IP/LEN | IP MASK }
  ```

### `undo car`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：remove traffic policing (CAR)
- 合法语法：

  ```text
  undo car
  ```

### `undo classifier`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流策略视图`
- CLI 帮助：unbind a classifier from the policy
- 合法语法：

  ```text
  undo classifier [NAME]
  ```

### `undo deny`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：undo deny
- 合法语法：

  ```text
  undo deny
  ```

### `undo destination address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：clear destination address match
- 合法语法：

  ```text
  undo destination address
  ```

### `undo destination address-set name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：clear the reusable NAT address-set match
- 合法语法：

  ```text
  undo destination address-set name
  ```

### `undo destination port`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：clear the transport port match
- 合法语法：

  ```text
  undo destination port
  ```

### `undo destination port-set name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：clear the reusable NAT port-set match
- 合法语法：

  ```text
  undo destination port-set name
  ```

### `undo destination vpn-instance`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：restore ANY VPN match
- 合法语法：

  ```text
  undo destination vpn-instance
  ```

### `undo hairpin enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT策略视图`
- CLI 帮助：prevent this policy's mappings from being used for NAT hairpin
- 合法语法：

  ```text
  undo hairpin enable
  ```

### `undo if-match`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流分类器视图`
- CLI 帮助：remove the classifier match rule
- 合法语法：

  ```text
  undo if-match [TYPE]
  ```

### `undo nat-policy address-pool name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a NAT address-pool
- 合法语法：

  ```text
  undo nat-policy address-pool name NAME
  ```

### `undo nat-policy address-set name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a NAT address-set
- 合法语法：

  ```text
  undo nat-policy address-set name NAME
  ```

### `undo nat-policy hairpin enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable NAT hairpin translations
- 合法语法：

  ```text
  undo nat-policy hairpin enable
  ```

### `undo nat-policy interface-pat-range`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the default interface PAT range
- 合法语法：

  ```text
  undo nat-policy interface-pat-range
  ```

### `undo nat-policy name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a NAT policy
- 合法语法：

  ```text
  undo nat-policy name NAME
  ```

### `undo nat-policy port-set name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a NAT port-set
- 合法语法：

  ```text
  undo nat-policy port-set name NAME
  ```

### `undo nat-policy sessions-per-worker`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the default per-worker session capacity
- 合法语法：

  ```text
  undo nat-policy sessions-per-worker
  ```

### `undo nat-policy timeout`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore one nat-policy session timeout
- 合法语法：

  ```text
  undo nat-policy timeout CLASS
  ```

### `undo nat-policy x86-tune expire-check-ms`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the default maintenance interval
- 合法语法：

  ```text
  undo nat-policy x86-tune expire-check-ms
  ```

### `undo nat-policy x86-tune lru-refresh-ms`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：restore the default maintenance interval
- 合法语法：

  ```text
  undo nat-policy x86-tune lru-refresh-ms
  ```

### `undo pat-port-range`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT地址池视图`
- CLI 帮助：restore the default address-pool PAT range
- 合法语法：

  ```text
  undo pat-port-range
  ```

### `undo permit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：undo permit
- 合法语法：

  ```text
  undo permit
  ```

### `undo port`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT端口集视图`
- CLI 帮助：remove a port or range from this NAT port-set
- 合法语法：

  ```text
  undo port { PORT | LOW-HIGH }
  ```

### `undo precedence`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流策略视图`
- CLI 帮助：remove classifier precedence from the policy
- 合法语法：

  ```text
  undo precedence
  ```

### `undo priority`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：derive priority from rule ID
- 合法语法：

  ```text
  undo priority
  ```

### `undo protocol`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：restore ANY protocol match
- 合法语法：

  ```text
  undo protocol
  ```

### `undo redirect`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：remove PBR redirect
- 合法语法：

  ```text
  undo redirect
  ```

### `undo remark dscp`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`流行为视图`
- CLI 帮助：remove DSCP remarking
- 合法语法：

  ```text
  undo remark dscp
  ```

### `undo rule`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`ACL视图`、`NAT策略视图`、`acl6`
- CLI 帮助：delete a NAT rule；delete an ACL rule
- 合法语法：

  ```text
  undo rule ID
  ```

### `undo session-limit`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT策略视图`
- CLI 帮助：remove this policy's session quota
- 合法语法：

  ```text
  undo session-limit
  ```

### `undo source address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：clear source address match
- 合法语法：

  ```text
  undo source address
  ```

### `undo source address-set name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：clear the reusable NAT address-set match
- 合法语法：

  ```text
  undo source address-set name
  ```

### `undo source port`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：clear the transport port match
- 合法语法：

  ```text
  undo source port
  ```

### `undo source port-set name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：clear the reusable NAT port-set match
- 合法语法：

  ```text
  undo source port-set name
  ```

### `undo source vpn-instance`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`NAT规则视图`
- CLI 帮助：restore ANY VPN match
- 合法语法：

  ```text
  undo source vpn-instance
  ```

### `undo traffic behavior`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a traffic behavior
- 合法语法：

  ```text
  undo traffic behavior NAME
  ```

### `undo traffic classifier`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a traffic classifier
- 合法语法：

  ```text
  undo traffic classifier NAME
  ```

### `undo traffic policy`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete a traffic policy
- 合法语法：

  ```text
  undo traffic policy NAME
  ```

## DHCP、LLDP 与 SNMP

### `address prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：configure a stateful IPv6 allocation prefix
- 合法语法：

  ```text
  address prefix X:X::X/M [life-time VALID PREFERRED]
  ```

### `display dhcp client`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv4 client state
- 合法语法：

  ```text
  display dhcp client [interface IF]
  ```

### `display dhcp configuration`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCP configuration summary
- 合法语法：

  ```text
  display dhcp configuration
  ```

### `display dhcp relay`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv4 relay state
- 合法语法：

  ```text
  display dhcp relay [interface IF]
  ```

### `display dhcp service`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCP service status
- 合法语法：

  ```text
  display dhcp service [verbose]
  ```

### `display dhcpv6 client`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv6 client state
- 合法语法：

  ```text
  display dhcpv6 client [interface IF]
  ```

### `display dhcpv6 client prefix`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv6 delegated-prefix state
- 合法语法：

  ```text
  display dhcpv6 client prefix [name PREFIX-NAME]
  ```

### `display dhcpv6 pool`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display IPv6 address pools and server leases
- 合法语法：

  ```text
  display dhcpv6 pool [name NAME] [all | used] [verbose]
  ```

### `display dhcpv6 relay`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv6 relay state
- 合法语法：

  ```text
  display dhcpv6 relay [interface IF]
  ```

### `display snmp-agent community`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display SNMPv2c read communities
- 合法语法：

  ```text
  display snmp-agent community
  ```

### `display snmp-agent sys-info`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display SNMP system information
- 合法语法：

  ```text
  display snmp-agent sys-info
  ```

### `display snmp-agent target-host`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display SNMP trap receivers
- 合法语法：

  ```text
  display snmp-agent target-host
  ```

### `display snmp-agent usm-user`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display SNMPv3 users
- 合法语法：

  ```text
  display snmp-agent usm-user
  ```

### `dns-domain-name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：configure DNS domain name
- 合法语法：

  ```text
  dns-domain-name VALUE
  ```

### `dns-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure IPv4 DNS server
- 合法语法：

  ```text
  dns-list X.X.X.X [X.X.X.X ...]
  ```

### `dns-server`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：configure IPv6 DNS server
- 合法语法：

  ```text
  dns-server VALUE
  ```

### `domain-name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure the DHCP domain name
- 合法语法：

  ```text
  domain-name DOMAIN
  ```

### `excluded-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：exclude an IPv6 address or range from allocation
- 合法语法：

  ```text
  excluded-address START [END]
  ```

### `excluded-ip-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：exclude an IPv4 address or range from allocation
- 合法语法：

  ```text
  excluded-ip-address START [END]
  ```

### `gateway-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure IPv4 gateway address
- 合法语法：

  ```text
  gateway-list X.X.X.X [X.X.X.X ...]
  ```

### `information-refresh`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：set the DHCPv6 information refresh interval
- 合法语法：

  ```text
  information-refresh INTEGER<600-4294967295>
  ```

### `lease`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure the IPv4 lease time
- 合法语法：

  ```text
  lease { unlimited | day DAYS [hour HOURS [minute MINUTES]] }
  ```

### `network`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`IPv4地址池视图`、`OSPF Area视图`、`RIPng视图`、`RIP视图`
- CLI 帮助：add an OSPF network；advertise a RIPng network；advertise a classful RIP network；configure the IPv4 pool network；originate a BGP network
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

### `prefix-delegation`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：configure an IPv6 delegated-prefix pool
- 合法语法：

  ```text
  prefix-delegation X:X::X/M INTEGER<1-128> [life-time VALID PREFERRED]
  ```

### `section`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure an allocatable IPv4 address range
- 合法语法：

  ```text
  section INTEGER<0-255> START [END]
  ```

### `snmp-agent`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable the SNMP agent
- 合法语法：

  ```text
  snmp-agent
  ```

### `snmp-agent community read`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure an SNMPv2c read community
- 合法语法：

  ```text
  snmp-agent community read COMMUNITY
  ```

### `snmp-agent protocol source-interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：bind the SNMP agent to an interface address
- 合法语法：

  ```text
  snmp-agent protocol source-interface { all-interface | IFNAME | vpn-instance VPN IFNAME }
  ```

### `snmp-agent protocol source-status all-interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：listen on all IPv4 interfaces in public and VPN instances
- 合法语法：

  ```text
  snmp-agent protocol source-status all-interface
  ```

### `snmp-agent sys-info contact`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set SNMP system contact
- 合法语法：

  ```text
  snmp-agent sys-info contact TEXT
  ```

### `snmp-agent sys-info location`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：set SNMP system location
- 合法语法：

  ```text
  snmp-agent sys-info location TEXT
  ```

### `snmp-agent sys-info version v2c`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable SNMP v2c
- 合法语法：

  ```text
  snmp-agent sys-info version v2c
  ```

### `snmp-agent sys-info version v3`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable SNMP v3
- 合法语法：

  ```text
  snmp-agent sys-info version v3
  ```

### `snmp-agent target-host trap address udp-domain`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure an SNMP trap receiver
- 合法语法：

  ```text
  snmp-agent target-host trap address udp-domain ADDRESS udp-port PORT params securityname NAME { v2c | v3 }
  ```

### `snmp-agent trap enable standard`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：enable standard startup and interface traps
- 合法语法：

  ```text
  snmp-agent trap enable standard
  ```

### `snmp-agent trap source`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：select the trap source interface
- 合法语法：

  ```text
  snmp-agent trap source IFNAME
  ```

### `snmp-agent usm-user v3`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：configure an SNMPv3 authPriv user
- 合法语法：

  ```text
  snmp-agent usm-user v3 USER authentication-mode sha2-256 AUTH privacy-mode aes128 PRIV
  ```

### `static-bind ip-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：bind an IPv4 address to a client MAC
- 合法语法：

  ```text
  static-bind ip-address X.X.X.X mac-address H-H-H
  ```

### `undo address prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove a stateful IPv6 allocation prefix
- 合法语法：

  ```text
  undo address prefix X:X::X/M
  ```

### `undo dns-domain-name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove DNS domain name
- 合法语法：

  ```text
  undo dns-domain-name VALUE
  ```

### `undo dns-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove IPv4 DNS server
- 合法语法：

  ```text
  undo dns-list [VALUE]
  ```

### `undo dns-server`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove IPv6 DNS server
- 合法语法：

  ```text
  undo dns-server VALUE
  ```

### `undo domain-name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove the DHCP domain name
- 合法语法：

  ```text
  undo domain-name
  ```

### `undo excluded-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove an excluded address or range
- 合法语法：

  ```text
  undo excluded-address START [END]
  ```

### `undo excluded-ip-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove an excluded address or range
- 合法语法：

  ```text
  undo excluded-ip-address START [END]
  ```

### `undo gateway-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove IPv4 gateway address
- 合法语法：

  ```text
  undo gateway-list [VALUE]
  ```

### `undo information-refresh`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：restore the default DHCPv6 information refresh interval
- 合法语法：

  ```text
  undo information-refresh
  ```

### `undo lease`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：restore the default lease time
- 合法语法：

  ```text
  undo lease
  ```

### `undo network`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`IPv4地址池视图`、`OSPF Area视图`、`RIPng视图`、`RIP视图`
- CLI 帮助：remove a BGP network；remove a RIP network；remove a RIPng network；remove an OSPF network；remove the IPv4 pool network
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

### `undo prefix-delegation`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove an IPv6 delegated-prefix pool
- 合法语法：

  ```text
  undo prefix-delegation X:X::X/M INTEGER<1-128>
  ```

### `undo section`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove an allocatable IPv4 address range
- 合法语法：

  ```text
  undo section INTEGER<0-255>
  ```

### `undo snmp-agent`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：remove all SNMP configuration and stop the agent
- 合法语法：

  ```text
  undo snmp-agent
  ```

### `undo snmp-agent community read`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an SNMPv2c read community
- 合法语法：

  ```text
  undo snmp-agent community read COMMUNITY
  ```

### `undo snmp-agent protocol source-interface`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：remove the SNMP source interface
- 合法语法：

  ```text
  undo snmp-agent protocol source-interface
  ```

### `undo snmp-agent sys-info contact`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：clear SNMP system contact
- 合法语法：

  ```text
  undo snmp-agent sys-info contact
  ```

### `undo snmp-agent sys-info location`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：clear SNMP system location
- 合法语法：

  ```text
  undo snmp-agent sys-info location
  ```

### `undo snmp-agent sys-info version v2c`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable SNMP v2c
- 合法语法：

  ```text
  undo snmp-agent sys-info version v2c
  ```

### `undo snmp-agent sys-info version v3`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable SNMP v3
- 合法语法：

  ```text
  undo snmp-agent sys-info version v3
  ```

### `undo snmp-agent target-host trap address udp-domain`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete all trap targets at an address
- 合法语法：

  ```text
  undo snmp-agent target-host trap address udp-domain ADDRESS
  ```

### `undo snmp-agent trap enable standard`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：disable standard traps
- 合法语法：

  ```text
  undo snmp-agent trap enable standard
  ```

### `undo snmp-agent trap source`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：remove the trap source interface
- 合法语法：

  ```text
  undo snmp-agent trap source
  ```

### `undo snmp-agent usm-user v3`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an SNMPv3 user
- 合法语法：

  ```text
  undo snmp-agent usm-user v3 USER
  ```

### `undo static-bind ip-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove a static IPv4 client binding
- 合法语法：

  ```text
  undo static-bind ip-address X.X.X.X
  ```

### `undo vpn-instance`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`、`IPv4地址池视图`、`OSPF视图`
- CLI 帮助：bind the pool to the default network instance；remove OSPF VPN binding
- 合法语法：

  ```text
  undo vpn-instance
  ```

### `vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`、`IPv4地址池视图`、`OSPF视图`
- CLI 帮助：bind OSPF process to a VPN instance；bind the pool to a VPN instance
- 合法语法：

  ```text
  vpn-instance NAME
  ```

## 诊断、清理与恢复

### `check system-software control-plane`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：check software compatibility without changing the device
- 合法语法：

  ```text
  check system-software control-plane TARGET rollback-package CURRENT
  ```

### `check system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：check software compatibility without changing the device
- 合法语法：

  ```text
  check system-software package TARGET rollback-package CURRENT
  ```

### `clear configuration candidate`

- 类别：Candidate管理命令
- 执行效果：仅丢弃当前会话尚未提交的修改。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：clear uncommitted configuration (two-stage)
- 合法语法：

  ```text
  clear configuration candidate
  ```

### `clear interface`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：clear interface traffic and error counters
- 合法语法：

  ```text
  clear interface TYPE N counter
  ```

### `clear nat-policy counters`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：clear nat-policy runtime counters without removing sessions
- 合法语法：

  ```text
  clear nat-policy counters
  ```

### `clear nat-policy sessions`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：clear nat-policy sessions
- 合法语法：

  ```text
  clear nat-policy sessions [name POLICY [rule RULE-ID]]
  ```

### `clear system-software info`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：Clear completed software transaction history
- 合法语法：

  ```text
  clear system-software info
  ```

### `display resource-mapping`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display runtime resource-mapping storage policy
- 合法语法：

  ```text
  display resource-mapping [vpp|linux|frr]
  ```

### `display saved-configuration`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the active startup CFG or a named CFG
- 合法语法：

  ```text
  display saved-configuration [FILE.cfg]
  ```

### `display startup`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the configuration file selected for the next start
- 合法语法：

  ```text
  display startup
  ```

### `display system mac-address`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display the system MAC address
- 合法语法：

  ```text
  display system mac-address
  ```

### `display system-software`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display installed software and upgrade or rollback transactions
- 合法语法：

  ```text
  display system-software [verbose]
  ```

### `display this`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display committed configuration of the current view
- 合法语法：

  ```text
  display this
  ```

### `display urpf`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：show per-interface uRPF mode
- 合法语法：

  ```text
  display urpf
  ```

### `display version`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display vortexros, system, VPP, DPDK and FRRouting version information
- 合法语法：

  ```text
  display version
  ```

### `display vrrp6`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 VRRPv3 information
- 合法语法：

  ```text
  display vrrp6 [brief|interface INTERFACE|statistics|protocol-information|VRID]
  ```

### `mtr`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：run mtr with numeric output (default -n)
- 合法语法：

  ```text
  mtr [OPTIONS] HOST
  ```

### `ping`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：send ICMP echo requests (default 5 packets)
- 合法语法：

  ```text
  ping [OPTIONS] HOST
  ```

### `reset dataplane`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：Activate saved dataplane settings
- 合法语法：

  ```text
  reset dataplane
  ```

### `reset ip arp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：reset dynamic IPv4 ARP entries
- 合法语法：

  ```text
  reset ip arp [interface TYPE N] [ip X.X.X.X]
  ```

### `reset ipv6 route-static group`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：reload an IPv6 route-static group external list
- 合法语法：

  ```text
  reset ipv6 route-static group {name GROUP|all}
  ```

### `reset mac-address`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：reset dynamically learned MAC addresses
- 合法语法：

  ```text
  reset mac-address [interface TYPE N] [mac-address H-H-H]
  ```

### `reset ospf`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：reset one ospf process so pending runtime settings take effect
- 合法语法：

  ```text
  reset ospf INTEGER<1-65535> process
  ```

### `reset ospfv3`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：reset one ospfv3 process so pending runtime settings take effect
- 合法语法：

  ```text
  reset ospfv3 INTEGER<1-65535> process
  ```

### `reset route-static group`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：reload an IPv4 route-static group external list
- 合法语法：

  ```text
  reset route-static group {name GROUP|all}
  ```

### `reset running-configuration`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：clear running configuration and restart enabled VPP; keep the saved CFG
- 合法语法：

  ```text
  reset running-configuration
  ```

### `reset saved-configuration`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：replace the active startup CFG or a named CFG with factory configuration
- 合法语法：

  ```text
  reset saved-configuration [FILE.cfg]
  ```

### `reset service bfd`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart the managed bfd routing service
- 合法语法：

  ```text
  reset service bfd
  ```

### `reset service bgp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart the managed bgp routing service
- 合法语法：

  ```text
  reset service bgp
  ```

### `reset service frr`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart a network service
- 合法语法：

  ```text
  reset service frr
  ```

### `reset service isis`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart the managed isis routing service
- 合法语法：

  ```text
  reset service isis
  ```

### `reset service ospf`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart the managed ospf routing service
- 合法语法：

  ```text
  reset service ospf [ipv4|ipv6|all]
  ```

### `reset service rip`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart the managed rip routing service
- 合法语法：

  ```text
  reset service rip [ipv4|ipv6|all]
  ```

### `reset service vpp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：restart a network service
- 合法语法：

  ```text
  reset service vpp
  ```

### `rollback system-software control-plane`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：rollback VortexROS control-plane software without restarting VPP
- 合法语法：

  ```text
  rollback system-software control-plane TARGET.deb rollback-package CURRENT.deb
  ```

### `rollback system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：rollback the complete VortexROS and VPP system package
- 合法语法：

  ```text
  rollback system-software package TARGET.tar rollback-package CURRENT.tar
  ```

### `simulate system-software control-plane`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：simulate package resolution and the software transaction without changing the device
- 合法语法：

  ```text
  simulate system-software control-plane TARGET rollback-package CURRENT
  ```

### `simulate system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：simulate package resolution and the software transaction without changing the device
- 合法语法：

  ```text
  simulate system-software package TARGET rollback-package CURRENT
  ```

### `traceroute`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：alias of tracert
- 合法语法：

  ```text
  traceroute [OPTIONS] HOST
  ```

### `tracert`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- CLI 帮助：trace the path with ICMP numeric probes (default -In)
- 合法语法：

  ```text
  tracert [OPTIONS] HOST
  ```

### `upgrade system-software control-plane`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：upgrade VortexROS control-plane software without restarting VPP
- 合法语法：

  ```text
  upgrade system-software control-plane TARGET.deb rollback-package CURRENT.deb
  ```

### `upgrade system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：upgrade the complete VortexROS and VPP system package
- 合法语法：

  ```text
  upgrade system-software package TARGET.tar rollback-package CURRENT.tar
  ```
