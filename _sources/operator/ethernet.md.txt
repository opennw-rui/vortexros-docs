# Ethernet

配置物理接口、地址和 MTU，查看链路及流量统计。

[命令参考](reference/interfaces.md)

## 接口状态

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


## 基本配置

用户视图和系统视图的接口选择帮助均按类型、编号两步显示。
例如先使用 `display interface ?` 查看 `Ethernet` 类型，再用
`display interface Ethernet ?` 查看可用编号。命令支持类型缩写，
例如 `display current-configuration interface ether 1`。

```text
interface Ethernet 1
 description uplink
 mtu 9000
 ip address 192.0.2.2 255.255.255.0
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


## 接口状态时间

`display interface`中的最近up/down时间来自接口实际状态变化，不会因为执行display而重置。控制服务重启后无法确认的历史时间显示 `-`；修改时区只会改变时间的显示方式。
