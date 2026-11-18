# HYB01：真实 DPDK 双端 Hybrid 验证

版本：两端控制 run13、VPP26.10.8、FRR1.8；.28 两个 QEMU guest，各1.5GiB/2vCPU，128×2MiB实际大页，数据口均由DPDK接管。无吞吐结论。

管理 eth0 不受管；Ethernet0 保留 C01 IPv6 对照。Ethernet1 两端通过 QEMU socket43012互联，实际连接已确认。数据配置来自真实交互CLI，每条命令观察提示符，commit后查询实际输出。

两端共用配置：全局VLAN100、101，Ethernet1 portswitch/hybrid/PVID100/untag100/tag101；Vlanif100地址198.18.100.1/24与.2/24，Vlanif101地址198.18.101.1/24与.2/24。R2的两个Vlanif显式MAC为0200-0030-0264/0265。

| 阶段 | 目标流 | 独立对照 | CLI/实际状态 |
| --- | --- | --- | --- |
| 初始克隆环境 | 100和101均0/3 | E0已有IPv6正常 | 两端相同machine-id导致派生BVI MAC相同；VPP记录mac move violations，尚未算Hybrid通过 |
| R2真实CLI设置不同Vlanif MAC | 100为3/3，101双向3/3 | E0独立 | 相同配置及链路，修改的变量只有两BVI MAC；pcap分别为无标签100和单标签101 |
| R1 undo tagged101，commit | 101为0/2 | 100为2/2 | display vlan101不再列E1，native BD101只余BVI |
| 恢复tagged101，undo untagged100，commit | 100为0/2 | 101为2/2 | display vlan100不再列E1，native BD100只余BVI |
| 恢复untag100，undo PVID，commit | 100为0/2 | 101为2/2 | display this省略默认PVID；native E1.1实际收包，E1.100只出不收 |
| 恢复PVID100，commit | 100为2/2 | E0 IPv6为2/2 | 双端真实save，最后无未提交Candidate |

不把预期撤销后的目标丢包当作缺陷；不把最初克隆MAC重复归为分类性能或抖动。此处没有冷启动/重置恢复结论，没有覆盖Access/Trunk所有变体或MAC撤销；后续受影响集合继续补验。

主要证据：.28 `/root/vros-cli-real-20261118/combos/Hybrid-evidence/{c01,c02}/terminal.raw`、同目录各自config.cfg，`hybrid-wire2-through-undo.pcap`。本地 `Hybrid-combo1-backend.txt`、`Hybrid-combo2-backend.txt` 为最终完整实际状态快照。

计数：本例新增12条本组未记过的canonical路径，包括Hybrid设置/撤销六条；参数、重复操作、对照流和本例场景不另增CLI路径数。与其他agent必须按path再去重。
