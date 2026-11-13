# 物理接口、聚合、VLAN、BD 与邻居

## 接口所有权

设备只允许一个转发平面管理物理接口。VPP未启用时，可在CLI中配置Linux能够识别的物理口；VPP接管完成后，只允许配置设备已经识别的业务接口。接管过程中接口配置暂时只读，避免同一接口同时由两套转发平面管理。

VortexROS要求VPP接口名与对应LCP Linux host接口名完全相同。`lcp host`只用于声明同名配对及tap/tun类型，不支持为接口设置别名；名称不同的交互配置会在进入Candidate时被拒绝。LCP接口名最多15字节，只允许字母、数字、`_`、`-`和`.`，且首字符必须是字母或数字；`/`、`:`、空白和其他特殊字符不允许。自动物理LCP也使用相同规则，不会静默截短或生成第二套Linux名称。升级前若旧CFG仍包含LCP别名、超长名称或特殊字符名称，必须先在旧版本中改名并同步更新引用；新版会明确拒绝加载，避免依赖关系被迁移到错误接口。这样接口状态、VRRP、DHCP、地址和统计始终使用同一个产品接口身份，避免把VPP名称误当成Linux名称。

```text
display vpp interface-ownership verbose
display interface brief
display ip interface brief
display ipv6 interface brief
```

状态含义：`^down`表示配置对象已创建但尚不满足底层数据面创建条件；普通`down`表示底层对象存在但链路或协议条件未满足。接口无IP不应因此down。

AF_PACKET 物理口根据底层 Linux 接口的实际载波更新链路状态。对端断开和恢复时，接口及依赖它的 Vlanif 会重新计算状态。Vlanif 所属 VLAN 至少需要一个管理启用且链路正常的有效成员；所有有效成员失效时转为 Down，成员恢复后自动回到 Up。显式 shutdown 继续约束接口的管理状态。

AF_PACKET 创建和重建时继承底层 Linux 接口的 MTU。显式修改父口 MTU 后，自动 L2 MTU 按新的运行值计算；显式配置的子接口 MTU继续独立生效。


`display interface brief`中的`CRC`只显示网卡驱动提供的硬件CRC/FCS坏帧计数；驱动或虚拟接口不支持该计数时显示`--`。CRC 为接收坏帧计数。发送方向显示 NIC/PMD 提供的总错误；目前没有独立的硬件发送 CRC 计数。物理口详情中的`Total Error`来自NIC/PMD的`rx_errors`和`tx_errors`；驱动没有提供时显示`-`。VPP 26.10 在统计接口上为 DPDK 硬件计数添加了 `xstats-` 前缀，CLI 会识别 CRC、硬件收发错误和详细单播／组播／广播计数。输入`Discard`只统计NIC接收队列无可用缓冲和VPP接收mbuf分配失败导致的资源丢弃，并映射到标准IF-MIB `ifInDiscards`；没有可靠输出丢弃来源时不显示输出`Discard`字段。VPP graph drop、punt及收发graph error在`VortexROS-VPP interface information`中分别显示，供转发路径诊断使用，不混入物理端口错误或标准丢弃计数。

接口详情不显示当前无法从VPP或NIC可靠取得的协商、MDI、流控、Pause、Giants、Runts、Fragments、Alignments、Symbols及输出Discard字段。Vlanif、Vbdif、LoopBack、Tunnel及其他虚拟接口的通用收发区只显示包数和字节数；VPP `/if/drops`可能包含策略、路由和协议处理丢弃，只在`VortexROS-VPP interface information`中以`Graph drop packets`显示一次。标准SNMP中没有可靠逻辑接口丢弃来源的实例保持不可用。

`InUti/OutUti`由daemon复用一条VPP统计连接，每秒读取标准字节计数，并使用最近300秒的成熟窗口按接口链路速率换算为一位小数的利用率。daemon启动、VPP重连、同名接口重建、计数器清零或尚未形成完整300秒窗口时显示`0.0%`；执行display命令本身不会临时采样或等待。统计读取连续超过3秒未成功时旧速率立即失效，不会把故障前的数值继续显示成当前状态。NVE和尚未创建数据面对象的隧道没有独立计数器，显示`--`而不是虚构零流量。CRC/FCS属于低频诊断计数，不进入每秒采样。

`display interface <接口>`同时显示当前1秒速率和最近300秒平均速率。daemon启动或VPP重连后的前两个有效样本之间，当前速率显示`--`；连续采样尚未达到300秒时，300秒平均值显示`--`，完整窗口形成后自动显示数值。详情中的输入、输出带宽利用率使用同一300秒平均值除以VPP报告的实际链路速率；窗口或速率不可用时显示`--`。此前固定显示的80%门限没有配置或告警行为，现已删除，不再把样式文字伪装成功能。计数器清零、接口运行索引变化或VPP会话变化会废弃该接口的旧窗口，不会把两个对象的累计计数相减。

物理口的速率、双工和介质类型只显示已有运行证据。VPP通用接口API提供速率和双工；介质类型从VPP硬件信息中的明确连接器或明确硬件类型识别，电口显示`COMMON COPPER`，光口显示`COMMON FIBER`，证据不足时显示`COMMON UNKNOWN`。当前API没有提供自协商、MDI和流控状态，因此这些字段显示`-`，不会根据链路速率泛化推断。

物理接口的单播、组播和广播分类计数默认关闭，未开启时在接口详情中显示`-`，对应IF-MIB分类计数实例不可用。需要观察时在物理接口视图开启：

```text
interface Ethernet 1
 statistic enable
commit
display interface Ethernet 1
```

VortexROS优先使用网卡驱动提供的分类计数；某一分类没有硬件计数时，才使用VPP详细统计节点的同类计数。该功能只允许配置在物理接口，不允许配置在子接口、Vlanif、LoopBack、隧道或聚合接口。`undo statistic enable`关闭分类采集。`clear interface Ethernet 1 counter`在当前vortexrosd/VPP运行代次内建立新的计数基线；接口详情、速率和SNMP随后都从零开始，但不改写NIC或VPP的原始计数。VPP或vortexrosd重启属于新的计数不连续代次，旧基线不再使用。

`display interface description`在表格前显示接口状态标记说明。接口名称上的`*down`、`^down`、`(l)`和`(s)`分别来自真实的管理关闭、standby、LoopBack和spoofing状态；E-Trunk、BFD和ETHOAM只有在对应运行态能够证明时才使用`(E)`、`(b)`、`(e)`，不会为了填充样式而虚构状态。

IP简表合并VPP与LCP地址。LCP接口正在删除或重建而无法完成地址观察时，该行地址与协议状态显示`unavailable`/`unknown`，且不计入协议UP或DOWN数量；这表示当前证据不足，不表示接口已经确认协议Down。其他接口仍正常显示。

## 数据面设备配置

```text
dataplane
 device 0000:03:00.0 name Ethernet 0
  mode dpdk
  queues rx 2 tx 2
  descriptors rx 1024 tx 1024
  undo hardware offload tso
 quit
 cpu main-core 2
 cpu worker-cores 3-5
quit
interface user-defined Ethernet0
 ip address 192.0.2.10 255.255.255.0
quit
commit
save
display dataplane verbose
reset dataplane
```

PCI 地址用于定位硬件，`name Ethernet 0` 将接口命名为 `Ethernet0`。物理口默认为
`kernel`。`undo mode` 恢复 Linux 驱动。按 `interface user-defined` 预配置的接口
以普通 `interface Ethernet0` 视图保存，地址和静态路由在设备就绪后下发。

`reset dataplane` 确认后生成 udev 规则、变更物理网卡名称并核对 Linux 配置。
之后为选择 DPDK 的设备生成 VPP 启动配置并接管。接管失败时恢复 Linux 驱动和回放地址、
路由，保留已经验证的 Ethernet 名称。外部网络管理器由用户维护。

### 邻居与 MAC 学习上限

```text
dataplane
 neighbor ipv4 limit 102400
 neighbor ipv6 limit 102400
 mac-address learn-limit 102400
quit
commit
save
display current-configuration configuration dataplane
display dataplane verbose
```
IPv4、IPv6 和 MAC 学习上限默认为 102400。配置省略上限时，直接应用当前版本的默认值。等于默认值的命令不会写入配置。
IPv4 和 IPv6 邻居上限范围为 4–2147483647，分别作用于 ARP 和 ND。提交后 Linux
立即更新对应协议族的三个回收阈值，分别为上限的四分之一、二分之一和全值（向下取整）。
VPP 在线时同步更新容量，VPP 启动和 Linux 重启时根据保存的配置回放。
`ipv6 nd max-number` 修改同一个 IPv6 容量值。

MAC 学习上限范围为 1–2147483647。它约束 VPP 全局动态学习，桥域还受自身学习限制。
MAC 配置变更后，保存并执行 `reset dataplane` 才生效。该参数不修改 Linux bridge 的学习上限。
三个 `undo` 命令分别恢复 102400。配置上限和实际可承载规模需要分别核验。

在 `dataplane` 视图中，`display this` 只显示该视图的已提交配置。进入设备子视图后，
它只显示选中的 PCI 设备。`display dataplane` 显示活动后端和 PCI 接管状态。`display dataplane verbose` 汇总运行信息，各部分也可单独查询。

- `display dataplane interfaces` 显示期望与活动模式、PCI 驱动及 VPP 当前和最大 RX 队列数。
- `display dataplane cpu` 显示 Linux 隔离 CPU 和 VPP 线程。
- `display dataplane memory` 显示 Linux 大页总量、空闲和保留量。
- `display dataplane iommu` 显示 IOMMU 组及受管设备所在组。
- `display dataplane tables` 对照期望容量、VPP 运行容量及 Linux GC 阈值。L2FIB 为空时，运行值不可读，显式生成的 MAC 启动值会单独标出。

## 物理接口与offload

用户视图和系统视图的接口选择帮助均按类型、编号两步显示。
例如先使用 `display interface ?` 查看 `Ethernet` 类型，再用
`display interface Ethernet ?` 查看可用编号。命令支持类型缩写，
例如 `display current-configuration interface ether 1`。

```text
interface Ethernet 1
 description uplink
 mtu 9000
 ip address 192.0.2.2 255.255.255.0
 undo hardware offload tso tx-checksum rx-checksum
```

设备直接读取物理接口实际支持的硬件卸载能力。除LRO外，支持的能力默认开启；使用 `undo hardware offload ...` 可以按接口关闭一个或多个能力。

当网卡不能按PPPoE、MPLS、L2TP、GRE、VXLAN或IP-in-IP内层流进行硬件RSS时，可以在物理入口启用flow steering。功能按接口生效，使用一套固定的产品参数，不创建或绑定profile，也不向用户暴露VPP内部调试开关：

```text
system-view
 interface Ethernet 1
  flow-steering enable
 commit
display flow-steering interface Ethernet 1
```

该功能只在VPP配置了两个或更多转发worker时激活；单worker设备保留配置但运行状态显示`inactive/single-worker`。解析最多检查256字节、4层封装、4个IPv6扩展头和8层MPLS标签，无法完整识别时使用稳定的外层会话散列，不丢包、不改变协议语义。它只决定入口worker，不替代Zebra、VPP FIB、ECMP或网卡本身已经提供的RSS。撤销接口绑定：

```text
interface Ethernet 1
 undo flow-steering enable
commit
```

IPv4继续使用主地址与`sub`从地址语义；IPv6地址为累加列表，不使用`sub`：

```text
interface LoopBack 0
 ipv6 address 2001:db8:100::1 64
 ipv6 address 2001:db8:200::1 64
```

同一接口最多配置16个IPv6全局单播地址。同一VPN实例内，同一IPv6前缀只允许归属一个接口；
未指定、多播、链路本地、IPv4映射地址以及物理接口上的回环地址在进入Candidate时拒绝。前缀长度
小于127时，前缀本身的全零接口标识保留为子网路由器任播地址，不能作为普通接口地址。

| 步骤 | Candidate变化 | commit后效果 | 验证 |
|---|---|---|---|
| 创建/进入接口 | 无或创建配置对象 | 不一定创建数据面 | `display this` |
| 配置MTU/IP | 保存本会话修改 | 提交后更新接口MTU和地址 | `display interface Ethernet 1` |
| 关闭offload | 保存关闭项 | 提交后关闭硬件支持的指定能力 | `display interface hardware offload Ethernet 1` |
| 开启详细统计 | 保存`statistic enable` | 提交后采集物理口报文分类计数 | `display interface Ethernet 1`、标准IF-MIB |
| 精确undo | 删除对应叶 | 恢复默认/撤销地址 | display及转发验证 |

## Eth-Trunk

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

## 三层子接口

```text
interface Ethernet 1.100
 encapsulation dot1q vid 100
 ip address 10.100.0.1 255.255.255.0
```

QinQ示例：

```text
interface Ethernet 1.200
 encapsulation qinq vid 200 ce-vid 20
 ip address 10.200.20.1 255.255.255.0
```

提交后，只有标签匹配的报文进入对应子接口。父接口down时子接口随之down；父接口恢复后自动恢复。使用以下命令验证：

```text
display interface Ethernet 1.100
display ip interface brief
display ip routing-table protocol direct
```

## VLAN、子接口与Vlanif

显式二层子接口未配置 `mtu` 时使用父端口的硬件 MTU 能力，三层子接口缺省使用 1500。父接口 MTU 下发后，VortexROS 恢复各子接口的目标值，可用 `display interface` 检查。

```text
vlan batch 100 200
interface Ethernet 1
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 100 200
interface Vlanif 100
 ip address 10.100.0.1 255.255.255.0
```

简单QinQ端口使用VRP风格的`dot1q-tunnel`。`port default vlan`把整个父接口作为唯一客户侧成员加入对应bridge-domain；不创建隐藏子接口，也不在父接口执行标签改写。对端trunk按外层服务VLAN分类并对称移除/恢复S-Tag，因此客户侧未打标签报文转为单层S-Tag，已有C-Tag的报文转为S-Tag+C-Tag。该模式不使用已删除的`port link-mode`兼容命令：

```text
vlan batch 200
interface Ethernet 2
 portswitch
 port link-type dot1q-tunnel
 port default vlan 200
```

`dot1q-tunnel`父接口接管该端口的完整客户侧分类空间，包括未打标签和所有客户VLAN标签，因此禁止在该父接口上创建任何显式L2/L3 VLAN子接口。trunk则只禁止显式子接口复用其已经派生的业务VLAN ID；即使显式子接口的instance后缀不同也会在Candidate/commit边界拒绝。该限制避免父接口与子接口同时接收同一报文，保证桥域成员、策略挂载和严格读回只有一个权威对象。

配置在二层物理接口或VLAN上的策略会作用于对应的trunk业务流量。Vlanif只有在VLAN中至少存在一个可用成员端口时才能正常up；没有可用成员时显示普通down，并撤销相关直连路由。

策略投影遵循实际承载对象：access和`dot1q-tunnel`的VLAN QoS/MQC绑定在整个父
接口，trunk的VLAN策略绑定在对应隐式业务子接口。简单QinQ不再生成客户侧
`父接口.VLAN`对象，因此不会把策略下发到不存在的接口；VLAN classifier中的匹配
条件仍保留。

从曾创建客户侧DEFAULT隐藏子接口的旧版本warm升级时，控制面会在同一VPP会话中
识别该父接口下带DEFAULT标志的旧子接口，先从其实际bridge-domain解绑再删除；
非DEFAULT显式子接口和其他父接口不属于该清理范围。清理后简单QinQ仍只保留父接口
这一权威客户侧成员。

`display vlan`使用一张表同时显示状态、MAC学习、描述和端口成员，端口状态中的`U/D`表示up/down，`TG/UT`表示tagged/untagged。表格宽度根据实际内容调整；端口之间间隔两个字符，每行最多显示四个端口，更多端口在下一行按首个接口位置继续显示：

```text
-----------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
-----------------------------------------------------------------

VID  Type    Status  MAC-LRN  Description    Ports
-----------------------------------------------------------------
1    common  enable  enable   VLAN 1         UT:eth2(D)  eth3(D)
10   common  enable  enable   To_CTC_ISP     UT:eth0(U)
20   common  enable  enable   To_LAN_Client  UT:eth1(U)
-----------------------------------------------------------------
```

`display ip interface brief`和`display ipv6 interface brief`保持相同的状态列布局，便于同时核对Physical、Protocol和VPN-Instance。

隐式默认MAC不进入 `display current-configuration` 或 `display this`。

启用交换功能后，每个VLAN对应的转发域默认采用以下行为：

- 动态MAC学习：开启；
- 广播和组播泛洪：开启；
- 未知单播泛洪：开启；
- 二层转发：开启；
- 动态MAC老化时间：300秒。

`enable switch`还会启用LCP二层控制通道。创建LCP对时，VortexROS根据配置模型明确下发L2或L3角色；linux-cp不根据接口名称、BVI、业务VLAN或VPP瞬时mode再次猜测。`vortexros-switchd`创建一座名为`switch`的VLAN-aware Linux bridge；只要接口配置了`portswitch`，对应父LCP TAP就加入其中，包括尚未配置`port link-type`的缺省VLAN端口和链路Down端口。VLAN配置只决定该bridge端口的VLAN成员关系，不决定端口是否属于bridge。Vlanif、Vbdif、路由物理口、LoopBack和隧道等L3 LCP均不加入`switch`，其IP地址仍属于各自Linux L3接口。trunk的业务VLAN仍由VPP隐式子接口承载，不为每个VLAN再创建一套Linux TAP或bridge，因此接口数量不会随VLAN/VNI线性膨胀。

`switch`自身不承载业务IP，其MTU自动设置为当前L2控制端口的最大MTU。switchd创建或重新校准bridge时会直接查询Linux bridge能力；若内核支持`fdb_local_vlan_0`则自动开启，不支持时不设置。接口从L3切换为switchport或从switchport切回L3时，只更新既有LCP对的角色和bridge成员关系，不删除重建TAP。

这座bridge只表示控制面状态：VPP继续负责MAC学习、老化、未知单播/广播泛洪和报文转发；Linux bridge端口关闭自主学习和泛洪。VPP新学、迁移或老化的动态MAC通过现有MAC事件同步为Linux `extern_learn` FDB；Linux内核的`offload`标记只由真实switchdev驱动设置，控制通道不会伪造该标记。Linux控制程序下发的静态FDB再经linux-cp进入对应VPP bridge-domain。普通业务报文不会为了同步MAC而复制到Linux，也没有新增VPP转发节点。ARP/ND、接口、地址、路由、MPLS和IS-IS继续使用原LCP通道。

```text
display lcp
display vlan
display mac-address
```

`display lcp`会同时显示二层控制通道、Linux bridge ifindex、控制端口数和原有LCP接口对。静态VXLAN继续使用NVE中的显式peer；BGP EVPN使用一座single VXLAN device（SVD）`vxlan0`承载所有动态VNI，不为每个VNI创建一套Linux bridge和VXLAN设备。完整配置和验证见[VXLAN EVPN](11-vxlan-evpn.md)。

动态MAC老化时间是全局参数。需要修改时，在系统视图执行：

```text
mac-address aging-time 600
commit
```

提交后，所有VLAN对应转发域的动态MAC老化时间变为600秒。恢复默认值：

```text
undo mac-address aging-time
commit
```

默认值不显示在配置中；只有非默认值才进入 `display current-configuration`。VPP以整分钟保存该参数，因此配置值必须是60秒的整数倍。

## BD与Vbdif

```text
bridge-domain 11
 l2 binding vlan 100
 vxlan vni 1011
interface Vbdif 11
 ip address 10.11.0.1 255.255.255.0
```

验证BD、VNI、MAC学习和L3网关：

```text
display bridge-domain 11
display mac-address
display interface Vbdif 11
```

删除前先解除Vbdif、VNI和VLAN绑定，避免业务仍在引用BD。

## ARP与代理ARP

IPv4 ARP和IPv6 ND邻居老化是VPP进程级参数，不依赖VLAN或bridge-domain。纯三层接口同样使用这些参数。默认值均为1200秒，并在VPP每次启动或重新连接后优先恢复，再下发接口、地址和业务配置。

```text
arp timeout 900
ipv6 nd stale-timeout 1800
ipv6 nd max-number 65536
ipv6 nd recycle enable
commit
```

恢复默认值：

```text
undo arp timeout
undo ipv6 nd stale-timeout
undo ipv6 nd max-number
undo ipv6 nd recycle
commit
```

`max-number`限制VPP IPv6邻居表容量；`recycle enable`在容量已满时回收最老的动态条目，静态邻居不参与动态回收。回收策略必须显式配置，`undo`恢复VPP启动时的默认策略。容量同步到 Linux ND 回收阈值。老化时间和回收开关作用于 VPP 邻居表。默认值不显示在配置中，非默认值通过 `display current-configuration` 和 `display ipv6 nd` 回读验证。

静态 IPv6 邻居绑定在三层数据面接口上。MAC 支持三段式和冒号分隔形式，保存时统一为冒号分隔形式。

```text
ipv6 neighbor 2001:db8:10::2 0211-2233-4455 interface Vlanif10
commit
display ipv6 neighbors static
undo ipv6 neighbor 2001:db8:10::2 02:11:22:33:44:55 interface Vlanif10
commit
```

多播、未指定IPv6地址，多播或全零MAC，以及二层或控制型接口都会在提交前被拒绝。提交后的静态项由Linux后端写入对应LCP接口，再由LCP同步至VPP；接口重建时按同一路径恢复，不再由VPP后端重复写入。动态邻居只属于运行态，不会写入配置。

静态ARP和单IP/范围代理ARP必须绑定一个真实、具备MAC且能发送ARP的L3接口；LoopBack和NVE不出现在补全中。

静态ARP只接受可用IPv4单播地址和六字节单播MAC；全零、组播或广播映射会在提交前拒绝。静态MAC
表项的出口必须实际属于该表项的桥域；trunk与业务桥域先转换为Linux控制端口和VLAN后再校验，
普通静态项由switchd写入Linux FDB并经LCP进入对应VPP bridge-domain，不能把其他桥域的端口写入当前桥域。

```text
arp proxy 10.10.10.12 10.10.10.14 interface Vlanif 100
display arp proxy
undo arp proxy 10.10.10.12 10.10.10.14 interface Vlanif 100
```

提交后，指定地址范围的ARP请求从所选三层接口代理响应。接口down/up或重新创建后，设备会自动恢复已经提交的代理配置。

## 接口状态时间

`display interface`中的最近up/down时间来自接口实际状态变化，不会因为执行display而重置。控制服务重启后无法确认的历史时间显示 `-`；修改时区只会改变时间的显示方式。

## 删除顺序

先解除路由、隧道、VRRP/BFD、策略和VPN引用，再删除IP、成员、Vlanif/BD/VLAN/聚合对象。校验器会在进入Candidate前拒绝明显的悬空引用。
