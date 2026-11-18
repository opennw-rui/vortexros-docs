# 查询来源

## 全接口监听

默认接收公网和 VPN 实例内的 IPv4 SNMP 查询。下面两条命令作用相同，选择一种即可：

```text
snmp-agent protocol source-interface all-interface
```

或：

```text
snmp-agent protocol source-status all-interface
```

监听范围不代替认证。还需启用对应协议版本，并配置只读 community 或 SNMPv3 用户。

## 限定公网接口

```text
snmp-agent protocol source-interface Ethernet0
```

Ethernet0 应已配置可用的 IPv4 地址。提交后，监控平台使用该接口地址查询。

## 限定 VPN 接口

示例中，设备与监控平台直连，监控平台位于 MONITOR 实例，地址为 198.18.249.2/30。设备配置：

```text
ip vpn-instance MONITOR
#
interface Ethernet 99
 ip binding vpn-instance MONITOR
 ip address 198.18.249.1 255.255.255.252
#
snmp-agent
snmp-agent sys-info version v3
snmp-agent usm-user v3 monitor authentication-mode sha2-256 AuthPass123 privacy-mode aes128 PrivPass123
snmp-agent protocol source-interface vpn-instance MONITOR Ethernet99
```

返回系统视图提交，监控平台使用 198.18.249.1 和上述 authPriv 凭据查询。若同时配置 Trap 源，它必须符合所选监听 VPN 的约束。

## 验证

```text
display snmp-agent sys-info
display snmp-agent usm-user
display interface Ethernet99
ping -vpn-instance MONITOR -c 2 198.18.249.2
```

实际 VPN 内查询已返回设备 sysName 为 VortexROS，IF-MIB 对应接口描述为 Ethernet99；VRF 内连通性探测为 2/2。接口索引由设备分配，应从本机 IF-MIB 读取，不要复制其他设备的数值。

接口查询应同时显示实际地址、VPN 归属和计数。对尚未出现的预配置接口，配置存在不表示查询地址已经可达。

## 撤销

恢复默认的全接口监听：

```text
undo snmp-agent protocol source-interface
commit
```

切换监听范围后重新核对 display 和监控平台查询；设备自动应用相关设置，无需手工修改 Linux 内核参数。不再使用 SNMP 时，执行 undo snmp-agent 并提交；只删除本例的接口或 VPN 时，先解除对应的 SNMP 引用。

[通知源与 Trap](notifications.md) · [参数](../reference/snmp.md) · [完整案例](../../examples/snmp.md)
