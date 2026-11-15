# 出口限速

## 拓扑与影响

已有开发隔离实验中，P1/P2通过host-p1a12/host-p2a12互连（198.19.80.1/30、198.19.80.2/30）。两端接口和路由已按[基础拓扑](nat/topology.md)准备，无叠加MQC CAR；测试接收端使用iperf3。

本例在P1物理出口对整条流量限速，不只限制某个业务。CAR处理超额报文丢弃，不能保证每个短期测量窗口的均值等于CIR。

## 配置

~~~text
system-view
interface host-p1a12
 qos lr outbound cir 100 pir 100 cbs 18750 pbs 31250 green pass yellow pass red discard
quit
commit
display current-configuration interface host-p1a12
display interface host-p1a12
~~~

CIR/PIR缺省单位kbps，CBS/PBS单位字节。这里只示例100kbps，避免把原来较大的示例参数误认成实验实际值。

## 真实效果

独立接收端的1Mbps UDP负载持续3秒：旧底层桶算术缺陷下接收968–970kbps，修复后接收168kbps、丢605包（83%）。三秒结果包含初始突发，不能冒称长期稳态168kbps或“必须等于100”。限速存在时普通ICMP3/3。

这些数据复用既有定向记录，本轮没有重新压测。它们证明超额流量被限制，不是设备峰值吞吐测量。需要自己的稳态验收时，应根据突发桶和目标速率选择足够长的窗口。

## 撤销

~~~text
system-view
interface host-p1a12
 undo qos lr outbound
quit
commit
display current-configuration interface host-p1a12
display health
~~~

原实际撤销后后端policer解绑并删除，健康ready3/3；紧随提交的applying过渡态未当成最终通过。确认不再限速后save。接口地址和共享underlay保留。

[功能及方向](../operator/qos.md) · [选择性流量CAR](../operator/mqc/actions.md)
