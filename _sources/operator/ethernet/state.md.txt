# 状态与链路

## 接口状态

设备只允许一个转发平面管理物理接口。VPP未启用时，可在CLI中配置Linux能够识别的物理口；VPP接管完成后，只允许配置设备已经识别的业务接口。接管过程中接口配置暂时只读，避免同一接口同时由两套转发平面管理。

数据面接口与同名控制接口使用一致身份。接口名称最多 15 字节，首字符为字母或数字，其余允许字母、数字、下划线、连字符及点；不允许空格、斜杠或冒号。物理口通过 dataplane device 名称配置，逻辑接口使用对应的 interface 入口。

```text
display vpp interface-ownership verbose
display interface brief
display ip interface brief
display ipv6 interface brief
```

状态含义：`^down`表示配置对象已创建但尚不满足底层数据面创建条件；普通`down`表示底层对象存在但链路或协议条件未满足。接口无IP不应因此down。

物理口按实际链路状态更新。Vlanif 所属 VLAN 至少需要一个管理启用、链路正常的有效成员；成员全部失效时 Down，恢复后自动 Up。shutdown 优先限制管理状态。接口没有 IP 不会因此 Down。

父口和显式子接口 MTU 分别管理，业务报文仍受实际出口及路径 MTU 限制。


`display interface brief`中的`CRC`只显示网卡驱动提供的硬件CRC/FCS坏帧计数；驱动或虚拟接口不支持该计数时显示`--`。CRC 为接收坏帧计数。发送方向显示 NIC/PMD 提供的总错误；目前没有独立的硬件发送 CRC 计数。物理口详情中的`Total Error`来自NIC/PMD的`rx_errors`和`tx_errors`；驱动没有提供时显示`-`。输入`Discard`只统计NIC接收队列无可用缓冲和VPP接收mbuf分配失败导致的资源丢弃，并映射到标准IF-MIB `ifInDiscards`；没有可靠输出丢弃来源时不显示输出`Discard`字段。VPP graph drop、punt及收发graph error在`VortexROS-VPP interface information`中分别显示，供转发路径诊断使用，不混入物理端口错误或标准丢弃计数。

接口详情不显示当前无法从VPP或NIC可靠取得的协商、MDI、流控、Pause、Giants、Runts、Fragments、Alignments、Symbols及输出Discard字段。Vlanif、Vbdif、LoopBack、Tunnel及其他虚拟接口的通用收发区只显示包数和字节数；VPP `/if/drops`可能包含策略、路由和协议处理丢弃，只在`VortexROS-VPP interface information`中以`Graph drop packets`显示一次。标准SNMP中没有可靠逻辑接口丢弃来源的实例保持不可用。

InUti/OutUti 使用最近 300 秒的完整窗口，按链路速率计算利用率。daemon启动、VPP重连、同名接口重建、计数器清零或尚未形成完整300秒窗口时显示`0.0%`；执行display命令本身不会临时采样或等待。统计读取连续超过3秒未成功时旧速率立即失效，不会把故障前的数值继续显示成当前状态。NVE和尚未创建数据面对象的隧道没有独立计数器，显示`--`而不是虚构零流量。CRC/FCS属于低频诊断计数，不进入每秒采样。

`display interface <接口>`同时显示当前1秒速率和最近300秒平均速率。daemon启动或VPP重连后的前两个有效样本之间，当前速率显示`--`；连续采样尚未达到300秒时，300秒平均值显示`--`，完整窗口形成后自动显示数值。详情中的输入、输出带宽利用率使用同一300秒平均值除以VPP报告的实际链路速率；窗口或速率不可用时显示`--`。计数器清零、接口运行索引变化或VPP会话变化会废弃该接口的旧窗口，不会把两个对象的累计计数相减。

速率、双工和介质按当前运行信息显示。电口为 COMMON COPPER，光口为 COMMON FIBER，未识别为 COMMON UNKNOWN。没有可读来源的自协商、MDI 和流控显示 -，不能据此认为该功能已关闭。

物理接口的单播、组播和广播分类计数默认关闭，未开启时在接口详情中显示`-`，对应IF-MIB分类计数实例不可用。需要观察时在物理接口视图开启：

```text
interface Ethernet 1
 statistic enable
```

CLI 操作：

```text
commit
display interface Ethernet 1
```

VortexROS优先使用网卡驱动提供的分类计数；某一分类没有硬件计数时，才使用VPP详细统计节点的同类计数。该功能只允许配置在物理接口，不允许配置在子接口、Vlanif、LoopBack、隧道或聚合接口。`undo statistic enable`关闭分类采集。`clear interface Ethernet 1 counter`在当前vortexrosd/VPP运行代次内建立新的计数基线；接口详情、速率和SNMP随后都从零开始，但不改写NIC或VPP的原始计数。VPP或vortexrosd重启属于新的计数不连续代次，旧基线不再使用。

display interface description 的 *down 表示管理关闭，^down 表示尚未满足创建条件，(l) 为 LoopBack，(s) 为 spoofing。其他状态标记按设备实际运行情况显示，表头提供相应说明。

IP简表合并VPP与LCP地址。LCP接口正在删除或重建而无法完成地址观察时，该行地址与协议状态显示`unavailable`/`unknown`，且不计入协议UP或DOWN数量；这表示当前证据不足，不表示接口已经确认协议Down。其他接口仍正常显示。


## 接口状态时间

`display interface`中的最近up/down时间来自接口实际状态变化，不会因为执行display而重置。控制服务重启后无法确认的历史时间显示 `-`；修改时区只会改变时间的显示方式。

[功能目录](../ethernet.md) · [逐条参数](../reference/interfaces.md)


## 管理关闭与查询

~~~text
interface Ethernet 0
 description UPLINK
 shutdown
#
commit
display interface brief
display interface description Ethernet 0
~~~

`shutdown` 后接口显示 `*down/down`，经过该口的业务停止。实际验证中，同 VLAN 另一成员仍为 Up 时，Vlanif 保持 Up；不能把关闭一个成员等同于整个 VLAN 失效。

在同一接口执行 `undo shutdown` 并提交后，接口恢复，探测 2/2；该操作没有重启整个数据面。描述使用 `undo description` 撤销。查看真实收发增长可用：

~~~text
display interface statistics
display interface statistics Ethernet 0
display interface statistics Vlanif 100
display lcp
~~~

接口统计应随实际业务增长。`display lcp` 可核对二层物理口及三层 Vlanif 的控制接口角色，不能只根据名称推断其二、三层归属。


## 按业务核对状态和计数

~~~text
display interface brief
display interface description
display interface statistics
display interface statistics Ethernet 0
display lcp
~~~

`display lcp` 用于核对数据接口与控制接口的关联及其二层、三层角色。一次双成员 VLAN100 的实际查询有两条二层物理关联和一条 Vlanif100 三层关联；二层物理口 MTU9706，Vlanif100 MTU1500。

在接口视图配置 `shutdown` 并提交后，该接口显示 `*down/down`，通过它的业务停止。若同一 VLAN 仍有另一有效成员，Vlanif 可以继续 Up；这不表示已关闭接口仍在转发。`undo shutdown` 并提交后，物理口恢复，双端业务探测恢复。只有全部有效成员失效时，Vlanif 才应随之 Down。

计数查询应在确有业务时观察增量。可以先查询指定接口，再产生业务、重新查询，最后按维护需要清零：

~~~text
clear interface Ethernet 0 counter
display interface statistics Ethernet 0
display interface Ethernet 0
~~~

清零后使用新的累计基线，不会重置硬件原始计数。协议和业务报文仍可立即增加计数，因此再次查询不一定恰好为零。接口重命名后仍按同一运行接口正确关联计数；详情、统计和速率使用相同的清零基线。
