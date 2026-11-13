# 介绍

VortexROS 是运行在 Ubuntu 上的网络操作系统。通过统一 CLI 配置接口、路由和网络服务。首次安装使用 Linux 数据面；需要 DPDK 时，再选择由 VPP 接管的网卡。

手册对应 **VortexROS 0.28 开发版（Debug 5）**。配套软件、更新及测试范围见[发布记录](release/index.md)。

首次使用请从[安装](installation/index.md)和[入门](quickstart.md)开始。已有设备可直接从左侧选择功能，也可按[配置案例](examples/index.md)完成一个任务，或在[命令参考](operator/reference/commands.md)查询语法。

~~~{toctree}
:hidden:
:maxdepth: 3

支持的硬件 <installation/hardware>
支持矩阵 <installation/support>
安装 <installation/index>
默认行为 <installation/defaults>
入门 <quickstart>
命令行 <operator/01-cli>
系统管理 <operator/02-system-services>
接口 <operator/03-interfaces-l2>
IP 路由 <operator/04-ip-routing>
路由协议 <operator/05-dynamic-routing>
ACL <operator/acl>
NAT <operator/nat>
流量策略 <operator/07-policy>
隧道 <operator/06-tunnels>
MPLS <operator/10-mpls-l3vpn>
网络服务 <operator/08-network-services>
诊断与恢复 <operator/09-operations>
常见故障 <troubleshooting/index>
配置案例 <examples/index>
命令参考 <operator/reference/commands>
发布记录 <release/index>
~~~
