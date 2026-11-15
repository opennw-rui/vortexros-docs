# 交换功能与保存

`enable switch`启用交换功能。关闭前先撤销显式VLAN、桥域、二层端口、网关和策略等依赖，否则提交会被拒绝。

~~~text
undo enable switch
commit
save
~~~

关闭后，未被业务引用的隐式默认VLAN不作为独立配置保存。重新启用交换功能时，仍需按所需业务配置端口和VLAN。

需要恢复启动配置时，先查看`display startup`，再执行`apply config`并确认。该操作会替换当前运行配置，应先保存需要保留的修改。

[VLAN端口](ports.md) · [配置管理](../cli/configuration.md)
