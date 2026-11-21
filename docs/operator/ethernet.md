# Ethernet

配置物理接口、地址和 MTU，查看链路及流量统计。

[命令参考](reference/interfaces.md)

## 工作原理与配置边界

以太网接口承担物理链路的收发，管理状态由 shutdown 控制，链路状态由网卡和对端协商决定。三层接口直接配置 IP；作为交换端口时，VLAN 接入与网关地址分别配置，不能把二层成员当作独立三层网关。

| 参数 | 用途与影响 |
| --- | --- |
| MTU | 限制可发送的网络层报文大小，需考虑隧道及标签开销 |
| MAC | 本接口的二层身份，修改可能使邻居缓存重新学习 |
| shutdown | 人工停止接口，依赖该接口的业务也受影响 |
| statistic enable | 开启相应统计，不等于启用转发或协议 |

先检查 PHY、Protocol、接口类型和有效地址，再分析丢弃及错误计数。小 MTU 的出口不能因网桥 MTU 较大而发送超长报文。网卡支持某项 offload 也不等于该项当前已开启，见[硬件卸载](offload.md)。

~~~{toctree}
:maxdepth: 2

ethernet/state
ethernet/transceiver
ethernet/settings
~~~


## 接口 MAC 地址

物理接口默认沿用接口本身的 MAC。没有原生 MAC 的逻辑接口使用系统规定的默认地址；无须为已有 MAC 的接口另行生成地址。

~~~text
interface Ethernet0
 mac-address 0200-aabb-2960
#
commit
display interface Ethernet0
~~~

覆盖地址同时用于数据面接口与其控制面端点。撤销恢复该接口的原生地址：

~~~text
interface Ethernet0
 undo mac-address
#
commit
display interface Ethernet0
~~~

MAC 变化会使对端的 ARP/ND 缓存需要重新解析，切换期间可能短暂丢包。验证时检查显示的硬件地址及双向连通性；不要只检查配置行是否消失。

## 详细报文统计

~~~text
interface Ethernet0
 statistic enable
#
commit
display interface Ethernet0
~~~

默认关闭详细分类计数。开启后可查看单播、组播和广播分类；总包数、总字节数与错误计数仍分别展示。网卡提供硬件分类计数时优先显示硬件值。

父接口存在 VLAN 子接口时，软件出口分类计数不能覆盖全部子接口流量。此时没有硬件来源的出口分类显示 `-`，总出口包数和字节数照常显示；`-` 不表示零流量。输出会提示该限制。不要将软件分类值相加后当作该物理端口的完整出口统计。

~~~text
interface Ethernet0
 undo statistic enable
#
commit
~~~


MAC 撤销后的显示应恢复接口原生地址。例如：

~~~text
Ethernet0 current state : UP
Line protocol current state : UP
Internet Address is 198.19.202.2/24
IPv6 Address is 2001:db8:202::2/64
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 02fe-4e89-b4b0
~~~

详细统计中，以下结果表示出口总流量存在，但父接口的软件分类无法完整覆盖子接口：

~~~text
Output: 131 packets, 10420 bytes
  Unicast:                        -    Multicast:                      -
  Broadcast:                      -    Total Error:                    -
~~~

删除最后一个子接口后，若使用软件分类，分类数值可继续显示；关闭详细统计后分类恢复为 `-`，总包数仍然可见。
