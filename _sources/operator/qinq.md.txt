# QinQ

在客户标签外加一层服务标签，隔离不同客户的二层业务。

[命令参考](reference/vlan.md)

## 配置与影响

简单QinQ端口使用VRP风格的`dot1q-tunnel`。`port default vlan`把整个父接口作为唯一客户侧成员加入对应bridge-domain；不创建隐藏子接口，也不在父接口执行标签改写。对端trunk按外层服务VLAN分类并对称移除/恢复S-Tag，因此客户侧未打标签报文转为单层S-Tag，已有C-Tag的报文转为S-Tag+C-Tag。配置示例：

```text
vlan batch 200
interface Ethernet 2
 portswitch
 port link-type dot1q-tunnel
 port default vlan 200
```

`dot1q-tunnel`父接口接管该端口的完整客户侧分类空间，包括未打标签和所有客户VLAN标签，因此不能同时在该父接口上创建 L2 或 L3 VLAN 子接口。Access、Trunk 和 Hybrid 不允许显式子接口复用其已承载的外层业务 VLAN ID，即使子接口编号不同也会拒绝该配置。其他 VLAN 的显式二层、三层子接口可以共存。同一报文只能由一个接口分类，重复匹配的配置会被拒绝。

查看 `display vlan` 核对服务 VLAN 和客户侧成员。

[完整双端案例](../examples/qinq.md)记录未打标签与客户VLAN10的真实流量、核心双标签报文、CLI成员和撤销结果。
