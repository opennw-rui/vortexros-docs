# 链路聚合

使用 Eth-Trunk 把多个物理接口组成一个逻辑接口。

[命令参考](reference/link-aggregation.md) · [配置案例](../examples/lacp.md)

## 配置与验证

聚合接口默认L3，支持static和LACP；成员必须是物理接口并满足兼容属性。加入后，成员不再允许独立配置L2/L3参数，聚合无关的ACL/QoS绑定按能力保留。

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

反复增删成员时只变更相关成员，不重建无变化的聚合接口。

删除单个成员或整个聚合接口：

```text
interface Eth-Trunk 10
 undo trunkport Ethernet 2
undo interface Eth-Trunk 10
commit
```

成员口退出聚合后，才可重新配置其独立的二层/三层属性。
