# IPv4 ACL

IPv4 ACL 以规则号顺序检查 IPv4 报文，首条命中决定放行/拒绝。定义不等于启用，绑定接口后才过滤；未命中的同地址族 IP 报文默认丢弃。

~~~text
system-view
~~~

配置清单：

~~~text
acl name WEB-IN advance
 rule 10 permit tcp source 10.0.0.0 0.0.0.255 destination-port eq 443
 rule 20 permit icmp icmp-type echo
 rule 100 deny ip
#
~~~

CLI 操作：

~~~text
commit
display acl name WEB-IN
~~~

source 的最后一项是通配掩码，例如 0.0.0.255 匹配 /24 网段。上例允许该网段到 TCP/443 的报文，但返回方向仍需单独满足沿途 ACL。若另加 tcp-flag syn，则只匹配 SYN 条件，不会自动放行后续数据报文。

接口绑定、双向连接检查和撤销步骤见[过滤案例](../../examples/acl.md)。

先解除所有 traffic-filter/MQC/SSH 保护引用，再执行 undo acl name NAME，提交后核对 ACL 和原业务。名称区分大小写。需要保留时 save。

[接口绑定](attachment.md) · [匹配参数](matching.md) · [完整语法](../reference/acl.md)
