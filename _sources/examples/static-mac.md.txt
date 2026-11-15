# 静态 MAC

## 拓扑和作用

本例把 CE1 的 MAC 固定到 PE1 的桥域出口，并关闭学习和未知单播泛洪。两台设备均运行 VortexROS。静态 MAC 决定二层出口，不创建 IP 路由或 ARP。

~~~text
PE1 Vbdif777 192.0.2.1/24
  BD777 / VLAN777
  Ethernet0 ───── CE1 Ethernet0 192.0.2.3/24
                       MAC 92:28:40:07:45:9d
~~~

静态MAC只决定二层目的MAC的出口，不创建IP路由或ARP。实际设备必须替换端口名和对端真实MAC；不能把示例MAC用于其他主机。

## CE1

~~~text
system-view
interface Ethernet0
 mac-address 9228-4007-459d
 ip address 192.0.2.3 255.255.255.0
quit
commit
~~~

MAC 地址只用于本例，请勿在同一网络重复使用。

## PE1完整配置

~~~text
system-view
enable switch
vlan 777
quit
bridge-domain 777 no-learn no-uu-flood
 l2 binding vlan 777
quit
interface Ethernet0
 portswitch
 port link-type access
 port default vlan 777
quit
interface Vbdif 777
 ip address 192.0.2.1 255.255.255.0
quit
mac-address static 9228-4007-459d Ethernet0 bridge-domain 777
commit
display bridge-domain 777
display mac-address bridge-domain 777
ping -a 192.0.2.1 -c 3 192.0.2.3
~~~

业务桥域777由模型映射为内部VPP桥域，不应手动依赖内部编号。出口必须属于本业务，跨VLAN端口会在配置校验时拒绝。关闭学习和未知单播泛洪会影响该域所有未知目的流量；本例是独占示例域，不应直接用在承载其他客户的桥域。

## 验证

~~~text
bridge-domain 777
  flood: on  uu-flood: off  forward: on  learn: off
  bvi: Vbdif777
  ports:
    Vbdif777         shg 0
    Ethernet0     shg 0

MAC Address       VLAN/VSI/BD                    Learned-From        Type
9228-4007-459d    -/-/777                        Ethernet0        static
Total items displayed = 1

3 packets transmitted, 3 received, 0% packet loss
~~~

查询时应找到本例目标 MAC；设备可能还有其他本地项。

## 撤销对照

~~~text
undo mac-address static 9228-4007-459d Ethernet0 bridge-domain 777
commit
display mac-address bridge-domain 777
ping -a 192.0.2.1 -c 3 192.0.2.3
~~~

目标 MAC 应不再存在。由于学习和未知单播泛洪仍关闭，目标单播出口消失后探测应失败。

最后撤销本例独占对象：

~~~text
undo interface Vbdif 777
interface Ethernet0
 undo portswitch
quit
undo bridge-domain 777
undo vlan 777
commit
display bridge-domain 777
display health
save
~~~

撤销后桥域应不存在，健康应恢复 ready。CE1 在 Ethernet0 撤销本例 IP 和 MAC 配置，再提交；各设备按需 save。共享交换设置及其他业务应保留。

[MAC功能](../operator/mac-table.md) · [桥域参数](../operator/reference/bridge-domains.md)
