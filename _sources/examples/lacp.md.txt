# LACP 聚合

两根链路组成一个 LACP 聚合，承载一个无标签 VLAN 和一个带标签 VLAN。成员全部不可用时，依赖聚合的 Vlanif 自动 Down；恢复一个有效成员后自动 Up，不需要手动重建 Vlanif。

## 拓扑与前提

```text
P1 Ethernet0 ---------------- Ethernet0 P2
   Ethernet1 ---------------- Ethernet1
       Eth-Trunk10               Eth-Trunk10
       native VLAN 400           native VLAN 400
       tagged VLAN 401           tagged VLAN 401

Vlanif400: 198.18.104.1/30 ---- 198.18.104.2/30
Vlanif401: 198.18.105.1/30 ---- 198.18.105.2/30
```

两端各使用 Ethernet0、Ethernet1 作为聚合成员。成员不能有独立 IP、其他聚合归属或冲突的二层配置，链路和 VLAN 必须对应。

成员只承担聚合传输，三层地址放在 Vlanif 上。此例会改变端口的转发归属，不能直接套用到当前管理链路。

## P1 配置

```text
system-view
```

配置清单：

```text
enable switch
vlan batch 400 401
interface Eth-Trunk 10
 mode lacp-static
 portswitch
 port link-type trunk
 port trunk pvid vlan 400
 port trunk allow-pass vlan 400 401
#
interface Ethernet0
 eth-trunk 10
#
interface Ethernet1
 eth-trunk 10
#
interface Vlanif 400
 ip address 198.18.104.1 255.255.255.252
#
interface Vlanif 401
 ip address 198.18.105.1 255.255.255.252
#
```

CLI 操作：

```text
commit
save
```

## P2 配置

```text
system-view
```

配置清单：

```text
enable switch
vlan batch 400 401
interface Eth-Trunk 10
 mode lacp-static
 portswitch
 port link-type trunk
 port trunk pvid vlan 400
 port trunk allow-pass vlan 400 401
#
interface Ethernet0
 eth-trunk 10
#
interface Ethernet1
 eth-trunk 10
#
interface Vlanif 400
 ip address 198.18.104.2 255.255.255.252
#
interface Vlanif 401
 ip address 198.18.105.2 255.255.255.252
#
```

CLI 操作：

```text
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

以下为相关接口的示例输出：

```text
LAG ID: 10                  WorkingMode: STATIC
System Priority: 65535      System ID: 02fe-aa2f-6a16
Operate status: up          Number Of Up Port In Trunk: 2

ActorPortName          Status   PortPri PortNo PortKey PortState Weight
Ethernet0              Selected 255     1      19      00111111  1
Ethernet1              Selected 255     2      19      00111111  1
```

系统 ID、端口号、Key 可能在重建后变化，应以示例输出为准。`Selected` 应与链路 Up、LACP collecting/distributing 状态一致；只看管理状态 Up 不能证明成员已参加转发。

### 成员全部关闭与恢复

在 P1 的专用示例成员口上执行：

```text
interface Ethernet0
 shutdown
#
interface Ethernet1
 shutdown
#
```

CLI 操作：

```text
commit
display interface brief
```

实际状态：

```text
Interface               PHY    Protocol
Eth-Trunk10             down   down
Vlanif400               down   down
Vlanif401               down   down
Ethernet0               *down  down
Ethernet1               *down  down
```

恢复一个成员：

```text
interface Ethernet0
 undo shutdown
#
```

CLI 操作：

```text
commit
display interface brief
ping -c 3 198.18.105.2
```

实际结果：

```text
Eth-Trunk10             up     up
Vlanif400               up     up
Vlanif401               up     up
Ethernet0               up     up
Ethernet1               *down  down

3 packets transmitted, 3 received, 0% packet loss
```

恢复 Ethernet1 并提交后，活动成员应回到 2。此步骤检查成员管理状态；物理断链时还应核对双方实际载波状态。

## 调整与撤销

有成员时不能直接切换聚合模式。应在同一 Candidate 中先撤销成员归属、调整模式、重新加入成员，再统一提交。

删除此专用案例前先迁移依赖 Vlanif 的路由与策略，再撤销 Vlanif、成员归属和聚合。成员撤销的入口是接口视图中的 `undo eth-trunk`。删除接口的入口是系统视图中的 `undo interface`，按删除提示确认。不要为了撤销本例而关闭其他业务仍在使用的全局交换功能。

[链路聚合](../operator/link-aggregation.md) · [VLAN 网关](vlan-gateway.md)
