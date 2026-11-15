# VortexROS 0.29-dev

0.29-dev使用统一CLI管理接口、路由、隧道、流量策略和网络服务。首次安装从Linux数据面启动，业务网卡可随后通过CLI配置为DPDK模式。当前配套版本见[软件组成](../installation/02-backends.md)。

## 配置和操作

- 每个管理会话拥有独立的待提交配置。通过`display configuration changes`检查修改，`commit`提交，`save`持久保存。
- 接口名称统一使用Ethernet编号；二层子接口、三层子接口、VLAN网关及聚合接口按用途配置。
- 本地账号支持network-operator、network-admin和system-admin。首次改密、SSH公钥、会话管理和Bash/sudo分别见[账号管理](../operator/aaa.md)。
- 首次安装、升级、检查、模拟和失败回退共用一个.run，安装器只更新版本发生变化的组件。

## 路由与网络服务

支持静态路由、路由组、OSPF/OSPFv3、BGP、IS-IS、RIP/RIPng、BFD和VRRP。IS-IS默认路由优先级15，RIP/RIPng100；显式配置可调整优先级。

支持VXLAN EVPN二层/三层业务、All-Active多归属、MPLS L3VPN和6PE。不同业务的RD、RT、VNI、地址族和底层可达性应分别规划。

DHCP客户端、服务端、中继及IPv6自动配置独立管理。空租约池显示零租约；其他健康实例的租约仍可查询。

## 本版行为调整

- ACL仅做无状态permit/deny过滤；TCP established是标志位匹配，不是会话跟踪。
- EVPN配置在保存恢复和业务撤销时保持一致；撤销接口最后一项二层配置后恢复三层接口角色。
- 6PE使用IPv6显式空标签承载IPv6报文，不需要用户手工修改FRR配置。
- 撤销MPLS标签路由后正常释放相关状态，不要求重启数据面。
- RIP在接口重建和路由服务恢复后重新参与协议并恢复已有路由。

完整配置、查询及撤销见[配置案例](../examples/index.md)。使用限制见[版本能力与限制](cli-validation.md)。
