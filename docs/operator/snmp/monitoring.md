# MIB 与服务检查

## 配置与连通性

~~~text
display snmp-agent sys-info
display snmp-agent community
display snmp-agent usm-user
display snmp-agent target-host
display health verbose
~~~

这些命令核对配置及健康；最终应从监控平台执行实际 SNMP 查询。接口 ACL、VPN 归属、IPv4 回程以及平台凭据必须一致。固定 source-interface 只监听所选 VPN 中该接口的主 IPv4；all-interface 覆盖 public 及已配置 IPv4 接口的 VPN。

## 推荐监控项目

| 对象 | 用途 |
| --- | --- |
| SNMPv2-MIB::system | 系统名、位置、运行时间 |
| HOST-RESOURCES-MIB | 系统运行时间及资源 |
| UCD-SNMP-MIB | 内存、CPU、负载等系统资源 |
| IF-MIB::ifTable / ifXTable | 接口描述、管理/链路状态、64 位计数 |
| ifCounterDiscontinuityTime | 计数清零或重建后的速率基线 |

IF-MIB 使用设备公开的接口清单。VPP 数据面读取对应接口的实际计数；接口尚未实际创建时，不产生虚构的接口计数。Linux 数据面使用已声明且实际存在的产品接口及其内核计数，不发布未纳管的宿主接口。驱动未提供的单播/广播分类和可靠链路速率显示为不可用。

物理端口、显式配置的 L2/L3 子接口及已创建的逻辑接口可以监控。公开接口有独立 LCP 配对时，另发布一行 `lcp-<接口名>`，用于查看该接口的控制面路径。此行的计数独立于公开接口。自动生成的 VLAN 承载子接口、内部 VXLAN 和 local0 不进入接口表。不能按“虚拟接口”一类全部排除，否则会丢失用户实际管理的子接口和隧道。ifAlias 对应接口 description。接口名称与身份不变时，数据面重建后监控索引保持稳定；计数重置仍需按 ifCounterDiscontinuityTime 重新建立速率基线。

流量速率使用 ifHCInOctets / ifHCOutOctets 的相邻采样差。发现计数不连续时重建基线；不要用 32 位计数计算高速接口速率。隧道统计内层流量，物理口还包含封装开销，两者不要求相等。缺少可靠来源的分类或错误计数不可用，不应解释成零。

## 范围与限制

支持 SNMPv2c 只读及 SNMPv3 authPriv，不支持 SET、SNMPv1、企业 MIB、IPv6 监听或 IPv6 Trap 目标。community 和 SNMPv3 密码进入受保护的配置及备份，应限制其访问权限。

删除被源接口配置引用的 VPN 会同时撤销 SNMP 配置并停止监听；需要继续监控时，在新 VPN 下显式重新配置。不会自动扩大为全接口监听。

接口清单暂时不可观测时，监控数据可能不可用；不能把查询失败当成真实 Down 或零流量。先检查 display health verbose、监听范围及接口状态。

## 撤销

按对象解除引用，或在不再需要 SNMP 时整体执行 undo snmp-agent、commit、save。再从原平台确认轮询不再返回。

[功能目录](../snmp.md) · [命令参数](../reference/snmp.md)

## 实际查询示例

以 Ethernet0 为例，先读取 ifDescr 找到索引，再查询同一索引的状态、描述和64位字节计数。索引由接口身份决定，不要把示例数字固定在监控模板中。

~~~text
IF-MIB::ifDescr.2047694891 = STRING: Ethernet0
IF-MIB::ifAlias.2047694891 = STRING: SNMP counter and trap validation
IF-MIB::ifHCInOctets.2047694891 = Counter64: 23540
IF-MIB::ifHCOutOctets.2047694891 = Counter64: 6342
~~~

在该接口完成六次1000字节 ping 后，输入计数增加至29856，输出计数增加至12636；SNMPv2c和SNMPv3均可读取。关闭接口后的标准 linkDown 通知携带同一索引及管理/运行状态2；恢复接口后 linkUp 携带状态1。通知依赖监控采样周期，不承诺与配置提交同时到达。


## 核对接口范围

先执行 `display interface brief` 查看公开接口，再从监控平台读取 ifName 和 ifNumber。SNMP 还会列出公开接口对应的 LCP 诊断行；配置尚未创建实际接口时，不要求存在计数器条目。以下为六个实际接口的查询节选，未列出可能存在的 LCP 诊断行：

~~~text
IF-MIB::ifName.430049419 = STRING: Ethernet0.3100
IF-MIB::ifName.866391688 = STRING: LoopBack221
IF-MIB::ifName.1263342616 = STRING: Ethernet0.3101
IF-MIB::ifName.1918639716 = STRING: Ethernet0.3202
IF-MIB::ifName.2042167659 = STRING: Ethernet0.3201
IF-MIB::ifName.2047694891 = STRING: Ethernet0
~~~

显式 L2 子接口 Ethernet0.3100 和 Ethernet0.3101 保留在清单中。内部 VLAN 和 VXLAN 不会额外产生监控条目。数据面重建后，上述接口身份不变时索引保持不变。示例索引只用于说明输出，应从本机查询获得。
