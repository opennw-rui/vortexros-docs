# 多 VNI 多归属

## 拓扑与前提

先完成 [All-Active 案例](all-active.md)：CE1 双接入 P1/P2，P3 接 CE2，VLAN/BD460、VNI50460 承载未打标签的第一项业务。本页在同一 ESI 上增加带 VLAN461 标签的第二项业务。两项业务使用独立 VNI 与 RT，保留原有 underlay 和 BGP EVPN 邻居。

~~~text
CE1 Eth-Trunk1       P1/P2 Eth-Trunk11       P3 Ethernet1       CE2 Ethernet0
未打标签 192.0.2.12   VLAN460 / VNI50460     PVID460            192.0.2.3
VLAN461  192.0.3.12   VLAN461 / VNI50461     VLAN461            192.0.3.3
同一 ESI：0000.1111.2222.1111.1111
~~~

本页给出对已完成基础案例的完整增量配置；不是跳过 underlay、RT 或 EVPN 邻居准备的独立空白设备配置。

## CE1 与 CE2

CE1 新增三层聚合子接口：

~~~text
system-view
~~~

配置清单：

~~~text
interface Eth-Trunk1.461
 vlan-type dot1q 461
 ip address 192.0.3.12 255.255.255.0
#
~~~

CLI 操作：

~~~text
commit
~~~

CE2 新增对应的三层子接口：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0.461
 vlan-type dot1q 461
 ip address 192.0.3.3 255.255.255.0
#
~~~

CLI 操作：

~~~text
commit
~~~

原父接口上的192.0.2.0/24业务继续不带标签。不要给同一个子接口再配置二层交换成员关系。

## P1

~~~text
system-view
~~~

配置清单：

~~~text
vlan batch 461
bridge-domain 461
 l2 binding vlan 461
 vxlan vni 50461
 evpn
  route-distinguisher 65000:1461
  vpn-target 65000:50461 export-extcommunity
  vpn-target 65000:50461 import-extcommunity
#
interface Eth-Trunk 11
 port trunk allow-pass vlan 461
#
interface Nve1
 vni 50461 head-end peer-list protocol bgp
#
~~~

CLI 操作：

~~~text
commit
~~~

## P2

~~~text
system-view
~~~

配置清单：

~~~text
vlan batch 461
bridge-domain 461
 l2 binding vlan 461
 vxlan vni 50461
 evpn
  route-distinguisher 65000:2461
  vpn-target 65000:50461 export-extcommunity
  vpn-target 65000:50461 import-extcommunity
#
interface Eth-Trunk 11
 port trunk allow-pass vlan 461
#
interface Nve1
 vni 50461 head-end peer-list protocol bgp
#
~~~

CLI 操作：

~~~text
commit
~~~

## P3

把原接入口改为trunk，保留PVID460：

~~~text
system-view
~~~

配置清单：

~~~text
vlan batch 461
bridge-domain 461
 l2 binding vlan 461
 vxlan vni 50461
 evpn
  route-distinguisher 65000:3461
  vpn-target 65000:50461 export-extcommunity
  vpn-target 65000:50461 import-extcommunity
#
interface Ethernet1
 port link-type trunk
 port trunk allow-pass vlan 460 461
 port trunk pvid vlan 460
#
interface Nve1
 vni 50461 head-end peer-list protocol bgp
#
~~~

CLI 操作：

~~~text
commit
~~~

allow-pass 在现有列表上增加VLAN；不得用清空列表操作代替新增。三个PE的VNI、RT相同，RD各不相同。

## 查询与业务

~~~text
display bgp evpn all routing-table
display mac-address bridge-domain 460
display mac-address bridge-domain 461
display vxlan tunnel
display health
~~~

P3的实际MAC显示摘录，接口按拓扑编号整理，下一跳组编号随运行变化：

~~~text
MAC Address       VLAN/VSI/BD       Learned-From                    Type
0200-0000-1212    -/-/461           evpn-nhg-50461-536870913        static
~~~

第二业务的客户MAC通过VNI50461指向ES下一跳组；第一业务仍通过VNI50460。两项业务的实际探测分别为：

~~~text
ping -a 192.0.3.12 -c 3 192.0.3.3
3 packets transmitted, 3 received, 0% packet loss

ping -a 192.0.2.12 -c 3 192.0.2.3
3 packets transmitted, 3 received, 0% packet loss
~~~

这些结果验证两个VNI在同一ESI上共同运行，不是带宽、负载分担比例或任意多租户规模保证。

## 独立撤销

先在P3停止第二VNI：

~~~text
system-view
~~~

配置清单：

~~~text
interface Nve1
 undo vni 50461
#
~~~

CLI 操作：

~~~text
commit
~~~

实际探测第二业务0/2，第一业务2/2，确认不会顺带撤销VNI50460。之后在P1/P2也撤销Nve1的VNI50461。若需要恢复第二业务，重新配置该VNI并提交。

完整移除第二业务时，再在三台PE删除bridge-domain461及允许VLAN461，并删除VLAN461；按CLI确认提示确认删除：

~~~text
system-view
~~~

配置清单：

~~~text
undo bridge-domain 461
interface Eth-Trunk 11
 undo port trunk allow-pass vlan 461
#
undo vlan 461
~~~

CLI 操作：

~~~text
commit
~~~

P3对应接口为Ethernet1，不是Eth-Trunk11。最后在CE1/CE2删除各自的.461子接口。保留VLAN460、VNI50460及共用的Nve1和BGP邻居。验证剩余业务后保存各设备配置。

[广播和分割水平验证](../../operator/evpn/multihoming.md) · [三层子接口](../../operator/subinterfaces-l3.md)
