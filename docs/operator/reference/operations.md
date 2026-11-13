# 诊断、清理与恢复


## `check system-software control-plane`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：check software compatibility without changing the device
- 合法语法：

  ```text
  check system-software control-plane TARGET rollback-package CURRENT
  ```

## `check system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：check software compatibility without changing the device
- 合法语法：

  ```text
  check system-software package TARGET rollback-package CURRENT
  ```

## `clear configuration candidate`

- 类别：Candidate管理命令
- 执行效果：仅丢弃当前会话尚未提交的修改。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：clear uncommitted configuration (two-stage)
- 合法语法：

  ```text
  clear configuration candidate
  ```

## `clear interface`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：clear interface traffic and error counters
- 合法语法：

  ```text
  clear interface TYPE N counter
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

## `clear system-software info`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：Clear completed software transaction history
- 合法语法：

  ```text
  clear system-software info
  ```

## `display resource-mapping`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display runtime resource-mapping storage policy
- 合法语法：

  ```text
  display resource-mapping [vpp|linux|frr]
  ```

## `display saved-configuration`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the active startup CFG or a named CFG
- 合法语法：

  ```text
  display saved-configuration [FILE.cfg]
  ```

## `display startup`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the configuration file selected for the next start
- 合法语法：

  ```text
  display startup
  ```

## `display system mac-address`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the system MAC address
- 合法语法：

  ```text
  display system mac-address
  ```

## `display system-software`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display installed software and upgrade or rollback transactions
- 合法语法：

  ```text
  display system-software [verbose]
  ```

## `display this`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display committed configuration of the current view
- 合法语法：

  ```text
  display this
  ```

## `display urpf`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：show per-interface uRPF mode
- 合法语法：

  ```text
  display urpf
  ```

## `display version`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display vortexros, system, VPP, DPDK and FRRouting version information
- 合法语法：

  ```text
  display version
  ```

## `display vrrp6`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IPv6 VRRPv3 information
- 合法语法：

  ```text
  display vrrp6 [brief|interface INTERFACE|statistics|protocol-information|VRID]
  ```

## `mtr`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：run mtr with numeric output (default -n)
- 合法语法：

  ```text
  mtr [OPTIONS] HOST
  ```

## `ping`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：send ICMP echo requests (default 5 packets)
- 合法语法：

  ```text
  ping [OPTIONS] HOST
  ```

## `reset dataplane`

应用需重启的数据面配置。VPP 和选中网卡的驱动归属可能变化，须安排业务窗口并保留管理通道。

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：Activate saved dataplane settings
- 合法语法：

  ```text
  reset dataplane
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

## `reset ipv6 route-static group`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reload an IPv6 route-static group external list
- 合法语法：

  ```text
  reset ipv6 route-static group {name GROUP|all}
  ```

## `reset mac-address`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reset dynamically learned MAC addresses
- 合法语法：

  ```text
  reset mac-address [interface TYPE N] [mac-address H-H-H]
  ```

## `reset ospf`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：reset one ospf process so pending runtime settings take effect
- 合法语法：

  ```text
  reset ospf INTEGER<1-65535> process
  ```

## `reset ospfv3`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：reset one ospfv3 process so pending runtime settings take effect
- 合法语法：

  ```text
  reset ospfv3 INTEGER<1-65535> process
  ```

## `reset route-static group`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：reload an IPv4 route-static group external list
- 合法语法：

  ```text
  reset route-static group {name GROUP|all}
  ```

## `reset running-configuration`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：clear running configuration and restart enabled VPP; keep the saved CFG
- 合法语法：

  ```text
  reset running-configuration
  ```

## `reset saved-configuration`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：replace the active startup CFG or a named CFG with factory configuration
- 合法语法：

  ```text
  reset saved-configuration [FILE.cfg]
  ```

## `reset service bfd`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed bfd routing service
- 合法语法：

  ```text
  reset service bfd
  ```

## `reset service bgp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed bgp routing service
- 合法语法：

  ```text
  reset service bgp
  ```

## `reset service frr`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart a network service
- 合法语法：

  ```text
  reset service frr
  ```

## `reset service isis`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed isis routing service
- 合法语法：

  ```text
  reset service isis
  ```

## `reset service ospf`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed ospf routing service
- 合法语法：

  ```text
  reset service ospf [ipv4|ipv6|all]
  ```

## `reset service rip`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed rip routing service
- 合法语法：

  ```text
  reset service rip [ipv4|ipv6|all]
  ```

## `reset service vpp`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart a network service
- 合法语法：

  ```text
  reset service vpp
  ```

## `rollback system-software control-plane`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：rollback VortexROS control-plane software without restarting VPP
- 合法语法：

  ```text
  rollback system-software control-plane TARGET.deb rollback-package CURRENT.deb
  ```

## `rollback system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：rollback the complete VortexROS and VPP system package
- 合法语法：

  ```text
  rollback system-software package TARGET.tar rollback-package CURRENT.tar
  ```

## `simulate system-software control-plane`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：simulate package resolution and the software transaction without changing the device
- 合法语法：

  ```text
  simulate system-software control-plane TARGET rollback-package CURRENT
  ```

## `simulate system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：simulate package resolution and the software transaction without changing the device
- 合法语法：

  ```text
  simulate system-software package TARGET rollback-package CURRENT
  ```

## `traceroute`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：alias of tracert
- 合法语法：

  ```text
  traceroute [OPTIONS] HOST
  ```

## `tracert`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：trace the path with ICMP numeric probes (default -In)
- 合法语法：

  ```text
  tracert [OPTIONS] HOST
  ```

## `upgrade system-software control-plane`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：upgrade VortexROS control-plane software without restarting VPP
- 合法语法：

  ```text
  upgrade system-software control-plane TARGET.deb rollback-package CURRENT.deb
  ```

## `upgrade system-software package`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- 用途（设备帮助）：upgrade the complete VortexROS and VPP system package
- 合法语法：

  ```text
  upgrade system-software package TARGET.tar rollback-package CURRENT.tar
  ```
