# DHCP

[配置指南](../dhcp.md)

共用命令：[`network`](dynamic-routing.md#cmd-network)。

## `address prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：configure a stateful IPv6 allocation prefix
- 合法语法：

  ```text
  address prefix X:X::X/M [life-time VALID PREFERRED]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X/M` | IPv6 prefix | 输入值 |
| X:X::X/M | `life-time` | address lifetimes | 可选 |
| life-time | `VALID` | valid lifetime seconds | 输入值 |
| VALID | `PREFERRED` | preferred lifetime seconds | 输入值 |

## `dhcp client classless-route enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：install learned classless routes
- 合法语法：

  ```text
  dhcp client classless-route enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `dhcp client default-route enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：install the learned default route
- 合法语法：

  ```text
  dhcp client default-route enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `dhcp client default-route preference`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the DHCP default route preference
- 合法语法：

  ```text
  dhcp client default-route preference INTEGER<1-255>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-255>` | route preference | 输入值 |

## `dhcp client-relay shutdown`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：Suspend DHCP client and relay on this interface
- 合法语法：

  ```text
  dhcp client-relay shutdown
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `dhcp relay server-ip`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：add a DHCPv4 relay server
- 合法语法：

  ```text
  dhcp relay server-ip X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | DHCPv4 server address | 输入值 |

## `dhcp select`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：select the DHCPv4 interface role
- 合法语法：

  ```text
  dhcp select { global | interface | relay }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `global` | use a matching global address pool | 关键字 |
| 命令后 | `interface` | use the interface primary subnet | 关键字 |
| 命令后 | `relay` | relay DHCP messages | 关键字 |

## `dhcp server dns-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure interface-pool DNS servers
- 合法语法：

  ```text
  dhcp server dns-list X.X.X.X [X.X.X.X]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 DNS server | 输入值 |
| X.X.X.X | `X.X.X.X` | IPv4 DNS server | 输入值、可选、可重复 |

## `dhcp server domain-name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure the interface-pool domain name
- 合法语法：

  ```text
  dhcp server domain-name DOMAIN
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `DOMAIN` | DNS domain name | 输入值 |

## `dhcp server excluded-ip-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：exclude addresses from the interface pool
- 合法语法：

  ```text
  dhcp server excluded-ip-address START [END]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `START` | first excluded IPv4 address | 输入值 |
| START | `END` | last excluded IPv4 address | 输入值、可选 |

## `dhcp server gateway-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure interface-pool gateway addresses
- 合法语法：

  ```text
  dhcp server gateway-list { X.X.X.X [X.X.X.X] | disable }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 gateway address | 输入值 |
| X.X.X.X | `X.X.X.X` | IPv4 gateway address | 输入值、可选、可重复 |
| 命令后 | `disable` | do not advertise a default gateway | 关键字 |

## `dhcp server ip-range`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure the allocatable interface-pool range
- 合法语法：

  ```text
  dhcp server ip-range START END
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `START` | first allocatable IPv4 address | 输入值 |
| START | `END` | last allocatable IPv4 address | 输入值 |

## `dhcp server lease`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure the interface-pool lease time
- 合法语法：

  ```text
  dhcp server lease { unlimited | day DAYS [hour HOURS [minute MINUTES]] }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `unlimited` | lease does not expire | 关键字 |
| 命令后 | `day` | lease days | 关键字 |
| day | `DAYS` | days | 输入值 |
| DAYS | `hour` | lease hours | 可选 |
| hour | `HOURS` | hours | 输入值 |
| HOURS | `minute` | lease minutes | 可选 |
| minute | `MINUTES` | minutes | 输入值 |

## `dhcp server static-bind ip-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind an interface-pool address to a client MAC
- 合法语法：

  ```text
  dhcp server static-bind ip-address X.X.X.X mac-address H-H-H
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | reserved IPv4 address | 输入值 |
| X.X.X.X | `mac-address` | client MAC address | 关键字 |
| mac-address | `H-H-H` | MAC address | 输入值 |

## `dhcpv6 client information-request`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：obtain non-address information by DHCPv6
- 合法语法：

  ```text
  dhcpv6 client information-request
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `dhcpv6 client pd`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：request an IPv6 delegated prefix
- 合法语法：

  ```text
  dhcpv6 client pd PREFIX-NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PREFIX-NAME` | delegated prefix name | 输入值 |

## `dhcpv6 client renew`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`接口视图`
- CLI 帮助：renew the DHCPv6 client lease now
- 合法语法：

  ```text
  dhcpv6 client renew
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `dhcpv6 duid`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：configure the DHCPv6 server identifier type
- 合法语法：

  ```text
  dhcpv6 duid { ll | llt }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ll` | link-layer address DUID | 关键字 |
| 命令后 | `llt` | link-layer address plus time DUID | 关键字 |

## `dhcpv6 pool`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create or enter an IPv6 address pool
- 合法语法：

  ```text
  dhcpv6 pool NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `DHCPV6-POOL` | IPv6 address pool name | 输入值 |

## `dhcpv6 relay destination`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：add a DHCPv6 relay destination
- 合法语法：

  ```text
  dhcpv6 relay destination X:X::X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X` | DHCPv6 server address | 输入值 |

## `dhcpv6 relay interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the DHCPv6 relay upper interface
- 合法语法：

  ```text
  dhcpv6 relay interface IF
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | DHCPv6 relay upper interface | 输入值 |

## `dhcpv6 server`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable the DHCPv6 server on an interface
- 合法语法：

  ```text
  dhcpv6 server POOL
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `DHCPV6-POOL` | DHCPv6 pool name | 输入值 |

## `display dhcp client`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv4 client state
- 合法语法：

  ```text
  display dhcp client [interface IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `interface` | interface name | 可选 |
| interface | `IF` | DHCP client interface | 输入值 |

## `display dhcp configuration`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCP configuration summary
- 合法语法：

  ```text
  display dhcp configuration
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `display dhcp relay`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv4 relay state
- 合法语法：

  ```text
  display dhcp relay [interface IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `interface` | interface name | 可选 |
| interface | `IF` | relay interface | 输入值 |

## `display dhcp service`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCP service status
- 合法语法：

  ```text
  display dhcp service [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `verbose` | include instance details | 可选、可组合 |

## `display dhcpv6 client`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv6 client state
- 合法语法：

  ```text
  display dhcpv6 client [interface IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `interface` | interface name | 可选 |
| interface | `IF` | DHCPv6 client interface | 输入值 |

## `display dhcpv6 client prefix`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv6 delegated-prefix state
- 合法语法：

  ```text
  display dhcpv6 client prefix [name PREFIX-NAME]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | delegated prefix name | 可选 |
| name | `PREFIX-NAME` | delegated prefix name | 输入值 |

## `display dhcpv6 pool`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display IPv6 address pools and server leases
- 合法语法：

  ```text
  display dhcpv6 pool [name NAME] [all | used] [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | pool name | 可选、可组合 |
| name | `DHCPV6-POOL` | IPv6 pool name | 输入值 |
| 命令后 | `all` | include every observed lease state | 可选、可组合 |
| 命令后 | `used` | include active allocated addresses and prefixes | 可选、可组合 |
| 命令后 | `verbose` | include pool and detailed active lease information | 可选、可组合 |

## `display dhcpv6 relay`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display DHCPv6 relay state
- 合法语法：

  ```text
  display dhcpv6 relay [interface IF]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `interface` | interface name | 可选 |
| interface | `IF` | relay interface | 输入值 |

## `display ip pool`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display IPv4 address pools and server leases
- 合法语法：

  ```text
  display ip pool [name NAME | interface TYPE N] [all | used] [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| all / used / 命令后 | `name` | global pool name | 可选 |
| name | `IP-POOL` | IPv4 pool name | 输入值 |
| IF / IP-POOL / 命令后 | `all` | include every observed lease state | 可选 |
| IF / IP-POOL / all / used / 命令后 | `verbose` | include pool and detailed active lease information | 可选 |
| IF / IP-POOL / 命令后 | `used` | include active allocated addresses | 可选 |
| all / used / 命令后 | `interface` | interface address pool | 可选 |
| interface | `IF` | interface name or TYPE N | 输入值 |

## `display ipv6 pool`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：display IPv6 pool information and server leases
- 合法语法：

  ```text
  display ipv6 pool [name NAME] [all | used] [verbose]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `name` | pool name | 可选、可组合 |
| name | `DHCPV6-POOL` | IPv6 pool name | 输入值 |
| 命令后 | `all` | include every observed lease state | 可选、可组合 |
| 命令后 | `used` | include active allocated addresses and prefixes | 可选、可组合 |
| 命令后 | `verbose` | include pool and detailed active lease information | 可选、可组合 |

## `dns-domain-name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：configure DNS domain name
- 合法语法：

  ```text
  dns-domain-name VALUE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | DNS domain name | 输入值 |

## `dns-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure IPv4 DNS server
- 合法语法：

  ```text
  dns-list X.X.X.X [X.X.X.X ...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 DNS server | 输入值 |
| X.X.X.X | `X.X.X.X` | IPv4 DNS server | 输入值、可选、可重复 |

## `dns-server`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：configure IPv6 DNS server
- 合法语法：

  ```text
  dns-server VALUE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | IPv6 DNS server | 输入值 |

## `domain-name`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure the DHCP domain name
- 合法语法：

  ```text
  domain-name DOMAIN
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `DOMAIN` | DNS domain name | 输入值 |

## `enable dhcp server`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enable DHCP servers
- 合法语法：

  ```text
  enable dhcp server
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `excluded-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：exclude an IPv6 address or range from allocation
- 合法语法：

  ```text
  excluded-address START [END]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `START` | first excluded address | 输入值 |
| START | `END` | last excluded address | 输入值、可选 |

## `excluded-ip-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：exclude an IPv4 address or range from allocation
- 合法语法：

  ```text
  excluded-ip-address START [END]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `START` | first excluded address | 输入值 |
| START | `END` | last excluded address | 输入值、可选 |

## `gateway-list`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure IPv4 gateway address
- 合法语法：

  ```text
  gateway-list X.X.X.X [X.X.X.X ...]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 gateway address | 输入值 |
| X.X.X.X | `X.X.X.X` | IPv4 gateway address | 输入值、可选、可重复 |

## `information-refresh`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：set the DHCPv6 information refresh interval
- 合法语法：

  ```text
  information-refresh INTEGER<600-4294967295>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<600-4294967295>` | refresh interval seconds | 输入值 |

## `ip address dhcp-alloc`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：obtain the IPv4 address by DHCP
- 合法语法：

  ```text
  ip address dhcp-alloc
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `ip pool`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：create or enter an IPv4 pool
- 合法语法：

  ```text
  ip pool NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP-POOL` | IPv4 pool name | 输入值 |

## `ipv6 address auto dhcp`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：obtain an IPv6 address by stateful DHCPv6
- 合法语法：

  ```text
  ipv6 address auto dhcp [hint X:X::X]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `hint` | requested IPv6 address | 可选 |
| hint | `X:X::X` | IPv6 address | 输入值 |

## `ipv6 address dhcpv6-prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：derive an interface address from a delegated prefix
- 合法语法：

  ```text
  ipv6 address dhcpv6-prefix PREFIX-NAME SUFFIX/PREFIXLEN
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PREFIX-NAME` | delegated prefix name | 输入值 |
| PREFIX-NAME | `SUFFIX/PREFIXLEN` | IPv6 suffix and downstream prefix length | 输入值 |

## `lease`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure the IPv4 lease time
- 合法语法：

  ```text
  lease { unlimited | day DAYS [hour HOURS [minute MINUTES]] }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `unlimited` | lease does not expire | 关键字 |
| 命令后 | `day` | lease days | 关键字 |
| day | `DAYS` | days | 输入值 |
| DAYS | `hour` | lease hours | 可选 |
| hour | `HOURS` | hours | 输入值 |
| HOURS | `minute` | lease minutes | 可选 |
| minute | `MINUTES` | minutes | 输入值 |

## `prefix-delegation`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：configure an IPv6 delegated-prefix pool
- 合法语法：

  ```text
  prefix-delegation X:X::X/M INTEGER<1-128> [life-time VALID PREFERRED]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X/M` | aggregate prefix | 输入值 |
| X:X::X/M | `INTEGER<1-128>` | delegated prefix length | 输入值 |
| INTEGER<1-128> | `life-time` | prefix lifetimes | 可选 |
| life-time | `VALID` | valid lifetime seconds | 输入值 |
| VALID | `PREFERRED` | preferred lifetime seconds | 输入值 |

## `section`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：configure an allocatable IPv4 address range
- 合法语法：

  ```text
  section INTEGER<0-255> START [END]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-255>` | section index | 输入值 |
| INTEGER<0-255> | `START` | first allocatable IPv4 address | 输入值 |
| START | `END` | last allocatable IPv4 address | 输入值、可选 |

## `static-bind ip-address`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：bind an IPv4 address to a client MAC
- 合法语法：

  ```text
  static-bind ip-address X.X.X.X mac-address H-H-H
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | reserved IPv4 address | 输入值 |
| X.X.X.X | `mac-address` | client MAC address | 关键字 |
| mac-address | `H-H-H` | MAC address | 输入值 |

## `undo address prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove a stateful IPv6 allocation prefix
- 合法语法：

  ```text
  undo address prefix X:X::X/M
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X/M` | IPv6 prefix | 输入值 |

## `undo dhcp client classless-route enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：do not install learned classless routes
- 合法语法：

  ```text
  undo dhcp client classless-route enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcp client default-route enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：do not install the learned default route
- 合法语法：

  ```text
  undo dhcp client default-route enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcp client-relay shutdown`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：Resume configured DHCP client and relay on this interface
- 合法语法：

  ```text
  undo dhcp client-relay shutdown
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcp relay server-ip`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove a DHCPv4 relay server
- 合法语法：

  ```text
  undo dhcp relay server-ip X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | DHCPv4 server address | 输入值 |

## `undo dhcp select`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the DHCPv4 server or relay role
- 合法语法：

  ```text
  undo dhcp select
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcp server dns-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove interface-pool DNS servers
- 合法语法：

  ```text
  undo dhcp server dns-list [X.X.X.X]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 DNS server | 输入值、可选 |

## `undo dhcp server domain-name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove the interface-pool domain name
- 合法语法：

  ```text
  undo dhcp server domain-name
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcp server excluded-ip-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove an interface-pool exclusion
- 合法语法：

  ```text
  undo dhcp server excluded-ip-address START [END]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `START` | first excluded IPv4 address | 输入值 |
| START | `END` | last excluded IPv4 address | 输入值、可选 |

## `undo dhcp server gateway-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the interface-address gateway default
- 合法语法：

  ```text
  undo dhcp server gateway-list [X.X.X.X]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 gateway address | 输入值、可选 |

## `undo dhcp server ip-range`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore allocation from the interface primary subnet
- 合法语法：

  ```text
  undo dhcp server ip-range
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcp server lease`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default interface-pool lease
- 合法语法：

  ```text
  undo dhcp server lease
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcp server static-bind ip-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove an interface-pool static binding
- 合法语法：

  ```text
  undo dhcp server static-bind ip-address X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | reserved IPv4 address | 输入值 |

## `undo dhcpv6 client information-request`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable DHCPv6 information requests
- 合法语法：

  ```text
  undo dhcpv6 client information-request
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcpv6 client pd`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable DHCPv6 prefix delegation
- 合法语法：

  ```text
  undo dhcpv6 client pd
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcpv6 duid`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：restore the default DHCPv6 server identifier
- 合法语法：

  ```text
  undo dhcpv6 duid
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dhcpv6 pool`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：delete an IPv6 address pool
- 合法语法：

  ```text
  undo dhcpv6 pool NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `DHCPV6-POOL` | IPv6 address pool name | 输入值 |

## `undo dhcpv6 relay destination`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove a DHCPv6 relay destination
- 合法语法：

  ```text
  undo dhcpv6 relay destination X:X::X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X` | DHCPv6 server address | 输入值 |

## `undo dhcpv6 relay interface`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove a DHCPv6 relay upper interface
- 合法语法：

  ```text
  undo dhcpv6 relay interface IF
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IF` | DHCPv6 relay upper interface | 输入值 |

## `undo dhcpv6 server`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the DHCPv6 server
- 合法语法：

  ```text
  undo dhcpv6 server
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo dns-domain-name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove DNS domain name
- 合法语法：

  ```text
  undo dns-domain-name VALUE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | DNS domain name | 输入值 |

## `undo dns-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove IPv4 DNS server
- 合法语法：

  ```text
  undo dns-list [VALUE]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | IPv4 DNS server | 输入值、可选 |

## `undo dns-server`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove IPv6 DNS server
- 合法语法：

  ```text
  undo dns-server VALUE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | IPv6 DNS server | 输入值 |

## `undo domain-name`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove the DHCP domain name
- 合法语法：

  ```text
  undo domain-name
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo enable dhcp server`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：disable DHCP servers
- 合法语法：

  ```text
  undo enable dhcp server
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo excluded-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove an excluded address or range
- 合法语法：

  ```text
  undo excluded-address START [END]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `START` | first excluded address | 输入值 |
| START | `END` | last excluded address | 输入值、可选 |

## `undo excluded-ip-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove an excluded address or range
- 合法语法：

  ```text
  undo excluded-ip-address START [END]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `START` | first excluded address | 输入值 |
| START | `END` | last excluded address | 输入值、可选 |

## `undo gateway-list`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove IPv4 gateway address
- 合法语法：

  ```text
  undo gateway-list [VALUE]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VALUE` | IPv4 gateway address | 输入值、可选 |

## `undo information-refresh`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：restore the default DHCPv6 information refresh interval
- 合法语法：

  ```text
  undo information-refresh
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ip address dhcp-alloc`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the DHCPv4 client
- 合法语法：

  ```text
  undo ip address dhcp-alloc
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ip pool`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：delete an IPv4 address pool
- 合法语法：

  ```text
  undo ip pool NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP-POOL` | IPv4 address pool name | 输入值 |

## `undo ipv6 address auto dhcp`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable the stateful DHCPv6 client
- 合法语法：

  ```text
  undo ipv6 address auto dhcp
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6 address dhcpv6-prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove an address derived from a delegated prefix
- 合法语法：

  ```text
  undo ipv6 address dhcpv6-prefix PREFIX-NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PREFIX-NAME` | delegated prefix name | 输入值 |

## `undo lease`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：restore the default lease time
- 合法语法：

  ```text
  undo lease
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo prefix-delegation`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`
- CLI 帮助：remove an IPv6 delegated-prefix pool
- 合法语法：

  ```text
  undo prefix-delegation X:X::X/M INTEGER<1-128>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X/M` | aggregate prefix | 输入值 |
| X:X::X/M | `INTEGER<1-128>` | delegated prefix length | 输入值 |

## `undo section`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove an allocatable IPv4 address range
- 合法语法：

  ```text
  undo section INTEGER<0-255>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-255>` | section index | 输入值 |

## `undo static-bind ip-address`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IPv4地址池视图`
- CLI 帮助：remove a static IPv4 client binding
- 合法语法：

  ```text
  undo static-bind ip-address X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | reserved IPv4 address | 输入值 |

## `undo vpn-instance`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`、`IPv4地址池视图`、`OSPF视图`
- CLI 帮助：bind the pool to the default network instance；remove OSPF VPN binding
- 合法语法：

  ```text
  undo vpn-instance
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ip-pool`**

此形式没有额外参数。

**适用视图：`dhcpv6-pool`**

此形式没有额外参数。

**适用视图：`ospf`**

此形式没有额外参数。

## `vpn-instance`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`DHCPv6地址池视图`、`IPv4地址池视图`、`OSPF视图`
- CLI 帮助：bind OSPF process to a VPN instance；bind the pool to a VPN instance
- 合法语法：

  ```text
  vpn-instance NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ip-pool`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VRF` | VPN instance name | 输入值 |

**适用视图：`dhcpv6-pool`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VRF` | VPN instance name | 输入值 |

**适用视图：`ospf`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `VPN` | VPN instance name | 输入值 |
