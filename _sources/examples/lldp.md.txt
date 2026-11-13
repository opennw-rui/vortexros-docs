# 发现直连邻居

**目标**：从本端确认相邻设备和端口，核对布线。

**前提**：实验链路已 Up，对端已开启 LLDP，且允许在该链路通告设备和端口信息。

## 配置

~~~text
system-view
enable lldp
interface Ethernet 1
 lldp enable
 quit
commit
~~~

LLDP 只发现直连二层邻居，不改变路由或地址分配。

## 验证

使用 `display lldp neighbor brief` 看邻居摘要，再用 `display lldp neighbor interface Ethernet 1` 核对远端标识。邻居不出现时先确认对端确实发送 LLDP。

## 撤销

在 Ethernet 1 执行 `undo lldp enable` 并提交。只有其他接口也不需要 LLDP 时才关闭全局开关。
