# 桥域

[配置指南](../bridge-domains.md)

## `bridge-domain`

- 类别：配置命令
- 视图：`系统视图`（也可从其他配置视图直接调用）
- 用途（设备帮助）：add the interface to a bridge-domain；create a bridge-domain and enter its view
- 合法语法：

  ```text
  bridge-domain ID
  ```
  ```text
  bridge-domain ID [bvi]
  ```

## `display bridge-domain`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display bridge-domains (service BD + VLAN domains)
- 合法语法：

  ```text
  display bridge-domain [ID]
  ```

## `display mac-address`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display the MAC address table
- 合法语法：

  ```text
  display mac-address [MAC | vlan VLAN-ID | bridge-domain BD | interface IF | static | dynamic]
  ```

## `l2 binding vlan`

- 类别：配置命令
- 视图：`BD视图`
- 用途（设备帮助）：bind a local VLAN into this bridge-domain
- 合法语法：

  ```text
  l2 binding vlan VLAN-ID
  ```

## `mac-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the interface MAC address
- 合法语法：

  ```text
  mac-address MAC
  ```

## `mac-address aging-time`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：set the dynamic MAC address aging time
- 合法语法：

  ```text
  mac-address aging-time INTEGER<60-15300>
  ```

## `mac-address static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：configure a static MAC address
- 合法语法：

  ```text
  mac-address static MAC IF bridge-domain BD
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

## `undo bridge-domain`

- 类别：配置命令
- 视图：`接口视图`、`系统视图`
- 用途（设备帮助）：delete a bridge-domain；remove the interface from a bridge-domain
- 合法语法：

  ```text
  undo bridge-domain
  ```
  ```text
  undo bridge-domain ID
  ```

## `undo l2 binding vlan`

- 类别：配置命令
- 视图：`BD视图`
- 用途（设备帮助）：remove VLAN binding from this bridge-domain
- 合法语法：

  ```text
  undo l2 binding vlan
  ```

## `undo mac-address`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：restore the default interface MAC address
- 合法语法：

  ```text
  undo mac-address
  ```

## `undo mac-address aging-time`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：restore the default dynamic MAC address aging time
- 合法语法：

  ```text
  undo mac-address aging-time
  ```

## `undo mac-address static`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a static MAC address
- 合法语法：

  ```text
  undo mac-address static MAC IF bridge-domain BD
  ```
