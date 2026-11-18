# IPv6 网关

VRRPv6 使用链路本地虚拟地址作为网关，也可在同组中增加全局单播虚拟地址。组内第一条地址必须是链路本地地址；系统会在保存和下发时自动排列。只有全局虚拟地址、没有链路本地虚拟地址的组不能提交。

## 配置

两台设备的 Ethernet0 接入同一网段。设备 A 使用以下配置：

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 ipv6 enable
 ipv6 address 2001:db8:100::1 64
 vrrp6 vrid 20 virtual-ip fe80::fe
 vrrp6 vrid 20 virtual-ip 2001:db8:100::fe
 vrrp6 vrid 20 priority 120
#
```

CLI 操作：

```text
commit
```

设备 B 使用地址 2001:db8:100::2/64，虚拟地址和 VRID 相同，省略 priority，使用默认优先级 100。双方的通告间隔必须一致，默认为 1 秒。IPv6 组无需 IPv4 的 version-3 命令。

默认允许抢占，默认不接收发给非地址拥有者虚拟 IP 的本机业务。需要 ping 虚拟地址或通过虚拟地址访问设备服务时，在两端加入 `vrrp6 vrid 20 accept-mode enable`。正常路由转发与虚拟地址上的本机服务应分别验证。

## 检查

```text
display vrrp6 brief
display vrrp6 interface Ethernet 0
display vrrp6 20
display vrrp6 statistics
```

应看到一台 Master、一台 Backup，虚拟地址顺序以 fe80::fe 开始。客户端使用链路本地网关时必须指定接口；同一链路上的所有设备还必须具有可达的业务路由。

## 撤销

先迁移客户端网关，再在两台设备执行：

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 undo vrrp6 vrid 20
#
```

CLI 操作：

```text
commit
display vrrp6 brief
```

删除组不删除接口原有的 IPv6 地址。单独撤销链路本地虚拟地址时，若还保留全局虚拟地址，提交会失败；应一起撤销整个组或补上另一条链路本地虚拟地址。

[功能目录](../vrrp.md) · [命令参数](../reference/vrrp.md)
