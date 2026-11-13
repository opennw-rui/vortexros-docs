# Ethernet 与接口

[配置指南](../ethernet.md)

## `description`

- 类别：配置命令
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- 用途（设备帮助）：NVE interface description；bridge-domain description；configure ACL description；configure group description；configure the VLAN description；configure the VPN instance description；configure the interface description；set NAT policy description；set NAT rule description
- 合法语法：

  ```text
  description TEXT
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

## `encapsulation`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure sub-interface encapsulation
- 合法语法：

  ```text
  encapsulation { dot1q | dot1ad } vid VLAN-ID | encapsulation qinq vid PE-VID ce-vid CE-VID
  ```

## `flow-steering enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable tunnel-aware ingress worker steering
- 合法语法：

  ```text
  flow-steering enable
  ```

(cmd-hardware-offload)=
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

## `ip address`

为三层接口设置地址。提交后形成直连网段，修改已有地址可能影响 SSH、邻居和路由。见[静态路由案例](../../examples/static-route.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv4 address
- 合法语法：

  ```text
  ip address IP MASK [sub]
  ```

## `ipv6 address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure an IPv6 address
- 合法语法：

  ```text
  ipv6 address IP PREFIXLEN
  ```

## `lcp host`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：create a same-name Linux control-plane interface mapping
- 合法语法：

  ```text
  lcp host HOST-IF [tap|tun]
  ```

(cmd-mode)=
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

## `shutdown`

- 类别：配置命令
- 视图：`BFD会话视图`、`接口视图`
- 用途（设备帮助）：shut down the interface；shutdown
- 合法语法：

  ```text
  shutdown
  ```

## `statistic enable`

- 类别：配置命令
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- 用途（设备帮助）：enable counters for this NAT policy；enable counters for this NAT rule；enable detailed interface packet statistics
- 合法语法：

  ```text
  statistic enable
  ```

## `undo description`

- 类别：配置命令
- 视图：`ACL视图`、`BD视图`、`NAT策略视图`、`NAT规则视图`、`VLAN视图`、`VPN实例视图`、`acl6`、`接口视图`、`静态路由组视图`
- 用途（设备帮助）：clear ACL description；clear NAT policy description；clear NAT rule description；clear NVE description；clear bridge-domain description；delete group description；delete the VLAN description；delete the VPN instance description；delete the interface description
- 合法语法：

  ```text
  undo description
  ```

## `undo encapsulation`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove the sub-interface encapsulation
- 合法语法：

  ```text
  undo encapsulation
  ```

## `undo flow-steering enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable ingress worker steering on the interface
- 合法语法：

  ```text
  undo flow-steering enable
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

## `undo ip address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete an IPv4 address
- 合法语法：

  ```text
  undo ip address [IP MASK]
  ```

## `undo ipv6 address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete an IPv6 address
- 合法语法：

  ```text
  undo ipv6 address [IP PREFIXLEN]
  ```

## `undo lcp host`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：delete the Linux control-plane interface mapping
- 合法语法：

  ```text
  undo lcp host
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

## `undo shutdown`

- 类别：配置命令
- 视图：`BFD会话视图`、`接口视图`
- 用途（设备帮助）：bring the interface up；undo shutdown
- 合法语法：

  ```text
  undo shutdown
  ```

## `undo statistic enable`

- 类别：配置命令
- 视图：`NAT策略视图`、`NAT规则视图`、`接口视图`
- 用途（设备帮助）：disable counters for this NAT policy；disable counters for this NAT rule；disable detailed interface packet statistics
- 合法语法：

  ```text
  undo statistic enable
  ```
