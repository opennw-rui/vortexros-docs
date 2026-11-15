# 多归属


All-Active 多归属使用同一 ESI 把 CE 同时接入 P1、P2，P3 作为远端 PE，P4 作为
Route Reflector。FRR 负责 Type-1/Type-4、DF 选举和 EVPN 路径选择；switchd 维护
Linux 控制对象；LCP 只负责在 Linux/FRR 与 VPP 之间传递多归属状态；VPP 执行
MAC ECMP、非 DF BUM 过滤、local-bias、split-horizon 和故障切换。

```text
                  P4 (RR)
                 /       \
CE1 == Eth-Trunk1 == P1   P2 == Eth-Trunk1 == CE1
                         \
                          P3 -- CE2
```

P1、P2 的 CE 侧 Eth-Trunk 使用相同 ESI。以下为 P1 示例；P2 使用相同 ESI、VLAN、
VNI 和 RT，但使用自己的 RD、VTEP 地址及物理成员：

```text
system-view
enable switch
evpn-overlay enable
vlan 101
bridge-domain 101
 l2 binding vlan 101
 vxlan vni 5010
 evpn
  route-distinguisher 65000:101
  vpn-target 65000:5010 both
 quit
quit
interface Eth-Trunk 1
 mode manual
 trunkport Ethernet 2
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 101
 port trunk pvid vlan 101
 esi 0000.0000.0000.0000.0001
quit
interface Nve 1
 source 10.255.0.1
 vni 5010 head-end peer-list protocol bgp
quit
bgp 65000
 peer 10.255.0.4 as-number 65000
 peer 10.255.0.4 connect-interface LoopBack 0
 l2vpn-family evpn
  peer 10.255.0.4 enable
 quit
quit
commit
```

Underlay 必须能分别到达 P1、P2、P3 的 VTEP；多归属 VTEP 当前使用 IPv4。P4
按普通 EVPN RR 配置，对 P1、P2、P3 启用 `l2vpn-family evpn` 并配置反射客户端。

使用以下命令确认 Type-1/Type-4、DF、远端 MAC ECMP 和设备健康：

```text
display bgp evpn all routing-table
display mac-address
display interface Eth-Trunk 1
display health
```

链路故障验收必须同时确认：故障成员退出本地 ES、远端 NHG 缩减为单成员、业务仍然
连通；链路恢复后 NHG 恢复双成员。VPP 冷重启验收必须确认本地 ES、远端 NHG 和
业务转发均恢复，不能只以其他 PE 仍能转发作为成功依据。

## 范围、实际记录和撤销

配套 FRR 只支持 All-Active，不提供 Single-Active，多归属 VTEP 限定 IPv4。上面的RR组网仍是模板；本轮另有三PE全互联的[完整All-Active案例](../../examples/evpn/all-active.md)，记录真实双成员组、双接入故障、恢复、冷回放及撤销。两种组网的证据不混用。

[ESI 生命周期案例](../../examples/evpn/esi.md)记录真实配置、ES local/up、Type-4 通告、VLAN400 转发和撤销后的端口恢复。双归属CE的补验见All-Active案例；单ESI增删与多PE故障验证仍分别记录。

撤销单个接入的多归属属性，在对应 Eth-Trunk 执行 `undo esi` 并提交，保留普通桥接和 VLAN 成员关系。只有确认业务无引用时才删除聚合、VNI 或桥域。

[实际生命周期](lifecycle.md) · [命令参考](../reference/evpn.md)
