# 系统服务

首装时安装器启动 VortexROS 管理的服务，并屏蔽 Ubuntu 包提供的独立 vpp.service 和 frr.service。后续由 vortexros.target 管理设备服务。

日常检查见[系统与服务](../operator/02-system-services.md)。软件包和服务重启由[升级与回退](07-upgrade-uninstall.md)中的事务管理。
