# 中继

Relay 把客户端广播/组播转发到另一个 DHCP 服务端，自己不分配租约。中继入口、上游路径及服务端返回到中继的路由都必须可用；客户端、中继和服务端属于不同的角色。

## DHCPv6

[完整三节点案例](../../examples/dhcpv6-relay.md)分别列出服务端、中继和客户端配置、租约检查和撤销。接口形式使用服务器组 ff05::1:3；应使用配套 DHCP 服务包，不要改成客户端/中继组 ff02::1:2。

组播请求的服务器回复可能使用同接口的另一个 IPv6 地址；中继必须有到实际回复源的可达路由。地址池应排除远端中继网关及其他静态地址，避免重复分配。

先检查 `display dhcp service verbose` 中的 Relay，再检查客户端及服务端的地址/前缀租约。无租约不能单凭 Relay 进程存在判定成功，需核对实际 Reply 和最终地址。

## 修改和撤销

更换上游目标前先检查路由和 VPN 归属。接口形式撤销 `dhcpv6 relay interface 上行接口`，指定地址形式撤销 `dhcpv6 relay destination 服务器地址`，提交后再撤销不再需要的上游地址与路由。接口 shutdown 暂停相应运行单元，保留配置；恢复后按原意图运行。

## DHCPv4

中继客户口在三层网段内配置网关地址，并指定服务器：

```text
interface Ethernet1
 ip address 198.18.11.1 24
 dhcp select relay
 dhcp relay server-ip 198.19.229.1
#
interface Ethernet0
 ip address 198.19.229.2 24
#
```

服务器使用同一 VPN 中的全局池，池网段属于远端客户链路，无需给服务器伪造该网段接口：

```text
enable dhcp server
ip pool REMOTE4
 network 198.18.11.0 mask 24
 section 0 198.18.11.100 198.18.11.120
 gateway-list 198.18.11.1
 dns-list 192.0.2.53
 lease day 0 hour 1
#
interface Ethernet0
 ip address 198.19.229.1 24
 dhcp select global
#
ip route-static 198.18.11.0 24 Ethernet0 198.19.229.2
```

客户端在连接中继的接口配置 `ip address dhcp-alloc`。分别提交后，检查 `display dhcp relay interface Ethernet1`、`display dhcp client` 与服务器的 `display ip pool name REMOTE4 verbose`。中继应显示服务器地址和 `running`；客户机实际取得 `198.18.11.100/24`、网关 `198.18.11.1`，服务器显示同一 MAC、地址、DNS `192.0.2.53` 及 3600 秒租期。仅中继进程运行不能代替租约和实际路由验证。

撤销时依次执行 `undo dhcp relay server-ip 198.19.229.1`、`undo dhcp select` 并提交，查询应不再列出目标中继；这不会强制客户端立即丢弃此前获得的租约。完整命令参数见[参考](../reference/dhcp.md)，服务器和客户端配置见[DHCPv4 案例](../../examples/dhcp.md)。

[DHCP 功能总览](../dhcp.md)
