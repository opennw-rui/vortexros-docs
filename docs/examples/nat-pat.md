# 接口 PAT

## 拓扑

本例验证 UDP 端口匹配、地址/端口集合、接口源 PAT 和策略会话上限。接口名称来自开发服务器隔离拓扑；设备上换成相应 Ethernet 接口。

```text
P1 host-p1a12 198.19.80.1/30 ─── 198.19.80.2/30 host-p2a12 P2
   出方向 NAT、UDP 客户端                UDP 回显服务 48100
```

两端接口均为三层口，属于 default VPN。此例不依赖默认路由，也不提供公网接入或防火墙规则。

## 两端地址

P1：

```text
system-view
interface host-p1a12
 ip address 198.19.80.1 255.255.255.252
 quit
commit
```

P2：

```text
system-view
interface host-p2a12
 ip address 198.19.80.2 255.255.255.252
 quit
commit
```

在 P2 的另一 Linux 终端启动 UDP 回显程序，测试结束用 Ctrl+C 停止。它是实验流量端点，需要 Python 3；不是产品后台服务。

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('198.19.80.2', 48100))
while True:
    data, peer = s.recvfrom(2048)
    print(peer, data, flush=True)
    s.sendto(data, peer)
```

## 策略

P1：

```text
nat-policy address-set name CLI-SRC
 address 198.19.80.1/32
 quit
nat-policy address-set name CLI-DST
 address 198.19.80.2/32
 quit
nat-policy port-set name CLI-SPORT
 port 47101-47103
 quit
nat-policy port-set name CLI-DPORT
 port 48100
 quit
nat-policy interface-pat-range 52000-52003
nat-policy name CLI-UDP
 statistic enable
 session-limit 4
 rule 10
  priority 7
  protocol udp
  source address-set name CLI-SRC
  destination address-set name CLI-DST
  source port 47100
  destination port 48100
  source vpn-instance default
  destination vpn-instance default
  action snat pat interface
  quit
 quit
interface host-p1a12
 nat-policy CLI-UDP outbound
 quit
commit
```

优先级数值越小越先匹配。各匹配项取交集；本例只转换指定 UDP 流，使用路由所选出口的接口地址。PAT 范围是全局接口源 PAT 参数，本例刻意缩小以便观察，不能直接照搬到生产容量配置。

## 实际流量与显示

在 P1 Linux 终端执行以下客户端，第一轮使用 47100。后面的轮次只改 `port`：

```python
import socket
port = 47100
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('198.19.80.1', port))
s.settimeout(3)
s.sendto(b'PAT-test', ('198.19.80.2', 48100))
print(s.recvfrom(2048))
s.close()
```

P1 CLI：

```text
display nat-policy sessions name CLI-UDP
display nat-policy statistics name CLI-UDP
display nat-policy runtime
display nat-policy workers
```

实测回显成功，P2 看到源 `198.19.80.1:52002`；CLI 同时显示：

```text
host-p1a12/outbound  FIB:0 -> FIB:0  Policy:CLI-UDP(1996602227)/10  Action:SNAT-PAT
198.19.80.1:47100 -> 198.19.80.2:48100  =>  198.19.80.1:52002 -> 198.19.80.2:48100
```

规则统计为 1 packet、49 bytes、Priority 7。策略数字 ID 和分配到的具体 PAT 端口会随环境变化。规则统计与逐会话包/字节统计独立，后者默认关闭，不能将未采集的零值解释成没有报文，见[统计说明](../operator/nat/sessions.md)。

## 端口集合与配额

保持上一条会话未过期，P1 修改规则并将策略上限降到 2：

```text
nat-policy name CLI-UDP
 session-limit 2
 rule 10
  undo source port
  undo destination port
  source port-set name CLI-SPORT
  destination port-set name CLI-DPORT
  quit
 quit
commit
```

分别以源端口 47101、47102 连续运行客户端。实测 47101 收到回包，P2 看到转换后端口 52000；47102 超时。此时活动会话数 2、worker Quota 增加 1，PAT fail/retry/exhaust 均为 0，说明是策略配额生效，并非端口耗尽。

```text
nat-policy name CLI-UDP
 undo session-limit
 quit
commit
```

再次使用 47102，实测转换为 52003，连续三个请求均收到回包。上限修改没有清理前面已存在的会话。

## 撤销

先撤销转换，明确保留放行行为：

```text
nat-policy name CLI-UDP
 rule 10
  undo source port-set name
  undo destination port-set name
  undo source address-set name
  undo destination address-set name
  undo source vpn-instance
  undo destination vpn-instance
  undo protocol
  undo priority
  undo action snat
  action no-nat
  quit
 quit
commit
```

使用新端口 47103 发起测试，P2 实际看到原始源端口 47103，回显成功。原有会话仍按自己的转换状态处理，因此必须用新流验证规则撤销。只清除唯一 action 而不补回动作或删除规则，提交会被拒绝，Running 保持原行为。

清理专用对象：

```text
interface host-p1a12
 undo nat-policy CLI-UDP outbound
 quit
undo nat-policy name CLI-UDP
undo nat-policy address-set name CLI-SRC
undo nat-policy address-set name CLI-DST
undo nat-policy port-set name CLI-SPORT
undo nat-policy port-set name CLI-DPORT
undo nat-policy interface-pat-range
commit
display nat-policy runtime
```

实测成功查询的 runtime 不再包含该策略。需要持久保存时执行 `save`；删除策略前必须先解除接口绑定。地址若属于已有链路，不随实验一起删除。
