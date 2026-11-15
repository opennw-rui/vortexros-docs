# EVPN 变更与恢复

## 撤销 ESI

在聚合接口视图执行`undo esi`并提交。聚合恢复为普通桥接成员，原有VLAN、成员接口及管理状态保留：

~~~text
interface Eth-Trunk 11
 undo esi
quit
commit
display interface Eth-Trunk 11
display bgp evpn all routing-table
~~~

多归属业务的远端下一跳组会随ES通告变化。变更期间检查剩余路径和客户业务，不能只查看本地聚合是否Up。

## 删除 VNI

`undo vni VNI`删除选定VNI的整个head-end绑定；带静态peer后缀时只删除该对端，带`protocol bgp`时只撤销动态发现。其他VNI保留。

先在NVE视图撤销绑定，提交后核对隧道、MAC及对应业务路由。删除BGP EVPN地址族前，必须先解除使用它的NVE依赖。

## 保存与重建

完成变更并确认业务正常后执行`save`。重建数据面后检查BGP邻居、EVPN路由、VXLAN隧道、业务FIB和客户连通性。

共用的NVE、BGP进程和底层路由不应随单个业务一起删除。完整操作见[二层业务](../../examples/evpn/l2vpn.md)、[三层业务](../../examples/evpn/l3vpn.md)和[多归属](../../examples/evpn/all-active.md)。
