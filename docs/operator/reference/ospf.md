# OSPF

[配置指南](../ospf.md)

共用命令：[`abr-summary`](dynamic-routing.md#cmd-abr-summary)、[`area`](dynamic-routing.md#cmd-area)、[`import-route`](dynamic-routing.md#cmd-import-route)、[`network`](dynamic-routing.md#cmd-network)、[`router-id`](dynamic-routing.md#cmd-router-id)。

## `bandwidth-reference`

- 类别：配置命令
- 视图：`ospfv3`
- 用途（设备帮助）：set the OSPFv3 reference bandwidth
- 合法语法：

  ```text
  bandwidth-reference INTEGER<1-4294967>
  ```

## `display ospf`

peer 查询邻接，routing 查询协议路由，lsdb 查询链路状态数据库。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display OSPF information
- 合法语法：

  ```text
  display ospf [process-id] lsdb [{router|network|summary|asbr|ase|nssa|opaque-*} [link-state-id]] [originate-router router-id|self-originate] [age {min-value|max-value} seconds]
  ```

## `nssa`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：configure a not-so-stubby area；configure an OSPFv3 nssa area
- 合法语法：

  ```text
  nssa [no-summary]
  ```

## `opaque-capability enable`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：enable OSPF opaque LSA capability
- 合法语法：

  ```text
  opaque-capability enable
  ```

## `ospf`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create an OSPF process and enter OSPF view
- 合法语法：

  ```text
  ospf INTEGER<1-65535> [router-id X.X.X.X] [vpn-instance NAME]
  ```

## `ospf bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：configure OSPF BFD timers
- 合法语法：

  ```text
  ospf bfd {min-tx-interval INTEGER<100-1000> | min-rx-interval INTEGER<100-1000> | detect-multiplier INTEGER<3-50>} ...
  ```

## `ospf bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable OSPF BFD on this interface
- 合法语法：

  ```text
  ospf bfd enable
  ```

## `ospf cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface cost
- 合法语法：

  ```text
  ospf cost INTEGER<1-65535>
  ```

## `ospf dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface router priority
- 合法语法：

  ```text
  ospf dr-priority INTEGER<0-255>
  ```

## `ospf enable`

在接口激活进程和区域，提交后发送 Hello。见[OSPF 案例](../../examples/ospf.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：enable OSPF on an interface
- 合法语法：

  ```text
  ospf enable INTEGER<1-65535> area X.X.X.X
  ```

## `ospf network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface network type
- 合法语法：

  ```text
  ospf network-type {broadcast|nbma|p2p|p2mp}
  ```

## `ospf passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：suppress OSPF Hellos on this interface
- 合法语法：

  ```text
  ospf passive
  ```

## `ospf timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface dead
- 合法语法：

  ```text
  ospf timer dead INTEGER<1-65535>
  ```

## `ospf timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface hello
- 合法语法：

  ```text
  ospf timer hello INTEGER<1-65535>
  ```

## `ospf timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface retransmit
- 合法语法：

  ```text
  ospf timer retransmit INTEGER<1-65535>
  ```

## `ospf timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set OSPF interface transmit-delay
- 合法语法：

  ```text
  ospf timer transmit-delay INTEGER<1-3600>
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

## `reset service ospf`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：restart the managed ospf routing service
- 合法语法：

  ```text
  reset service ospf [ipv4|ipv6|all]
  ```

## `stub`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：configure a stub area；configure an OSPFv3 stub area
- 合法语法：

  ```text
  stub [no-summary]
  ```

## `undo bandwidth-reference`

- 类别：配置命令
- 视图：`ospfv3`
- 用途（设备帮助）：restore the OSPFv3 reference bandwidth
- 合法语法：

  ```text
  undo bandwidth-reference
  ```

## `undo nssa`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：restore a normal OSPF area；restore a normal OSPFv3 area
- 合法语法：

  ```text
  undo nssa
  ```

## `undo opaque-capability enable`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：disable OSPF opaque LSA capability
- 合法语法：

  ```text
  undo opaque-capability enable
  ```

## `undo ospf`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an OSPF process
- 合法语法：

  ```text
  undo ospf INTEGER<1-65535>
  ```

## `undo ospf bfd`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPF BFD timers
- 合法语法：

  ```text
  undo ospf bfd {min-tx-interval | min-rx-interval | detect-multiplier} ...
  ```

## `undo ospf bfd enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable OSPF BFD on this interface
- 合法语法：

  ```text
  undo ospf bfd enable
  ```

## `undo ospf cost`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPF interface cost
- 合法语法：

  ```text
  undo ospf cost
  ```

## `undo ospf dr-priority`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface router priority
- 合法语法：

  ```text
  undo ospf dr-priority
  ```

## `undo ospf enable`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：disable OSPF on an interface
- 合法语法：

  ```text
  undo ospf enable INTEGER<1-65535>
  ```

## `undo ospf network-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface network type
- 合法语法：

  ```text
  undo ospf network-type
  ```

## `undo ospf passive`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore OSPF Hellos on this interface
- 合法语法：

  ```text
  undo ospf passive
  ```

## `undo ospf timer dead`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface dead
- 合法语法：

  ```text
  undo ospf timer dead
  ```

## `undo ospf timer hello`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface hello
- 合法语法：

  ```text
  undo ospf timer hello
  ```

## `undo ospf timer retransmit`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface retransmit
- 合法语法：

  ```text
  undo ospf timer retransmit
  ```

## `undo ospf timer transmit-delay`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default OSPF interface transmit-delay
- 合法语法：

  ```text
  undo ospf timer transmit-delay
  ```

## `undo stub`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：restore a normal OSPF area；restore a normal OSPFv3 area
- 合法语法：

  ```text
  undo stub
  ```
