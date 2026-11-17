# Hybrid

Hybrid 允许分别指定每个 VLAN 的出方向标签行为，适合在同一端口同时接入需要标签与不需要标签的业务。

* `tagged`：出方向保留或添加该 VLAN 的外层标签。
* `untagged`：出方向不携带该 VLAN 的外层标签。
* PVID：只决定无标签和 VID 0 报文的入方向归属，**不决定出方向是否带标签**。
* 同一 VLAN 不能同时属于 tagged 与 untagged 列表。切换前先撤销原列表中的该 VLAN。

缺省 PVID 为 1，缺省 VLAN 1 为 untagged。PVID 必须也在 tagged 或 untagged 成员列表中，无标签报文才可进入对应业务。业务 VLAN 范围为 1–4094。

## 配置

Ethernet0 的 VLAN 100 作为无标签业务，VLAN 200 携带标签；对端端口配置相同的 VLAN 与标签行为。

```text
system-view
enable switch
vlan batch 100 200
interface Ethernet 0
 portswitch
 port link-type hybrid
 undo port hybrid untagged vlan 1
 port hybrid pvid vlan 100
 port hybrid untagged vlan 100
 port hybrid tagged vlan 200
#
commit
```

VLAN 100 的终端报文可以不带标签；VLAN 200 的对端必须使用标签。也可以将 PVID 100 配成 tagged，此时无标签报文仍归入 VLAN 100，但出方向添加 VLAN 100 标签，配置对端时应注意这一差异。

## 验证

```text
display vlan 100
display vlan 200
display mac-address
display current-configuration interface Ethernet 0
```

VLAN 100 应显示 UT，VLAN 200 应显示 TG。分别验证两种业务的双向流量，并使用未允许的 VLAN 作为不连通对照。改变 tagged/untagged 行为会影响对端接收，可能造成现有会话中断。

## 实际显示

以下为对应端口组合的实际查询节选：

```text
VID  Type    Status  MAC-LRN  Description      Ports
----------------------------------------------------------------------------
100  common  enable  enable   VLAN 100         UT:Ethernet0(U)  Ethernet1(U)
200  common  enable  enable   VLAN 200         TG:Ethernet0(U)  Ethernet1(U)
```

## 撤销

```text
system-view
interface Ethernet 0
 undo port hybrid tagged vlan 200
 undo port hybrid untagged vlan 100
 undo port hybrid pvid vlan
#
commit
```

PVID 恢复为 1，但不会恢复已删除的 untagged VLAN 1；需恢复默认成员时执行 `port hybrid untagged vlan 1`。恢复为三层接口使用 `undo portswitch`。配置完成后可执行 `save` 保存启动配置。

[交换端口](ports.md) · [命令参考](../reference/vlan.md)
