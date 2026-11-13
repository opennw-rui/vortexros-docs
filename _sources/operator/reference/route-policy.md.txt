# 路由策略

[配置指南](../route-policy.md)

## `apply as-path`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：prepend AS numbers to the BGP AS path
- 合法语法：

  ```text
  apply as-path ASNUM [ASNUM ...]
  ```

## `apply community`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set BGP community values
- 合法语法：

  ```text
  apply community VALUE [VALUE ...] [additive]
  ```

## `apply cost`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set route metric
- 合法语法：

  ```text
  apply cost VALUE
  ```

## `apply ip-address next-hop`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set an IPv4 next hop
- 合法语法：

  ```text
  apply ip-address next-hop X.X.X.X
  ```

## `apply ipv6 next-hop`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set an IPv6 next hop
- 合法语法：

  ```text
  apply ipv6 next-hop X:X::X
  ```

## `apply large-community`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set BGP large-community values
- 合法语法：

  ```text
  apply large-community VALUE [VALUE ...] [additive]
  ```

## `apply local-preference`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set local preference
- 合法语法：

  ```text
  apply local-preference VALUE
  ```

## `apply origin`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set the BGP origin attribute
- 合法语法：

  ```text
  apply origin {igp|egp|incomplete}
  ```

## `apply tag`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set route tag
- 合法语法：

  ```text
  apply tag INTEGER<0-4294967295>
  ```

## `continue node`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：continue evaluation at a later route-policy node
- 合法语法：

  ```text
  continue node INTEGER<1-65535>
  ```

## `display route-policy`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display route policies
- 合法语法：

  ```text
  display route-policy [NAME [verbose]]
  ```

## `if-match cost`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set route metric
- 合法语法：

  ```text
  if-match cost INTEGER<0-4294967295>
  ```

## `if-match ip-prefix`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：match an IP prefix list
- 合法语法：

  ```text
  if-match ip-prefix NAME
  ```

## `if-match ipv6 address prefix-list`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：match an IPv6 prefix list
- 合法语法：

  ```text
  if-match ipv6 address prefix-list NAME
  ```

## `if-match protocol`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：match the route source protocol
- 合法语法：

  ```text
  if-match protocol {direct|static|ospf|ospfv3|isis|rip|ripng|bgp}
  ```

## `if-match tag`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：set route tag
- 合法语法：

  ```text
  if-match tag INTEGER<0-4294967295>
  ```

## `route-policy`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a route policy node and enter its view
- 合法语法：

  ```text
  route-policy NAME {permit|deny} node INTEGER<1-65535>
  ```

## `undo apply as-path`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the AS-path prepend action
- 合法语法：

  ```text
  undo apply as-path
  ```

## `undo apply community`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the BGP community action
- 合法语法：

  ```text
  undo apply community
  ```

## `undo apply cost`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：restore default route metric
- 合法语法：

  ```text
  undo apply cost
  ```

## `undo apply ip-address next-hop`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the IPv4 next-hop action
- 合法语法：

  ```text
  undo apply ip-address next-hop
  ```

## `undo apply ipv6 next-hop`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the IPv6 next-hop action
- 合法语法：

  ```text
  undo apply ipv6 next-hop
  ```

## `undo apply large-community`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the BGP large-community action
- 合法语法：

  ```text
  undo apply large-community
  ```

## `undo apply local-preference`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：restore default local preference
- 合法语法：

  ```text
  undo apply local-preference
  ```

## `undo apply origin`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the BGP origin action
- 合法语法：

  ```text
  undo apply origin
  ```

## `undo apply tag`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove route tag
- 合法语法：

  ```text
  undo apply tag
  ```

## `undo continue`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：stop evaluation after this route-policy node
- 合法语法：

  ```text
  undo continue
  ```

## `undo if-match cost`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove route metric
- 合法语法：

  ```text
  undo if-match cost
  ```

## `undo if-match ip-prefix`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove an IP prefix match
- 合法语法：

  ```text
  undo if-match ip-prefix NAME
  ```

## `undo if-match ipv6 address prefix-list`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove an IPv6 prefix match
- 合法语法：

  ```text
  undo if-match ipv6 address prefix-list NAME
  ```

## `undo if-match protocol`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove the route source protocol match
- 合法语法：

  ```text
  undo if-match protocol
  ```

## `undo if-match tag`

- 类别：配置命令
- 视图：`路由策略视图`
- 用途（设备帮助）：remove route tag
- 合法语法：

  ```text
  undo if-match tag
  ```

## `undo route-policy`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a route policy
- 合法语法：

  ```text
  undo route-policy NAME [permit|deny node INTEGER<1-65535>]
  ```
