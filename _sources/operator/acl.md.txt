# ACL

匹配报文并决定放行或拒绝，也可用作 MQC 的分类条件。

[命令参考](reference/acl.md) · [配置案例](../examples/acl.md)

## 配置与验证

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
