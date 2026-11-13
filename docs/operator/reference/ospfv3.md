# OSPFv3

[配置指南](../ospfv3.md)

共用命令：[`abr-summary`](dynamic-routing.md#cmd-abr-summary)、[`area`](dynamic-routing.md#cmd-area)、[`import-route`](dynamic-routing.md#cmd-import-route)、[`router-id`](dynamic-routing.md#cmd-router-id)。

## `display ospfv3`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display OSPFv3 information
- 合法语法：

  ```text
  display ospfv3 [process-id|vpn-instance NAME] [brief|peer|interface|lsdb|routing]
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

## `reset ospfv3`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：reset one ospfv3 process so pending runtime settings take effect
- 合法语法：

  ```text
  reset ospfv3 INTEGER<1-65535> process
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
