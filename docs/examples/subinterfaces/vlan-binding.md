# VLAN 接入与业务桥域

## 拓扑与作用

三台设备均运行 VortexROS。CE1 发送不带标签的报文，PE1 将接入 VLAN 962 绑定到业务桥域 962，通过二层子接口向 CE2 发送带服务标签的报文。Vbdif 提供本业务的三层地址。

~~~text
CE1 Ethernet0 ── Ethernet0 PE1 Ethernet1.962 ── Ethernet0.963 CE2
198.19.197.2/24             Vbdif962                    Vbdif963
2001:db8:197::2/64          .1 / ::1                    .3 / ::3
      无标签                         802.1ad VLAN 964
~~~

设备上的 VLAN、桥域和子接口编号相互独立。本例 VLAN 与 PE1 桥域恰好同号，CE2 的子接口编号及桥域则使用 963；线上标签由封装命令指定为 964，不能复用本设备已存在的全局 VLAN 962。以下端口均为本例专用，不能覆盖正在使用的地址或 VLAN。

## CE1

进入系统视图后配置：

~~~text
interface Ethernet0
 ip address 198.19.197.2 255.255.255.0
 ipv6 enable
 ipv6 address 2001:db8:197::2 64
#
~~~

执行 commit。

## PE1

~~~text
enable switch
vlan 962
#
bridge-domain 962
 l2 binding vlan 962
#
interface Ethernet0
 portswitch
 port link-type access
 port default vlan 962
#
interface Ethernet1.962 mode l2
 encapsulation dot1ad vid 964
 bridge-domain 962
#
interface Vbdif962
 ip address 198.19.197.1 255.255.255.0
 ipv6 enable
 ipv6 address 2001:db8:197::1 64
#
~~~

执行 commit。Ethernet1 父口上不能存在会抢占本例标签分类的其他业务。

## CE2

~~~text
enable switch
bridge-domain 963
#
interface Ethernet0.963 mode l2
 encapsulation dot1ad vid 964
 bridge-domain 963
#
interface Vbdif963
 ip address 198.19.197.3 255.255.255.0
 ipv6 enable
 ipv6 address 2001:db8:197::3 64
#
~~~

执行 commit。二层子接口本身不配置 IP，地址属于 Vbdif。

## 查询与实际结果

PE1：

~~~text
display bridge-domain 962
display interface Ethernet1.962
display vlan 962
display mac-address bridge-domain 962
health check
~~~

实测桥域明细中的成员如下；接口名按本例拓扑统一表示：

~~~text
bridge-domain 962
  bvi: Vbdif962
  ports:
    Vbdif962        shg 0
    Ethernet0       shg 0
    Ethernet1.962   shg 0
~~~

接口显示 Encapsulation is dot1ad, VLAN 964，PHY 和 Protocol 均为 Up。链路报文的标签类型为 0x88a8、VLAN 964。此组合已验证全局 VLAN 962 与显式外层 VID 964 可同时提交；Vbdif962 到对端 Vbdif963 的 IPv4、IPv6 探测均为 3 发 3 收。桥域编号、子接口后缀和线上标签不能混为同一资源。

CE1：

~~~text
ping -c 3 198.19.197.3
ping ipv6 -c 3 2001:db8:197::3
~~~

实际两项结果均为：

~~~text
3 packets transmitted, 3 received, 0% packet loss
~~~

首次访问或替换对端接口后可能需要重新解析地址。若 IP 地址移到了另一接口，核对新的 MAC 映射；旧邻居项仍指向原接口时，可使用 reset ip arp interface Ethernet0 清除本口动态 ARP，并重新检查。此命令要求确认，不会删除接口地址。

## QinQ 变体

两端分别在已有二层子接口视图中，将封装改为：

~~~text
encapsulation qinq vid 964 ce-vid 963
~~~

提交会重新建立该子接口的封装，业务可能短暂中断。两端必须同时匹配外标签 964、内标签 963。该命令的外、内标签均为 0x8100；不要与上述单层 0x88a8 封装混用。

实测接口显示：

~~~text
Encapsulation is QinQ, Outer VLAN 964, Inner VLAN 963
~~~

报文中存在两层 0x8100 标签；完成邻居解析后，IPv4 探测为 3 发 3 收，IPv6 为 2 发 2 收。封装变更后的首次探测也记录过地址解析期间的丢包，不能把接口 Up 单独视为流量恢复证明。

## 绑定撤销与故障影响

PE1 在 bridge-domain 962 视图下执行 undo l2 binding vlan，然后提交：

- 接入口 Ethernet0 回到普通 VLAN 962，不再属于业务桥域。
- 显式配置的 Ethernet1.962 仍属于业务桥域 962，原封装保留。
- CE1 到 CE2 的本例业务中断，实测 IPv4 为 2 发 0 收。
- CE2 到 PE1 Vbdif962 的独立链路仍可用，IPv4 和 IPv6 均为 2 发 2 收。

重新配置 l2 binding vlan 962 并提交可恢复接入。PE1 的 Ethernet1 关闭时，其子接口自动 Down；只要 Ethernet0 仍为有效成员，Vbdif962 仍可 Up。Vbdif 的状态应结合全部成员判断。

## 完整撤销

先撤销本例额外的路由、静态 MAC 或策略引用，再按设备执行。

PE1：

~~~text
interface Ethernet0
 undo portswitch
#
undo interface Ethernet1.962
undo interface Vbdif962
undo bridge-domain 962
undo vlan 962
~~~

CE2：

~~~text
undo interface Ethernet0.963
undo interface Vbdif963
undo bridge-domain 963
~~~

CE1：

~~~text
interface Ethernet0
 undo ip address
 undo ipv6 address 2001:db8:197::2 64
 undo ipv6 enable
#
~~~

各端 commit 后，查询本例接口、桥域、MAC 表与直连路由，确认专用对象消失；需要保持撤销结果时再 save。仅撤销 encapsulation 而保留子接口会产生不完整配置，提交会被拒绝，不能作为删除业务的方法。
