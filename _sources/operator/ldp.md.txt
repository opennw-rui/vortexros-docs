# MPLS 与 LDP

使用 LDP 在 IPv4 核心网分发 MPLS 传输标签。

[命令参考](reference/mpls.md)

## 使用前提

1. 先为设备配置稳定的 IPv4 LSR ID，通常使用 LoopBack 地址。
2. 全局启用 MPLS 后，再启用 LDP。
3. 在参与 MPLS 转发的三层接口上分别启用 MPLS 和 LDP。
4. 底层 IPv4 IGP 必须先使各节点的 LSR ID 和 LDP transport address 可达。

MPLS 只能用于三层接口。配置了 `portswitch` 的二层接口不能启用 MPLS。

## 基本 LDP 配置

```text
system-view
mpls lsr-id 10.0.0.1
mpls
mpls ldp

interface LoopBack 0
 ip address 10.0.0.1 255.255.255.255
 quit

interface Ethernet 1
 ip address 192.0.2.1 255.255.255.252
 mpls
 mpls ldp
 quit
commit
save
```

`mpls` 打开接口 MPLS 转发能力；`mpls ldp` 使该接口参与 LDP 邻居发现。
两者是独立配置，系统不会根据 LDP 配置猜测接口转发身份。

## TTL 模式

缺省使用 uniform 模式，IP TTL 会传播到 MPLS 标签栈：

```text
ttl propagate
```

如需隐藏 MPLS 核心跳数，可使用 pipe 模式：

```text
undo ttl propagate
```

Linux sysctl 是该模式的权威状态；LCP 将变化同步为 VPP 标签路径的 pipe 或
uniform 属性，不改变 FRR 的协议计算。


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

LDP接口、邻居、标签绑定和Zebra LSP均通过对应daemon的VTY流一次解析并直接输出，
不会把大表完整反序列化后再排版。转发标签仍单独读取VPP LFIB，避免用控制面状态代替
数据面验收。

功能验收必须同时确认 LDP 邻居、标签绑定、Zebra/Linux netlink 状态、VPP MPLS
FIB 和 CE 间实际流量。只看到配置存在不能证明数据面已生效。




## 删除与恢复

撤销顺序建议先关闭接口 LDP，再关闭接口 MPLS，最后关闭全局 LDP/MPLS：

```text
interface Ethernet 1
 undo mpls ldp
 undo mpls
 quit
undo mpls ldp
undo mpls
commit
```

VPP 或 LCP 重启后，LCP 从当前 Linux netlink 状态恢复 MPLS 对象；FRR 保持协议和
标签的唯一权威来源。系统不会从旧 VPP 索引或控制层缓存重建另一份标签状态。

## 排障

1. `display mpls ldp peer` 无邻居：核对接口 LDP、链路地址、IGP 和 transport
   address 可达性。
2. 有 LDP 邻居但 VPP 无标签：依次核对 `display mpls lsp` 与
   `display mpls forwarding-table`，定位 Zebra 到 LCP 的转换边界。
3. VPN 路由无导出标签：核对 RD、VPN-Target、FRR/Zebra 标签池及 VPN 地址族状态。
4. 控制面正常但业务不通：核对内外层标签、VRF 路由、CE 路由及 MTU，并用实际
   CE 到 CE 流量验证。
