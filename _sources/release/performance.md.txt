# 性能测试

0.29-dev本轮未进行新的吞吐、满表或跨版本性能测试。此前试验版本的产品对比表不再在正式手册发布。以下仅保留明确标注来源的上游性能参考，不能作为VortexROS或自有插件的性能保证。

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
