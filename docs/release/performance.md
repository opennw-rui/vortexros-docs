# 性能测试

下列数据来自不同的测试环境。控制层 CLI 耗时、隔离 memif 实收速率和上游 PDR 分别报告。

## 控制层

| 真实 CLI，3,200 条 ACL 规则 | Debug 4 | Debug 5 |
| --- | ---: | ---: |
| MTU 编辑，三次中位数 | 54.20 ms | 34.67 ms |
| 显式 Candidate 刷新，单次对照 | 118.36 ms | 39.49 ms |

成对测试由夹具发布新的 Running。由第二个真实 CLI 会话提交后，第一会话另一次显式刷新为 43.09 ms。[Debug 5 发布记录](https://github.com/opennw-rui/VortexROS/releases/tag/v0.28-dev-debug5)

Debug 4 的 IPv4/IPv6 FIB 分别用 50,000 条路由对照组合过滤，输出保持逐字节一致。IPv4 CLI 峰值内存从 58–76 MiB 降为 49–50 MiB，IPv6 从 127–142 MiB 降为 52–54 MiB。范围对应不同过滤组合。[Debug 4 测试记录](https://github.com/opennw-rui/VortexROS/releases/tag/v0.28-dev-debug4)

## VPP 隔离测试

双 VPP memif 升载和恢复测试的最高实收约为 **6.67 Mpps**。持续学习期间触发 MAC 扫描，L2FIB 计数与逐条读回均为 3,707。该样本未命中 handoff 拥塞与 worker refork 的精确交错，也未在 MAC 扫描内部插桩。结果适用于该隔离拓扑。

## FD.io CSIT

各 CPU、网卡及驱动组合的公开测试入口见[支持的硬件](../installation/hardware.md#公开性能数据)。

FD.io 的 VPP 26.06 与 26.10 成对测量使用 E810 和单 worker。下表是部分 PDR 结果，单位 Mpps；IPv6 用例为 78 字节帧，其余为 64 字节帧。

| 路径 | 驱动 | 26.06 | 26.10 |
| --- | --- | ---: | ---: |
| IPv4 基础转发 | DPDK | 23.72 | 24.84 |
| IPv6 基础转发 | AVF | 20.74 | 23.01 |
| 二层桥接及 MAC 学习 | AVF | 33.37 | 32.69 |
| 出方向 50 条 ACL、1 万流 | AVF | 17.27 | 16.41 |
| VXLAN 桥接及 MAC 学习 | DPDK | 13.84 | 13.85 |

[FD.io CSIT 26.10 报告](https://csit.fd.io/cdocs/release_notes/current/#csit-2610-selected-performance-comparisons)。这些是上游 VPP 用例；配套 MQC、NAT Policy、AmneziaWG 没有同条件的跨版本吞吐对照。
