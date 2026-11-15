# 进程与接口

## 区域 network 激活

```text
ospf 1 router-id 10.0.0.1
 opaque-capability enable
 area 0.0.0.0
  network 10.0.12.1 0.0.0.0 description P1-P2
```

`opaque-capability enable` 只支持默认 VPN 实例；当前 FRR 后端明确拒绝在命名 VPN 中打开 Opaque LSA 总开关，控制层在提交前拒绝这个组合。它允许交换 Opaque LSA，但不会自行生成 TE 等应用的 LSA。

`network`只能在area视图中输入。提交后，地址匹配的接口开始发送Hello报文；只有两端area、网络类型、认证和计时等条件兼容时才会建立邻居。


## 接口激活

```text
ospf 1 router-id 10.0.0.1
interface Vlanif 12
 ospf enable 1 area 0.0.0.0
 ospf network-type p2p
 ospf cost 10
 ospf dr-priority 100
 ospf timer hello 3
 ospf timer dead 12
 ospf timer retransmit 4
 ospf timer transmit-delay 2
```

同一进程只能选择 `network` 或接口 `ospf enable` 一种激活方式；混用会在命令进入待提交配置前报错。广播网络上的DR优先级范围为0至255，0表示不参与DR/BDR选举。


[OSPF 总览](../ospf.md) · [完整案例](../../examples/ospf.md) · [命令参数](../reference/ospf.md)
