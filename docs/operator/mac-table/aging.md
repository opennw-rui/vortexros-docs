# 老化与静态项

## 老化与检查

动态MAC老化时间是全局参数。需要修改时，在系统视图执行：

```text
mac-address aging-time 600
commit
```

提交后，所有VLAN对应转发域的动态MAC老化时间变为600秒。恢复默认值：

```text
undo mac-address aging-time
commit
```

默认值不显示在配置中；只有非默认值才进入 `display current-configuration`。VPP以整分钟保存该参数，因此配置值必须是60秒的整数倍。

用 `display mac-address` 查看实际表项。

静态 MAC 表项的出口必须实际属于该表项的桥域；trunk与业务桥域先转换为Linux控制端口和VLAN后再校验，
普通静态项由switchd写入Linux FDB并经LCP进入对应VPP bridge-domain，不能把其他桥域的端口写入当前桥域。

[功能目录](../mac-table.md) · [命令参数](../reference/bridge-domains.md)

[静态MAC完整案例](../../examples/static-mac.md)记录关闭学习/未知单播泛洪后的真实3/3，以及删除目标项后的0/3对照。
