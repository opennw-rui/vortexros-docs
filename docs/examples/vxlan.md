# 静态 VXLAN

## 拓扑

~~~text
Vbdif404 192.0.2.9/30                         192.0.2.10/30 Vbdif404
P1（VTEP 10.201.12.1）────── P2 ──────（VTEP 10.201.23.3）P3
                     VLAN 404 / VNI 4404
~~~

三台路由器运行 VPP。P2 只转发底层 IP。P1—P2 使用 10.201.12.0/24，P2—P3 使用 10.201.23.0/24；P2 的两侧地址末尾均为 .2。P1 到 10.201.23.0/24 的下一跳是 10.201.12.2，P3 到 10.201.12.0/24 的下一跳是 10.201.23.2。先确认 VTEP 地址双向可达，路径允许 VXLAN UDP。

本例复用已经配置底层源地址的 Nve1。若是新建 Nve1，在各自的 NVE 视图先执行 `source 10.201.12.1` 或 `source 10.201.23.3`。启用交换功能后再开始；实验用 Vbdif 自身探测，不需要额外主机。

## P1 配置

~~~text
system-view
vlan batch 404
bridge-domain 404
 l2 binding vlan 404
 vxlan vni 4404
quit
interface Nve1
 vni 4404 head-end peer-list 10.201.23.3
quit
interface Vbdif 404
 ip address 192.0.2.9 255.255.255.252
quit
commit
~~~

## P3 配置

~~~text
system-view
vlan batch 404
bridge-domain 404
 l2 binding vlan 404
 vxlan vni 4404
quit
interface Nve1
 vni 4404 head-end peer-list 10.201.12.1
quit
interface Vbdif 404
 ip address 192.0.2.10 255.255.255.252
quit
commit
~~~

两端将同一 VNI 加入本地桥域，手工指定远端 VTEP；没有 BGP EVPN 自动发现。P2 不配置桥域或 NVE。

## 验证

**P1：**

~~~text
display vxlan tunnel
display bridge-domain 404
ping -n -c 3 -t 1500 192.0.2.10
~~~

P3 反向执行 `ping -n -c 3 -t 1500 192.0.2.9`。实验输出节选：

~~~text
bridge-domain 404
  description: --
  flood: on  uu-flood: off  forward: on  learn: on  arp-term: off  arp-ufwd: off  mac-age: 0
  bvi: Vbdif404
  ports:
    Vbdif404         shg 0
    vxlan_tunnel1    shg 1

 --- 192.0.2.10 ping statistics ---
 3 packets transmitted, 3 received, 0% packet loss, time 2003ms

 --- 192.0.2.9 ping statistics ---
 3 packets transmitted, 3 received, 0% packet loss, time 2004ms
~~~

## 撤销

在 P1 执行：

~~~text
system-view
interface Nve1
 undo vni 4404 head-end peer-list 10.201.23.3
quit
commit
ping -n -c 3 -t 1000 192.0.2.10
~~~

实测返回 `ping: connect: Network is unreachable`。P3 同样撤销远端条目，将地址改为 10.201.12.1。最后在两端删除实验 Vbdif、桥域和 VLAN：

~~~text
undo interface Vbdif 404
undo bridge-domain 404
undo vlan 404
commit
display bridge-domain 404
~~~

两端实测均显示 `(no bridge-domain)`。共用的 Nve1 和底层路由仍保留。

[静态 VXLAN 配置指南](../operator/vxlan.md)
