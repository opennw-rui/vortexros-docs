# MPLS L3VPN

通过 BGP VPN 地址族在 MPLS 核心上传输客户路由。需要先建立 [MPLS 与 LDP](ldp.md) 的底层标签路径。

## 配置

PE 上的 VPN-instance 需要 RD 和导入/导出 VPN-Target，BGP VPN 地址族需要与远端
PE 或 RR 建立 MP-BGP 会话。进入 VPN-instance 地址族时，VortexROS 按产品缺省
语义自动向 FRR 下发 `label vpn export auto`，无需也不允许用户重复配置该后端命令：

```text
bgp 65000
 peer 10.0.0.4 as-number 65000
 peer 10.0.0.4 connect-interface LoopBack 0
 ipv4-family vpnv4
  peer 10.0.0.4 enable
  quit
 ipv4-family vpn-instance CUST-A
  import-route direct
  import-route static
  quit
quit
commit
```

FRR 为 VPN 路由分配导出标签；VortexROS 不创建第二套标签分配器。VPN-instance
下配置的全部 RT 会作为完整列表直接覆盖后端当前值；目标方向变为空时才精确撤销
该方向的旧列表。

VPNv4/VPNv6 传输地址族缺省启用 VPN-Target 过滤，缺省项不写入配置。RR 或
Inter-AS Option B 场景需要保留全部 VPN 路由时可关闭过滤：

```text
bgp 65000
 ipv4-family vpnv4
  undo policy vpn-target
 ipv6-family vpnv6
  undo policy vpn-target
```

再次输入 `policy vpn-target` 恢复缺省过滤行为，恢复后的缺省项不显示。


## 排障

1. `display mpls ldp peer` 无邻居：核对接口 LDP、链路地址、IGP 和 transport
   address 可达性。
2. 有 LDP 邻居但 VPP 无标签：依次核对 `display mpls lsp` 与
   `display mpls forwarding-table`，定位 Zebra 到 LCP 的转换边界。
3. VPN 路由无导出标签：核对 RD、VPN-Target、FRR/Zebra 标签池及 VPN 地址族状态。
4. 控制面正常但业务不通：核对内外层标签、VRF 路由、CE 路由及 MTU，并用实际
   CE 到 CE 流量验证。
