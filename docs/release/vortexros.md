# VortexROS 更新

**当前版本：0.28-dev-debug5。** [完整发布说明](https://github.com/opennw-rui/VortexROS/releases/tag/v0.28-dev-debug5)

- 普通 CLI 编辑只复制涉及的配置域；跨会话同步只发送 Running 的变化字段；显式刷新时复用未变化的配置子树。
- 路由组刷新在收到旧基线拒绝时，使用同一目标镜像继续完成发布。隔离验证从 50,000 条起始路由收敛到 2 条目标路由，撤销 49,998 条旧路由。
- 配套系统升级包包含控制层和 VPP，沿用已安装 FRR；空白系统的单文件安装器内嵌配套 FRR。安装方式见[安装](../installation/index.md)。

开发服务器的 QEMU 隔离环境验证了升级，确认原有配置和 VPP 启动配置保持一致，并核对了 IPv4 FIB 与 IPv6 静态邻居。Debug 5 的安装验证使用系统归档升级；同版首装文件核对了内嵌归档及发布资产。
