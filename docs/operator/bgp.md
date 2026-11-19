# BGP

BGP 以邻居交换路由，各地址族控制发布和接收的前缀。全系统一个主 BGP AS；重复输入同一 AS 进入已有视图，不同 AS 被拒绝，65535 不可用。

按会话、组继承、路由属性或地址族进入子页。先验证会话建立，再确认路由选择及业务，不以配置存在代替路由生效。

## 工作原理与适用场景

BGP-4（RFC 4271）在自治系统之间或同一 AS 内交换可达性和路径属性。会话 Established 只说明邻居通信成立；是否收发、优选及安装某条路由，还取决于地址族、发布条件、策略和下一跳可达性。

| 场景 | 规划要点 |
| --- | --- |
| eBGP 外部互联 | 两端 AS、邻居地址、底层路由和出入策略 |
| iBGP 内部传播 | 全互联或路由反射，以及下一跳解析 |
| IPv4 / IPv6 | 分别启用对应地址族与邻居 |
| MPLS VPN / EVPN | 除会话外还要规划 RD、RT、标签或 VNI |

前缀存在于 network 配置中不等于已发布，需满足相应路由存在条件。路由策略允许的范围应显式规划，尤其避免把内部或默认路由意外传向外部。BGP 缺省系统优先级为 254；Local Preference、MED、AS_PATH 等属于 BGP 自身的选路属性。

修改认证、AS、传输源或重置会话可能中断所有相关地址族；只调整策略时，优先使用本手册所述的相应刷新方式。通过邻居计数、具体前缀明细和实际业务共同确认。

~~~{toctree}
:maxdepth: 2

bgp/peers
bgp/groups
bgp/reflection
bgp/attributes
bgp/multipath
bgp/families
bgp/queries
~~~

[完整双端案例](../examples/bgp.md) · [路由策略案例](../examples/bgp-policy.md) · [命令参数](reference/bgp.md) · [EVPN](11-vxlan-evpn.md)
