# 软件组成与兼容性

| 组件 | 职责 | 当前发布 |
| --- | --- | --- |
| VortexROS | CLI、配置提交和后端收敛 | 0.28 开发版 Debug 9 |
| VortexROS-VPP | DPDK、转发及 LCP | 26.10.4，五个运行包须使用同一构建 |
| FRR | 动态路由协议和 Zebra 控制面 | 10.7.1-vortexros-1.5-dev |

首装 .run 已包含以上组件，并从 Ubuntu 软件源补齐系统依赖。安装后可用 display version 查看版本，用 display service verbose 检查服务。
