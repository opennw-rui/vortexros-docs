# 出口限速

## 拓扑与影响

两台 VortexROS Ethernet0 直连，P1 为 198.19.80.1/30，P2 为 198.19.80.2/30。先按[NAT 基础拓扑](nat/topology.md)的 P1/P2 部分配置地址；本例不绑定 NAT 或叠加 MQC CAR。

接口限速约束整条出方向流量，包括协议报文。超额报文被丢弃，不是排队整形。短窗口受突发桶影响，平均值不保证等于 CIR。

## P1

~~~text
system-view
interface Ethernet0
 qos lr outbound cir 100 pir 100 cbs 18750 pbs 31250 green pass yellow pass red discard
quit
commit
display current-configuration interface Ethernet0
display interface Ethernet0
~~~

CIR/PIR 缺省单位为 kbps，CBS/PBS 为字节；上述限值为 100kbps。不要用于仍承载重要管理或路由协议的接口。

## 验证

P1/P2 双向 Ping 对端，确认低于限额的基础通信正常；查询接口配置和速率。若要量出限速效果，需让实际业务超过 100kbps 并持续足够时间，同时记录接收速率与丢包。VortexROS CLI 不提供通用流量发生器，少量 Ping 不能证明稳态限速数值；业务终端或专用流量仪不参与设备配置。

## 撤销

~~~text
system-view
interface Ethernet0
 undo qos lr outbound
quit
commit
display current-configuration interface Ethernet0
display health
~~~

确认限速配置消失、健康 ready，再用新业务检查不再受此限额约束，最后 save。接口地址及共享底层配置可以保留。

[功能及方向](../operator/qos.md) · [选择性 CAR](../operator/mqc/actions.md)
