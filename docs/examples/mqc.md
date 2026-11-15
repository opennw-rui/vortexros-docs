# MQC 报文标记

## 拓扑

~~~text
P1 Ethernet0 192.0.2.81/30 ─── 192.0.2.82/30 Ethernet0 P2
            出方向标记                         接收侧抓包
~~~

两端运行 VPP，并使用专用三层测试口。这个例子只按目的 IPv4 地址匹配，将 DSCP 改为 AF11（十进制 10）；不配置限速或丢弃。先确认 P1 的测试口没有其他出方向流量策略。

## 配置 P2

~~~text
system-view
interface Ethernet0
 ip address 192.0.2.82 255.255.255.252
 quit
commit
~~~

## 配置 P1

先配置地址并确认能 Ping 通 P2，再配置并绑定策略。

~~~text
system-view
interface Ethernet0
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
interface Ethernet0
 traffic-policy LAB-POLICY outbound
 quit
commit
~~~

匹配条件覆盖从该口发往 192.0.2.82 的 IPv4 报文；ICMP 只是本例的探测流量。其他流量走默认分类，不会被这条规则标记。

## 验证

在 P1 执行 `display traffic policy user-defined LAB-POLICY`。示例输出：

~~~text
  User Defined Traffic Policy Information:
    Policy: LAB-POLICY
      Classifier: LAB-DST Precedence: 10
        Behavior: LAB-MARK
        Remark:
          dscp af11(10)
~~~

在 P1 执行 ping -n -c 3 -t 1000 192.0.2.82，确认业务仍可达。DSCP AF11 对应 10，IPv4 ToS 在 ECN 为 0 时为 0x28。display 查询用于核对策略配置，不能单独证明报文已改写；需要检查字段时，在链路使用报文分析设备观察同类新报文的 DSCP。

## 撤销

在 P1 先解除绑定，再删除仅供此示例使用的对象：

~~~text
system-view
interface Ethernet0
 undo traffic-policy outbound
 quit
undo traffic policy LAB-POLICY
undo traffic behavior LAB-MARK
undo traffic classifier LAB-DST
commit
~~~

重复业务探测，确认策略解除后仍能普通转发。需要检查 DSCP 恢复时观察新报文；若接口地址也只供本例使用，再在两端撤销。

[MQC 配置指南](../operator/mqc.md)

## 匹配全部与恢复默认优先级

在同一拓扑的 P2 出口改用 if-match any，覆盖所有报文。两端沿用 192.0.2.81/30 与 192.0.2.82/30，无需更换地址。

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
interface Ethernet0
 traffic-policy CLI-MARK outbound
 quit
commit
ping -c 3 -a 192.0.2.82 192.0.2.81
display traffic policy user-defined CLI-MARK
```

DSCP 20 对应 ECN 为 0 时的 ToS 0x50。any 会匹配该方向所有报文，包括控制流量；应确认作用范围后使用。

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
ping -c 1 -a 192.0.2.82 192.0.2.81
```

查询策略应显示 Precedence: 0，且不再包含 Remark。撤销时先解除绑定，再删除对象：

```text
interface Ethernet0
 undo traffic-policy outbound
 quit
undo traffic policy CLI-MARK
undo traffic behavior CLI-REMARK
undo traffic classifier CLI-ANY
commit
```
