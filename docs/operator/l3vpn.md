# MPLS L3VPN

通过 BGP VPN 地址族在 MPLS 核心上传输客户路由。需要先建立 [MPLS 与 LDP](ldp.md) 的底层标签路径。

[配置案例](../examples/mpls-l3vpn.md)

## 工作原理与标识规划

MPLS L3VPN（RFC 4364）通过 PE 上的独立 VPN 路由表隔离客户网络，再用 MP-BGP 交换带标签的 VPN 路由。P 核心提供标签承载，不需要保存全部客户路由。

RD 区分可能重叠的 VPN 前缀；RT 控制路由导入导出，不能用 RD 相同代替正确的 RT 策略。一项业务可配置多个导入/导出 RT，但应检查是否意外连通原本隔离的租户。

配置顺序围绕底层 IGP/标签承载、PE 间 BGP VPN 地址族、VPN 实例及客户接口展开。先检查标签和 VPN 路由，再从 CE 到 CE 验证双向业务。撤销一端时，远端旧路由及标签也应按协议收敛移除。

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
 #
 ipv4-family vpn-instance CUST-A
  import-route direct
  import-route static
#
```

CLI 操作：

```text
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
 #
 ipv6-family vpnv6
  undo policy vpn-target
```

再次输入 `policy vpn-target` 恢复缺省过滤行为，恢复后的缺省项不显示。


## VPNv6 的源接口前提

同一 IPv4 MP-BGP 会话承载 VPNv6 时，指定的 connect-interface 也应启用 IPv6 并配置可用的 IPv6 地址。例如，给两端 LoopBack0 分别配置全局 IPv6 /128，再在 ipv6-family vpnv6 下启用已有 IPv4 邻居。接口 IPv6 默认关闭，不能只配置 VPNv6 邻居而忽略源接口。

优先使用经 IGP 发布并已获得 LDP 标签路径的 LoopBack /32 建立 MP-BGP。仅有到物理直连接口的 IP 路由，不等于具备可导入 VPN 路由的标签路径。

## 实际验证结果

IPv4 与 IPv6 VPN 表均获得对端 RD65000:292、RT65000:290 的前缀；相应 VRF 路由有效并指向 public-net 的传输下一跳。实际 IPv4、IPv6探测均为3/3；核心侧分别捕获到携带标签145和144的请求。

删除对应地址族的导入 VPN-Target 后，两条业务前缀均从 VRF 路由表消失，IPv4探测不再成功。撤销临时 MP-BGP 传输邻居及RD/RT后，VPNv4/VPNv6表恢复为空。标签由设备分配，示例数字不是固定配置。

该结果确认了带标签的请求方向和业务连通性；未单独强制本例回复方向也使用标签。部署验收应同时核对两个方向的客户路由和核心路径，避免把直接回程误认为双向 MPLS 验证。

## 排障

1. `display mpls ldp peer` 无邻居：核对接口 LDP、链路地址、IGP 和 transport
   address 可达性。
2. 有 LDP 邻居但 VPP 无标签：依次核对 `display mpls lsp` 与
   `display mpls forwarding-table`，定位 Zebra 到 LCP 的转换边界。
3. VPN 路由无导出标签：核对 RD、VPN-Target、FRR/Zebra 标签池及 VPN 地址族状态。
4. BGP在OPEN后返回Cease6/0：承载IPv6地址族时，检查源接口是否已启用IPv6并具备IPv6地址。
5. 控制面正常但业务不通：核对内外层标签、VRF 路由、CE 路由及 MTU，并用实际
   CE 到 CE 流量验证。
