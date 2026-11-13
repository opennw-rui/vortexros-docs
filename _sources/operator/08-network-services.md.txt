# DHCP 与 LLDP

本章说明VortexROS提供的DHCPv4/DHCPv6客户端、服务器、中继以及LLDP功能。系统自身的DNS解析由Linux负责；DHCP客户端不会把租约中的DNS服务器写入系统解析器。

## DHCPv4服务器

先在系统视图启用DHCP服务：

```text
enable dhcp server
commit
```

全局开关只控制 IPv4 和 IPv6 服务端。Client、Relay 和 DHCPv6-PD 按接口配置运行。
旧配置里已有 Client 或 Relay 但全局 DHCP 关闭时，加载后会在该接口保留
`dhcp client-relay shutdown`。用 `undo dhcp client-relay shutdown` 恢复该接口的已有配置。


使用全局地址池时，创建地址池并在三层接口启用：

```text
ip pool LAN4
 network 192.0.2.0 mask 255.255.255.0
 gateway-list 192.0.2.1
 section 0 192.0.2.100 192.0.2.200
 dns-list 1.1.1.1 8.8.8.8
 lease day 1
#
interface Vlanif 100
 ip address 192.0.2.1 255.255.255.0
 dhcp select global
```

接口属于VPN实例时，DHCP服务器按地址族和VPN实例运行独立Kea进程，租约及监听不会落入默认路由域。全局地址池必须绑定同一VPN实例；接口地址池直接继承接口的VPN归属：

```text
ip pool BLUE-LAN
 vpn-instance BLUE
 network 192.168.100.0 mask 255.255.255.0
 section 0 192.168.100.100 192.168.100.200
#
interface Vlanif 100
 ip binding vpn-instance BLUE
 ip address 192.168.100.1 255.255.255.0
 dhcp select global
```

提交后用`display dhcp service verbose`确认服务器行的`VPN-Instance`为`BLUE`且`Ready`为`true`，再用`display ip pool name BLUE-LAN verbose`核对实际租约。接口的LCP host、VRF master或本地地址尚未就绪时，服务器不会被误报为Ready。

池中的`dns-list`只作为DHCP Option通告给外部客户端，不改变VortexROS主机的`/etc/resolv.conf`。
全局地址池使用`section <编号> <起始地址> [结束地址]`限制可动态分配的地址段；可配置多个互不重叠的
section，编号范围为0至255。未配置section时使用network中的全部可用主机地址。网关、排除地址、
接口本机地址和静态绑定仍会从section中扣除。`gateway-list`与`dns-list`保持录入顺序，第一项是
客户端收到的首选地址，保存和重载不会按数值重新排序。
全局池应用到接口时，该接口在此子网内的全部本地IPv4地址都会自动从动态分配范围排除。
同一VPN实例内，一个IPv4或IPv6地址池只能绑定一个接口；当前版本不提供跨接口共享子网模型，
重复绑定会在进入Candidate时给出明确错误。

也可以直接使用接口主地址所在网段生成接口地址池。未配置`gateway-list`时，接口主IPv4地址自动作为客户端网关：

```text
interface Vlanif 20
 ip address 198.51.100.254 255.255.255.0
 dhcp select interface
 dhcp server ip-range 198.51.100.100 198.51.100.200
 dhcp server dns-list 1.1.1.1 8.8.8.8
 dhcp server lease day 1
#
commit
```

如需通告同网段内的其他网关，可用`dhcp server gateway-list X.X.X.X [X.X.X.X]`显式替换默认值。`undo dhcp server gateway-list`恢复“接口主地址作为网关”的默认行为。确实不希望发送Router Option时，使用`dhcp server gateway-list disable`。接口本机使用的所有IPv4地址始终从动态地址池排除，与通告哪个网关无关。

接口地址池使用`dhcp server ip-range <起始地址> <结束地址>`限制可分配范围；起止地址必须属于接口
主IPv4网段且均为可用主机地址。该范围存在时优先使用它，`undo dhcp server ip-range`恢复从接口
主网段的全部可用主机地址分配。接口地址池只保存一个显式范围；需要多个不连续地址段时使用全局
地址池的多个`section`。

验证：

```text
display dhcp service verbose
display ip pool
display current-configuration
```

`Ready`只有在Kea控制接口正常、主进程拥有正确的UDP监听、每个已配置LCP接口保持admin UP且目标地址仍可用时才显示为`true`；监听数量相同但绑定到无关地址，或服务启动后接口关闭、地址消失，都会判定为未就绪。一个服务器接口配置多个本地地址时，Kea会监听该接口的全部可用地址，因此中继可以把请求发往其中任一明确配置的服务地址。IPv6允许Kea使用能够覆盖已配置接口的UDP/547通配监听，但接口与地址可服务条件仍须满足。后台审计会持续执行这组检查，并在接口恢复后重新收敛。可用Linux的`ss -lunp`作辅助诊断，但产品状态以`display dhcp service verbose`的权威回读为准。

关闭接口上的服务器角色：

```text
interface Vlanif 100
 undo dhcp select
commit
```

确认没有接口继续使用DHCP服务器、客户端或中继后，可在系统视图关闭整个DHCP功能：

```text
undo enable dhcp server
commit
```

## DHCPv4客户端

```text
interface Ethernet 1
 ip address dhcp-alloc
commit
display dhcp client
```

客户端只接收和维护IPv4地址、默认路由、classless route及租约生命周期。撤销：

```text
interface Ethernet 1
 undo ip address dhcp-alloc
commit
```

VPP启用时，DHCP客户端运行在VPP为业务接口建立的LCP host接口上。报文仍通过对应VPP物理接口收发，客户端不会重新绑定、独占或接管物理网卡。这样IPv4与IPv6租约采用同一套生命周期、VRF、撤销和重启恢复逻辑，并且可以完整处理默认路由和classless route。租约中的DNS选项不写入Linux系统解析配置。

接口`shutdown`只暂停对应的DHCP client、relay和PD运行单元，配置意图仍保留。子接口还继承父接口的有效管理状态：父接口关闭时子接口单元同时暂停；父接口恢复后，只有自身未配置`shutdown`的子接口才按原配置恢复。该行为不删除租约配置，也不会把显式关闭的子接口强制拉起。

默认会安装DHCP学习到的默认路由，默认优先级为60。可以调整优先级，或显式禁止默认路由：

```text
interface Ethernet 1
 dhcp client default-route preference 80
 # 如不需要上游默认路由：
 undo dhcp client default-route enable
```

## DHCP服务器租约查看

`display ip pool`同时列出全局IPv4地址池、接口地址池和仍在使用的Kea租约。接口定位既支持完整名称，也支持VRP风格的类型与编号分词；以下三条都能直接显示摘要和活动租约：

```text
display ip pool
display ip pool name OFFICE
display ip pool interface vlanif 20
```

默认视图和`used`都只显示仍有效的已分配地址；`all`显示Kea仍保留的全部租约状态，包括已过期或被拒绝的记录。`used`可以放在接口选择器之前或之后，例如`display ip pool used interface vlanif 20 verbose`。不存在`display ip pool use`命令。表格包含地址池或接口、客户端IP、MAC、Client-ID、剩余租期、状态、主机名和VPN实例。租约来自Kea控制Socket的权威运行态，不读取可能正在写入的CSV文件；读取失败会明确报错，不会把观察失败显示为零租约。

`verbose`把租约表切换成逐项详情，因此不必同时指定`used`。每条IPv4租约显示IP、MAC、网关、DNS、地址范围、域名、Client-ID、主机名、VPN实例、Kea服务实例、Subnet ID、状态、最近一次客户端事务时间、到期时间、有效租期和剩余租期。`used verbose`语义相同；`all verbose`还会展开已过期、declined及Kea保留的其他状态。没有由客户端提供的字段明确显示为`-`，不会根据MAC猜测厂商、操作系统或设备型号。

DHCPv6服务器使用相同的运行态语义：

```text
display dhcpv6 pool name V6-POOL used
display ipv6 pool name V6-POOL all
display ipv6 pool name V6-POOL verbose
```

IPv6输出区分IA_NA、IA_TA和IA_PD，并显示DUID、IAID、地址或委派前缀、Subnet ID、客户端事务时间、到期时间、剩余租期和状态。租约属于运行数据，不进入Candidate、CFG或SQLite配置投影。

Classless Static Route Option存在并启用解析时，按标准优先使用该选项，不再同时采用Router Option。无论默认路由来自哪个DHCP选项，`undo dhcp client default-route enable`都会阻止其中的`/0`，普通明细路由仍可安装。

## DHCPv6

```text
dhcpv6 pool LAN6
 address prefix 2001:db8:100::/64
 dns-server 2001:4860:4860::8888
#
interface Vlanif 100
 dhcpv6 server LAN6
```

验证和撤销：

```text
display dhcp service verbose
display ipv6 pool
interface Vlanif 100
 undo dhcpv6 server
commit
```

DHCPv6客户端和中继在对应接口视图配置；可使用`?`查看地址请求、前缀委派和中继目标的完整参数。DHCPv6客户端同样绑定LCP host接口，因此不会与VPP争用物理接口。

同一DHCPv6地址池内的地址前缀和委派前缀必须使用同一组有效/首选生命周期；显式生命周期最小为
60秒，首选生命周期不得大于有效生命周期。重叠的委派前缀在进入Candidate时即被拒绝，不会留到
Kea启动阶段才失败。

有状态地址、前缀委派以及立即续租的示例：

```text
interface Ethernet 1
 ipv6 address auto dhcp
 dhcpv6 client pd CPE-PREFIX
commit
display dhcpv6 client interface Ethernet 1
display dhcpv6 client prefix name CPE-PREFIX
# 在接口视图立即请求续租：
interface Ethernet 1
 dhcpv6 client renew
```

`display dhcpv6 client`分别显示IA_NA地址和IA_PD委派前缀，不会用其中一个字段遮盖另一个字段。`dhcpv6 client renew`是立即执行的运行命令，不进入Candidate或保存配置。

DHCPv6地址和IPv6路由器发现是两项独立功能。DHCPv6不会提供IPv6默认网关；默认路由来自Router Advertisement。需要同时从RA生成全局地址并接受RA默认路由时，可使用组合命令：

```text
interface Ethernet 1
 ipv6 address auto global default
commit
display ipv6 interface brief
display ipv6 neighbors
display ipv6 routing-table
```

若只需要其中一项，也可分别使用`ipv6 address auto slaac`或`ipv6 nd ra default-route enable`。使用有状态DHCPv6获取地址、同时从RA获取默认路由时，可以组合`ipv6 address auto dhcp`与`ipv6 nd ra default-route enable`，无需同时启用SLAAC地址生成。

VortexROS只在已配置的接口上开启RA接收。VPP模式下由该接口的LCP host接收RA，Linux内核执行DAD并维护前缀、首选时间、有效时间和Router Lifetime，linux-cp再把有效地址和路由同步到VPP。即使系统开启IPv6转发，该接口仍会使用明确的RA接收策略；其他接口不会被全局放开。接口属于VPN实例时，LCP接口先加入对应Linux VRF，学习结果留在该VPN的路由域内。

组合意图可一次撤销：

```text
interface Ethernet 1
 undo ipv6 address auto global default
commit
```

分别配置的地址自动生成与默认路由也可以用各自的精确`undo`撤销。

撤销全部RA功能后，控制面关闭该接口的RA、自动前缀和默认路由接收，并清理内核中由RA协议安装的路由及可识别的SLAAC地址。DHCPv6地址不属于这套清理范围。

## LLDP

```text
enable lldp
commit
display lldp neighbor brief
display lldp neighbor
```

关闭LLDP：

```text
undo lldp enable
commit
```

LLDP未收敛或后端不可用时会在`display health`和告警中显示，但不会触发VPP物理接口所有权回滚。

## SNMP

第一版提供标准 SNMPv2c 只读查询和 SNMPv3 `authPriv`。默认以一个VRF-aware
UDP/161 socket覆盖public及所有已配置VPN实例；可固定到public接口的主IPv4地址，
也可固定到VPN内的接口。trap
发送到NMS UDP 162，设备本地不会监听UDP 162。SNMPv3固定使用SHA2-256认证和
AES128隐私保护，认证与隐私密码均至少8个字符。

设备自动维护符合RFC 3411长度限制的SNMP engine ID。首次创建或用户集合变化时会
初始化Net-SNMP持久USM状态；普通配置提交、daemon恢复和master重启会从受管持久
文件恢复用户及engineBoots，不需要重复配置用户。

SNMPv2c 示例：

```text
snmp-agent
snmp-agent sys-info version v2c
snmp-agent sys-info contact Network Operations
snmp-agent sys-info location IDC-A
snmp-agent protocol source-interface LoopBack0
snmp-agent community read monitor
snmp-agent trap source LoopBack0
snmp-agent target-host trap address udp-domain 192.0.2.50 udp-port 162 params securityname monitor v2c
snmp-agent trap enable standard
commit
save
```

不固定监听接口时无需配置source-interface；下面两种显式写法语义相同，都会用
一个listener接收public和全部VPN实例的请求，而不是为每个IP地址启动一个进程：

```text
snmp-agent protocol source-interface all-interface
snmp-agent protocol source-status all-interface
```

若只允许从某一VPN实例中的接口接收查询，VPN和source-interface在同一条命令中
指定；该接口和trap source必须属于同一VPN。master和listener使用该接口主IPv4
建立VRF内的内部通道，不要求VPN中另行配置loopback路由：

```text
snmp-agent protocol source-interface vpn-instance INT Tunnel1
commit
# 恢复public及全部VPN实例的全接口监听
undo snmp-agent protocol source-interface
commit
```

SNMPv3 示例：

```text
snmp-agent sys-info version v3
snmp-agent usm-user v3 secure-monitor authentication-mode sha2-256 AuthPass123 privacy-mode aes128 PrivPass123
snmp-agent target-host trap address udp-domain 192.0.2.51 udp-port 162 params securityname secure-monitor v3
commit
```

配置和服务检查：

```text
display snmp-agent sys-info
display snmp-agent community
display snmp-agent usm-user
display snmp-agent target-host
display health verbose
```

这些`display snmp-agent`命令显示已提交配置；`commit`后的backend读回会核对三个
服务和UDP 161监听。最终运行验收仍应从NMS执行下列标准SNMP查询，不能只以配置
存在代替协议可达。

从 NMS 验证标准 OID：

```bash
snmpget -v2c -c monitor 192.0.2.1 sysName.0
snmpget -v2c -c monitor 192.0.2.1 HOST-RESOURCES-MIB::hrSystemUptime.0
snmpget -v2c -c monitor 192.0.2.1 UCD-SNMP-MIB::memTotalReal.0
snmpwalk -v2c -c monitor 192.0.2.1 IF-MIB::ifXTable
snmpget -v3 -l authPriv -u secure-monitor -a SHA-256 -A AuthPass123 \
  -x AES -X PrivPass123 192.0.2.1 sysName.0
```

标准Linux系统、CPU、内存、存储和负载信息继续由Net-SNMP提供。IF-MIB则完全由
VortexROS/VPP提供：只显示VortexROS接口，不显示Linux `lo`、VRF master或其他
控制面netdevice；`ifAlias`显示接口description。累计字节、错误数和计数不连续时间
来自VPP数据面。每个LCP host端以`lcp-<接口名>`作为单独的诊断接口显示，其累计值
来自对应VPP host software interface，不与原接口相加。产品接口和LCP诊断接口使用
不同的稳定身份域确定性生成ifIndex，不依赖Linux ifIndex、VPP sw_if_index或额外持久化文件；
接口身份不变时，LCP/VPP重建不会改变监控索引。当前不会把总包数冒充单播、组播或广播包数。VPP重启、
接口重建或计数清零后，监控系统应依据 `ifCounterDiscontinuityTime` 重建速率基线。
同一次不连续事件的该值保持不变；只有新的计数回退、接口身份变化或VPP代次变化
才会产生新值。接口表使用固定AgentX表注册，支持标准GET、GETNEXT和GETBULK，
删除的接口行会同步撤销而不会留作历史实例。

监控平台应直接对`ifHCInOctets`/`ifHCOutOctets`做相邻采样差，不应改用32位计数，
也不应设置“低于某值视为无流量”的设备侧阈值。隧道口统计内层流量，物理口统计
线侧流量及封装开销，二者不要求相等。Vlanif和LoopBack使用VPP逻辑接口统计；当前
配套VPP的simulated Ethernet输出会重复累计一次TX，SNMP适配层只去除这项重复，
不修改数据面，也不把LCP或物理成员计数并入逻辑接口。验证新接入时至少检查system、HOST-RESOURCES、
UCD-SNMP、完整接口清单、接口description、管理/链路状态、64位计数和低速连续流量。

完整撤销会停止 UDP 161 监听并删除全部 SNMP 配置：

```text
undo snmp-agent
commit
save
```

SNMP community 和 SNMPv3 密码随 root-only CFG 以明文保存。第一版不支持 SNMP
SET、SNMPv1、企业 MIB、IPv6 监听或 trap 目标、多 network namespace context，
也不会把 VPP 统计写回 Linux `/proc`、sysfs 或 `ip -s link`。固定源接口模式下，
固定source-interface时只接受对应public或VPN路由域中的目标接口；`all-interface`
通过单socket同时覆盖public和全部具有已配置IPv4接口的VPN。接口与所选VPN不一致时在Candidate
校验阶段拒绝，不会等到服务启动后才失败。

删除被SNMP source-interface引用的VPN实例会同时撤销整套SNMP配置并关闭UDP 161，
不会把原凭据自动改成全接口监听。若仍需SNMP，应在VPN删除后显式重新配置所需
监听范围和凭据。

配置`snmp-agent trap source`后，通知报文使用该接口主IPv4作为UDP源地址；
`snmp-agent trap enable standard`启用标准`linkUp`/`linkDown`通知。设备为Net-SNMP
内部状态查询维护独立的受管身份，不会把它显示为用户USM配置，也不改变外部SNMPv3
只支持`authPriv`的产品约束。

若VPP统计仍可读但接口清单或LCP身份暂时无法确认，设备不会发布一份带当前时间的
虚假`down`/MTU 0接口快照；最后一次已验证快照在3.5秒后自然变为不可用，身份恢复
后才重新出现。
