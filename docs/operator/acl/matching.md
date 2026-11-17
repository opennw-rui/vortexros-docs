# 规则与匹配

| 字段 | 含义与影响 |
|---|---|
| 规则号 | 从小到大匹配；后面的规则不会改写已经命中的决定 |
| permit / deny | 无状态放行/丢弃；没有自动反向放行 |
| source / destination | 同地址族地址/通配掩码，未指定则不限制对应地址 |
| source-port / destination-port | TCP/UDP 的 eq/range 端口匹配 |
| icmp-type / icmp6-type | 对应地址族 ICMP 类型/代码 |
| tcp-flag | TCP 控制位，包括 established；不是连接跟踪 |

SCTP 支持协议与地址匹配，不支持端口条件。IPv4 协议号 1 表示 ICMP，IPv6 协议号 58 表示 ICMPv6。需要按 DSCP、VLAN 或报文长度分类时，使用相应 MQC 功能。

修改规则后执行 commit 才生效。已被接口或 MQC 引用的 ACL 会随规则修改更新，无需先解绑再绑定；变更可能立即放行或阻断业务，请先核对规则号和匹配范围。参数和完整子命令见[规则参考](../reference/acl.md)。

[IPv4](ipv4.md) · [IPv6](ipv6.md) · [配置案例](../../examples/acl.md)
