# IPv4 服务端

## IPv4 服务端

先在系统视图启用DHCP服务：

```text
enable dhcp server
commit
```

全局开关只控制 IPv4 和 IPv6 服务端。Client、Relay 和 DHCPv6-PD 按接口配置运行。
暂停某个接口上的客户端或中继可用 `dhcp client-relay shutdown`；`undo dhcp client-relay shutdown` 恢复该接口原有角色，不影响服务器角色。


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
本地 IPv4 子网的池不能同时映射到两个接入口，当前不支持跨接口共享同一子网；IPv6 池的显式服务器绑定也只能使用一个接口。全局 IPv4 池属于 VPN 实例，远端客户链路由中继的 giaddr 选择地址池，不要求服务器接口位于客户子网。

也可以直接使用接口主地址所在网段生成接口地址池。未配置`gateway-list`时，接口主IPv4地址自动作为客户端网关：

```text
interface Vlanif 20
 ip address 198.51.100.254 255.255.255.0
 dhcp select interface
 dhcp server ip-range 198.51.100.100 198.51.100.200
 dhcp server dns-list 1.1.1.1 8.8.8.8
 dhcp server lease day 1
#
```

CLI 操作：

```text
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

`Ready=true` 表示服务器已在配置的接口和地址上就绪。接口关闭、地址消失或服务无法查询时，不应把已有租约记录当成服务器仍可服务的证明。恢复接口后再次检查服务状态，并让客户端重新申请或续租。

实际全局池验证中，配置 `lease day 0 hour 2`、两台 DNS、域名和 MAC 静态绑定后，客户端收到：

```text
Your-IP 198.18.11.111
Subnet-Mask: 255.255.255.0
Default-Gateway: 198.18.11.1
Domain-Name-Server: 192.0.2.53, 192.0.2.54
Domain-Name: global.example
Lease-Time: 7200
```

`display ip pool name LAN4 verbose` 可同时检查实际 IP、MAC、客户端标识、网关、DNS、域名、剩余租期及 VPN。接口池验证中，显式租期 5400 秒在 `undo dhcp server lease` 后恢复为 86400 秒；撤销 DNS 和域名后，新回复不再通告这些选项，而撤销显式网关仍保留接口主地址作为默认网关。

修改分配范围或撤销静态绑定不会立即强制客户端放弃其已有租约。更换池身份、从接口池改用全局池时，也应检查旧租约是否仍占用目标地址；不能仅根据静态配置存在就判断该地址已成功分配。

关闭接口上的服务器角色：

```text
interface Vlanif 100
 undo dhcp select
```

CLI 操作：

```text
commit
```

在系统视图关闭全局 DHCP 服务端开关时，先撤销仍使用服务端角色的接口配置。客户端、中继和 PD 不受该开关控制：

```text
undo enable dhcp server
commit
```


[DHCP 功能与开关](../dhcp.md) · [逐条命令参数](../reference/dhcp.md)

## 服务异常与恢复

DHCP 服务不可用时，`display health` 会显示未就绪，租约查询也可能返回真实的服务错误。不要把已有租约或能正常转发的静态业务等同于 DHCP 已恢复。排除服务故障后，系统会继续完成配置和实际状态核对；通过 `display health`、`display ip pool` 以及客户端续租确认恢复。

DHCP 启动失败不会要求重启已正常工作的整个数据面。已有接口及路由的实际转发与 DHCP 分配能力应分别检查。一次服务启动故障验证中，健康状态保持未就绪、原业务探测2/2；排除故障后自动恢复就绪，业务探测仍为2/2。这不是对所有故障或吞吐能力的保证。
