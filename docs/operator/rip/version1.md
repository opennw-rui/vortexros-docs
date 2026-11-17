# RIPv1

RIPv1 不携带掩码，使用有类路由，更新通过广播发送；不适用于需要任意长度掩码的通告。需要变长掩码或现代协议互通时选择 RIPv2。

~~~text
rip 96 vpn-instance BLUE
 version 1
 network 172.30.0.0
#
commit
display rip 96 interface
display rip 96 route
~~~

显式 version 1 后，接口的 Send/Receive 均应为1。未配置版本时默认发送2、接收1/2；显式 version 2 则限制双方版本为2。因此不能只看发送版本推断接收限制。

network 控制哪些本地接口参加 RIP。配置与对端通信后，应在协议表和实际路由表中同时看到远端网络，默认优先级100，链路每经过一台路由器增加一跳。接口 Up 后仍须等待正常协议更新，不能据此直接认定路由恢复。

[完整双端聚合案例](../../examples/rip-v1.md) · [参数参考](../reference/rip.md)
