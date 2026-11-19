# TCP MSS

TCP MSS 只调整带 MSS 选项的 TCP SYN，包括请求和应答。它将过大的值调小，不放大对端值、不改变接口 MTU，也不解决 UDP 分片。修改后只影响新连接，已有 TCP 连接不会重新协商。

## 工作原理与适用范围

TCP MSS 是一端在 SYN 中通告的最大 TCP 数据段大小（RFC 6691）。接口 MSS 调整修改握手中的该选项，以减少经过低 MTU 隧道时的大报文问题；它不会改变接口 MTU，也不对 UDP 分片或已有 TCP 连接追溯生效。

配置值应扣除实际 IP/TCP 及隧道开销。非对称路径需要分别检查两个方向的握手。禁止必要的 ICMP 路径 MTU 反馈也可能导致业务失败，不能只用降低 MSS 掩盖所有 MTU 配置问题。

验证使用新建 TCP 连接，同时检查 SYN 的 MSS 和实际数据传输。只看到配置或 SYN 成功，不能证明大数据报文已经通过；撤销后同样用新连接核对。

## 配置

在流量经过的接口上选择自动或固定模式，两者互斥：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 tcp mss clamp
#
~~~

CLI 操作：

~~~text
commit
~~~

固定上限为 1200：

~~~text
interface Ethernet0
 tcp mss 1200
#
~~~

CLI 操作：

~~~text
commit
~~~

自动模式随接口 MTU 更新。常规无扩展头的示例：

| 接口 MTU | IPv4 MSS 上限 | IPv6 MSS 上限 |
| --- | --- | --- |
| 1500 | 1460 | 1440 |
| 1320 | 1280 | 1260 |

封装及更小的端到端 MTU 仍需另行规划。

## 双端检查

两台 VortexROS 的 Ethernet0 直连，分别配置 192.0.2.1/30、192.0.2.2/30，在 P1 的 Ethernet0 配置 MSS。按 [BGP 对等体](../examples/bgp.md)建立两端 BGP，或让该接口承载其他真实 TCP 业务；修改 MSS 后使用新连接检查。

~~~text
display current-configuration interface Ethernet0
display interface Ethernet0
display bgp peer
~~~

配置显示可确认模式与上限，BGP Established 说明 TCP 会话可建立；它们均不直接显示 SYN 的 MSS。需要确认报文字段时，在链路上用报文分析设备检查新 SYN/SYN-ACK：原值高于上限时应变为上限，原值较小时应保持原值。Ping 不能验证 MSS。

## 撤销与排查

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo tcp mss
#
~~~

CLI 操作：

~~~text
commit
~~~

若为本例修改过 MTU，再恢复原 MTU；不要撤销实际业务需要的 MTU。重新建立 TCP 连接，核对不再受本功能限制。没有变化时检查是否为旧连接、实际经过的接口、SYN 是否包含 MSS，以及原值是否已低于上限。验证后 save 保存。

[命令参考](reference/mss.md) · [QoS 案例](../examples/qos.md)
