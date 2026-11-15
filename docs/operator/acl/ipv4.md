# IPv4 ACL

IPv4 ACL 以规则号顺序检查 IPv4 报文，首条命中决定放行/拒绝。定义不等于启用，绑定接口后才过滤；未命中的同地址族 IP 报文默认丢弃。

~~~text
system-view
acl name WEB-IN advance
 rule 10 permit tcp source 10.0.0.0 0.0.0.255 destination-port eq 443 tcp-flag syn
 rule 20 permit icmp icmp-type echo
 rule 100 deny ip
quit
commit
display acl name WEB-IN
~~~

source 的最后一项是通配掩码，不是子网掩码。只允许 SYN 不会自动放行后续 TCP 报文；Web 访问策略需按完整双向业务设计，不应将此字段演示直接当作可用的有状态防火墙。

ACL动作只有permit和deny。完整绑定及流量检查见[过滤案例](../../examples/acl.md)。例如：

~~~text
acl name DOC-STATELESS advance
 rule 10 permit ip
 rule 20 deny ip
~~~

先解除所有 traffic-filter/MQC/SSH 保护引用，再执行 undo acl name NAME，提交后核对 ACL 和原业务。名称区分大小写。需要保留时 save。

[接口绑定](attachment.md) · [匹配参数](matching.md) · [完整语法](../reference/acl.md)
