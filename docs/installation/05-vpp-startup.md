# 启用 DPDK 数据面

在 Linux 数据面验证基本连通性后，再按[数据面设备配置](../operator/03-interfaces-l2.md#数据面设备配置)为选中的 PCI 设备设置名称、驱动、队列、CPU 和大页。先确认业务口与管理口的归属。

commit 接受配置，save 保存配置。需要重启的数据面设置由 reset dataplane 应用。VPP 会重启，所选网卡可能切换驱动，经过这些接口的业务可能短暂中断。

重置后使用 display dataplane、display interface brief 和实际流量核对恢复情况。远程部署见[保护管理连接](01-management-safety.md)。
