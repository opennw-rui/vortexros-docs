# 软件组成与兼容性

| 组件 | 职责 | Debug 6 配套包 |
|---|---|---|
| VortexROS | CLI、配置提交和后端收敛 | 0.30~dev+run44.debug6 |
| VortexROS-VPP | DPDK、转发及LCP | 26.10.9+vortexros.debug6-release，五个运行包使用同一构建 |
| FRR | 动态路由协议和Zebra | 10.7.1-vortexros-1.10-dev |
| Kea | DHCPv4/DHCPv6服务 | 3.0.3-1+vortexros1 |

单文件.run包含上述组件，并从Ubuntu软件源补齐必要依赖。安装器比较组件包版本，仅安装发生变化的组件。候选软件是否已公开发布，见[发布记录](../release/index.md)。

安装后用display version核对实际版本，用display service verbose检查服务。安装包中的版本与运行进程身份需要分别核对，不能只看文件名。
