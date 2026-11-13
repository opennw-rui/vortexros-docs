# FRR 更新

**当前配套版本：10.7.1-vortexros-1.5-dev。** Debug 5 未更新 FRR 包。[配套 FRR 发布说明](https://github.com/opennw-rui/vortexros-frr/releases/tag/v10.7.1-vortexros-1.5-dev)

此配套版本回移了 FRRouting 对默认 BGP 实例隐藏并恢复时的 EVPN 状态修复（[#23851](https://github.com/FRRouting/frr/pull/23851)，固定在 `6c068bfd707e`），以及关联的 [10.7 回移](https://github.com/FRRouting/frr/pull/23676)。打包时 #23851 仍在上游审查；这里记录配套包采用的版本。

FRR 发布时在开发服务器通过真实 CLI 验证了重启、Running 配置回放、VPN 路由恢复和实际连通性。这里没有独立的 FRR 吞吐或收敛延时对比。
