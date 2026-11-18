# Vlanif 网关

Vlanif 为同编号 VLAN 提供三层网关。先启用交换功能、创建 VLAN 并配置接入端口，再创建 Vlanif 和网关地址；完整双端配置见[VLAN 网关案例](../../examples/vlan-gateway.md)。

## 激活条件

| 状态 | 必要条件 |
|---|---|
| PHY Up | Vlanif 未 shutdown、已成功创建，所属 VLAN 至少有一个实际转发成员处于管理 Up 且链路 Up |
| Protocol Up | PHY Up，且 Vlanif 已配置有效 IPv4 或 IPv6 地址 |
| 自动 Down | 所有 VLAN 成员链路断开、成员全部退出该 VLAN，或 Vlanif 被 shutdown |
| 自动恢复 | 成员重新满足条件，且 Vlanif 没有被显式 shutdown |

access 端口须属于该 VLAN；trunk 端口须允许该 VLAN。只创建 VLAN、只设置 PVID 或只有网关自身，不足以使 Vlanif Up。ipv6 enable 不等于已配置 IPv6 地址。二层端口无需配置 IP，网关地址应放在 Vlanif 上。

## 检查

~~~text
display vlan 100
display interface Vlanif 100
display ip interface brief
display ip routing-table protocol direct
~~~

先检查 VLAN 的实际端口及链路，再检查网关地址、直连路由和客户到网关的探测。Up 不代表客户地址、VLAN 标签或业务回程路由已经正确。

## 停用与删除

临时停用在 Vlanif 视图执行 shutdown；恢复使用 undo shutdown。删除前解除路由协议、策略及其他引用，再执行 undo interface Vlanif 100 并 commit。删除网关不会自动表示二层 VLAN 业务也应删除；仍共用的 VLAN 和成员端口应保留。需要启动后保持当前配置时执行 save。
