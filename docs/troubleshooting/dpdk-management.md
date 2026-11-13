# 切换 DPDK 后管理连接中断

通过已验证的本地、串口或云控制台进入设备，先确认本次接管是否完成，再恢复管理口。以下步骤针对 VortexROS 管理的物理口。

~~~text
display dataplane
display dataplane interfaces
display interface brief
display health verbose
display alarm active
~~~

1. 若接管失败并已回到 Linux，从 Ubuntu 用 `ip -br address`、`ip route` 和 `ip -6 route` 核对接口名、地址和管理回程，再检查 OpenSSH 监听。接口名可能已按已验证的 Ethernet 命名保留。
2. 若活动模式为 DPDK，核对管理地址及回程路由是否随 VPP/LCP 恢复。若计划把该端口还给 Linux，在控制台进入对应 `dataplane device` 视图执行 `undo mode`，提交、保存，再从用户视图执行 `reset dataplane` 并确认。
3. 用第二个终端重新建立 SSH，进入 CLI 并检查相关接口和业务，再关闭控制台。若接管或回退仍不成功，先记录运行状态和日志。

设备视图、重置和影响见[数据面配置](../operator/dataplane.md)，变更前的检查见[管理连接保护](../installation/01-management-safety.md)。
