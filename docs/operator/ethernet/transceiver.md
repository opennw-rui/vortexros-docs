# 光模块诊断

从 0.30-dev Debug 8 开始，可以查询物理以太网端口上光模块的型号和数字诊断数据。诊断用于检查链路光功率、温度及是否接近模块的告警阈值。

~~~text
display interface Ethernet0 transceiver
display interface Ethernet 0 transceiver
~~~

两种写法等效。DPDK 端口使用 VortexROS 的物理端口名。由 Linux 驱动持有的网卡也可以使用实际的设备名，例如 `enp3s0`。聚合口请查询它的物理成员，VLAN 子接口请查询父端口。

查询立即生效，命令无需提交或保存。不同网卡和模块的显示字段会有所不同。

| 字段 | 如何读 |
| --- | --- |
| Vendor Part Number | 厂商提供的模块型号 |
| TX Power、Laser output power | 本端模块发出的光功率 |
| RX Power、Receiver signal average optical power | 本端模块收到的光功率。多通道模块可分别显示每条通道 |
| Temperature、Module temperature | 模块当前温度 |
| High/Low Alarm、High/Low Warning | 模块提供的告警和预警上下限 |

下面的示例节选展示了单通道模块的读数和告警阈值。

~~~text
Interface: Ethernet0
  Module Base Information:
    Vendor Part Number: SFP10G-LR-SIM
  Module Diagnostics:
    Current Values:
      Temperature: 42.00 °C
      TX Average Power: 1.2500 mW (.97 dBm)
      RX Average Power: .4000 mW (-3.98 dBm)
    Alarm Thresholds:
      Temperature High: 80.00 °C, Low: -10.00 °C
      TX Power High: 2.0000 mW (3.01 dBm), Low: .1500 mW (-8.24 dBm)
      RX Power High: 1.6000 mW (2.04 dBm), Low: .0630 mW (-12.01 dBm)
~~~

读数以设备显示的单位为准，例如光功率为 mW 或 dBm。判断功率是否异常时，用同一模块、同一方向或通道的读数与相应阈值比较。对端收光偏低时，可以同时对照本端发光和对端收光，再检查光纤、接头及链路损耗。

端口未插模块、网卡驱动无法读取模块或使用虚拟端口时，查询会提示数据不可用。只显示基本信息时，进一步查看模块是否支持 DOM/DDM，以及当前驱动和模块组合是否提供诊断与阈值。
