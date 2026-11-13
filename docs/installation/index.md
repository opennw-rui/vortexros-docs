# 首次安装

在空白 **Ubuntu 26.04 amd64** 上，执行一次单文件安装器即可完成正常首装。

## 下载并运行

从 [当前版本发布页](https://github.com/opennw-rui/VortexROS/releases/tag/v0.28-dev-debug5) 下载对应的 .run 文件，在 Ubuntu 终端执行：

~~~bash
sudo sh ./vortexros-install_0.28-dev-debug5_amd64.run
~~~

安装器需要访问已配置的 Ubuntu APT 软件源。它更新软件包索引，安装必要依赖和内嵌的 VortexROS、VPP、FRR，启动受 VortexROS 管理的服务，并屏蔽发行版提供的独立 VPP 和 FRR 服务。首装使用 **Linux 数据面**。业务口改用 DPDK 是后续独立操作，会改变对应网卡的驱动归属。

## 安装完成后

执行以下命令进入 CLI：

~~~bash
sudo vortexros
~~~

接下来按[从零到 Ping](../quickstart.md)配置实验口、提交并验证连通性。已有 VortexROS 的设备请使用[升级与回退](07-upgrade-uninstall.md)。

~~~{toctree}
:maxdepth: 1

00-planning
01-management-safety
02-backends
04-system-services
05-vpp-startup
06-first-start
07-upgrade-uninstall
08-hardware-acceptance
~~~
