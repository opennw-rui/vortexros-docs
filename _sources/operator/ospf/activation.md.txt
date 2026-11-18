# 进程与接口

## 区域 network 激活

```text
ospf 1 router-id 10.0.0.1
 opaque-capability enable
 area 0.0.0.0
  network 10.0.12.1 0.0.0.0 description P1-P2
```

opaque-capability enable 仅支持默认 VPN 实例，命名 VPN 不支持此开关。开启后允许交换 Opaque LSA。本版本未提供 MPLS-TE 等扩展应用的本地发布配置；该开关本身不会产生一条 TE 通告。

`network`只能在area视图中输入。提交后，地址匹配的接口开始发送Hello报文；只有两端area、网络类型、认证和计时等条件兼容时才会建立邻居。


## 接口激活

```text
ospf 1 router-id 10.0.0.1
#
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


## 进程参数与实际结果

```text
ospf 1
 auto-cost reference-bandwidth 50000
 maximum-paths 2
 log-adjacency-changes detail
 opaque-capability enable
#
```

参考带宽单位为 Mbit/s，同一 OSPF 域应一致配置。显式接口 ospf cost 优先于自动计算。maximum-paths 限制可安装的等价路径数量；它不保证拓扑中一定存在对应数量的等价路径。日志开关记录邻接变化，不改变邻居建立条件。

实际接口原 Cost 为 10，配置上面的参考带宽后变为 5；display ospf 显示 Maximum paths: 2。撤销相应参数并提交后，接口 Cost 恢复为 10，到 OSPF 学习目标的探测为 2/2。该 Cost 对应具体接口带宽，不能作为其他型号或链路的固定值。

查询与撤销：

```text
display ospf
display ospf interface Ethernet0
display ospf routing
```

在 OSPF 进程视图撤销，再提交：

```text
undo auto-cost reference-bandwidth
undo maximum-paths
undo log-adjacency-changes
undo opaque-capability enable
commit
```

撤销恢复产品所用后端的默认行为。Opaque 开关不会代替 Opaque LSA 应用配置，不能仅因当前数据库没有该类 LSA 就认定开关未生效。


## 接口定时器

在两端相连的接口使用一致的 Hello/Dead 值。以下将 Hello/Dead 改为 2/8 秒，LSA 重传间隔改为 3 秒，传输延迟设为 2 秒：

~~~text
interface Ethernet0
 ospf timer hello 2
 ospf timer dead 8
 ospf timer retransmit 3
 ospf timer transmit-delay 2
#
~~~

commit 后通过 display ospf 1 interface 检查 Hello、Dead 和 Retransmit，通过 display ospf 1 peer 检查 Full 和剩余 Dead 时间。本例接口显示 Hello 2s、Dead 8s、Retransmit 3s，邻居为 Full，目标探测 2/2。transmit-delay 是通告 LSA 时计入的估计传输延迟，不是延迟普通业务报文的排队定时器。

恢复时在同一接口执行四条对应的 undo ospf timer 命令并提交；默认值为 Hello 10 秒、Dead 40 秒、Retransmit 5 秒和 Transmit-delay 1 秒。两端协调修改，避免暂时不匹配使邻居中断。

## 接口属性与静默

`ospf cost` 是本端接口的出方向开销。一次实际验证中，接口 Cost 从 10 改为 37，对端另一条开销为 10 的路由总开销相应从 20 变为 47；`undo ospf cost` 后恢复为 20。显式开销不等同于接口带宽。

`ospf network-type` 支持 `broadcast`、`p2p`、`p2mp` 和 `nbma`。网络类型决定邻居发现和 DR/BDR 行为，不改变业务接口的三层地址。修改可能使邻居重新建立，应核对两端类型及 Hello/Dead 条件。实际验证分别显示 `POINTOPOINT`、`POINTOMULTIPOINT`、`BROADCAST` 和 `NBMA`；广播网络中 Priority 0 的设备为 DROther，对端为 DR。恢复类型和优先级分别使用 `undo ospf network-type`、`undo ospf dr-priority`。

NBMA 不等同于广播自动发现。当前接口类型配置不提供静态 OSPF 邻居命令；若网络需要两端均以纯 NBMA 静态邻居建立，应先确认支持范围，不能只设置类型就期待自动发现。本次 NBMA 验证使用仍能发起邻居发现的广播对端，邻居 Full、路由存在且目标探测成功；不能据此外推任意 NBMA 拓扑都能建立。

接口下的 `ospf passive` 与进程下的 `silent-interface Ethernet0` 操作同一静默属性。静默停止 OSPF Hello，不关闭业务接口，也不立即删除所有已学习路由；已有邻居可保留到 Dead 定时器到期。实际默认 40 秒的验证中，静默生效后邻居最终消失，相关 OSPF 路由和动态 BFD 会话撤销，直连路由保留；`undo ospf passive` 或 `undo silent-interface Ethernet0` 后重新建立 Full 并恢复路由。提交后瞬间仍看到旧邻居不等于配置未生效。

## BFD 与 OSPF

```text
interface Ethernet0
 ospf bfd enable
 ospf bfd min-tx-interval 200 min-rx-interval 300 detect-multiplier 4
#
```

BFD 参数单位为毫秒。两端按各自接收、发送要求协商，实际发送间隔可能有协议允许的抖动，不能把要求间隔当成每一包的精确定时。上述实际会话为 Up，配置接收 300、发送 200、检测倍数 4。分别撤销三个定时参数并保持 BFD 开启后，恢复产品默认的接收/发送 1000 毫秒、检测 3 次。`undo ospf bfd enable` 取消 OSPF 的 BFD 绑定，已有 OSPF Hello 机制继续工作；动态会话在不再被协议使用后撤销。

验证命令：

```text
display ospf interface Ethernet0
display ospf peer
display ospf routing
display bfd session all
```

VPN 实例中使用对应的 `display ospf vpn-instance 名称 ...` 形式，BFD 表中的 VPN 和接口应与目标邻居一致。停止某个邻居或撤销 BFD 绑定，不应误把其他 VPN 仍在使用的会话当成残留。
