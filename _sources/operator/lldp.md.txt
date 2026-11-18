# LLDP

发现直连二层邻居及其端口信息。

[命令参考](reference/lldp.md) · [配置案例](../examples/lldp.md)

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
