# L3VPN

L3VNI 为租户路由提供 VXLAN 传输；BGP EVPN Type-5 交换 IP 前缀。它与 MPLS L3VPN 的标签传输不同，不能将 VPNv4 学到的前缀当作 Type-5 成功。

## 配置和限制

在 VPN-instance 中配置 L3VNI、对应地址族 RD/RT，把租户接口绑定到该 VPN。BGP 的租户 IPv4/IPv6 地址族配置路由引入及 `advertise l2vpn evpn`。内部服务 SVI/桥域由系统管理，不在 NVE 下重复创建同编号 L2VNI。

## RD 与 VPN target

同一台 PE 的一个 L3VNI 使用一组 EVPN RD、import RT 和 export RT。只有一个地址族启用 `advertise l2vpn evpn` 时，使用该地址族的设置；IPv4、IPv6 都启用时，两族的 RD、import RT 集合、export RT 集合分别必须一致。可以逐项编辑 Candidate，但不一致的配置不能提交，不会改变当前运行配置。

| 设置 | P1 IPv4 | P1 IPv6 | P2 IPv4 / IPv6 |
|---|---|---|---|
| RD | 65000:1801 | 65000:1801 | 65000:1802 |
| import RT | 65000:50081、65000:50082、65000:50083 | 65000:50083、65000:50081、65000:50082 | 65000:50081 |
| export RT | 65000:50081、65000:50082 | 65000:50082、65000:50081 | 65000:50081、65000:50083 |

RT 按集合比较，输入顺序不影响含义，支持多个 RT。import 与 export 可以采用不同集合；其他 PE 的 RD 可以不同。远端路由携带的 export RT 只要有一个与本地 import RT 匹配，即可导入；移除最后一个匹配的 import RT 后才会撤销该路由。

这些共享规则仅适用于向同一个 L3VNI 发布的 EVPN 地址族。没有启用 EVPN 通告的 MPLS VPN IPv4/IPv6 地址族仍独立配置 RD/RT。

修改 RD 会撤销旧 RD 下的 Type-5 并重新发布。修改 RT 会重新计算导入、导出关系，可能使业务路由立即变化；在两个地址族完成所需修改后统一提交，再查询双栈路由与连通性。

[完整双 PE 案例](../../examples/evpn/l3vpn.md)使用 CLI-TYPE5、VNI50081、RT65000:50081，没有 VPNv4/VPNv6 传输邻居。两端均通过 EVPN 交换租户双栈前缀。

## 验证

~~~text
display bgp evpn all routing-table
display ip routing-table vpn-instance CLI-TYPE5 198.18.196.2 32
display ipv6 routing-table vpn-instance CLI-TYPE5 2001:db8:196::2 128
ping -vpn-instance CLI-TYPE5 -c 2 -a 198.18.196.1 198.18.196.2
ping ipv6 vpn-instance CLI-TYPE5 -c 2 -a 2001:db8:196::1 2001:db8:196::2
~~~

检查远端 Type-5、租户路由与实际下一跳，并用对应 VPN 源地址发起 IPv4/IPv6 双向探测。重建数据面后应再次检查路由与连通性。

## 撤销与保存

在两个租户地址族撤销 advertise l2vpn evpn 并提交，远端租户前缀应消失，而未撤销的 L2VNI 保留。再按依赖顺序撤销 BGP 租户地址族、接口和 VPN。共用 NVE、EVPN 邻居及底层路由应保留，核对后 save。

[功能范围](../11-vxlan-evpn.md) · [MPLS L3VPN](../l3vpn.md)

## 多个 RT 的操作示例

在已有 L3VPN 上，P1 保持 RT 65000:50081，并增加第二个导出 RT；两个 EVPN 地址族都作相同修改：

```text
ip vpn-instance CLI-TYPE5
 ipv4-family
  vpn-target 65000:602 export-extcommunity
 #
 ipv6-family
  vpn-target 65000:602 export-extcommunity
#
commit
```

对端保留原导入 RT，增加 65000:602 和不匹配的 65000:603：

```text
ip vpn-instance CLI-TYPE5
 ipv4-family
  vpn-target 65000:602 import-extcommunity
  vpn-target 65000:603 import-extcommunity
 #
 ipv6-family
  vpn-target 65000:603 import-extcommunity
  vpn-target 65000:602 import-extcommunity
#
commit
```

两族输入顺序不同仍表示同一集合。此时导入集合与导出集合可以不同。在对端的两个地址族分别执行 `undo vpn-target 65000:50081 import-extcommunity`，统一提交后，65000:602 仍匹配远端路由，路由和业务保留。实测对应查询和探测摘要为：

```text
Destinations : 1         Routes : 1
1 packets transmitted, 1 received, 0% packet loss
```

再从两个地址族都移除 65000:602 的导入配置，只留下不匹配的 65000:603 后，远端前缀从租户表撤销：

```text
Destinations : 0         Routes : 0
```

全局 EVPN 表仍可能保留该前缀，表示邻居仍在通告；它不等于已导入本租户。恢复任一匹配的导入 RT 并提交，才重新导入。完成练习后，在两端撤销新加的 65000:602、65000:603，保留原有 65000:50081，查询双栈路由及业务后 `save`。

## 删除单个 BGP 租户地址族

`undo ipv4-family vpn-instance NAME` 或 IPv6 对应命令会要求确认，并删除该 BGP 地址族的网络、路由引入、策略及 EVPN 通告。另一个地址族和 VPN-instance 本身保留。实测 IPv4 地址族删除后，远端 IPv4 Type-5 撤销，IPv6 路由及双向业务继续可用；反向删除 IPv6 地址族时 IPv4 继续可用。

恢复时需要重新配置被删除的地址族内容，例如 `import-route direct` 和 `advertise l2vpn evpn`；仅重新进入视图不能恢复已经删除的配置。恢复后分别检查 IPv4、IPv6，不能用仍工作的另一族替代验收。
