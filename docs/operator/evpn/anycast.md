# Anycast 网关


Vbdif 启用 `vxlan anycast-gateway enable` 前必须配置明确的网关 MAC。未配置时，Candidate 会拒绝，Running 保持原配置。

开发拓扑的桥域450/VNI10450使用如下真实配置：

```text
interface Vbdif 450
 mac-address 0200-0000-0450
 ip address 198.18.145.1 255.255.255.0
 vxlan anycast-gateway enable
 quit
commit
display interface Vbdif450
display bgp evpn all routing-table
```

Linux 与 VPP 的网关 MAC 均为 `02:00:00:00:04:50`；FRR 实际 VNI 显示 `Advertise-gw-macip: Yes`，BGP 出现 `0:48:0200-0000-0450:32:198.18.145.1` 的 Type-2 路由。对端 CE 在旧 MAC 的邻居缓存尚未更新时首轮3包全丢；网关发起邻居交互后，CE 缓存已变为新 MAC，CE→网关及网关→CE 均3/3。修改网关 MAC 会影响对端缓存，部署时应在维护窗口处理；不能将最初失败省略成全程无损。

撤销 `undo vxlan anycast-gateway enable` 并提交后，FRR 显示 `Advertise-gw-macip: No`，网关通告撤销。显式 MAC 和接口 IP 是独立配置，不随开关自动删除。本次拓扑仅有一个活动网关，没有据此宣称完成双网关漫游或全套 All-Active 故障验收。


## 使用顺序

先完成 L2VPN 的 underlay、桥域、BGP EVPN 和接入。Anycast 缺省关闭，需显式网关 MAC 后才可启用。改变 MAC 会影响主机 ARP/ND 缓存，应协调两端参数并比较通告和流量。本页 VLAN450 是已有实验的增量配置，不能单独建立完整 EVPN。

[配置案例](../../examples/evpn/anycast.md) · [L2VPN 基础配置](../../examples/evpn/l2vpn.md)
