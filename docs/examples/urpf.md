# uRPF 源地址检查

## 拓扑

~~~text
                    检查入口
P2 p2a12 ───────── host-p1a12 P1
  192.0.2.82/30     192.0.2.81/30

P2 host-p2e12 ──── host-p1e12 P1
  10.201.12.2/24    10.201.12.1/24
                    到 203.0.113.82/32 的回程经此口
~~~

P1 使用 VPP，两个口属于同一默认路由域。P2 的 `p2a12` 是专用 Linux 测试端口；两个测试源都从它发出。第二个源地址 `203.0.113.82` 放在 P2 的 loopback，P1 到它的回程故意走另一条链路。不要在有合法非对称转发的业务入口直接开启严格模式。

## 准备 P1

底层 10.201.12.0/24 已在两端配置并互通。再配置入口和用于对照的静态路由：

~~~text
system-view
interface host-p1a12
 ip address 192.0.2.81 255.255.255.252
 quit
ip route-static 203.0.113.82 255.255.255.255 10.201.12.2
commit
display ip fib
~~~

实际 FIB 输出节选：

~~~text
192.0.2.80/30         normal    0      1         -        -              host-p1a12        -
203.0.113.82/32       normal    20     1         -        10.201.12.2    host-p1e12        -
~~~

## 准备 P2

以下是在隔离环境的 Linux 端执行的命令：

~~~bash
sudo ip address add 192.0.2.82/30 dev p2a12
sudo ip address add 203.0.113.82/32 dev lo
sudo ip route replace 192.0.2.81/32 dev p2a12
~~~

## 验证

配置前先观察基线。P2 开一个终端抓取从 P1 返回的第二个源地址的应答：

~~~bash
sudo timeout -s INT 8 tcpdump -l -n -c 1 -i any 'icmp[icmptype] = icmp-echoreply and src host 192.0.2.81 and dst host 203.0.113.82'
~~~

在 P2 另一个终端从两个源分别探测。由于第二条是非对称路径，以返回链路抓包判断 P1 是否实际转发应答，不能只看测试主机上的 Ping 汇总。

~~~bash
ping -n -I 192.0.2.82 -c 3 -W 1 192.0.2.81
ping -n -I 203.0.113.82 -c 3 -W 1 192.0.2.81
~~~

在 P1 启用严格模式：

~~~text
system-view
interface host-p1a12
 ip urpf strict
 quit
commit
display urpf
~~~

实际 CLI 输出节选：

~~~text
Interface   AF   Dir    Mode    Table
host-p1a12  ip4  input  strict  0
~~~

重复探测。同入口直连源仍 3 发 3 收；另一源的应答抓包在启用前、启用后分别为：

~~~text
p2e12 In  IP 192.0.2.81 > 203.0.113.82: ICMP echo reply, id 1299, seq 1, length 64

0 packets captured
~~~

严格检查要求收到报文的接口与到源地址的回程路径一致。此例的 FIB 未更改，变化来自入口检查。

## 撤销

~~~text
system-view
interface host-p1a12
 undo ip urpf
 quit
commit
display urpf
~~~

实测严格模式表项消失，并再次从 P2 的另一条链路捕获应答：

~~~text
p2e12 In  IP 192.0.2.81 > 203.0.113.82: ICMP echo reply, id 1684, seq 1, length 64
~~~

实验结束后，按原路径撤销测试静态路由，再删除测试地址。保留原有的底层互连。

[uRPF 配置指南](../operator/urpf.md)
