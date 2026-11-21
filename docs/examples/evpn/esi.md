# ESI 配置变更

## 前提

按 [All-Active](all-active.md)先完成 CE、三台 PE、Eth-Trunk11、VLAN/BD460 与 VNI50460。ESI 标识同一以太网段，两台接入 PE 必须一致，不能为不同客户接入重复使用。

## 查询

~~~text
display current-configuration interface Eth-Trunk 11
display bgp evpn all routing-table
display mac-address bridge-domain 460
display interface Eth-Trunk 11
~~~

应有本段 Type-4 通告及远端客户 MAC 对应的 ES 下一跳组。双归属的链路关闭、恢复和完整删除见前置案例。

## 撤销与重新加入

以下操作会改变多归属关系。先协调两台接入 PE 与 CE 的接入方式，再进入维护步骤。仅在一台撤销 ESI，而另一台仍发布原 ESI、CE 继续双链路发送，可能触发 MAC 移动保护，导致部分 VLAN 中断。

在选定接入 PE 执行：

~~~text
system-view
~~~

配置清单：

~~~text
interface Eth-Trunk 11
 undo esi
#
~~~

CLI 操作：

~~~text
commit
~~~

该设备不再以此 ESI 参与多归属，普通聚合及 VLAN 配置仍保留。先协调另一台 PE 与 CE 的接入，避免在同一个无环保护的二层网络中无计划地撤销 ESI。

需要恢复时，在同一聚合视图重新配置原 ESI 0000.1111.2222.1111.1111 并提交，重新检查通告、MAC 和双向探测。确认后 save 保存当前选择；改变 ESI 会影响分流、DF 与远端下一跳，不属于无中断操作。


## 实际变更结果

单台 PE 撤销后，本机的 Type-1/Type-4 通告消失，另一台 PE 的同段通告保留；Eth-Trunk11 仍为 Up，原 VLAN460/461 配置保留。本次单台撤销试验中，普通帧探测 1/1，带 VLAN461 标记的探测 0/1；这是两端 ESI 不一致时不能承诺无损变更的实际影响。

恢复同一 ESI：

```text
interface Eth-Trunk 11
 esi 0000.1111.2222.1111.1111
#
```

```text
commit
display current-configuration interface Eth-Trunk11
display bgp evpn all routing-table | include 00:00:11:11:22:22:11:11:11:11
display eth-trunk 11
save
```

实际恢复后，本机 Type-1/Type-4 通告重新出现，普通帧和 VLAN461 客户探测均为 1/1；健康状态 ready、无活动告警。变更方案应协调两台 PE 与 CE，并按业务 VLAN 分别验证。

## Debug 8 恢复后的业务检查

已有客户 MAC 可随 ESI 恢复自动重新通告。先在远端核对客户 MAC 的 Type-2 和两条 ES 路径，再从 CE 侧分别验证 IPv4、IPv6。从接入两侧检查 MAC 归属时，客户 MAC 应走对应本地接入。检查通过后继续保存配置，无需为恢复通告而清 MAC。
