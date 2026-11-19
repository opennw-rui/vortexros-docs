# Debug 2

本版在0.30-dev Debug1基础上新增灵活QinQ和统一日志查询，改进数据面配置显示、
NUMA查询、软件包名解析及端口模式转换。FRR1.9和Kea配套版本保持不变。

## 更新方式

下载[本版统一安装包](https://github.com/opennw-rui/VortexROS/releases/tag/v0.30-dev-debug2)，执行：

~~~sh
sudo sh ./vortexros_0.30-dev-debug2_amd64.run
~~~

同一文件支持检查、模拟和安装，按组件实际版本选择更新内容。
原启动配置保留；本版配套VPP需要重启，其承载业务会短暂中断。
维护前确认已提交并保存，更新后用display version、display health和实际业务地址核对。
操作和回退步骤见[升级与回退](../installation/07-upgrade-uninstall.md)。

## 灵活QinQ

在Hybrid客户接口按C-VLAN选择S-VLAN；网络侧增加服务标签，回程保留原客户标签。
同一服务可以包含多个不连续客户VLAN，不必逐个创建子接口。

~~~text
interface Ethernet0
 portswitch
 port link-type hybrid
 port vlan-stacking vlan 10 to 12 30 stack-vlan 100
#
~~~

服务VLAN100须预先创建。默认VLAN1仍遵循普通Hybrid成员配置；
若只允许指定客户集合，应明确撤销默认untagged VLAN1。

本版验证了双向流量、广播/未知单播准入、部分与整组撤销、保存恢复、
接口策略继承、VLAN限速和服务桥域绑定。完整配置、显示及撤销见[灵活QinQ](../operator/qinq-flexible.md)。
同一S-VLAN仍共享MAC学习域，不等同于为每个客户VLAN建立独立学习范围。

## 日志和运行状态

新增[统一日志查询](../operator/operations/logs.md)：

~~~text
display logbuffer
display logbuffer service frr last 100
display logbuffer service control since 10 last 50
~~~

默认显示本次启动最近100条记录，沿用过滤和分页。
查询直接使用系统日志，不增加独立日志服务；只读用户也可通过授权入口查询。

数据面设备显示实际PCI NUMA节点；unknown表示设备没有给出节点，
unavailable表示无法读取。不能将这两者当作NUMA0。
登录横幅、display version及软件包版本对应当前实际控制层版本。

## 配置与模式切换

dataplane配置先显示CPU、大页和IOMMU等全局项，再显示设备，分隔统一使用#。
配置读取、视图查询和保存恢复使用相同语义。

Access、Trunk、Hybrid切换前须清理当前模式的非默认VLAN、PVID及QinQ规则。
撤销VLAN1也是非默认状态；需要恢复当前模式的默认成员后再转换。
重复输入相同模式不清空现有业务。步骤见[端口模式](../operator/vlan/ports.md)。

在/VortexROS/install中的系统包可直接使用包名，不必写完整路径。
检查、模拟、升级和回退沿用相同软件仓库范围。

## 接口MAC保持

更新后，LCP接口保留对应原接口的MAC，避免系统默认持久地址策略在接口重建时
改写MAC而造成邻居缓存短时失效。此设置限定于产品命名的TAP接口，
不修改其他宿主网卡或第三方TAP的地址策略，无需新增CLI配置。

## 已知范围

- 本次保持FRR1.9。隔离验证中确认的FRR静态ECMP inactive成员删除问题没有并入此配套包：
  删除无效成员后FRR候选下一跳可能暂时保留旧项，应结合路由详情和实际FIB核对。
- 灵活QinQ性能数据来自规定速率、帧长和线程布局，不是硬件线速或所有策略组合保证。
- 已存在的低优先历史待证项维持原状态，不将未复现称为已修复。

完整变更与本次安装包验收范围见[软件发布说明](https://github.com/opennw-rui/VortexROS/releases/tag/v0.30-dev-debug2)。
