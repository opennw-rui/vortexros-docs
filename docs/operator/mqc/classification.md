# 分类器

MQC 处理 IPv4 和 IPv6 业务报文；`if-match any` 匹配此范围内的全部报文。在交换端口上，它也不表示匹配 ARP、LLDP、LACP 或自定义 EtherType 的非 IP 二层帧。


分类器选择交给流行为处理的报文；它本身不决定放行或丢弃。


operator and 要求所有条件同时满足；operator or 只要求任一条件满足。
空分类器不匹配全部流量，需要匹配全部时使用 if-match any。
ACL 条件只将 ACL 的 permit 结果作为匹配；if-match not acl 反选此结果。
最终放行或丢弃仍由流行为决定。

下面的设备从 Vlanif110 接收客户端流量，从 Ethernet1 发往服务器。
客户端为 198.18.30.99，服务器为 198.18.31.2；接口和路由先按
[完整案例](../../examples/mqc.md)的组网方法准备，并替换为本节地址。
此例拒绝指定 UDP 流量，其他流量继续匹配后续项。
端口范围包含两端，packet-length 为 IP 报文长度，不含以太网头。

~~~text
system-view
traffic classifier SEL-AND operator and
 if-match dscp ef
 if-match protocol ip
 if-match protocol-number 17
 if-match source-ip 198.18.30.0/24
 if-match destination-ip 198.18.31.2/32
 if-match source-port 42000 to 42010
 if-match destination-port 49000
 if-match packet-length 100 to 200
 if-match outbound-interface Ethernet1
#
traffic behavior SEL-DROP
 deny
#
traffic policy SEL-POL
 classifier SEL-AND behavior SEL-DROP precedence 19
#
interface Ethernet1
 traffic-policy SEL-POL outbound
#
commit
display traffic classifier user-defined SEL-AND
display traffic policy user-defined SEL-POL
~~~

实际查询显示 Operator: and，Rule(s) 下列出全部九条条件，DSCP EF 显示为 46。
IPv4 UDP、DSCP46、源端口42000、目的端口49000、IP长度124字节的三个报文全部被丢弃；
只把源端口改为42011后，出口收到3/3。

## 其他匹配条件的效果

以下为同一 deny 行为的实际匹配和不匹配对照，0/3表示三个报文均未从目标出口发出。

| 条件 | 匹配结果 | 不匹配结果 |
|---|---|---|
| dscp ef | DSCP46为0/3 | DSCP0为3/3 |
| acl SELACL，ACL允许UDP源端口42000 | 42000为0/3 | 42001为3/3 |
| not acl SELACL | 42001为0/3 | 42000为3/3 |
| vlan-id110，trunk承载110，再AND dscp ef | 同VLAN、DSCP46为0/3 | 同VLAN、DSCP0为3/3 |
| vlan-id110，access PVID110，再AND dscp ef | 无标签、DSCP46为0/3 | 无标签、DSCP0为3/3 |
| tcp syn-flag | SYN为0/3 | 仅ACK为3/3 |
| tcp-flags 0x10 mask 0x10 | ACK为0/3 | 仅SYN为3/3 |
| vxlan-vni1001 OR protocol ipv6 | VNI1001和IPv6分别为0/3 | IPv4、VNI1002为3/3 |

VLAN 条件要求绑定接口实际承载目标 VLAN。VXLAN VNI 条件必须在能看到外层封装的位置匹配，
不能在解封装后用它选择外层 VNI。
inbound-interface 匹配策略看到的输入接口，outbound-interface 匹配实际出口；
从三层 VLAN 接口进入的报文，其输入接口可为 Vlanif110。

## 删除条件与策略

undo if-match TYPE 删除该类条件，undo if-match 删除分类器全部条件。
display this 和当前配置展示 Running，提交前用 display configuration candidate merge 检查修改。

~~~text
interface Ethernet1
 undo traffic-policy outbound
#
traffic policy SEL-POL
 undo classifier SEL-AND
#
undo traffic policy SEL-POL
undo traffic behavior SEL-DROP
undo traffic classifier SEL-AND
commit
~~~

实际撤销后，原先受限的 IPv4 UDP 和 TCP SYN 均恢复3/3。核对业务后执行 save。


[逐条参数和限制](../reference/mqc.md) · [完整配置案例](../../examples/mqc.md)

## Access 端口按业务 VLAN 分类

Access 端口收到的无标签报文按端口 PVID 匹配 VLAN 条件。
下面拒绝 Ethernet0 所承载 VLAN110 中 DSCP EF 的流量，其余流量继续转发：

~~~text
system-view
traffic classifier ACCESS110 operator and
 if-match dscp ef
 if-match vlan-id 110
#
traffic behavior ACCESS-DENY
 deny
#
traffic policy ACCESS-P
 classifier ACCESS110 behavior ACCESS-DENY precedence 10
#
interface Ethernet0
 portswitch
 port link-type access
 port default vlan 110
 traffic-policy ACCESS-P inbound
#
commit
display traffic classifier user-defined ACCESS110
display traffic policy applied-record
~~~

示例实际结果为 DSCP46 出口收到0/3，DSCP0收到3/3。
修改端口 PVID 会同时更新策略的业务 VLAN 上下文；条件仍需与新的承载 VLAN 一致。
将 VLAN 条件策略绑定到未承载该 VLAN 的接口时，编辑被拒绝，不会等提交后才停止业务。

在分类器、流行为、流策略、VLAN 和接口视图执行 display this，可以查看该视图已提交的配置。
未提交修改用 display configuration candidate merge 查看。

~~~text
interface Ethernet0
 undo traffic-policy inbound
#
undo traffic policy ACCESS-P
undo traffic behavior ACCESS-DENY
undo traffic classifier ACCESS110
commit
~~~

实际撤销后，原先被拒绝的 DSCP46 流量恢复3/3，其他接口和策略不需要重建。
