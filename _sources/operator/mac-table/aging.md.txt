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

静态 MAC 的出口必须属于对应业务桥域；access、trunk 和 VLAN 映射应先配置正确，跨桥域出口会被拒绝。

[功能目录](../mac-table.md) · [命令参数](../reference/bridge-domains.md)

[静态MAC完整案例](../../examples/static-mac.md)说明关闭学习与未知单播泛洪时，如何验证目标静态 MAC 的转发及删除效果。
