# 代理 ARP

代理 ARP 让设备在指定三层接口上，为配置范围内的 IPv4 地址回答 ARP。它适用于主机认为目标在本地网段、目标实际需要经过路由器到达的场景。

它不替代路由，也不执行 NAT。设备必须有到目标的路由，目标必须有回程路由。只有列出的地址范围会被代理；其他可路由地址不会因此自动获得代理响应。

[命令参考](reference/neighbors.md)

## 使用条件

接口必须是具备以太网 MAC 的三层接口，例如物理口、三层聚合口、Vlanif 或 Vbdif。二层成员口、LoopBack 和 NVE 不能作为代理入口。接口绑定的 VPN 实例决定其路由域。

Linux 数据面使用显式代理邻居项。VPP 数据面先处理普通 ARP，再把代理入口上未回答的请求交给 Linux；地址范围仍由同一份配置生成，不需要另外配置 VPP 原生命令。

## 配置案例

以下是开发服务器真实 CLI 验证使用的地址和接口。接口名称需替换为实际设备名称。

```text
CE                  P1                        P2                  Linux 目标端
198.18.11.100/24 -- host-p1q13
                   198.18.11.1/24
                   host-p1a12 -- host-p2a12
                   198.19.80.1/30  198.19.80.2/30
                                  host-p2e23 -- p3e23
                                  198.19.23.2/24  198.19.23.3/24
                                                  lo: 198.18.11.150/32
```

CE 认为198.18.11.150与自己直接相连，因此直接请求目标的 MAC。P1 代理回答，随后按主机路由将数据交给 P2。

### P1

```text
system-view
interface host-p1q13
 ip address 198.18.11.1 24
quit
interface host-p1a12
 ip address 198.19.80.1 30
quit
ip route-static 198.18.11.150 32 198.19.80.2
arp proxy 198.18.11.150 198.18.11.150 interface host-p1q13
commit
save
```

起始、结束地址相同表示代理一个地址；配置连续范围时更改结束地址即可。

### P2

```text
system-view
interface host-p2a12
 ip address 198.19.80.2 30
quit
interface host-p2e23
 ip address 198.19.23.2 24
quit
ip route-static 198.18.11.150 32 198.19.23.3
ip route-static 198.18.11.0 24 198.19.80.1
commit
save
```

### Linux 端点

目标端在已连接 P2 的以太网口上设置地址，并把目标地址放在 Loopback。实验中的该口名为p3e23：

```sh
ip link set p3e23 up
ip address add 198.19.23.3/24 dev p3e23
ip address add 198.18.11.150/32 dev lo
ip route add 198.18.11.100/32 via 198.19.23.2 dev p3e23
```

CE 使用198.18.11.100/24；实验中的接口名为cli-r4：

```sh
ip link set cli-r4 up
ip address add 198.18.11.100/24 dev cli-r4
ip route add default via 198.18.11.1
```

这些是端点操作，不是在 VortexROS CLI 中执行的命令。已有同名地址或路由时保留原配置，不要重复添加。

## 验证

P1 查询代理状态：

```text
[~P1] display arp proxy
Start Address    End Address      Interface            State
198.18.11.150    198.18.11.150    host-p1q13           active
Total items displayed = 1
```

CE 发起实际流量：

```text
ping -n -c 3 198.18.11.150
64 bytes from 198.18.11.150: icmp_seq=1 ttl=62 time=102 ms
64 bytes from 198.18.11.150: icmp_seq=2 ttl=62 time=28.1 ms
64 bytes from 198.18.11.150: icmp_seq=3 ttl=62 time=99.5 ms
3 packets transmitted, 3 received, 0% packet loss
```

这是共享开发服务器上的功能结果，不是延迟或吞吐性能保证。清空邻居后的首次探测还包含代理应答、下一跳解析时间；本次首次3包中收到1包，收敛后上述3包全部收到。实际部署若持续丢包，应检查代理入口、目标路由和回程，不能只依据配置项存在判断成功。

本例还实际验证了：

- 保留代理配置并保存，重建 P1 数据面后，配置恢复，健康状态为ready、零告警。
- 为范围外的198.18.11.151添加指向另一接口的路由后，CE 仍未收到该地址的代理 ARP 响应。
- 撤销代理并清空 CE 对应邻居缓存后，原地址不再获得代理响应。

## 撤销

P1 撤销本例的代理和目标主机路由：

```text
system-view
undo arp proxy 198.18.11.150 198.18.11.150 interface host-p1q13
undo ip route-static 198.18.11.150 32 198.19.80.2
commit
display arp proxy
save
```

实际查询结果为：

```text
Total items displayed = 0
```

P2 撤销本例新增的目标主机路由：

```text
system-view
undo ip route-static 198.18.11.150 32 198.19.23.3
commit
save
```

如果回程网段路由和接口地址还被其他业务使用，应保留。Linux 测试端另行删除本例新增的 Loopback 地址和主机回程路由。

撤销会删除显式代理项，并在 VPP 上关闭该接口不再需要的请求转交；不会为了撤销代理而关闭接口的普通三层转发。
