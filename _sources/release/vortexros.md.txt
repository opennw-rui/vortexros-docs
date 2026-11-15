# VortexROS 0.29-dev

正式手册从0.29-dev开始。当前控制包为0.29~dev+run1，统一安装包包含配套VPP26.10.7、FRR1.7-dev和Kea修复包。软件候选包仍未公开发布，本文不提供此前试验版本的安装附件。

## 本版能力与修复

- Candidate私有编辑、跨会话增量同步、Running快照与代号一致；路由组增量与精确拒绝后的同目标镜像回退。
- 本地AAA三种角色、首次改密、SSH和Bash/sudo；账号投影失败保持登录限制，沿用告警和自动收敛。
- 同一.run完成首次安装、升级、检查、模拟和失败回退，按组件版本安装；Linux-only与VPP数据面分别核对状态，逐项检查关键服务。
- 静态路由导入动态协议、IS-IS在线Level切换、RIP/RIPng默认preference100及IS-IS15、OSPF/OSPFv3查询和重算。
- RIP重建接口释放旧多播订阅，Zebra重连后重放已有路由；完整根因和恢复记录见[RIP](../operator/rip.md)。
- DHCPv6租约类型、正常空租约和多实例汇总，中继与Information-Request；配套Kea采用上游服务器组修复。
- CLI视图、帮助、补全、配置显示、接口身份、数据面容量与软件事务显示按当前命令参考统一。
- EVPN双栈Type-5、ESI生命周期、Anycast端点、静态FDB、VNI撤销及冷回放；接口归属、RA/SLAAC、静态ND和Proxy ARP按恢复阶段处理。

## 本轮新增修复

1. ACL只保留无状态permit/deny，删除permit-reflect入口、配置读取和下发。TCP established仍是标志位匹配。
2. EVPN的vni子上下文和exit-vni正确解析，冷清理不再生成无效no exit-vni；VRF下L3VNI仍是叶子。
3. 6PE根据已有标签邻居意图生成FRR的IPv6 explicit-null策略，首次启用刷新已有本地起源，最后邻居撤销时取消策略。未增加用户配置项，未改FRR源码。
4. 物理接口最后一项二层配置撤销后，现有LCP对正确切回L3，复用已有角色API。
5. LCP的MPLS表不再调用仅支持IP的MFIB生命周期函数，修正最后标签路由撤销时的崩溃。见[VPP说明](vpp.md)。

功能树和案例扩展为独立页面，包含拓扑、两端配置、参数作用、真实display、报文和撤销。新补All-Active、6PE、静态MAC及简单QinQ；既有已通过且未受影响的功能沿用原始证据，未重复全量或CI。

最终包的身份、QEMU事务和验证边界见[CLI实测记录](cli-validation.md)；逐条参考的覆盖边界见[手册覆盖](manual-coverage.md)。当前工作树未提交产品代码、未推送软件或部署真机。
