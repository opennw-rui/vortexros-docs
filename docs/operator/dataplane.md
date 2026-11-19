# 数据面

首次安装默认使用 Linux 数据面。按 PCI 设备选择 DPDK，其他接口继续归 Linux；没有全局 kernel/vpp 模式切换命令。

配置页说明期望值，查询页说明实际值；二者必须分开比较。驱动、队列和启动参数按提示保存、重置后生效；在线 offload 按接口能力表处理。

## 资源与业务的关系

CPU、NUMA 内存、网卡驱动和队列决定转发资源如何使用，接口 IP、VLAN、路由及策略决定业务如何转发。两类配置分开组织：数据面视图规划资源，接口及协议视图规划业务。

NUMA 节点表示处理器、内存和 PCI 设备的局部关系。优先让转发线程、网卡及大页位于适合的节点，可以减少跨节点访问；CPU 编号相邻不代表属于同一物理核心或节点，先查询实际拓扑。没有统一适合所有硬件的核心数或队列数。

资源配置显示已提交的目标值，运行查询显示实际状态。保存不等于当前线程或驱动已经切换，需要重置或主机重启的项目按提示操作，并预留业务中断窗口。缺省表容量是上限配置，不是满表吞吐保证。

~~~{toctree}
:maxdepth: 2

dataplane/devices
dataplane/resources
dataplane/plugins
dataplane/tables
dataplane/bridge-mtu
dataplane/recovery
~~~

[硬件卸载](offload.md) · [流量分发](flow-steering.md) · [命令参数](reference/dataplane.md)
