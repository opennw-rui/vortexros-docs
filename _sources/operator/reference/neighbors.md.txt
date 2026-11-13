# ARP 与 ND

[配置指南](../neighbors.md)

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

## `display ipv6 nd`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 neighbor discovery information
- 合法语法：

  ```text
  display ipv6 nd
  ```

## `display ipv6 neighbors`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 neighbor information
- 合法语法：

  ```text
  display ipv6 neighbors [interface IF | vpn-instance VRF | static | dynamic]
  ```

## `ipv6 nd max-number`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the IPv6 neighbor database capacity
- 合法语法：

  ```text
  ipv6 nd max-number INTEGER<1-4294967295>
  ```

## `ipv6 nd recycle`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure IPv6 neighbor recycling at capacity
- 合法语法：

  ```text
  ipv6 nd recycle { enable | disable }
  ```

## `ipv6 nd stale-timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the dynamic IPv6 neighbor stale aging time
- 合法语法：

  ```text
  ipv6 nd stale-timeout INTEGER<60-172800>
  ```

## `ipv6 neighbor`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static IPv6 neighbor
- 合法语法：

  ```text
  ipv6 neighbor IPV6 MAC interface IF
  ```

## `reset ip arp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reset dynamic IPv4 ARP entries
- 合法语法：

  ```text
  reset ip arp [interface TYPE N] [ip X.X.X.X]
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

## `undo ipv6 nd max-number`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the VPP default IPv6 neighbor capacity
- 合法语法：

  ```text
  undo ipv6 nd max-number
  ```

## `undo ipv6 nd recycle`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the VPP default IPv6 neighbor recycle policy
- 合法语法：

  ```text
  undo ipv6 nd recycle
  ```

## `undo ipv6 nd stale-timeout`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default IPv6 neighbor stale aging time
- 合法语法：

  ```text
  undo ipv6 nd stale-timeout
  ```

## `undo ipv6 neighbor`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static IPv6 neighbor
- 合法语法：

  ```text
  undo ipv6 neighbor IPV6 MAC interface IF
  ```
