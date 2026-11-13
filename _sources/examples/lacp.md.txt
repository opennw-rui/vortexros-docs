# LACP 聚合

**目标**：用两根链路组成一个三层上联。一根链路断开时，剩余可用成员继续转发。

**前提**：两端均支持 LACP，Ethernet 1、Ethernet 2 为实验口，未承载管理或单独业务。对端将对应两口加入同一 LACP 聚合，地址设为 192.0.2.2/30。

## 配置

~~~text
system-view
interface Eth-Trunk 10
 mode lacp-static
 trunkport Ethernet 1 to Ethernet 2
 ip address 192.0.2.1 255.255.255.252
 quit
commit
~~~

地址配置在聚合接口上。成员口不再独立承载三层配置。参见[链路聚合](../operator/link-aggregation.md)。

## 验证

查看 `display eth-trunk 10`，确认两端都有活动成员；Ping 192.0.2.2。断开一根实验链路，确认剩余成员转发，再插回并等待成员恢复。

## 撤销

在系统视图执行 `undo interface Eth-Trunk 10`，提交后核对成员已退出。先迁移引用聚合接口的路由和策略。
