# DHCP

配置 IPv4 与 IPv6 地址分配、客户端和中继。系统自身 DNS 解析由 Linux 管理。

[命令参考](reference/dhcp.md) · [配置案例](../examples/dhcpv6.md) · [配置案例](../examples/dhcp.md)

## IPv4 服务端

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

Debug 9 已包含 DHCPv6 IA_NA/IA_TA/IA_PD 类型解码以及 Kea 正常空租约结果的修复。正常空库应显示零租约；同地址族的空实例不会阻断其他实例的租约或池名筛选。传输和服务错误仍报错。历史输出见[实测案例](../examples/dhcpv6.md#验证)。

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

IPv6 默认网关来自 [RA 与 SLAAC](ipv6-autoconfig.md)。
