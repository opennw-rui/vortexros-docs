# SNMP

[配置指南](../snmp.md)

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
