# OSPF 跨区域

本例在 O101 VPN 实例中，经区域边界路由器 R2，将 R3 的外部路由发布给 R1。三台路由器均运行 VortexROS。R2 在 Area0 与 Area101 之间转发；R3 是引入直连路由的 ASBR。

```text
R1 Ethernet0 ── Ethernet0 R2 Ethernet1 ── Ethernet1 R3
   198.18.101.1/30   .2        198.18.201.2/30   .1
        Area101                       Area0
                                      R3 LoopBack248:203.0.113.104/32
```

## 三端配置

在三台设备上先进入系统视图。绑定 VPN 会清除接口原有地址，请在绑定后配置地址。

R1：

```text
ip vpn-instance O101
#
ospf 101 router-id 1.1.1.101 vpn-instance O101
#
interface Ethernet0
 ip binding vpn-instance O101
 ip address 198.18.101.1 30
 ospf enable 101 area 0.0.0.101
#
```

R2：

```text
ip vpn-instance O101
#
ospf 101 router-id 2.2.2.101 vpn-instance O101
#
interface Ethernet0
 ip binding vpn-instance O101
 ip address 198.18.101.2 30
 ospf enable 101 area 0.0.0.101
#
interface Ethernet1
 ip binding vpn-instance O101
 ip address 198.18.201.2 30
 ospf enable 101 area 0.0.0.0
#
```

R3：

```text
ip vpn-instance O101
#
ospf 101 vpn-instance O101
 router-id 3.3.3.101
 import-route direct cost 37 type 2
#
interface Ethernet1
 ip binding vpn-instance O101
 ip address 198.18.201.1 30
 ospf enable 101 area 0.0.0.0
#
interface LoopBack248
 ip binding vpn-instance O101
 ip address 203.0.113.104 32
#
```

每端执行 `commit`。LoopBack248 不直接激活 OSPF；它通过 `import-route direct` 成为外部路由。该命令会引入同一 VPN 中符合条件的其他直连前缀，应确认这是所需的发布范围。广播网络的 DR/BDR 选举和 SPF 需要收敛时间，不能只看到2-Way就判断配置失败。

## 查询和流量

```text
display ospf vpn-instance O101 peer
display ospf vpn-instance O101 abr-asbr
display ospf vpn-instance O101 lsdb asbr
display ospf 101 lsdb 4
display ospf vpn-instance O101 lsdb ase 203.0.113.104
display ip routing-table vpn-instance O101 203.0.113.104 32
ping -vpn-instance O101 -a 198.18.101.1 -c 2 203.0.113.104
```

实际收敛后，两段邻接均为 Full。R1 收到四类 LSA：

```text
Type      : Sum-Asbr
Ls id     : 3.3.3.101
Adv rtr   : 2.2.2.101
Len       : 28
Net mask  : 0.0.0.0
TOS 0  Metric: 10
```

四类 LSA 描述到 ASBR 的区域间可达性；它不是203.0.113.104的外部前缀。该前缀位于五类 LSA 中，R1 实际选中 OSPF Preference150、Cost37，经198.18.101.2转发；指定源地址的双跳探测2/2成功。E2 的外部度量37与到 ASBR 的内部代价分别表达，不应把四类 LSA 的10直接加到显示的E2 Cost37上。`lsdb asbr` 和数字类型4返回同一类结果。

## 撤销

R3 停止外部引入：

```text
ospf 101 vpn-instance O101
 undo import-route direct
#
commit
```

在 R1 核对203.0.113.104/32退出路由表、对应五类 LSA被撤销，以及不再需要的四类 ASBR 可达信息退出。Age3600的冲洗条目可能短暂保留，应同时检查路由表。撤销引入不删除 R3 的 LoopBack 地址，也不关闭两段邻接。

完全拆除此案例时，先撤销各接口的 `ospf enable 101`，再删除只供案例使用的进程、地址与 VPN；不要删除还承载其他业务的接口或实例。需要保存结果时，每端执行 `save`。
