# 从零到 Ping

在空白 Ubuntu 26.04 amd64 上安装 VortexROS，保留 Linux 数据面，然后用一条静态路由验证连通性。本例使用独立实验接口，保留现有管理连接。

| 实验对象 | IPv4 地址 |
| --- | --- |
| VortexROS 业务口 | 192.0.2.2/24 |
| 同网段的上游网关 | 192.0.2.1 |
| 由上游可达、允许 ICMP 的目标 | 203.0.113.1 |

这些地址是文档示例。实际操作请换成实验网的地址、接口及目标。

## 进入 CLI

按[首次安装](installation/index.md)运行单文件安装器。安装结束后在 Ubuntu 终端执行：

~~~bash
sudo vortexros
~~~

使用 display interface brief 确认业务口名称。初始数据面由 Linux 管理。

## 配置地址与路由

下面以现有接口 `Ethernet 1` 为例。使用实际库存中显示的业务接口。

~~~text
system-view
interface Ethernet 1
 description LAB-UPLINK
 ip address 192.0.2.2 255.255.255.0
 undo shutdown
 quit
ip route-static 203.0.113.0 255.255.255.0 192.0.2.1
display configuration candidate
commit
~~~

## 验证并保存

~~~text
display interface brief
display ip routing-table
ping 192.0.2.1
ping 203.0.113.1
~~~

先确认接口和直连网关可达，再检查静态路由与目标回程。确认结果后回到用户视图保存：

~~~text
return
save
~~~

按提示确认保存。 `commit` 将 Candidate 应用到 Running，`save` 将 Running 写入启动配置。后续配置 DPDK 前，请阅读[数据面设备配置](operator/03-interfaces-l2.md#数据面设备配置)与[管理连接保护](installation/01-management-safety.md)。
