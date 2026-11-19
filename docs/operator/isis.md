# IS-IS

IPv4/IPv6 共用同一个 IS-IS 进程；Level-1、Level-2 缺省路由优先级均为15。Level与Preference是不同概念，切换Level后需检查各级邻接、LSDB和实际路由。

## 工作原理与层次规划

IS-IS 依据 ISO/IEC 10589 建立链路状态邻接，并通过 IP 路由扩展承载 IPv4、IPv6 前缀。NET 包含区域和系统标识；系统标识必须唯一。Level-1 面向区域内，Level-2 连接区域间路由，L1/L2 设备连接两种层次。

| 项目 | 对运行的影响 |
| --- | --- |
| NET / Area | 决定系统身份及 L1 邻接的区域条件 |
| Level | 决定建立哪类邻接、在哪个层次发布和学习路由 |
| IPv4 / IPv6 | 地址族启用与接口地址分别检查 |
| Cost / SPF | 决定协议内部路径；不等于路由优先级 |

VortexROS 的 L1、L2 缺省优先级均为 15。在线变更 Level 会改变可参与的邻接和路由范围，应安排收敛窗口，核对撤销的前缀也已从系统路由表消失。适合需要分层的内部网络，不是跨自治系统的策略协议。

~~~{toctree}
:maxdepth: 2

isis/activation
isis/redistribution
isis/spf
isis/operations
~~~
