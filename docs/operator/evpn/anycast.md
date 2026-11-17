# Anycast 网关


Vbdif 启用 `vxlan anycast-gateway enable` 前必须配置明确的网关 MAC。未配置时，Candidate 会拒绝，Running 保持原配置。

以下在桥域 101/VNI 5010 上增加网关：

```text
interface Vbdif 101
 mac-address 0200-0000-0101
 ip address 192.0.2.254 255.255.255.0
 vxlan anycast-gateway enable
#
```

CLI 操作：

```text
commit
display interface Vbdif101
display bgp evpn all routing-table
```

网关 MAC 应与显式配置一致，BGP 中应出现对应的网关 MAC/IP Type-2 通告。更换网关 MAC 会使客户端旧 ARP/ND 缓存暂时失效，应安排维护窗口，待邻居更新后检查双向流量。

执行 undo vxlan anycast-gateway enable 并提交后，网关通告应撤销。显式 MAC 和接口 IP 属于独立配置，不随该开关删除；双网关部署还需协调两端 MAC、IP 和接入策略。


## 多归属与路由条件

Anycast 网关所在的 Vbdif 必须已配置地址、正确绑定租户 VPN，且对应桥域有可用的本地接入或 VXLAN 路径。仅创建 Vbdif 或启用 Anycast 开关不代表租户路由已经可达；还应确认 EVPN 邻居、远端前缀、VTEP 下一跳及路由器 MAC。

使用对称 IRB 并让客户通过多归属 Ethernet Segment 接入时，同一客户的所有三层转发 PE 都应具备相同租户的 L3VNI 和一致的网关 IP/MAC。不能只在部分 PE 配置三层租户、却让所有 PE 都成为该客户的等价路由下一跳；否则可能出现二层互通、部分三层路径无法转发的情况。先检查每条实际下一跳，再做客户到远端租户前缀及反向流量验证。

## 使用顺序

先按完整案例完成底层、桥域、BGP EVPN 和客户接入。Anycast 缺省关闭，需显式网关 MAC；该页为已有桥域增加网关，不能独立建立完整 EVPN。

[配置案例](../../examples/evpn/anycast.md) · [L2VPN 基础配置](../../examples/evpn/l2vpn.md)
