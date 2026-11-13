# MQC

[配置指南](../mqc.md)

共用命令：[`apply config`](policy.md#cmd-apply-config)。

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

## `undo if-match`

- 类别：配置命令
- 视图：`流分类器视图`
- 用途（设备帮助）：remove the classifier match rule
- 合法语法：

  ```text
  undo if-match [TYPE]
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
