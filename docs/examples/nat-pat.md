# 源 NAT

**目标**：让实验网段访问外部 IPv4 网络，使用路由所选出接口地址和端口转换。

**前提**：VPP 已运行；Vlanif 100 是实验 LAN 三层网关；外部接口已有 IPv4 地址和有效路由。入接口以 192.0.2.0/24 为实验网段。

## 配置

~~~text
system-view
nat-policy address-set name LAB-LAN
 address 192.0.2.0/24
 quit
nat-policy name LAB-SNAT
 statistic enable
 rule 10
  source address-set name LAB-LAN
  action snat pat interface
  quit
 quit
interface Vlanif 100
 nat-policy LAB-SNAT inbound
 quit
commit
~~~

规则只匹配从该接口进入且源地址属于实验网段的流量。该策略不创建上游路由。参见 [NAT](../operator/nat.md)。

## 验证

从 LAN 发起一次新的 TCP 连接；查看 `display nat-policy sessions name LAB-SNAT`，确认原始与转换后的地址，再看 `display nat-policy statistics name LAB-SNAT` 的计数变化及客户端是否收到回包。

## 撤销

在 Vlanif 100 撤销 `undo nat-policy LAB-SNAT inbound`，返回系统视图撤销 `undo nat-policy name LAB-SNAT` 和 `undo nat-policy address-set name LAB-LAN`，提交后用新连接确认该策略不再匹配。不要用全局会话清理替代检查。
