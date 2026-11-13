# BFD 故障检测

**目标**：在实验链路上建立独立 BFD 会话，观察路径失效。独立会话只提供检测状态；需要联动撤路时，应使用对应协议的 BFD 绑定。

**前提**：两台设备的 Ethernet 1 直连，地址为 192.0.2.1/30、192.0.2.2/30，双向可达。

## 配置

~~~text
system-view
bfd
bfd TO-PEER bind peer-ip 192.0.2.2 source-ip 192.0.2.1 interface Ethernet 1
 log-session-changes
 quit
commit
~~~

对端交换源和对端地址。保留当前缺省收发间隔 1000 ms、检测次数 3；实际检测时间由会话协商决定。参见 [BFD](../operator/bfd.md)。

## 验证

查看 `display bfd session TO-PEER`，确认状态及实际定时器。在实验链路断开、恢复后观察 Down 和 Up，区分会话检测与路由协议收敛。

## 撤销

在两端的系统视图执行 `undo bfd TO-PEER` 并提交。不要关闭仍被其他协议或会话使用的全局功能。
