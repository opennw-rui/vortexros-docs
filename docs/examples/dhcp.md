# DHCP 地址池

## 拓扑与用途

服务器 P2 的 `Ethernet0` 与客户端 P1 的 `Ethernet0` 直接相连，地址段为 `172.20.15.0/24`。服务器接口属于 `DHCP-EMPTY` VPN 实例，客户端接口属于本机的 `CLI-UNDER` 实例。两个名称是各节点的本地路由域，不要求相同。两端均使用 VortexROS 配置服务和客户端。

服务器采用全局地址池，指定分配范围、排除地址、固定绑定、网关、DNS、域名和一小时租期。客户端动态安装地址；学习到的路由是否安装，由客户端路由开关控制。DNS 选项不会改写 Linux 系统解析配置。

## 两端配置

P2：

```text
system-view
```

配置清单：

```text
ip vpn-instance DHCP-EMPTY
#
enable dhcp server
ip pool CLI-LAN
 vpn-instance DHCP-EMPTY
 network 172.20.15.0 mask 255.255.255.0
 section 0 172.20.15.100 172.20.15.120
 excluded-ip-address 172.20.15.105 172.20.15.106
 static-bind ip-address 172.20.15.110 mac-address c2a6-5677-567c
 gateway-list 172.20.15.1
 dns-list 8.8.8.8 1.1.1.1
 domain-name cli.example
 lease day 0 hour 1
#
interface Ethernet0
 ip binding vpn-instance DHCP-EMPTY
 ip address 172.20.15.1 255.255.255.0
 dhcp select global
#
```

CLI 操作：

```text
commit
```

固定绑定的 MAC 必须替换为客户端实际 MAC。不要在仍由其他 DHCP 服务器管理的同一广播域直接复制本例。

P1：

```text
system-view
```

配置清单：

```text
ip vpn-instance CLI-UNDER
#
interface Ethernet0
 ip binding vpn-instance CLI-UNDER
 ip address dhcp-alloc
#
```

CLI 操作：

```text
commit
```

先绑定 VPN 实例，再配置地址或客户端。修改绑定会清除接口的原地址配置。两个 VPN 实例均使用各自默认的 IPv4 地址族；需要接入已有实例时，不重复创建。

## 验证

```text
display dhcp service verbose
display ip pool name CLI-LAN verbose
display ip pool interface Ethernet0 verbose
```

在空租约库时，查询成功并显示 `Used 0`；客户端获取地址后，全局池显示 `Used 1`。租约按服务器返回的子网编号归属地址池，不能仅凭地址所在网段判断。即使接口保留了旧接口池配置，新全局池租约也不会计入接口池。

客户端取得的地址、服务器和租期应与地址池相符。以下为客户端示例输出：

```text
display dhcp client interface Ethernet0
ping -vpn-instance CLI-UNDER -a 172.20.15.110 -c 3 172.20.15.1
```

实际探测：`3 packets transmitted, 3 received, 0% packet loss`。后续将 DNS 改为 `1.1.1.1`，池详情也显示该值。撤销显式租期后再次续租，实际租期为默认 `86400` 秒；这与修改前的 `3600` 是不同阶段的结果。

## 接口池方式

若每个接口只需要一个地址池，可在已配置地址的接口下使用：

```text
interface Ethernet0
 dhcp select interface
 dhcp server ip-range 172.20.15.100 172.20.15.120
 dhcp server gateway-list 172.20.15.1
 dhcp server dns-list 1.1.1.1
 dhcp server lease day 0 hour 1
#
```

CLI 操作：

```text
commit
```

这会切换接口的服务模式。全局池与接口池的配置可以保留，只有当前选中的模式在此接口提供服务。模式切换不删除已有租约：在原池配置仍保留时，历史租约继续归属原池，当前接口池不会重复计数。配置或未到期租约的存在，都不表示客户端此刻在线。接口池扩展参数及撤销语法见[命令参考](../operator/reference/dhcp.md)。

## 保存、修改与撤销

验证后执行 `save`。修改选项后，应让客户端续租再检查报文或租约，不能只看配置已提交。

P1 停用客户端：

```text
system-view
```

配置清单：

```text
interface Ethernet0
 undo ip address dhcp-alloc
#
```

CLI 操作：

```text
commit
```

P2 停用服务并删除全局池：

```text
system-view
```

配置清单：

```text
interface Ethernet0
 undo dhcp select
#
undo ip pool CLI-LAN
```

CLI 操作：

```text
commit
```

撤销后查询客户端、池和服务状态，确认本例绑定、动态地址及动态路由已移除。静态地址和 VPN 配置是独立对象，不随 DHCP 自动删除。其他接口仍提供 DHCP 时保留全局开关，否则再 undo enable dhcp server、提交并保存。

## 切换模式后的租约核对

同一网段从全局池切换到接口池后，分别查询，确认租约没有被混算：

```text
<VortexROS> display ip pool interface Ethernet 1 verbose
<VortexROS> display ip pool name LAN used
```

一次实际切换中，接口池子网编号为 892164763，只统计新分配的一个租约；原全局池子网编号为 331230444，保留两个尚未过期的历史租约。两份查询分别显示 `Used 1`、`Used 2`。子网编号由池名、地址族和 VPN 实例确定，实际数值随配置不同；同网段不等于同一个地址池。
