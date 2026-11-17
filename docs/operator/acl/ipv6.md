# IPv6 ACL

IPv6 使用独立 ACL 对象和地址语义。IPv4 的 permit ip 不能作为 IPv6 兜底；两族 ACL 名称在产品中需全局唯一。

~~~text
system-view
~~~

配置清单：

~~~text
acl ipv6 name V6-IN advance
 rule 10 permit icmpv6 icmp6-type neighbor-solicitation
 rule 20 permit tcp destination-port eq 443 tcp-flag established
 rule 100 permit ipv6
#
~~~

CLI 操作：

~~~text
commit
display acl ipv6 name V6-IN
~~~

established 只匹配 TCP ACK/RST 等控制位，任何符合字段的报文都可命中，不验证此前是否建立连接。应保留业务所需的邻居发现、错误与路径 MTU 报文，避免只放行 TCP 后导致 IPv6 控制报文中断。

IPv6 ACL 同样只执行无状态 permit 或 deny。

完整配置、查询结果和连接检查见[ACL 案例](../../examples/acl.md)。解除接口及其他引用后执行 undo acl ipv6 name NAME，提交后核对规则已删除及业务符合预期，再执行 save。

[规则字段](matching.md) · [接口绑定](attachment.md)

## 方向与地址族检查

在三层入口绑定 `deny icmpv6 destination 2001:db8:909::2/128`，实际 IPv6 探测无回复，同时 IPv4 对照 2/2。原位置将该条规则改为 permit 后，IPv6 恢复 3/3。把同一拒绝规则改绑至三层出口，同样阻止目标 IPv6 探测，IPv4 对照仍为 2/2；解绑、删除后 IPv6 恢复 2/2。

IPv6 匹配前缀写成 `地址/长度`，例如上面的 `/128`；不能在 ACL 规则里写成两个独立参数 `地址 128`。这与接口地址命令的参数格式不同。
