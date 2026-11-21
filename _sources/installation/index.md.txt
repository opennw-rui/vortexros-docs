# 首次安装

在空白 **Ubuntu 26.04 amd64** 上，执行一次单文件安装器即可完成正常首装。

选型见[支持的硬件](hardware.md)和[支持矩阵](support.md)，首装后的状态见[默认行为](defaults.md)。

## 下载并运行

从 [Debug 9 Release](https://github.com/opennw-rui/VortexROS/releases/tag/v0.30-dev-debug9) 获取单文件安装包和校验文件。在 Ubuntu 终端校验后安装。

~~~bash
sha256sum -c SHA256SUMS
sudo sh ./vortexros_0.30-dev-debug9_amd64.run
~~~

安装器需要访问已配置的 Ubuntu APT 软件源。它更新软件包索引，安装必要依赖和内嵌的 VortexROS、VPP、FRR 和 Kea，启动受 VortexROS 管理的服务，并屏蔽发行版提供的独立 VPP 和 FRR 服务。首装使用 **Linux 数据面**。业务口改用 DPDK 是后续独立操作，会改变对应网卡的驱动归属。

## 安装完成后

执行以下命令进入 CLI：

~~~bash
sudo vortexros
~~~

需要受管 SSH 登录时，先按[本地账号与 SSH](../operator/aaa.md)创建管理员；出厂配置没有内置账号。安装和使用手册统一在线维护，安装包不内置另一套用户手册。

默认安装包会在设备首次启动 VortexROS 时开启 72 小时试用。授权状态、到期行为及导入流程见[授权与试用](license.md)。

接下来按[从零到 Ping](../quickstart.md)配置示例口、提交并验证连通性。已有 VortexROS 的设备请使用[升级与回退](07-upgrade-uninstall.md)。

~~~{toctree}
:maxdepth: 1

00-planning
01-management-safety
02-backends
04-system-services
05-vpp-startup
06-first-start
license
07-upgrade-uninstall
08-hardware-acceptance
~~~
