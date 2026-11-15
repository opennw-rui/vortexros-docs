# VRRP 网关

**目标**：让两台路由器共享一个 IPv4 默认网关，主路由器故障后由备用路由器接管。

**前提**：两台设备的 Vlanif 100 接入同一 VLAN，接口地址分别为 192.0.2.1/24 和 192.0.2.2/24，且双方都有可用上游路径。

## 配置

两台设备均运行下列命令。仅首选主机在 `quit` 前加入 `vrrp vrid 10 priority 120`；备用机保持默认优先级 100。

~~~text
system-view
interface Vlanif 100
 vrrp vrid 10 version-3 send-packet-mode v3-only
 vrrp vrid 10 virtual-ip 192.0.2.254
 quit
commit
~~~

客户端使用 192.0.2.254 作为网关，不使用任一设备的物理地址。参见 [VRRP](../operator/vrrp.md)。

## 验证

用 `display vrrp brief` 确认一台 Master、一台 Backup。从客户端连续探测虚拟网关和上游。断开 Master 的示例 VLAN 接口，确认 Backup 接管且上游探测恢复；重新接入后观察角色。

## 撤销

先迁移客户端网关。在两台 Vlanif 100 上撤销 `undo vrrp vrid 10` 并提交。

## 单节点撤销的真实结果

另一次隔离 CLI 验证在已有 Vlanif400 上创建 IPv4/IPv6 VRRP40，使用198.18.104.3和fe80::40。该部分只验证单节点配置及撤销，不代替上文双机主备切换。

```text
interface Vlanif400
 vrrp vrid 40 version-3 send-packet-mode v3-only
 vrrp vrid 40 virtual-ip 198.18.104.3
 vrrp6 vrid 40 virtual-ip fe80::40
quit
commit
display vrrp brief
display vrrp6 brief
```

示例输出：

```text
40    Master  Vlanif400  IPv4  198.18.104.3  100       100     1.00s
40    Master  Vlanif400  IPv6  fe80::40    100       100     1.00s
```

```text
interface Vlanif400
 undo vrrp vrid 40
 undo vrrp6 vrid 40
quit
commit
display vrrp brief
display vrrp6 brief
```

两个查询均成功返回 `Total: 0`。接口原有地址保留。
