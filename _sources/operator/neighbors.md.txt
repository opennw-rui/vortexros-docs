# ARP 与 ND

检查和管理 IPv4 ARP 与 IPv6 ND 邻居。

`display arp` 的 `AGE(M)` 表示后端报告的邻居条目距上次更新的时间，按分钟取整显示，不是剩余过期时间。小于30秒或后端没有提供年龄时留空；静态项和接口自身地址的年龄也留空。

[命令参考](reference/neighbors.md)

~~~{toctree}
:maxdepth: 2

neighbors/configuration
neighbors/ipv6-query
~~~
