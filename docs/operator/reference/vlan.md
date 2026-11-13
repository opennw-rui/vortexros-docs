# VLAN

[配置指南](../vlan.md)

## `display vlan`

查询成员、链路和标签处理。U/D 表示端口状态，TG/UT 表示带标签或不带标签。

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VLAN information
- 合法语法：

  ```text
  display vlan [VLAN-ID | summary]
  ```

## `display vlan summary`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VLAN summary
- 合法语法：

  ```text
  display vlan summary
  ```

## `enable switch`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable the L2 switch instance
- 合法语法：

  ```text
  enable switch
  ```

## `port default vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the access port default VLAN
- 合法语法：

  ```text
  port default vlan VLAN-ID
  ```

## `port link-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the L2 port link type
- 合法语法：

  ```text
  port link-type { access | dot1q-tunnel | trunk }
  ```

## `port trunk allow-pass vlan`

为当前 trunk 放行指定 VLAN。对端也须允许该 VLAN。撤销会中断相应 VLAN 经此口的转发。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：allow VLANs on a trunk port
- 合法语法：

  ```text
  port trunk allow-pass vlan { VLAN-LIST | all }
  ```

## `port trunk pvid vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the trunk native VLAN
- 合法语法：

  ```text
  port trunk pvid vlan VLAN-ID
  ```

## `portswitch`

把接口设为二层交换口。先处理已有三层地址及依赖。见[VLAN 网关案例](../../examples/vlan-gateway.md)。

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：switch the aggregate to Layer 2 mode；switch the interface to L2 mode
- 合法语法：

  ```text
  portswitch
  ```

## `switchport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：switch the interface to L2 mode
- 合法语法：

  ```text
  switchport
  ```

## `undo enable switch`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable the L2 switch instance
- 合法语法：

  ```text
  undo enable switch
  ```

## `undo port default vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the access port default VLAN to 1
- 合法语法：

  ```text
  undo port default vlan
  ```

## `undo port link-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore portswitch-only L2 mode (access VLAN 1)
- 合法语法：

  ```text
  undo port link-type
  ```

## `undo port trunk allow-pass vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove allowed VLANs from a trunk port
- 合法语法：

  ```text
  undo port trunk allow-pass vlan { VLAN-LIST | all }
  ```

## `undo port trunk pvid vlan`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the trunk native VLAN to 1
- 合法语法：

  ```text
  undo port trunk pvid vlan [VLAN-ID]
  ```

## `undo portswitch`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：return the aggregate to Layer 3 mode；return the interface to L3 mode
- 合法语法：

  ```text
  undo portswitch
  ```

## `undo switchport`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：return the interface to L3 mode
- 合法语法：

  ```text
  undo switchport
  ```

## `undo vlan`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a VLAN
- 合法语法：

  ```text
  undo vlan VLAN-ID [to VLAN-ID]
  ```

## `undo vlan batch`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete VLANs in a batch
- 合法语法：

  ```text
  undo vlan batch { VLAN-ID [to VLAN-ID] } *
  ```

## `undo vlan-type`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove the sub-interface VLAN binding
- 合法语法：

  ```text
  undo vlan-type
  ```

## `vlan`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：create a VLAN and enter VLAN view
- 合法语法：

  ```text
  vlan VLAN-ID [to VLAN-ID]
  ```

## `vlan batch`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：create VLANs in a batch
- 合法语法：

  ```text
  vlan batch { VLAN-ID [to VLAN-ID] } *
  ```

## `vlan-type dot1q`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：bind the sub-interface to a VLAN (dot1q)
- 合法语法：

  ```text
  vlan-type dot1q VLAN-ID [inner VLAN-ID]
  ```
