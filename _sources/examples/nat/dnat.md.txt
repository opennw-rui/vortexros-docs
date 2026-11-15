# DNAT

将外部目的地址和端口改为内网服务。本例把 198.19.81.1 发布到 198.18.11.2，源地址保持外部客户端地址。

## 前提与参数

显式端口转换只支持 TCP/UDP（或对应协议号6/17），不能把 SCTP 会话查询能力等同于 SCTP 端口转换。

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。端口转换使用直接 destination port，不能同时保留 destination port-set。省略 action 的 port 则不改目的端口。该动作不等同于防火墙放行；接口 ACL 也必须允许业务。

## 配置

P1 从用户视图开始；接口与基础路由由前置拓扑提供：

~~~text
system-view
nat-policy name LAB-DNAT
 statistic enable
 rule 10
  protocol icmp
  destination address 198.19.81.1/32
  action dnat 198.18.11.2
 quit
quit
interface Ethernet0
 nat-policy LAB-DNAT inbound
quit
nat-policy name LAB-LAN-PASS
quit
interface Ethernet1
 nat-policy LAB-LAN-PASS inbound
quit
commit
~~~

## 验证

P2 执行 `ping -a 198.19.80.2 -c 3 198.19.81.1`，然后在 P1 查询：

~~~text
display nat-policy name LAB-DNAT
display nat-policy statistics name LAB-DNAT
display nat-policy sessions action dnat
~~~

应能往返，且目的地址从 198.19.81.1 变为 198.18.11.2，源地址保持 198.19.80.2。在会话中核对原始和转换后的地址；ICMP 使用标识符而非 TCP/UDP 端口。

Ping 成功只证明往返路径，应同时核对转换结果。查看状态要紧接探测执行，避免会话已老化。地址池耗尽和端口范围需要对应并发业务验证，不能从三次 Ping 推断。

## 撤销与保存

P1 系统视图：

~~~text
system-view
interface Ethernet0
 undo nat-policy LAB-DNAT inbound
quit
interface Ethernet1
 undo nat-policy LAB-LAN-PASS inbound
quit
undo nat-policy name LAB-DNAT
undo nat-policy name LAB-LAN-PASS
commit
display nat-policy runtime
display nat-policy interfaces
~~~

解除绑定后再发起新连接，确认不再采用该策略。基础拓扑的普通路由仍在，撤销 NAT 不一定使业务断开，应比较转换结果而非只看 ping。需要重启保留配置时，在提交并验证后执行 `save`；撤销后也再次保存。

[功能说明](../../operator/nat/dnat.md) · [命令参数](../../operator/reference/nat.md)

## TCP/UDP 端口发布

若 P3 的 VortexROS 已按 WireGuard 案例在 UDP 51820 提供服务，可把本例 rule 10 改为以下内容。先撤销 ICMP 规则，再创建 UDP 规则；外侧 WireGuard 对端的 endpoint 指向 198.19.81.1:18080，并用 `display wireguard` 检查握手与收发。

~~~text
nat-policy name LAB-DNAT
 undo rule 10
 rule 10
  protocol udp
  destination address 198.19.81.1/32
  destination port 18080
  action dnat 198.18.11.2 port 51820
 quit
quit
commit
~~~
显式端口映射只适用于 TCP/UDP；服务自身的密钥、允许地址、回程路由和 ACL 仍需正确配置。
