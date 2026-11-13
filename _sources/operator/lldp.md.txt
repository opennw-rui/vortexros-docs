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
