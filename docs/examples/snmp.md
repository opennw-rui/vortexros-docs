# SNMP 轮询

## 拓扑与作用

VortexROS Ethernet0 使用 192.0.2.65/30，连接地址为 192.0.2.66/30 的监控平台（NMS）。NMS 是外部监控应用，不承担本例的路由或 CE 功能。通过平台自身的管理界面配置地址与设备轮询，无需在路由器上运行 Linux 网络命令。

本例演示 SNMPv2c 只读轮询。community 不加密，实际管理网络优先使用 [SNMPv3 authPriv](../operator/snmp.md)。

## VortexROS 配置

~~~text
system-view
~~~

配置清单：

~~~text
sysname SNMP-LAB
interface Ethernet0
 ip address 192.0.2.65 255.255.255.252
#
snmp-agent
snmp-agent sys-info version v2c
snmp-agent sys-info contact Network Operations
snmp-agent sys-info location Site-A
snmp-agent protocol source-interface Ethernet0
snmp-agent community read lab-read
~~~

CLI 操作：

~~~text
commit
display snmp-agent sys-info
~~~

只允许访问指定源接口的主 IPv4 地址，没有启用 Trap 或写权限。已有监控配置时，应保留其他对象。

## 监控平台设置

| 项目 | 值 |
| --- | --- |
| 设备地址 | 192.0.2.65 |
| 协议与端口 | SNMPv2c，UDP 161 |
| community | lab-read |
| sysName.0 | .1.3.6.1.2.1.1.5.0 |
| sysLocation.0 | .1.3.6.1.2.1.1.6.0 |

两端先确认三层可达，平台所在网络及接口 ACL 应允许轮询和回包。

## 验证

VortexROS 示例输出：

~~~text
SNMP agent configuration: enabled
Versions: v2c=true v3=false
Contact: Network Operations
Location: Site-A
Source interface: Ethernet0
VPN instance: public-net
~~~

在平台执行上述 OID 查询，应返回 sysName 为 SNMP-LAB、sysLocation 为 Site-A。随后按[监控项目](../operator/snmp/monitoring.md)加入接口状态及 64 位流量计数。仅看到配置 enabled 不能代替平台实际查询。

## 撤销

若本例是设备唯一的 SNMP 配置，可整体关闭：

~~~text
system-view
undo snmp-agent
commit
display snmp-agent sys-info
~~~

平台应不再收到回复，但管理地址仍可达。共享监控配置时，只撤销本例 community、源和相关对象。拆除专用管理链路时再撤销其 IP，按需 save；不要切断仍在使用的管理连接。
