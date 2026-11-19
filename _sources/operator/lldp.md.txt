# LLDP

发现直连二层邻居及其端口信息。

[命令参考](reference/lldp.md) · [配置案例](../examples/lldp.md)

## 工作原理与使用边界

LLDP（IEEE 802.1AB）在相邻链路上发布设备、端口和能力等信息，用于接线核对与拓扑发现。它不建立路由，也不转发到远端跨越多跳发现网络。

按全局和接口配置选择发布范围。对不可信接入链路公开设备标识可能泄露网络信息，应只在需要发现的端口启用。对端不支持、没有发送或报文被链路策略过滤时，本端没有邻居记录不一定表示物理链路断开。

修改后核对本端发送接口和对端接收记录；邻居信息按通告 TTL 老化，关闭后不必立即从对端表中消失。详细字段和操作见下列页面。

## 配置与验证

```text
enable lldp
commit
display lldp neighbor brief
display lldp neighbor interface Ethernet 1
```

关闭LLDP：

```text
undo enable lldp
commit
```

LLDP未收敛或后端不可用时会在`display health`和告警中显示，但不会触发VPP物理接口所有权回滚。

`display lldp local` 的 `Device system MAC` 是设备系统 MAC。线上通告的
Chassis ID 使用各物理接口的 MAC，按对端 `display lldp neighbor interface`
及实际 LLDP 报文逐口核对。设备系统 MAC 与这些接口 MAC 可以不同。

## 单端口控制与邻居老化

开启全局 LLDP 后，物理接口默认发送并接收通告。只需关闭某个端口时，不要关闭全局开关：

```text
system-view
```

配置清单：

```text
interface Ethernet 0
 undo lldp enable
#
```

CLI 操作：

```text
commit
display lldp local
display lldp neighbor brief
```

在对端查看邻居可能仍看到旧记录，直到其保持时间到期。这不表示关闭失败；核对最后收到时间是否继续更新。实际双链路验证中，关闭一条链路的本端 LLDP 后，该端口没有再发出本机通告，另一端口继续每 30 秒发送；关闭端口仍能收到对端通告，不能把收到的包误认为本端仍在发送。

恢复时，在该端口执行 `lldp enable` 并提交，随后在两端查询邻居。关闭全局 LLDP 则使用 `undo enable lldp`；此后本机 LLDP 查询明确提示功能未启用。此过程不改变业务转发与 IP 地址。
