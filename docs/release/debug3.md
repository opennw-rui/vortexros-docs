# Debug 3

本版配套FRR为10.7.1-vortexros-1.10-dev，VPP和Kea沿用Debug 2版本。使用本版统一.run更新，安装器按组件实际版本选择更新内容。

## 静态ECMP

修复撤销不可用ECMP成员后，路由详情仍残留旧成员的问题。恢复解析路由不会重新加入已经撤销的配置成员。

同时修复递归解析从可用变为不可用时，实际路径没有及时更新的问题。保留配置的路径可以随解析恢复重新参加ECMP；永久撤销的配置成员则保持删除。

配置、查询、影响与精确撤销见[静态路由收敛](../operator/static-routing/lifecycle.md)。

## 更新注意事项

本版更新控制层和FRR，系统包事务会重启相关产品服务，包括VPP；VPP软件包版本保持不变。路由和邻居需要重新恢复，业务会短暂中断。维护前先commit、save；更新后核对版本、健康、RIB/FIB及实际业务。

不需要重新配置未变化的VPP、Kea或现有业务。升级、检查、模拟和回退沿用[统一安装器](../installation/07-upgrade-uninstall.md)。

使用[Debug 3统一安装包](https://github.com/opennw-rui/VortexROS/releases/tag/v0.30-dev-debug3)。
对应控制层DEB为0.30~dev+run39.debug3，配套FRR为10.7.1-vortexros-1.10-dev。
VPP仍为26.10.9+vortexros.debug2-release，Kea仍为3.0.3-1+vortexros1。
