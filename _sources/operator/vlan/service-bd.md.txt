# 业务桥域绑定

## 服务桥域 VLAN 绑定撤销

开发服务器使用空闲 VLAN666、bridge-domain666 设置 l2 binding vlan666，提交后 display this 显示该绑定。撤销命令是无参数的 undo l2 binding vlan；提交后 bridge-domain666 仍保留，但 display this 不再包含绑定。最后删除临时桥域与 VLAN。该隔离检查验证绑定配置的创建和撤销；具体业务转发沿用已有服务桥域案例，不将无端口桥域冒充流量验证。

[功能目录](../vlan.md) · [命令参数](../reference/vlan.md)
