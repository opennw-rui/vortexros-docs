# 链路聚合

使用 Eth-Trunk 把多个物理接口组成一个逻辑接口。

[命令参考](reference/link-aggregation.md) · [配置案例](../examples/lacp.md)

## 工作原理与链路规划

链路聚合把多个物理成员组成一个逻辑 Eth-Trunk。LACP 按 IEEE 802.1AX 协商成员，业务通常按流散列选择成员，因此单条流不保证获得所有成员带宽之和。

两端应采用兼容的聚合模式、成员速率和业务 VLAN 配置。上层 IP、VLAN 或策略应按聚合接口的配置约束使用，不把成员端口当作完全独立的业务接口。增加成员也不意味着旧流量会均匀重分配。

适合链路冗余和多流负载分担。验证成员选中状态、聚合接口状态、多条业务流及单成员故障恢复；仅聚合接口 Up 不能证明所有成员都在转发。

## 配置与验证

聚合接口默认L3，支持手工聚合（manual）和静态 LACP（lacp-static）；成员必须是物理接口并满足兼容属性。加入后，成员不再允许独立配置L2/L3参数，聚合无关的ACL/QoS绑定按能力保留。

```text
interface Eth-Trunk 10
 mode lacp-static
 trunkport Ethernet 1 to Ethernet 2
 mtu 9000
 ip address 198.51.100.1 255.255.255.0
```

```text
display eth-trunk 10
display interface Eth-Trunk 10
```

手工聚合不交换 LACP 协商报文，两端必须使用一致的链路连接和聚合方式。静态 LACP 则要求成员完成协商并进入 Selected 状态。

只调整成员时，其他未变化的成员继续保留。切换聚合模式会重建聚合接口，期间业务会短暂中断；不能直接在仍有成员的聚合上改变模式。

删除单个成员或整个聚合接口：

```text
interface Eth-Trunk 10
 undo trunkport Ethernet 2
#
undo interface Eth-Trunk 10
```

CLI 操作：

```text
commit
```

成员口退出聚合后，才可重新配置其独立的二层/三层属性。


## 切换模式

在同一 Candidate 中先移出成员，再改模式并重新加入，最后统一提交。例如将两个成员的聚合改为手工模式：

~~~text
interface Eth-Trunk 10
 undo trunkport Ethernet 1 to Ethernet 2
 mode manual
 trunkport Ethernet 1 to Ethernet 2
#
commit
display eth-trunk 10
~~~

`undo mode` 同样恢复默认手工模式。默认模式不会写入配置。两端应协调切换；一端使用 LACP、另一端使用手工模式不属于本例的可用连接。

成员退出聚合后，控制层自动建立该物理接口自己的三层接管端点，保留其管理 Up/Down 状态；此后可以在同一次提交中绑定 VPN 实例并配置独立 IP。成员仍属于聚合时，不允许在它上面配置独立三层地址。
