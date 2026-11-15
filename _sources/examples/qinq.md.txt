# QinQ

## 拓扑与用途

将客户侧未打标签或已有C-Tag的报文，统一装入服务VLAN2200穿过二层核心。两端边缘口使用dot1q-tunnel，核心口用trunk；出口移除服务标签，保留客户原有标签。这个动作不是IP路由、NAT或任意标签翻译。

~~~text
CE-A ce2 ─ host-p2docmh PE2 host-p2d23 ─ host-p3d23 PE3 host-p3docce ─ remote0 CE-B
             QinQ客户口        trunk S2200          QinQ客户口
未打标签：198.18.209.2/24                                        198.18.209.3/24
客户VLAN10：198.18.210.2/24                                      198.18.210.3/24
~~~

本例使用开发服务器隔离VPP/LCP实例与真实veth端点。VPP基础口已经由实验启动清单创建；物理设备应替换为各自实际接口。客户口不得保留其他三层地址或子接口；核心链路本例独占，避免与其他trunk分类冲突。

## 端点

CE-A Linux：

~~~sh
ip link set ce2 up
ip address add 198.18.209.2/24 dev ce2
ip link add link ce2 name ce2.10 type vlan id 10
ip link set ce2.10 up
ip address add 198.18.210.2/24 dev ce2.10
~~~

CE-B Linux：

~~~sh
ip link set remote0 up
ip address add 198.18.209.3/24 dev remote0
ip link add link remote0 name remote0.10 type vlan id 10
ip link set remote0.10 up
ip address add 198.18.210.3/24 dev remote0.10
~~~

端点接口如原先属于bond/bridge，应先按自身操作系统解除该归属。本实验的CE-A另保留其他测试地址，以上新网段不与它们重叠。

## PE2

~~~text
system-view
enable switch
vlan 2200
quit
interface host-p2docmh
 portswitch
 port link-type dot1q-tunnel
 port default vlan 2200
quit
interface host-p2d23
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 2200
quit
commit
~~~

## PE3

~~~text
system-view
enable switch
vlan 2200
quit
interface host-p3docce
 portswitch
 port link-type dot1q-tunnel
 port default vlan 2200
quit
interface host-p3d23
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 2200
quit
commit
~~~

客户侧父接口接管全部标签分类空间，不能再在同一父接口创建独立L2/L3子接口。客户C-Tag10与服务S-Tag2200是不同层次，不应把客户VLAN10也配置为此核心trunk的业务VLAN。部署时还要考虑额外标签开销和两端实际MTU；本例没有测量最大帧长。

## 实际CLI和流量

~~~text
display vlan 2200
display current-configuration interface host-p2docmh
display health
~~~

PE2真实输出节选：

~~~text
VID   Type    Status  MAC-LRN  Description      Ports
2200  common  enable  enable   VLAN 2200        UT:host-p2docmh(U)
                                                TG:host-p2d23(U)

Health state              : ready
Running/Actual generation : 2/2
Reconcile state           : in-sync
Active alarms             : 0
~~~

PE3对应为host-p3docce、host-p3d23，健康ready、代号7/7、零告警。UT表示客户侧业务接入，不代表收到的客户报文一定没有C-Tag。

CE-A发起：

~~~sh
ping -n -c 3 198.18.209.3
ping -n -c 3 198.18.210.3
~~~

两个网段均实际3发3收。CE-B反向分别探测1包，均1/1。核心原始口抓到实际双层标签：

~~~text
ethertype 802.1Q (0x8100), vlan 2200, ethertype 802.1Q (0x8100), vlan 10,
ethertype IPv4, 198.18.210.2 > 198.18.210.3: ICMP echo reply
~~~

抓包窗口实际只捕获一包后结束，不宣称收齐了预设的四包，也不把此功能探测当作吞吐/丢包率测试。

## 撤销

PE2：

~~~text
interface host-p2docmh
 undo portswitch
quit
interface host-p2d23
 undo portswitch
quit
undo vlan 2200
commit
display vlan 2200
display health
save
~~~

PE3用自身两个接口执行相同撤销。真实CLI返回VLAN2200不存在；PE2代号3/3、PE3代号8/8，均ready、零告警。客户VLAN10再次探测为3发0收，业务已撤销。保存应答Y并等待成功；共享核心口上有其他VLAN时只撤本例的allow-pass，不能清空整个端口。

Linux端点最后删除本例新增的.10接口和198.18.209.0/24地址，保留原有地址和其他业务。

[QinQ功能](../operator/qinq.md) · [子接口](subinterfaces/index.md) · [VLAN参数](../operator/reference/vlan.md)
