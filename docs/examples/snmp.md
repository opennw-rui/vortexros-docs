# SNMP 轮询

## 拓扑

~~~text
VortexROS host-labnms 192.0.2.65/30 ─── 192.0.2.66/30 NMS
                  UDP 161
~~~

使用专用实验管理链路。设备接口已识别，NMS 安装 Net-SNMP 客户端。实验设备的系统名为 `SNMP-LAB`。本例仅在隔离链路上演示 SNMPv2c 只读查询；community 不加密，生产环境优先使用 [SNMPv3 authPriv](../operator/snmp.md)。

## 配置 VortexROS

~~~text
system-view
interface host-labnms
 ip address 192.0.2.65 255.255.255.252
 quit
commit
snmp-agent
snmp-agent sys-info version v2c
snmp-agent sys-info contact Lab Operations
snmp-agent sys-info location Isolated-Lab
snmp-agent protocol source-interface host-labnms
snmp-agent community read lab-read
commit
display snmp-agent sys-info
~~~

这里只允许目标为指定接口主 IPv4 地址的轮询。没有启用 trap，也没有写权限。若设备已经有 SNMP 配置，应调整现有对象，并保留其他监控使用的设置。

## 配置 NMS

在 Linux 的专用接口上配置地址；示例接口名为 `mgmt0`：

~~~bash
sudo ip link set mgmt0 up
sudo ip address add 192.0.2.66/30 dev mgmt0
~~~

本例的 NMS 使用 Linux veth 接入 VPP AF_PACKET。若复用同样的隔离拓扑且 AF_PACKET 关闭了校验和卸载，先在 NMS 测试端口执行 `sudo ethtool -K mgmt0 tx off`，让 Linux 在发送前填好 UDP 校验和。普通 NMS 不需要这一步。

## 验证

先核对配置。开发服务器隔离环境的 CLI 实际输出：

~~~text
SNMP agent configuration: enabled
Versions: v2c=true v3=false
Contact: Lab Operations
Location: Isolated-Lab
Source interface: host-labnms
VPN instance: public-net
~~~

查询系统名和位置。数字 OID 不依赖本地安装 MIB 文本。在 NMS 执行：

~~~bash
snmpget -v2c -c lab-read -m '' -On -t 1 -r 0 192.0.2.65 \
  .1.3.6.1.2.1.1.5.0 .1.3.6.1.2.1.1.6.0
~~~

独立 NMS 经 `192.0.2.65:161` 收到的实际回复：

~~~text
.1.3.6.1.2.1.1.5.0 = STRING: "SNMP-LAB"
.1.3.6.1.2.1.1.6.0 = STRING: "Isolated-Lab"
~~~

## 撤销

专用测试设备上可撤销整套 SNMP：

~~~text
system-view
undo snmp-agent
commit
~~~

共享设备应只撤销本实验新增的 community 等设置，不应删除其他监控的 SNMP 配置。撤销后运行 `display snmp-agent sys-info`，待监听服务停止后从同一 NMS 重复原查询。实际输出：

~~~text
SNMP agent configuration: disabled
Versions: v2c=false v3=false

Timeout: No Response from 192.0.2.65.
~~~

撤销后，实验 NMS 仍能 ping 通管理地址。管理接口地址可按原用途保留。
