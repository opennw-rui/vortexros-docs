# ACL

ACL 只做无状态过滤，动作只有 permit 和 deny，不建立连接表，也不根据正向放行自动放行反向报文。TCP established 是标志位匹配，不是会话状态。

~~~{toctree}
:maxdepth: 2

acl/ipv4
acl/ipv6
acl/matching
acl/attachment
~~~

[完整双端案例](../examples/acl.md) · [逐条参数](reference/acl.md)
