# 出口限速

**目标**：在实验出口启用两速率三色限速。

**前提**：VPP 已运行，Ethernet 1 是独立实验出口，没有叠加的 MQC CAR。使用接口帮助确认本机速率和突发单位。

## 配置

~~~text
system-view
interface Ethernet 1
 qos lr outbound cir 100000 pir 100000 cbs 18750000 pbs 31250000 green pass yellow pass red discard
 quit
commit
~~~

绿、黄报文放行，红色报文丢弃。该配置作用于整个接口出方向。只想限制特定流量时，应使用 [MQC](../operator/mqc.md) 分类。

## 验证

用 `display current-configuration interface Ethernet 1` 核对绑定。从测试发送端依次提供低于和高于设定的持续负载，对比接收端速率和丢包；不要只用一次短突发判断限速。

## 撤销

在 Ethernet 1 执行 `undo qos lr outbound` 并提交；在相同负载下核对限速已撤销。
