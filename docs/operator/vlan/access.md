# Access

Access 用于连接一个 VLAN 的终端。缺省为 VLAN 1；配置其他 VLAN 前应先创建该 VLAN。

| 收到的报文 | 处理 |
|---|---|
| 无标签或优先级标签 VID 0 | 归入端口 PVID |
| 单层标签、VID 等于 PVID | 接收并去掉标签 |
| 其他 VID 或叠加标签 | 不作为该 Access VLAN 的业务接收 |

出方向不携带该 VLAN 的标签。VID 0 不建立独立 VLAN，PCP/DEI 在后续需要添加标签时保留。普通路由接口不会因为配置了其他交换端口而变为 Access。

## 配置

Ethernet0 与 Ethernet1 连接同一 VLAN 的两台终端，终端使用同一 IP 网段。

```text
system-view
enable switch
vlan 100
#
interface Ethernet 0
 portswitch
 port link-type access
 port default vlan 100
#
interface Ethernet 1
 portswitch
 port link-type access
 port default vlan 100
#
commit
```

通过 `display vlan 100` 检查两个 UT 成员，使用终端间双向 ping 验证连通性，通过 `display mac-address` 检查终端 MAC 的端口归属。切换端口类型或 VLAN 会改变其广播域，现有流量可能短暂中断。

## 实际显示

以下为对应端口组合的实际查询节选：

```text
VID  Type    Status  MAC-LRN  Description      Ports
----------------------------------------------------------------------------
100  common  enable  enable   VLAN 100         UT:Ethernet0(U)  Ethernet1(U)
```

## 撤销

恢复为三层端口前先撤销依赖该端口的二层业务。以下命令删除交换端口配置，不删除 VLAN 本身。

```text
system-view
interface Ethernet 0
 undo portswitch
#
interface Ethernet 1
 undo portswitch
#
commit
```

[交换端口](ports.md) · [命令参考](../reference/vlan.md)
