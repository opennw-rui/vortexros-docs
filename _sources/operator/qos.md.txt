# QoS

在接口或 VLAN 上按方向限速。

[命令参考](reference/qos.md) · [配置案例](../examples/qos.md)

## 配置与验证

若接口已经使用MQC police又配置接口QoS限速，CLI会给出INFO提示：高负载时两层限速可能产生额外丢包抖动，建议统一使用MQC限速。提示不会自动删除或合并用户配置。

```text
interface Ethernet 1
 qos lr outbound cir 1000000 pir 1000000 cbs 187500000 pbs 312500000 green pass yellow pass red discard
```

提交后，对接口出方向使用两速率三色限速；速率和突发参数以命令提示中的单位为准。查看接口配置与计数，确认实际流量是否达到预期：

```text
display this
display interface Ethernet 1
```

```text
interface Ethernet 1
 undo qos lr outbound
commit
```
