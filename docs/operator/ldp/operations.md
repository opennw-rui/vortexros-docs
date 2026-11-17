# 会话、标签与撤销

## 查询与验证

```text
display mpls interface
display mpls ldp peer
display mpls ldp interface
display mpls ldp binding
display mpls lsp
display mpls forwarding-table
display bgp vpnv4 all routing-table
display ip routing-table vpn-instance CUST-A
```

- `display mpls ldp ...` 显示 FRR LDP 控制面状态；
- `display mpls lsp` 显示 Zebra 的 MPLS 表；
- `display mpls forwarding-table` 显示 VPP 实际 MPLS FIB。

大型标签表逐项显示，总数见表尾。需要确认标签已用于转发时，查询 display mpls forwarding-table，并检查相应业务是否连通。

检查 LDP 邻居、标签绑定、MPLS 转发表、路由出口及业务连通性。只有邻居 Up 不足以证明标签路径已经可用；以 display mpls forwarding-table 和跨核心业务探测联合确认。


## 删除与恢复

撤销顺序建议先关闭接口 LDP，再关闭接口 MPLS，最后关闭全局 LDP/MPLS：

```text
interface Ethernet 1
 undo mpls ldp
 undo mpls
#
undo mpls ldp
undo mpls
```

CLI 操作：

```text
commit
```

数据面重启后，设备会根据当前 MPLS/LDP 配置和协议状态恢复标签转发。等待 LDP 邻居及标签恢复后，再核对 MPLS 转发表和业务连通性；不需要手工恢复上次运行分配的标签编号。


## 排障

1. `display mpls ldp peer` 无邻居：核对接口 LDP、链路地址、IGP 和 transport
   address 可达性。
2. 有 LDP 邻居但 VPP 无标签：依次核对 `display mpls lsp` 与
   `display mpls forwarding-table`，定位 Zebra 到 LCP 的转换边界。
3. VPN 路由无导出标签：核对 RD、VPN-Target、FRR/Zebra 标签池及 VPN 地址族状态。
4. 控制面正常但业务不通：核对内外层标签、VRF 路由、CE 路由及 MTU，并用实际
   CE 到 CE 流量验证。

[功能目录](../ldp.md) · [命令参数](../reference/mpls.md)

## 标签路径查询示例

三台设备通过OSPF与LDP建立核心后，首台设备到远端LoopBack192.0.2.252/32的绑定与LSP为：

~~~text
AF    Prefix             Local Label  Remote Label  Peer ID        In-Use
ipv4  192.0.2.252/32     30           19            198.19.80.2   yes

In Label  Out Label  Type  Next Hop       Interface  State
30        19         LDP   198.19.80.2    Ethernet0  installed
~~~

以上仅摘取相关条目，接口按业务连接编号为Ethernet0。查询VPP转发表也存在对应路径；发往192.0.2.252的实际三次探测均成功，核心侧捕获到三份标签19报文。设备分配的标签可能不同，应比较本机出标签与下一跳入标签，不要照抄表内数字。
