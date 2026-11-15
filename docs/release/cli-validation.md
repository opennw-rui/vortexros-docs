# CLI 实测记录

本页面向0.29-dev。下表复用已通过且实现未受影响的真实终端、后端及流量证据，完整步骤链接到相应案例；它不是本轮将所有功能重新执行一遍的结果。

实验采用Ubuntu26.04.1 QEMU，VPP/FRR节点使用独立网络命名空间及AF_PACKET；另有virtio PCI接口接管记录。配置和查询来自产品交互终端，流量来自实际端点或抓包。组件原生查询与产品CLI分别标注。

## 功能结果

| 功能 | 本轮实际观察 | 配置与撤销步骤 |
| --- | --- | --- |
| OSPF | public 与 VPN 邻居 Full；E2 摘要及明细有长度、metric 37；路由和实际跨节点探测成功 | [OSPF](../examples/ospf.md) |
| OSPFv3 | 邻居 Full、两族作用域查询正确；默认路由撤销后查询为零，保留外部前缀探测成功；ECMP 参数 4→默认 256，同一进程存活 | [OSPFv3](../examples/ospfv3.md) |
| BGP、路由策略 | Established；MED 123、LocalPref 150、AS-path 65111 65112 与策略一致；策略和邻居详细查询有实际路由 | [BGP](../examples/bgp.md)、[路由策略](../examples/bgp-policy.md) |
| IS-IS | 双族邻接 Up、LSDB/路由有值；在线改变 Level 后实际同步；默认 preference 15 | [IS-IS](../examples/isis.md) |
| RIP/RIPng | 各有 5 条实际路由，接口和统计有值；撤销实例后查询不再存在；默认 preference 100 | [RIP](../examples/rip.md)、[RIPng](../examples/ripng.md) |
| BFD | 实际 Up，默认 1000/1000/3；静态和协议绑定、继承及撤销有对照；撤销后会话为零、协议邻接保留 | [BFD](../examples/bfd.md) |
| VRRP | IPv4、IPv6 组实际 Master，撤销后 Total 0；单节点结果不冒充两台故障切换 | [VRRP](../examples/vrrp.md) |
| 静态路由组 | IPv4/IPv6 手工、文件及 HTTP 来源有实际路由；刷新时一增一删；撤销后前缀消失 | [路由组](../examples/route-group.md) |
| MPLS L3VPN | LDP 邻居 Operational，标签、LSP、VPN 路由和业务探测有值；接口与全局撤销后 LDP 接口及邻居为零 | [MPLS L3VPN](../examples/mpls-l3vpn.md) |
| VLAN、聚合 | trunk/access、允许列表、聚合成员均有实际投影；精确动态 MAC 清除保留静态项，流量后重新学习 | [VLAN](../examples/vlan-gateway.md)、[聚合](../examples/lacp.md) |
| L2/L3 子接口 | dot1q、dot1ad/QinQ 两端配置、转发、父接口 Down/Up 和删除已实际验证 | [L2 子接口](../operator/subinterfaces-l2.md)、[L3 子接口](../operator/subinterfaces-l3.md) |
| 静态 VXLAN、EVPN | L2 远端 MAC 和数据流有值；ESI 撤销保持成员管理状态；bare undo vni 清理实际路由 | [VXLAN](../examples/vxlan.md)、[EVPN](../examples/evpn/l2vpn.md) |
| EVPN L3 双栈 | 独立 tenant、两端无需 VPN transport peers；IPv4/IPv6 双向各 2/2；撤销 Type 5 后远端前缀均为零 | [EVPN L3](../examples/evpn/l3vpn.md) |
| GRE、IP-in-IP | 实际隧道流量及撤销；GRE 显式 default、key 撤销和协议重建有对照 | [GRE](../examples/gre.md)、[IP-in-IP](../examples/ip-in-ip.md) |
| WireGuard、AmneziaWG | 两端配置、握手、双栈流量、保存回放、endpoint/PSK 和撤销；AWG 高级签名、junk 参数按实际版本核对 | [WireGuard](../examples/wireguard.md)、[AmneziaWG](../examples/amneziawg.md) |
| ACL、uRPF | ACL 指定流量 0/3，撤销后 3/3；uRPF strict 拒绝非对称源、loose 接受，双族对照 | [ACL](../examples/acl.md)、[uRPF](../examples/urpf.md) |
| MQC、MSS | PBR 改变实际出口；DSCP 20 抓包 TOS 0x50、撤销回 0；双栈 MSS 按线侧 SYN 核对 | [MQC](../examples/mqc.md)、[MSS](../operator/mss.md) |
| 接口 policer | 原单速率桶下溢复现后修正；100 kbps、3 秒 UDP 实测含初始突发约 168 kbps，丢弃约 83%；撤销后健康恢复 | [QoS](../examples/qos.md) |
| NAT | 接口/地址池 PAT、NO-PAT、静态、DNAT、TWICE-NAT 和回流有实际 HTTP/UDP 对端结果；端口、quota、会话清除和撤销有对照 | [NAT](../examples/nat-pat.md) |
| DHCPv4/v6 | 实际地址、保留地址、租期、DNS/域名；空实例汇总和池名筛选正确；IPv6 中继与 Information-Request 有实际回复 | [DHCPv4](../examples/dhcp.md)、[DHCPv6](../examples/dhcpv6.md)、[中继](../examples/dhcpv6-relay.md) |
| RA、静态 ND、Proxy ARP | 三种 RA 意图和撤销、实际邻居与代理流量；恢复阶段按接口归属处理 | [IPv6 自动配置](../operator/ipv6-autoconfig.md)、[Proxy ARP](../operator/proxy-arp.md) |
| LLDP | 动态接口索引分离后启用成功，独立对端抓到对应 Port ID；撤销后端口不再发布 | [LLDP](../examples/lldp.md) |
| SNMP | 标准查询、64 位字节差、linkDown/linkUp 及 VPN 源接口查询；普通接口编辑期间 master PID 不变 | [SNMP](../operator/snmp.md) |
| 数据面 | 主核 0、worker、队列、描述符保存及实际激活；撤销恢复驱动默认；DPDK→kernel 保留名称/IP，实际探测 2/2 | [数据面](../operator/dataplane.md) |
| Flow Steering | 两个 worker 下实际 active，GRE 命中、handoff/resume 计数递增，探测 4/4；最终 26.10.6 包启用后 GRE 2/2，撤销首次提交成功、列表为空、仍 2/2 | [Flow Steering](../operator/flow-steering.md) |
| 配置与恢复 | Candidate、保存、指定 Saved 重置、Running 清空保留 Saved 校验值；交换启停后的回放修复；VRF 表号身份归一后回放成功且四类探测各 2/2；出厂恢复实际清理受管账号 | [配置管理](../operator/01-cli.md)、[运维](../operator/09-operations.md) |

具体原始输出、配置前提和失败处理以链接章节为准。表中两次或三次成功探测是定向功能证据，不是吞吐、满表容量或长时间可靠性保证。

## 新补验与最终包

[All-Active](../examples/evpn/all-active.md)、[6PE](../examples/mpls/6pe.md)、[静态MAC](../examples/static-mac.md)和[简单QinQ](../examples/qinq.md)已补齐缺少的实际转发和撤销证据。工作树诊断构建与最终统一包的新验收分开记录。

最终包：`vortexros-0.29-dev-run1-amd64.run`，SHA-256：

~~~text
d0ab84f64269ae9fc81aa8db5fced008daf3e5ee0dc8bccc90c2fc4a04949fe0
~~~

控制包0.29~dev+run1、五个VPP包26.10.7+vortexros-vpp、FRR1.7-dev、Kea3.0.3-1+vortexros1。包名与实际安装版本均已核对；同一文件完成下列定向验收。

| 最终包验收 | 实际结果 |
|---|---|
| 预检和组件比较 | Linux主实例只计划更新控制包和五个VPP包，FRR/Kea跳过；安装后同包检查返回所有版本已安装 |
| 故障自动回退 | 事务20261115T112610Z-106657，在validating停止route-zapi，安装器自动恢复原0.29控制包和VPP26.10.6，完成90秒观察并rolled-back；运行返回1为注入故障的预期结果 |
| 正常升级 | 同一.run事务20261115T113010Z-111574完成180秒连续观察并committed，返回0；Linux数据面不变、主VPP服务停止，独立原生服务保持masked |
| 配置和身份 | 两次事务主启动CFG校验值均不变；dpkg文件校验干净；实际CLI、daemon、switchd和linux_nl插件哈希与包内一致；FRR主PID83256保持 |
| 无状态ACL | 最终CLI分别拒绝IPv4/IPv6 permit-reflect，permit/deny可创建、显示，删除后查询对象不存在 |
| EVPN数据面重建 | 保存配置后通过真实CLI reset service vpp，P1运行26.10.7、ready2/2、零告警；远端恢复双成员ES组，CE流量3/3 |
| 6PE | 产品CLI建立LDP和标签邻居，Remote labels为2，实际FIB路径encap mpls2，双向各3/3 |
| 6PE撤销 | 撤销后目标IPv6路由0、LDP邻居0，P2/P3 VPP PID116488/116478均不变；ready、零告警，没有靠重启掩盖原崩溃 |
| 二层角色和业务撤销 | 撤掉ESI、VNI及最后portswitch配置后，MAC/隧道0，ES成员组消失、端点流量0/3；三节点分别ready3/3、6/6、8/8、零告警，均保存成功 |

本轮没有重跑全量CLI、CI、未受影响的AAA/Bash、RIP及其他协议。先前控制进程冷回放、6PE已有network在线启用刷新、静态MAC与QinQ的定向证据沿用；这几项没有重标为最终包重新执行。原异常RIP进程66313仍保留供复核。

软件源码和安装包未推送GitHub、未发布软件Release或部署真机。用户手册独立提交发布。

## 覆盖边界

820条规范命令路径与当前Registry逐项对照。输入文本匹配只用于找遗漏，不是820个独立成功断言；各功能的创建、实际状态、流量和撤销以具体案例为准。参数取值、所有协议组合、精确竞争时序、满表规模、硬件吞吐和长期可靠性没有被穷举。

主Linux实例的包升级/自动回退与隔离VPP节点的功能恢复分别证明，不外推为真机DPDK升级验收。共享实验环境曾出现buffer耗尽及内存限额不足，这些资源前提与产品缺陷分开处理，不据此修改默认值。
