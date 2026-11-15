# 性能参考

硬件选型需要同时考虑CPU、网卡、接口驱动、报文长度、封装层数和实际业务功能。基本IPv4转发、ACL、加密隧道和VXLAN的处理成本不同，不能用单项转发速率代表所有业务。

FD.io CSIT提供公开的VPP性能结果，可按CPU、网卡、驱动和用例筛选：

- [CSIT测试数据](https://csit.fd.io/report/)
- [CSIT 26.10报告](https://csit.fd.io/cdocs/release_notes/current/#csit-2610-selected-performance-comparisons)
- [测试台规格](https://csit.fd.io/cdocs/infrastructure/fdio_dc_testbed_specifications/)

使用这些数据时，应核对版本、帧长、worker数量、驱动、功能组合和丢包标准。上游结果仅适用于其注明的条件，不是VortexROS或自有插件的设备吞吐保证。

可使用的CPU和网卡路径见[支持的硬件](../installation/hardware.md)。VortexROS当前不提供按CPU或网卡型号承诺的统一吞吐数值。
