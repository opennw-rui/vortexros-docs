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

`dot1q-tunnel`父接口接管该端口的完整客户侧分类空间，包括未打标签和所有客户VLAN标签，因此不能同时在该父接口上创建 L2 或 L3 VLAN 子接口。

显式子接口使用的实际外层 VID 与全局 VLAN 对象互斥，适用于所有父接口和 dot1q/dot1ad/QinQ，配置顺序不影响结果。子接口实例后缀、bridge-domain编号及内层客户VID独立，不占用全局VLAN编号。不同父接口可复用没有全局VLAN对象的同一外层VID；同一父接口的匹配集合不能重叠。系统为交换端口派生的内部对象不按显式子接口处理。

开发候选还支持固定外层、多个内层 VID 或任意内层的[显式 L2 子接口](subinterfaces-l2.md#固定外层多个内层的-qinq)。它复用同一套原生子接口分类，不是新的父端口规则引擎，也不改变上述简单 QinQ 端口语义。多内层的对称标签恢复有限制，提交前必须明确选择保留标签或只移除外层，不能直接沿用固定双标签的 pop2 默认值。

查看 `display vlan` 核对服务 VLAN 和客户侧成员。

[完整双端案例](../examples/qinq.md)记录未打标签与客户VLAN10的真实流量、核心双标签报文、CLI成员和撤销结果。
