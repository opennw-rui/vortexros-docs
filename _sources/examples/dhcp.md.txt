# DHCP 地址池

## 拓扑与用途

服务器 P2 的 `host-p2r12` 与客户端 P1 的 `host-p1r12` 直接相连，地址段为 `172.20.15.0/24`。服务器接口属于 `DHCP-EMPTY` VPN 实例，客户端接口属于本机的 `CLI-UNDER` 实例。两个名称是各节点的本地路由域，不要求相同。本例使用开发服务器的隔离接口名，部署时换成实际接口。

服务器采用全局地址池，指定分配范围、排除地址、固定绑定、网关、DNS、域名和一小时租期。客户端动态安装地址；学习到的路由是否安装，由客户端路由开关控制。DNS 选项不会改写 Linux 系统解析配置。

## 两端配置

P2：

```text
system-view
ip vpn-instance DHCP-EMPTY
 quit
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
 quit
interface host-p2r12
 ip binding vpn-instance DHCP-EMPTY
 ip address 172.20.15.1 255.255.255.0
 dhcp select global
 quit
commit
```

固定绑定的 MAC 必须替换为客户端实际 MAC。不要在仍由其他 DHCP 服务器管理的同一广播域直接复制本例。

P1：

```text
system-view
ip vpn-instance CLI-UNDER
 quit
interface host-p1r12
 ip binding vpn-instance CLI-UNDER
 ip address dhcp-alloc
 quit
commit
```

先绑定 VPN 实例，再配置地址或客户端。修改绑定会清除接口的原地址配置。两个 VPN 实例均使用各自默认的 IPv4 地址族；需要接入已有实例时，不重复创建。

## 实际结果

```text
display dhcp service verbose
display ip pool name CLI-LAN verbose
display ip pool interface host-p2r12 verbose
```

在空租约库时，查询成功并显示 `Used 0`；客户端获取地址后，全局池显示 `Used 1`。即使接口保留了未启用的旧接口池配置，租约仍归属当前启用的全局池，接口池查询不重复计数。

客户端实际取得 `172.20.15.110/24`，服务器为 `172.20.15.1`，租期为 `3600` 秒。底层 Kea 租约列表同时有该条记录。客户端真实 CLI：

```text
display dhcp client interface host-p1r12
ping -vpn-instance CLI-UNDER -a 172.20.15.110 -c 3 172.20.15.1
```

实际探测：`3 packets transmitted, 3 received, 0% packet loss`。后续将 DNS 改为 `1.1.1.1`，池详情也显示该值。撤销显式租期后再次续租，实际租期为默认 `86400` 秒；这与修改前的 `3600` 是不同阶段的结果。

## 接口池方式

若每个接口只需要一个地址池，可在已配置地址的接口下使用：

```text
interface host-p2r12
 dhcp select interface
 dhcp server ip-range 172.20.15.100 172.20.15.120
 dhcp server gateway-list 172.20.15.1
 dhcp server dns-list 1.1.1.1
 dhcp server lease day 0 hour 1
 quit
commit
```

这会切换接口的服务模式。全局池与接口池的配置可以保留，只有当前选中的模式参与此接口的服务和显示。配置本身存在，不表示该模式正在运行。接口池扩展参数及撤销语法见[命令参考](../operator/reference/dhcp.md)。

## 保存、修改与撤销

验证后执行 `save`。修改选项后，应让客户端续租再检查报文或租约，不能只看配置已提交。

P1 停用客户端：

```text
system-view
interface host-p1r12
 undo ip address dhcp-alloc
 quit
commit
```

P2 停用服务并删除全局池：

```text
system-view
interface host-p2r12
 undo dhcp select
 quit
undo ip pool CLI-LAN
commit
```

本轮实际撤销后，相关客户端和服务端进程停止，成功的池及服务查询均为空；客户端动态地址、动态路由已撤销。保留接口本身的静态地址及 VPN 配置，不将它们当作 DHCP 自动清理对象。若其他接口仍提供 DHCP，保留全局开关；全部不再使用时再 `undo enable dhcp server` 并提交、保存。
