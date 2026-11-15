# All-Active 多归属

## 拓扑与前提

两台接入PE共享一个ESI，CE以静态balance-xor聚合双接入；第三台PE承载远端主机。三台PE全互联IBGP EVPN，无需RR。全部VTEP为IPv4，业务为L2VNI；不把此例当作Single-Active或L3VNI多归属。

~~~text
CE bond0 192.0.2.12/24
  ce1 ── host-p1docmh ── P1(198.19.80.1)
  ce2 ── host-p2docmh ── P2(198.19.80.2) ── P3(198.19.23.3)
                                               host-p3docce ── 192.0.2.3/24
P1—P2: 198.19.80.0/30
P2—P3: 198.19.23.0/24
VLAN/BD460，VNI50460，RT65000:50460
ESI0000.1111.2222.1111.1111
~~~

开发服务器使用QEMU中的隔离netns和VPP AF_PACKET承载；下面的host-*替换为各设备实际由VPP管理的物理接口。先完成数据面启动与接口库存，原生AF_PACKET实验口必须写入该实例启动清单，单次动态创建不能保证VPP重启后存在。生产DPDK设备按[数据面配置](../../operator/dataplane/devices.md)管理。

CE与远端主机是Linux流量端点，不运行VortexROS。CE先创建balance-xor、layer3+4散列的bond，两个接入口都加入bond且Up；MAC固定02:00:00:00:12:12，地址192.0.2.12/24。远端端口Up并配置192.0.2.3/24。链路两端不带标签，以接入PVID460进入业务。

## Linux 流量端点

在CE实验namespace中，ce1/ce2已与两台PE对应物理测试口相连：

~~~bash
ip link add bond0 type bond mode balance-xor xmit_hash_policy layer3+4
ip link set bond0 address 02:00:00:00:12:12
ip link set ce1 master bond0
ip link set ce2 master bond0
ip link set ce1 up
ip link set ce2 up
ip link set bond0 up
ip address add 192.0.2.12/24 dev bond0
~~~

远端主机：

~~~bash
ip link set remote0 up
ip address add 192.0.2.3/24 dev remote0
~~~

端点均在同一二层子网，不需要默认网关。用于注入断链的Linux命令仅作用于CE端相应ce1/ce2，不修改生产管理口。

## P1 完整业务配置

~~~text
system-view
enable switch
evpn-overlay enable
interface host-p1a12
 ip address 198.19.80.1 255.255.255.252
quit
ip route-static 198.19.23.0 255.255.255.0 198.19.80.2
vlan 460
bridge-domain 460
 l2 binding vlan 460
 vxlan vni 50460
 evpn
  route-distinguisher 65000:1460
  vpn-target 65000:50460 export-extcommunity
  vpn-target 65000:50460 import-extcommunity
 quit
quit
interface Eth-Trunk 11
 mode manual
 trunkport host-p1docmh
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 460
 port trunk pvid vlan 460
 esi 0000.1111.2222.1111.1111
quit
interface Nve1
 source 198.19.80.1
 vni 50460 head-end peer-list protocol bgp
quit
bgp 65000
 router-id 1.1.1.1
 peer 198.19.80.2 as-number 65000
 peer 198.19.23.3 as-number 65000
 peer 198.19.23.3 connect-interface host-p1a12
 l2vpn-family evpn
  peer 198.19.80.2 enable
  peer 198.19.23.3 enable
 quit
quit
commit
~~~

## P2 完整业务配置

~~~text
system-view
enable switch
evpn-overlay enable
interface host-p2a12
ip address 198.19.80.2 255.255.255.252
quit
interface host-p2e23
ip address 198.19.23.2 255.255.255.0
quit
vlan 460
bridge-domain 460
 l2 binding vlan 460
 vxlan vni 50460
 evpn
  route-distinguisher 65000:2460
  vpn-target 65000:50460 export-extcommunity
  vpn-target 65000:50460 import-extcommunity
 quit
quit
interface Eth-Trunk 11
 mode manual
 trunkport host-p2docmh
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 460
 port trunk pvid vlan 460
 esi 0000.1111.2222.1111.1111
quit
interface Nve1
 source 198.19.80.2
 vni 50460 head-end peer-list protocol bgp
quit
bgp 65000
 router-id 2.2.2.2
 peer 198.19.80.1 as-number 65000
 peer 198.19.23.3 as-number 65000
 peer 198.19.23.3 connect-interface host-p2a12
 l2vpn-family evpn
  peer 198.19.80.1 enable
  peer 198.19.23.3 enable
 quit
quit
commit
~~~

## P3 完整业务配置

~~~text
system-view
enable switch
evpn-overlay enable
interface host-p3e23
 ip address 198.19.23.3 255.255.255.0
quit
ip route-static 198.19.80.0 255.255.255.252 198.19.23.2
vlan 460
bridge-domain 460
 l2 binding vlan 460
 vxlan vni 50460
 evpn
  route-distinguisher 65000:3460
  vpn-target 65000:50460 export-extcommunity
  vpn-target 65000:50460 import-extcommunity
 quit
quit
interface host-p3docce
 portswitch
 port link-type access
 port default vlan 460
quit
interface Nve1
 source 198.19.23.3
 vni 50460 head-end peer-list protocol bgp
quit
bgp 65000
 router-id 3.3.3.3
 peer 198.19.80.1 as-number 65000
 peer 198.19.80.2 as-number 65000
 l2vpn-family evpn
  peer 198.19.80.1 enable
  peer 198.19.80.2 enable
 quit
quit
commit
~~~

先检查两段underlay与各VTEP互通，再等待EVPN邻居建立。RD各自唯一，ESI/VLAN/VNI/RT在业务两端一致。bridge-domain EVPN视图的RT分别配置import-extcommunity和export-extcommunity，不能使用该视图不支持的both缩写。

## 查询与正常转发

三台PE分别执行：

~~~text
display bgp evpn all routing-table
display vxlan tunnel
display mac-address bridge-domain 460
display health
~~~

P1/P2还执行display interface Eth-Trunk 11。真实CLI中有Type-1、Type-4及MAC/IP通告，P3的CE MAC指向ES下一跳组：

~~~text
0200-0000-1212    -/-/460    evpn-nhg-50460-536870913    static
~~~

后端辅助回读（不是产品额外的CLI）：

~~~text
id 268435458 via 198.19.80.1 scope link proto zebra fdb
id 268435459 via 198.19.80.2 scope link proto zebra fdb
id 536870913 group 268435458/268435459 proto zebra fdb
~~~

在CE和远端主机的Linux终端分别ping对端，正常稳定时两向均3/3。首次建网的0/3及1/3记录保留；这里不宣称无损或测量收敛时间。接口/组ID由运行时分配，不应写成固定配置。

## 单链路失败与恢复

P1：

~~~text
interface host-p1docmh
 shutdown
quit
commit
display interface Eth-Trunk 11
~~~

实验中同步关闭CE的ce1，模拟真实断链两端状态。实际P1聚合Down，P3下一跳组只剩198.19.80.2，CE→远端3/3，P2成为DF。P1执行undo shutdown并提交，CE恢复ce1后，再对P2接入口执行同样的shutdown/undo shutdown（CE对应ce2）。

P2接入口Down时，组只剩198.19.80.1，CE→远端同样3/3；两端恢复后重新出现双成员。该流量测试证明剩余路径可转发，不是所有散列桶、BUM复制或split-horizon穷举。

## 保存和冷恢复

在各节点提交并核对后save，应答Y且等待保存成功，再进行恢复试验。不能把配置尚未保存时的控制进程重启当作Running持久化验收。

VPP重启必须先保证基础承载接口的启动清单完整。初次实验遗漏动态AF_PACKET口，真实reset被接口恢复屏障拒绝，该失败不是转发成功。之后补齐实验启动清单。

补验还确认控制层把exit-vni当作可取反叶子的缺陷，导致冷回放出现no exit-vni。修正VNI上下文解析和退出命令后，在同一后端版本上继续核对恢复；修前函数反例失败、修后定向测试通过。修后保存配置并执行冷启动恢复：P1 ready1/1、零告警；P3重新出现双成员组，CE→远端3/3。P2历史实验混有其他业务及失效运行缓存，最终补验将其替换为只含本例业务的独立实例，未把恢复另一套历史配置的失败写成All-Active成功。最终撤销另列如下。

[多归属功能](../../operator/evpn/multihoming.md) · [EVPN参数](../../operator/reference/evpn.md)

## 撤销和实际结果

P1、P2分别执行以下配置（PE2把端口名换为host-p2docmh）：

~~~text
interface Eth-Trunk 11
 undo esi
quit
interface host-p1docmh
 undo eth-trunk
quit
undo interface Eth-Trunk 11
interface Nve 1
 undo vni 50460
quit
undo bridge-domain 460
undo vlan 460
commit
~~~

P3执行：

~~~text
interface host-p3docce
 undo portswitch
quit
interface Nve 1
 undo vni 50460
quit
undo bridge-domain 460
undo vlan 460
commit
display mac-address bridge-domain 460
display vxlan tunnel
display health
~~~

各节点MAC查询Total items displayed = 0，VXLAN隧道Total: 0。远端PE的ES清单为空，下一跳中不再有本例ES成员组；CE向远端发送3包，0包返回，说明撤销后的业务没有残留可达路径。三台最终健康均ready、in-sync、零告警。underlay IP和共享BGP会话没有随业务撤销。

P3首次撤销失败的记录没有丢弃：在前一步MPLS撤销引起VPP替换后，接口最后一项二层配置被移除，控制层遗漏了现有LCP对的L2→L3更新，二层控制通道返回Invalid value。补齐这条物理口角色转换后，用真实CLI重复原撤销操作，P3代号3/3、健康ready，MAC和隧道均归零。该修正复用现有角色设置API，没有新增回退或忽略错误。

本例结束后按需撤销专用EVPN邻居和实验underlay静态路由；共享邻居不能随本业务删除。save应答Y并等待成功，使撤销也能持久保存。

## 0.29-dev run1最终包核对

最终.run安装后，三节点使用包内daemon和VPP。P1保存本例配置，再通过真实CLI执行reset service vpp，实际版本26.10.7、健康ready2/2、零告警；远端重新出现双成员ES组，CE→远端3/3。该项为VPP数据面重建，不冒称同时重新做了一轮控制进程冷启动或双接入故障测试。

按本页步骤撤销后，三节点MAC均0，P3隧道0、ES组消失、端点0/3；健康分别为3/3、6/6、8/8、零告警，均保存成功。两条接入分别故障的已通过结果沿用前面的实际记录，没有重复运行。
