# IPv4 服务端

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

在系统视图关闭全局 DHCP 服务端开关时，先撤销仍使用服务端角色的接口配置。客户端、中继和 PD 不受该开关控制：

```text
undo enable dhcp server
commit
```


[DHCP 功能与开关](../dhcp.md) · [逐条命令参数](../reference/dhcp.md)
