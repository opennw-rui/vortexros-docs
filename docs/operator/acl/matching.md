# 规则与匹配

| 字段 | 含义与影响 |
|---|---|
| 规则号 | 从小到大匹配；后面的规则不会改写已经命中的决定 |
| permit / deny | 无状态放行/丢弃；没有自动反向放行 |
| source / destination | 同地址族地址/通配掩码，未指定则不限制对应地址 |
| source-port / destination-port | TCP/UDP 的 eq/range 端口匹配 |
| icmp-type / icmp6-type | 对应地址族 ICMP 类型/代码 |
| tcp-flag | TCP 控制位，包括 established；不是连接跟踪 |

SCTP 只支持协议与地址匹配，不能配置端口条件。数字协议号仍受地址族约束：IPv4 的1才是 ICMP，IPv6 的58才是 ICMPv6。DSCP、VLAN、长度等不是这套 ACL 字段，按相应 MQC 功能配置，不暗中转换。

修改规则进入 Candidate，失败不应改变原规则；commit 后更新被引用的实际 ACL。MQC 引用内容修改后不必解绑再绑定。参数和完整子命令见[规则参考](../reference/acl.md)。

[IPv4](ipv4.md) · [IPv6](ipv6.md) · [真实案例](../../examples/acl.md)
