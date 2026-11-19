# QoS

在接口或 VLAN 上按方向限速。

[命令参考](reference/qos.md) · [配置案例](../examples/qos.md)

## 限速原理与参数

接口限速根据速率及突发桶为报文分色，再按颜色动作处理。它是流量监管，不是把所有超速报文缓存等待发送；发生 discard 时业务可能丢包，TCP 速率也可能因此回落。

| 参数 | 含义 |
| --- | --- |
| CIR / PIR | 承诺速率与峰值速率，单位以 CLI 参数说明为准 |
| CBS / PBS | 允许的突发量，不能直接当作速率 |
| green / yellow / red | 对不同颜色报文的处理动作 |
| inbound / outbound | 相对于绑定接口的处理方向 |

适合限制整个接口或 VLAN 的带宽；按业务分类限速使用 MQC。过小突发桶可能在平均速率低于目标时仍造成短突发丢弃。规划时结合报文大小、协议突发和实际链路能力，不把应用测出的速率当成参数单位。

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
```

CLI 操作：

```text
commit
```
