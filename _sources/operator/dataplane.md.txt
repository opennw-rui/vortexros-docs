# 数据面

首次安装默认使用 Linux 数据面。按 PCI 设备选择 DPDK，其他接口继续归 Linux；没有全局 kernel/vpp 模式切换命令。

配置页说明期望值，查询页说明实际值；二者必须分开比较。驱动、队列和启动参数按提示保存、重置后生效；在线 offload 按接口能力表处理。

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
