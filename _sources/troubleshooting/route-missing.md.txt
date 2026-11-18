# 邻居正常但 FIB 缺路由

BGP 已 Established，目标前缀仍未转发。先检查目标前缀是否进入本设备 RIB，再检查下一跳和活动数据面。以下为默认路由域的 IPv4 示例；业务在 VPN 实例中时，应在同一 VPN 下核对。

~~~text
display bgp peer
display bgp routing-table
display ip routing-table 203.0.113.0 24
display dataplane
display health verbose
display alarm active
~~~

1. BGP 表没有目标前缀时，核对对端是否通告该地址族和精确前缀，并检查本端导入、对端导出策略。
2. BGP 有前缀而 RIB 没有优选项时，核对下一跳能否递归解析，以及是否有更优路径。修正解析路由或策略后重新查询。
3. RIB 已优选时，VPP 数据面用 `display ip fib` 查目标前缀、下一跳和出接口；Linux 数据面可在 Ubuntu 用 `ip route get 203.0.113.1` 查实际选择。命名 VPN 分别使用 `display ip fib vpn-instance BLUE` 或 `ip route get 203.0.113.1 vrf BLUE`，用实际名称替换 BLUE。
4. 若 RIB 已选中、下一跳已解析，但活动 FIB 仍缺项，记录受影响前缀及 `display health verbose`、告警和 `journalctl -u vortexros-route-zapi` 的同一时段输出。修正后从源业务端测目标和回程，再保存配置。

普通 VPP 路径的 `Lookup-Table` 显示 `-`，显式查表显示目标 VPP 表号，目标为默认表时显示 `0`。见[路由表与 FIB](../operator/routing-tables.md)。
