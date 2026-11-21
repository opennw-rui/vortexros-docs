# 0.30-dev Debug 9

[下载单文件安装包及详细发布说明](https://github.com/opennw-rui/VortexROS/releases/tag/v0.30-dev-debug9)

Debug 9 默认提供设备首次启动开始的 72 小时试用，并增加光模块查询。版本号为 `0.30-dev-debug9`，Debian 包版本为 `0.30~dev.debug9`。配套组件见[版本说明](index.md)。

## 操作变化

- [授权与试用](../installation/license.md) 说明首次使用、永久授权导入、升降级和到期处理。
- [光模块诊断](../operator/ethernet/transceiver.md) 说明 DPDK 与 Linux 物理口的读取条件、功率、温度和阈值。
- [MPLS L3VPN](../operator/l3vpn.md#通告命名-vpn-的缺省路由) 可按 IPv4、IPv6 地址族分别开启或撤销缺省路由通告。
- [EVPN 多归属](../operator/evpn/multihoming.md) 恢复 ESI 后会重新通告已有客户 MAC，可从两台接入 PE 和远端逐一核对。
- [IPv4 邻居配置](../operator/neighbors/configuration.md#撤销同网段次地址) 同前缀仍被主地址覆盖时，撤销次地址保留动态 ARP。
- [升级与回退](../installation/07-upgrade-uninstall.md) 按版本与包内容选择组件，同版本重建包也可更新。已有授权跟随设备保留。

## 第三轮真实 CLI 验证

| 阶段 | 结果 |
| --- | --- |
| 全量阶段 | 共 852 条路径。456 条完整通过，393 条按所测范围通过，3 条部分通过。 |
| 后续补验 | 补验了 ESI 配置、撤销和同网段次地址撤销的已知失败场景。两条新增 VPN 缺省路由命令使命令参考达到 854 条。 |
| 缺陷修复 | 全量阶段 20 组，后续修复 4 组。后续涵盖三组 ESI 和一组次地址 ARP。安装器以及授权预检修复单列。 |
| 最终安装包 | 同一文件在隔离 QEMU 和真机升级成功。真机核对了配置、永久授权和路由恢复，BFD 为 Up、OSPF 为 Full、INT 对端探测收回 3/3。 |

真实 CLI 验收包含保存回放、OSPF 激活方式切换、小内存大页冷启动、混合数据面、VPN 双栈缺省路由、EVPN 多归属及多个组合业务。测试通过范围以所测配置、协议地址族和拓扑为准。全量 CLI 与最终包的定向验证口径见[完整发布说明](https://github.com/opennw-rui/VortexROS/releases/tag/v0.30-dev-debug9)。

逐条历史结果可查 [852 条 CLI 验收台账](https://github.com/opennw-rui/vortexros-docs/blob/main/validation/third-cli-coverage.tsv)。台账保留当时的三项部分通过，后续补测单独记录。
