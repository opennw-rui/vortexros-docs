# IPv6 ACL

IPv6 使用独立 ACL 对象和地址语义。IPv4 的 permit ip 不能作为 IPv6 兜底；两族 ACL 名称在产品中需全局唯一。

~~~text
system-view
acl ipv6 name V6-IN advance
 rule 10 permit icmpv6 icmp6-type neighbor-solicitation
 rule 20 permit tcp destination-port eq 443 tcp-flag established
 rule 100 permit ipv6
quit
commit
display acl ipv6 name V6-IN
~~~

established 只匹配 TCP ACK/RST 等控制位，任何符合字段的报文都可命中，不验证此前是否建立连接。应保留业务所需的邻居发现、错误与路径 MTU 报文，避免只放行 TCP 后导致 IPv6 控制报文中断。

工作树真实 CLI 已确认 IPv6 permit-reflect 拒绝，普通动作显示为：

~~~text
acl ipv6 name DOC6-STATELESS advance
 rule 10 permit ipv6
 rule 20 deny ipv6
~~~

数据面过滤的现有 IPv6 结果见[ACL 案例](../../examples/acl.md)。解除接口及其他引用后执行 undo acl ipv6 name NAME；提交、查询和流量对照后再保存。

[规则字段](matching.md) · [接口绑定](attachment.md)
