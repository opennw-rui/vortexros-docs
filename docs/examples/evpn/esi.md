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

在其中一台接入 PE 执行：

~~~text
system-view
interface Eth-Trunk 11
 undo esi
quit
commit
~~~

该设备不再以此 ESI 参与多归属，普通聚合及 VLAN 配置仍保留。先协调另一台 PE 与 CE 的接入，避免在同一个无环保护的二层网络中无计划地撤销 ESI。

需要恢复时，在同一聚合视图重新配置原 ESI 0000.1111.2222.1111.1111 并提交，重新检查通告、MAC 和双向探测。确认后 save 保存当前选择；改变 ESI 会影响分流、DF 与远端下一跳，不属于无中断操作。
