# ESI 生命周期

## 场景与前提

检查聚合接口从普通桥接切换为本地 Ethernet Segment，再恢复普通桥接。原隔离拓扑已有聚合、VLAN400、EVPN 邻居及两端业务，普通桥接探测2/2。底层建网参见[L2VPN](l2vpn.md)，多 PE/CE 组网见[多归属](../../operator/evpn/multihoming.md)。

下面的聚合编号须替换为本地已建立业务的实验 Eth-Trunk。本例是生命周期增量操作，没有声称建立完整双归属 CE。

## 创建与验证

在选定的 Eth-Trunk 视图：

~~~text
esi 0000.0000.0000.0000.0010
quit
commit
display bgp evpn all routing-table
display interface Eth-Trunk 1
display health
~~~

真实 FRR ES 清单为 local/up，CLI 出现对应 Type-4 通告，VLAN400 探测2/2。ES 清单来自后端回读，不能冒称产品另外存在一条 ES 查询命令。

## 撤销

~~~text
system-view
interface Eth-Trunk 1
 undo esi
quit
commit
display interface Eth-Trunk 1
display health
~~~

真实撤销一次提交成功，Linux/VPP 端口 Up，FRR ES 清单为空，健康 ready；即刻探测1/2，稳定后2/2。普通 VLAN 和聚合配置保留。需要持久保存时执行 `save`。

本例不证明无损切换、MAC ECMP 或完整 All-Active 故障恢复，不能把组网模板中的预期当作实测。
