# ACL、QoS、MQC、MSS 与 nat-policy

## ACL

```text
acl name WEB-IN advance
 rule 10 permit tcp source 10.0.0.0 0.0.0.255 destination-port eq 443 tcp-flag syn
 rule 15 permit icmp icmp-type echo
 rule 20 deny ip
```

ACL可被接口traffic-filter、MQC classifier和SSH源地址保护等功能引用。删除ACL前必须先解除所有引用。

直接绑定到接口：

```text
interface Vlanif 100
 traffic-filter inbound acl WEB-IN
```

提交后，进入Vlanif100的报文按规则序号从小到大匹配。首条匹配规则决定permit或deny；进入ACL检查
但未匹配任何规则的同地址族IP报文默认丢弃。零规则ACL绑定到接口后只默认丢弃它所属的地址族；
ACL仅创建、未绑定接口时不会过滤接口流量。

例如只拒绝Telnet、其余IPv4流量放行时，必须显式配置末尾兜底规则：

```text
acl name BLOCK-TELNET advance
 rule 10 deny tcp destination-port eq 23
 rule 100 permit ip
```

`permit ip`只兜底IPv4。IPv6策略使用独立对象：

```text
acl ipv6 name V6-IN advance
 rule 10 permit icmpv6 icmp6-type neighbor-solicitation
 rule 20 permit tcp destination-port eq 443 tcp-flag established
 rule 100 permit ipv6
```

ICMP type/code与TCP标志直接投影到VPP ACL字段；不支持的DSCP、VLAN、长度、时间段等条件应使用对应
功能，ACL不会暗中转成MQC。IPv4与IPv6 ACL名称必须保持全局唯一。
SCTP规则支持协议与地址匹配，不支持源/目的端口条件；TCP、UDP仍支持`eq`和`range`。数字协议
必须遵循地址族：IPv4协议1可配置`icmp-type`，IPv6协议58可配置`icmp6-type`，跨族组合在进入
Candidate前被拒绝。

```text
display acl name WEB-IN
display acl ipv6 name V6-IN
display interface Vlanif 100
```

```text
interface Vlanif 100
 undo traffic-filter inbound
undo acl name WEB-IN
undo acl ipv6 name V6-IN
commit
```

## 接口QoS

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

## MQC

```text
traffic classifier WEB-CLASS operator and
 if-match acl WEB-IN
#
traffic behavior WEB-BEHAVIOR
 car cir 100000 pir 100000 cbs 18750000 pbs 31250000 green pass yellow pass red discard
 redirect vpn-instance BLUE
#
traffic policy WEB-POLICY
 classifier WEB-CLASS behavior WEB-BEHAVIOR precedence 10
#
interface Vlanif 100
 traffic-policy WEB-POLICY inbound
```

`redirect vpn-instance BLUE`不改目的地址，IPv4/IPv6分别进入BLUE对应FIB查目的地址，支持直连、静态、动态、递归、ECMP和默认路由；无匹配时按FIB miss丢弃，不回退原VPN。table-only、next-hop和interface三种redirect互斥。

同一behavior可以同时执行CAR、remark和redirect。重定向到VPN后，报文只在目标VPN中重新查找一次路由，不会反复执行同一重定向形成循环。

```text
display traffic classifier user-defined WEB-CLASS
display traffic behavior user-defined WEB-BEHAVIOR
display traffic policy user-defined WEB-POLICY
```

修改被MQC引用的ACL后，新的匹配规则在本次commit成功后生效；无需解除并重新绑定traffic policy。

## TCP MSS Clamp

TCP MSS Clamp只处理包含MSS选项的TCP SYN报文。报文中的MSS大于出接口MTU允许的上限时才会被改小；原值已经足够小或报文不是SYN时不会修改。

自动模式随接口MTU变化重新计算上限：

```text
interface Tunnel 1
 tcp mss clamp
```

也可以指定固定MSS：

```text
interface Tunnel 1
 tcp mss 1360
```

接口MTU变化后，自动模式无需重新配置。使用 `display this` 和接口统计检查配置及报文变化。删除：

```text
interface Tunnel 1
 undo tcp mss
commit
```

## nat-policy

在`display nat-policy name ?`中，`<NAT-POLICY>`表示可输入策略名，后续各行列出当前Candidate中已有的策略名；Tab和`?`使用相同的大小写无关字母顺序。

```text
nat-policy address-set name INSIDE
 address 10.0.0.0/8
#
nat-policy port-set name WEB
 port 80
 port 443
#
nat-policy name INTERNET
 statistic enable
 rule 10
  source address-set name INSIDE
  destination port-set name WEB
  action snat pat interface
```

接口绑定：

```text
interface Vlanif 100
 nat-policy INTERNET inbound
```

统计默认关闭；只有在policy或rule下显式配置 `statistic enable` 后才更新对应计数。未启用统计时，display会明确显示统计关闭。

```text
display nat-policy name INTERNET
display nat-policy statistics name INTERNET
clear nat-policy counters
display nat-policy sessions
clear nat-policy sessions
```

`display nat-policy sessions`不带参数时展示全部活动会话。也可以任意组合下列条件；多个条件采用AND语义，并由数据面按原始（转换前）五元组直接筛选：

```text
display nat-policy sessions [protocol { tcp | udp | icmp | sctp | 0..255 }]
 [source-ip IPV4] [destination-ip IPV4]
 [source-port PORT] [destination-port PORT]
 [worker INDEX] [core CPU-ID] [name POLICY] [rule RULE-ID]
 [action { no-nat | static-nat | snat-no-pat | snat-pat | dnat | twice-nat }]
 [hairpin { enable | disable }]
```

例如，查看`INTERNET`策略中由CPU 6处理、目的端口为443的TCP PAT会话：

```text
display nat-policy sessions protocol tcp destination-port 443 core 6 name INTERNET action snat-pat
```

会话按块显示。首行是协议、状态、worker、CPU核心、剩余时间和计数，第二行是接口、方向、FIB、policy/rule和动作，第三行显示原始五元组到转换后五元组。TCP、UDP和SCTP显示端口；ICMP显示identifier；GRE、ESP、AH、OSPF等无端口协议只显示地址，避免把内部零值误当成端口。

NAT回流默认关闭。需要先开启全局开关，再在包含DNAT、twice-NAT或静态NAT发布规则的policy中开启：

```text
nat-policy hairpin enable
nat-policy name INTERNET
 hairpin enable
commit
```

关闭时可撤销policy或全局开关：

```text
nat-policy name INTERNET
 undo hairpin enable
quit
undo nat-policy hairpin enable
commit
```

两个开关必须同时开启。显式NO_NAT和本接口的显式转换决定优先；回流只使用同一FIB中的唯一发布映射。开关不会强制清除已有会话。验证时应同时测试客户端到公网映射地址的正向连接、服务端回包恢复、同一端口多连接、会话清除后端口复用，以及关闭后已有会话不断、新会话不再回流。

新增、修改或删除规则后，只影响相关policy和接口绑定。已有会话继续按会话状态处理，新连接使用新的规则。

解除接口绑定后再删除policy和对象：

```text
interface Vlanif 100
 undo nat-policy INTERNET inbound
undo nat-policy name INTERNET
undo nat-policy port-set name WEB
undo nat-policy address-set name INSIDE
commit
```

## 策略继承

配置在二层物理接口或VLAN上的ACL、QoS、MQC和nat-policy会作用到相应的trunk业务流量。Eth-Trunk成员使用聚合接口的二层/三层属性，成员接口下不重复显示父接口配置。

## 组合验证

| 顺序 | 验证点 |
|---|---|
| ACL | 分类与丢弃计数正确 |
| 输出MSS | 只修改超限SYN |
| MQC | classifier、CAR、remark、redirect均生效 |
| nat-policy | 新会话、普通回程、NAT回流、PAT和统计开关正确 |
| 输出 | 无重复TTL/Hop-Limit递减或循环 |

组合策略验证完成后，再使用各功能的统计命令确认命中顺序和计数与业务流量一致。
