# LACP 聚合

两根链路组成一个 LACP 聚合，承载一个无标签 VLAN 和一个带标签 VLAN。成员全部不可用时，依赖聚合的 Vlanif 自动 Down；恢复一个有效成员后自动 Up，不需要手动重建 Vlanif。

## 拓扑与前提

```text
P1 host-p1b1 ---------------- host-p2b1 P2
   host-p1b2 ---------------- host-p2b2
       Eth-Trunk10               Eth-Trunk10
       native VLAN 400           native VLAN 400
       tagged VLAN 401           tagged VLAN 401

Vlanif400: 198.18.104.1/30 ---- 198.18.104.2/30
Vlanif401: 198.18.105.1/30 ---- 198.18.105.2/30
```

本例使用开发服务器隔离拓扑中实际的 AF_PACKET 接口名。物理设备应替换成对应的 Ethernet 接口。成员口必须已存在，且没有独立 IP、其他聚合归属或冲突的二层配置；两端链路与 VLAN 必须对应。

成员只承担聚合传输，三层地址放在 Vlanif 上。此例会改变端口的转发归属，不能直接套用到当前管理链路。

## P1 配置

```text
system-view
enable switch
vlan batch 400 401
interface Eth-Trunk 10
 mode lacp-static
 portswitch
 port link-type trunk
 port trunk pvid vlan 400
 port trunk allow-pass vlan 400 401
 quit
interface host-p1b1
 eth-trunk 10
 quit
interface host-p1b2
 eth-trunk 10
 quit
interface Vlanif 400
 ip address 198.18.104.1 255.255.255.252
 quit
interface Vlanif 401
 ip address 198.18.105.1 255.255.255.252
 quit
commit
save
```

## P2 配置

```text
system-view
enable switch
vlan batch 400 401
interface Eth-Trunk 10
 mode lacp-static
 portswitch
 port link-type trunk
 port trunk pvid vlan 400
 port trunk allow-pass vlan 400 401
 quit
interface host-p2b1
 eth-trunk 10
 quit
interface host-p2b2
 eth-trunk 10
 quit
interface Vlanif 400
 ip address 198.18.104.2 255.255.255.252
 quit
interface Vlanif 401
 ip address 198.18.105.2 255.255.255.252
 quit
commit
save
```

`save` 按提示确认。PVID 400 选择无标签流量所属 VLAN；允许列表决定哪些 VLAN 可以通过。缺省允许的 VLAN 1 若不需要，应显式撤销其允许关系。

## 验证

在 P1 执行：

```text
display eth-trunk 10
display interface brief
ping -c 3 198.18.104.2
ping -c 3 198.18.105.2
```

已有功能验收在 Ubuntu 26.04.1 QEMU 的两个独立 VPP 节点上通过真实交互 CLI 验证。以下摘取实际输出，省略其他接口：

```text
LAG ID: 10                  WorkingMode: STATIC
System Priority: 65535      System ID: 02fe-aa2f-6a16
Operate status: up          Number Of Up Port In Trunk: 2

ActorPortName          Status   PortPri PortNo PortKey PortState Weight
host-p1b1              Selected 255     1      19      00111111  1
host-p1b2              Selected 255     2      19      00111111  1
```

系统 ID、端口号、Key 可能在重建后变化，应以实际输出为准。`Selected` 应与链路 Up、LACP collecting/distributing 状态一致；只看管理状态 Up 不能证明成员已参加转发。

### 成员全部关闭与恢复

在 P1 的专用实验成员口上执行：

```text
interface host-p1b1
 shutdown
 quit
interface host-p1b2
 shutdown
 quit
commit
display interface brief
```

实际状态：

```text
Interface               PHY    Protocol
Eth-Trunk10             down   down
Vlanif400               down   down
Vlanif401               down   down
host-p1b1               *down  down
host-p1b2               *down  down
```

恢复一个成员：

```text
interface host-p1b1
 undo shutdown
 quit
commit
display interface brief
ping -c 3 198.18.105.2
```

实际结果：

```text
Eth-Trunk10             up     up
Vlanif400               up     up
Vlanif401               up     up
host-p1b1               up     up
host-p1b2               *down  down

3 packets transmitted, 3 received, 0% packet loss
```

随后恢复 `host-p1b2` 并提交，实际活动成员重新变为 2。这里验证的是通过真实 CLI 控制成员管理状态的依赖收敛，不能把它称作物理拔线或硬件线速测试。

## 调整与撤销

有成员时直接切换聚合模式会被拒绝。应在同一 Candidate 中先撤销成员归属、调整模式，再重新加入成员并提交；本轮对 manual 与 lacp-static 的同次编辑切换已做真实 CLI 验证。

删除此专用案例前先迁移依赖 Vlanif 的路由与策略，再撤销 Vlanif、成员归属和聚合。成员撤销的入口是接口视图中的 `undo eth-trunk`。删除接口的入口是系统视图中的 `undo interface`，按删除提示确认。不要为了撤销本例而关闭其他业务仍在使用的全局交换功能。

[链路聚合](../operator/link-aggregation.md) · [VLAN 网关](vlan-gateway.md)
