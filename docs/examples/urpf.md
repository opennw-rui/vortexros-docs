# uRPF

## 拓扑与作用

两台 VortexROS 通过两条三层链路连接。P2 从 Ethernet0 发包，但 P1 到其 LoopBack0 的最佳回程经 Ethernet1，以此区分严格和宽松源地址检查。

| 链路 | P1 | P2 |
| --- | --- | --- |
| Ethernet0—Ethernet0 | 192.0.2.81/30 | 192.0.2.82/30 |
| Ethernet1—Ethernet1 | 10.201.12.1/24 | 10.201.12.2/24 |
| P2 LoopBack0 | — | 203.0.113.82/32 |

严格模式要求源地址的最佳回程接口等于入接口，会拒绝合法的非对称路由；宽松模式只要求存在符合条件的源地址路由。

## P1

~~~text
system-view
interface Ethernet0
 ip address 192.0.2.81 255.255.255.252
quit
interface Ethernet1
 ip address 10.201.12.1 255.255.255.0
quit
ip route-static 203.0.113.82 255.255.255.255 10.201.12.2
commit
~~~

## P2

~~~text
system-view
interface Ethernet0
 ip address 192.0.2.82 255.255.255.252
quit
interface Ethernet1
 ip address 10.201.12.2 255.255.255.0
quit
interface LoopBack0
 ip address 203.0.113.82 255.255.255.255
quit
ip route-static 192.0.2.81 255.255.255.255 192.0.2.81
commit
~~~

## 检查与启用

P2 先分别以链路地址和 LoopBack 地址 Ping P1；未启用检查时均应可达：

~~~text
ping -a 192.0.2.82 -c 3 192.0.2.81
ping -a 203.0.113.82 -c 3 192.0.2.81
~~~

P1 检查回程并启用严格模式：

~~~text
display ip routing-table 203.0.113.82
system-view
interface Ethernet0
 ip urpf strict
quit
commit
display current-configuration interface Ethernet0
~~~

重复两条 Ping：192.0.2.82 的回程仍在 Ethernet0，应成功；203.0.113.82 的回程在 Ethernet1，应被拒绝。切换成 ip urpf loose 并提交后，LoopBack 源探测应恢复。不能仅用一条直接连接的源地址探测来区分 strict 与 loose。

## 撤销

P1 在 Ethernet0 执行 undo ip urpf 并提交，再检查双向可达性。若拆除本例，在两端撤销专用静态路由、接口地址，并删除 P2 的 LoopBack0；每项使用对应的 undo 命令。提交后按需 save。

[uRPF 功能](../operator/urpf.md) · [接口参数](../operator/reference/interfaces.md)
