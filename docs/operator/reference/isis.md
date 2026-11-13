# IS-IS

[配置指南](../isis.md)

共用命令：[`import-route`](dynamic-routing.md#cmd-import-route)。

## `cost-style`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set IS-IS metric style
- 合法语法：

  ```text
  cost-style {narrow|wide|transition}
  ```

## `display isis`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display IS-IS information
- 合法语法：

  ```text
  display isis [process-id] [brief|peer|lsdb|route|interface|spf-delay|traffic-eng]
  ```

## `hostname dynamic`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：enable the IS-IS dynamic hostname
- 合法语法：

  ```text
  hostname dynamic
  ```

## `ipv6 import-route`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：redistribute IPv6 routes into IS-IS
- 合法语法：

  ```text
  ipv6 import-route {direct|static|ospfv3|bgp}
  ```

## `is-level`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set IS-IS level
- 合法语法：

  ```text
  is-level {level-1|level-2|level-1-2}
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

## `network-entity`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set an IS-IS network entity title
- 合法语法：

  ```text
  network-entity NET
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

## `set-overload-bit`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：set the IS-IS overload bit
- 合法语法：

  ```text
  set-overload-bit
  ```

## `spf-delay-ietf`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：configure IETF SPF backoff timers
- 合法语法：

  ```text
  spf-delay-ietf init-delay MS short-delay MS long-delay MS holddown MS time-to-learn MS
  ```

## `undo hostname`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：restore the default IS-IS hostname
- 合法语法：

  ```text
  undo hostname
  ```

## `undo ipv6 import-route`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：stop redistributing IPv6 routes into IS-IS
- 合法语法：

  ```text
  undo ipv6 import-route PROTOCOL
  ```

## `undo is-level`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：restore IS-IS level
- 合法语法：

  ```text
  undo is-level
  ```

## `undo isis`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an IS-IS process
- 合法语法：

  ```text
  undo isis INTEGER<1-65535>
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

## `undo network-entity`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：remove an IS-IS network entity title
- 合法语法：

  ```text
  undo network-entity NET
  ```

## `undo set-overload-bit`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：clear the IS-IS overload bit
- 合法语法：

  ```text
  undo set-overload-bit
  ```

## `undo spf-delay-ietf`

- 类别：配置命令
- 视图：`IS-IS视图`
- 用途（设备帮助）：disable IETF SPF backoff timers
- 合法语法：

  ```text
  undo spf-delay-ietf
  ```
