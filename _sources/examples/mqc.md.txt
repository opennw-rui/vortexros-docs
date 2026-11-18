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
~~~

配置清单：

~~~text
interface Ethernet0
 ip address 192.0.2.82 255.255.255.252
#
~~~

CLI 操作：

~~~text
commit
~~~

## 配置 P1

先配置地址并确认能 Ping 通 P2，再配置并绑定策略。

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 ip address 192.0.2.81 255.255.255.252
#
~~~

CLI 操作：

~~~text
commit
ping -n -c 3 -t 1000 192.0.2.82
~~~

~~~text
traffic classifier LAB-DST operator or
 if-match destination-ip 192.0.2.82/32
#
traffic behavior LAB-MARK
 remark dscp 10
#
traffic policy LAB-POLICY
 classifier LAB-DST behavior LAB-MARK precedence 10
#
interface Ethernet0
 traffic-policy LAB-POLICY outbound
#
~~~

CLI 操作：

~~~text
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
~~~

配置清单：

~~~text
interface Ethernet0
 undo traffic-policy outbound
#
undo traffic policy LAB-POLICY
undo traffic behavior LAB-MARK
undo traffic classifier LAB-DST
~~~

CLI 操作：

~~~text
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
#
traffic behavior CLI-REMARK
 remark dscp 20
#
traffic policy CLI-MARK
 classifier CLI-ANY behavior CLI-REMARK precedence 7
#
interface Ethernet0
 traffic-policy CLI-MARK outbound
#
```

CLI 操作：

```text
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
#
traffic policy CLI-MARK
 undo precedence
#
```

CLI 操作：

```text
commit
ping -c 1 -a 192.0.2.82 192.0.2.81
```

查询策略应显示 Precedence: 0，且不再包含 Remark。撤销时先解除绑定，再删除对象：

```text
interface Ethernet0
 undo traffic-policy outbound
#
undo traffic policy CLI-MARK
undo traffic behavior CLI-REMARK
undo traffic classifier CLI-ANY
```

CLI 操作：

```text
commit
```

## 入方向、出方向与 ACL 的组合

可在同一台路由器两侧接口分别标记同一类转发流量：入方向行为设 DSCP20，出方向行为设 DSCP10。实际报文验证中，只有入方向时接收端 ToS 为0x50，增加出方向后为0x28；撤销两侧策略后恢复0。后一次标记覆盖前一次，但不会覆盖 DSCP以外的匹配字段。

入方向 ACL 在 MQC之前过滤。在同类 UDP验证中，未绑定 ACL时接收端能收到报文；绑定拒绝规则后报文被丢弃；将同一条已绑定规则改为 permit并提交后，接收恢复。不能用“未收到报文”单独证明 ACL生效，还要确认接口和数据面健康，并保留放行对照。

撤销时先解除 ACL和流策略绑定，再删除不再使用的 ACL、策略、行为和分类器。撤销后的新报文已确认可以正常转发，DSCP回到原值；当前配置不再保留这些示例对象。

## CAR、拒绝和空分类器

同一条出方向策略使用 `if-match any`，行为配置 100kbps CAR 后，超过限额的 UDP 业务出现实际丢弃；撤销 CAR 后，约 1Mbps 的同一负载收到 251/251 个报文。短窗口含突发量，这里用于检查规则是否执行，不是稳态吞吐或设备性能结论。

将行为改为 `deny`，IPv4 和 IPv6 对照探测均无回复；`undo deny` 后恢复普通放行。在拒绝行为仍存在的情况下，从分类器撤销 `if-match any` 后，查询显示无匹配规则、运行匹配计数为 0，原业务恢复。没有匹配条件的分类器不等于显式匹配全部；只有需要覆盖全部报文时才使用 `if-match any`。
