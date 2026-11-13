# VortexROS 0.28 操作手册

本手册面向设备管理员，说明VortexROS 0.28的功能、配置命令、生效结果、检查方法和撤销步骤。功能限制会在相应章节中明确说明。

## 配置指南

1. [CLI、Candidate、commit 与 save](01-cli.md)
2. [系统访问、健康与服务](02-system-services.md)
3. [物理接口、聚合、VLAN、BD 与邻居](03-interfaces-l2.md)
4. [IPv4/IPv6、VPN、静态路由与路由组](04-ip-routing.md)
5. [路由策略、OSPF、BGP、IS-IS、RIP、BFD 与 VRRP](05-dynamic-routing.md)
6. [GRE、IP-in-IP、VXLAN/NVE、WireGuard 与 AmneziaWG](06-tunnels.md)
7. [ACL、QoS、MQC、MSS 与 nat-policy](07-policy.md)
8. [DHCP、LLDP 与 SNMP](08-network-services.md)
9. [诊断、清理、健康与服务恢复](09-operations.md)
10. [MPLS LDP 与 L3VPN](10-mpls-l3vpn.md)
11. [VXLAN EVPN](11-vxlan-evpn.md)
12. [全命令参考](reference/commands.md)

首次在新硬件上部署时，还必须完成[真机首次验收](../installation/08-hardware-acceptance.md)。
该检查用于确认驱动接管、LCP、重启恢复和管理连接，不以实验室结果代替设备实测。

## 通用阅读约定

- `[*VortexROS]`表示当前会话 Candidate 已修改；`[~VortexROS]`表示无未提交修改。
- 配置命令先保存在当前登录会话中，输入 `commit` 后才正式生效。
- `save`只保存全局 Running；不保存任何会话私有 Candidate。
- `undo`应按对象精确撤销。被引用对象通常必须先解除引用。
- 示例名称、地址和输出均已脱敏；计时、计数器、接口索引等运行值以设备实测为准。

## 推荐的操作顺序

配置业务时建议按以下顺序操作：

```text
配置 -> display configuration candidate -> commit -> display this
     -> display 运行状态 -> 转发/邻居验证 -> 精确 undo -> commit
     -> save -> 设备重启 -> 再次验证
```

完整命令语法和可用视图请查看[全命令参考](reference/commands.md)。

~~~{toctree}
:maxdepth: 1

02-system-services
03-interfaces-l2
04-ip-routing
05-dynamic-routing
06-tunnels
07-policy
08-network-services
10-mpls-l3vpn
11-vxlan-evpn
~~~
