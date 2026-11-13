# QoS

[配置指南](../qos.md)

## `qos lr`

- 类别：配置命令
- 视图：`VLAN视图`、`接口视图`
- 用途（设备帮助）：configure interface or VLAN rate limit (2-rate 3-color)
- 合法语法：

  ```text
  qos lr { inbound | outbound } cir CIR [pir PIR] [cbs CBS] [pbs PBS] [green|yellow|red pass|discard]
  ```

## `undo qos lr`

- 类别：配置命令
- 视图：`VLAN视图`、`接口视图`
- 用途（设备帮助）：remove interface or VLAN rate limit
- 合法语法：

  ```text
  undo qos lr { inbound | outbound }
  ```
