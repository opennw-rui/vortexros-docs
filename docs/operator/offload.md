# 硬件卸载

查看网卡/驱动能力与当前启用状态，只有产品提供的控制项才可用CLI修改。

~~~text
display interface hardware offload Ethernet 1
~~~

| 列 | 含义 |
|---|---|
| Supported | 驱动报告支持该能力，不代表已开启 |
| Active | 实际启用状态，不能由配置推断 |
| Control=online | 产品可在线控制的能力 |
| Control=disabled | 对应产品控制项已显式禁用 |
| Control=driver | 由驱动决定，当前CLI不提供逐项开启入口 |

同一份接口策略可在接口视图和dataplane设备视图编辑，不是两份独立配置。当前可配置项以`hardware offload ?`为准，包括GSO、TSO、收发校验和与多段报文。关闭RX/TX校验和前，需在同次命令先关闭依赖它们的TSO。

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 1
 undo hardware offload gso
#
~~~

CLI 操作：

~~~text
commit
display interface hardware offload Ethernet 1
~~~

恢复使用 `hardware offload gso` 并提交。恢复默认不保证每个驱动细项都变成Active=yes，未开放控制的driver项仍按驱动实际状态显示。GSO是软件分段，TSO是硬件TCP分段，二者不是同一层功能。

修改后检查Active列；需要重新初始化驱动的项目应按提示重建数据面。操作步骤见[数据面激活与恢复](dataplane/recovery.md)。

[数据面设备](dataplane/devices.md) · [完整参数](reference/interfaces.md)
## 工作原理与能力判读

硬件卸载由网卡承担部分校验、分段或标签处理，减少 CPU 工作。Supported 表示驱动报告的能力，Active 表示当前状态，Control 表示能在线修改还是需要重新启动数据面；三者应分开看。

接收校验卸载帮助识别报文校验结果；发送校验卸载让网卡补齐校验和。TSO 面向 TCP 分段，软件 GSO 可按协议在软件中完成分段，两者并非同一个开关。VLAN strip/insert 则改变标签在网卡与数据面之间的呈现，不能仅凭抓包是否看见标签判断链路上实际是否带标签。

接口在线配置与 dataplane 设备启动配置有不同生效时机，按子页所列能力选择入口。修改后检查 Active 状态、收发错误及业务；网卡支持某项功能并不意味着驱动允许运行中切换。
