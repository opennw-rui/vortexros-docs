# QinQ

在客户标签外加一层服务标签，隔离不同客户的二层业务。

[命令参考](reference/vlan.md)

## 配置与影响

简单QinQ端口使用VRP风格的`dot1q-tunnel`。`port default vlan`把整个父接口作为唯一客户侧成员加入对应bridge-domain；不创建隐藏子接口，也不在父接口执行标签改写。对端trunk按外层服务VLAN分类并对称移除/恢复S-Tag，因此客户侧未打标签报文转为单层S-Tag，已有C-Tag的报文转为S-Tag+C-Tag。该模式不使用已删除的`port link-mode`兼容命令：

```text
vlan batch 200
interface Ethernet 2
 portswitch
 port link-type dot1q-tunnel
 port default vlan 200
```

`dot1q-tunnel`父接口接管该端口的完整客户侧分类空间，包括未打标签和所有客户VLAN标签，因此禁止在该父接口上创建任何显式L2/L3 VLAN子接口。trunk则只禁止显式子接口复用其已经派生的业务VLAN ID；即使显式子接口的instance后缀不同也会在Candidate/commit边界拒绝。该限制避免父接口与子接口同时接收同一报文，保证桥域成员、策略挂载和严格读回只有一个权威对象。

从曾创建客户侧DEFAULT隐藏子接口的旧版本warm升级时，控制面会在同一VPP会话中
识别该父接口下带DEFAULT标志的旧子接口，先从其实际bridge-domain解绑再删除；
非DEFAULT显式子接口和其他父接口不属于该清理范围。清理后简单QinQ仍只保留父接口
这一权威客户侧成员。


查看 `display vlan` 核对服务 VLAN 和客户侧成员。
