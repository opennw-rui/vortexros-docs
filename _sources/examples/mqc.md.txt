# MQC 报文标记

## 拓扑

~~~text
P1 host-p1a12 192.0.2.81/30 ─── 192.0.2.82/30 host-p2a12 P2
            出方向标记                         接收侧抓包
~~~

两端运行 VPP，并使用专用三层测试口。这个例子只按目的 IPv4 地址匹配，将 DSCP 改为 AF11（十进制 10）；不配置限速或丢弃。先确认 P1 的测试口没有其他出方向流量策略。

## 配置 P2

~~~text
system-view
interface host-p2a12
 ip address 192.0.2.82 255.255.255.252
 quit
commit
~~~

## 配置 P1

先配置地址并确认能 Ping 通 P2，再配置并绑定策略。

~~~text
system-view
interface host-p1a12
 ip address 192.0.2.81 255.255.255.252
 quit
commit
ping -n -c 3 -t 1000 192.0.2.82
~~~

~~~text
traffic classifier LAB-DST operator or
 if-match destination-ip 192.0.2.82/32
 quit
traffic behavior LAB-MARK
 remark dscp 10
 quit
traffic policy LAB-POLICY
 classifier LAB-DST behavior LAB-MARK precedence 10
 quit
interface host-p1a12
 traffic-policy LAB-POLICY outbound
 quit
commit
~~~

匹配条件覆盖从该口发往 192.0.2.82 的 IPv4 报文；ICMP 只是本例的探测流量。其他流量走默认分类，不会被这条规则标记。

## 验证

在 P1 执行 `display traffic policy user-defined LAB-POLICY`。实际输出节选：

~~~text
  User Defined Traffic Policy Information:
    Policy: LAB-POLICY
      Classifier: LAB-DST Precedence: 10
        Behavior: LAB-MARK
        Remark:
          dscp af11(10)
~~~

在 P2 的 Linux 环境执行下列抓包命令；实验中底层 veth 名为 `p2a12`，生产设备应在实际接收链路上观察。随后从 P1 执行 `ping -n -c 3 -t 1000 192.0.2.82`。

~~~bash
sudo tcpdump -n -vv -c 1 -i any 'icmp and dst host 192.0.2.82'
~~~

实际抓包节选。P1 同时收到 3 个回包：

~~~text
p2a12 P   IP (tos 0x28, ttl 64, id 60590, offset 0, flags [DF], proto ICMP (1), length 84)
    192.0.2.81 > 192.0.2.82: ICMP echo request, id 36772, seq 1, length 64
~~~

`0x28 >> 2 = 10`。这是接收侧的报文证据；只查看策略显示无法证明实际改写。

## 撤销

在 P1 先解除绑定，再删除仅供此实验使用的对象：

~~~text
system-view
interface host-p1a12
 undo traffic-policy outbound
 quit
undo traffic policy LAB-POLICY
undo traffic behavior LAB-MARK
undo traffic classifier LAB-DST
commit
~~~

重复抓包和探测。实测仍是 3 发 3 收，接收侧同类新报文恢复为 `tos 0x0`。如果地址也为本次实验新建，再分别在两端撤销对应 `ip address`。

[MQC 配置指南](../operator/mqc.md)

## 匹配全部与恢复默认优先级

本轮另在 P2 出接口验证 `if-match any`。链路地址为 P2 `host-p2a12` 的 `198.19.80.2/30` 与 P1 `host-p1a12` 的 `198.19.80.1/30`，两端均为 default VPN。地址配置沿用前面的三层接口步骤，不能与前一案例的 192.0.2.0/30 混用。

P2：

```text
traffic classifier CLI-ANY operator or
 if-match any
 quit
traffic behavior CLI-REMARK
 remark dscp 20
 quit
traffic policy CLI-MARK
 classifier CLI-ANY behavior CLI-REMARK precedence 7
 quit
interface host-p2a12
 traffic-policy CLI-MARK outbound
 quit
commit
ping -c 3 -a 198.19.80.2 198.19.80.1
display traffic policy user-defined CLI-MARK
```

P1 接收侧实际抓到三条 ICMP 请求，均为 `tos 0x50`，即 DSCP 20；P2 探测 3/3。`any` 会匹配该方向上的所有报文，包括控制流量，应确认作用范围后使用。

撤销标记、恢复优先级默认值，保留放行：

```text
traffic behavior CLI-REMARK
 undo remark dscp
 permit
 quit
traffic policy CLI-MARK
 undo precedence
 quit
commit
ping -c 1 -a 198.19.80.2 198.19.80.1
```

实测策略显示 `Precedence: 0`、不再包含 Remark；P1 同类新报文为 `tos 0x0`，回包 1/1。撤销时先解除绑定，再删除对象：

```text
interface host-p2a12
 undo traffic-policy outbound
 quit
undo traffic policy CLI-MARK
undo traffic behavior CLI-REMARK
undo traffic classifier CLI-ANY
commit
```
