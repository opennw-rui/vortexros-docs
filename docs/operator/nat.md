# NAT

通过 NAT 策略执行源地址、目的地址或双向转换。

[命令参考](reference/nat.md) · [配置案例](../examples/nat-pat.md)

## 配置与验证

在`display nat-policy name ?`中，`<NAT-POLICY>`表示可输入策略名，后续各行列出当前Candidate中已有的策略名；Tab和`?`使用相同的大小写无关字母顺序。

```text
nat-policy address-set name INSIDE
 address 10.0.0.0/8
#
nat-policy port-set name WEB
 port 80
 port 443
#
nat-policy name INTERNET
 statistic enable
 rule 10
  source address-set name INSIDE
  destination port-set name WEB
  action snat pat interface
```

接口绑定：

```text
interface Vlanif 100
 nat-policy INTERNET inbound
```

统计默认关闭；只有在policy或rule下显式配置 `statistic enable` 后才更新对应计数。未启用统计时，display会明确显示统计关闭。

```text
display nat-policy name INTERNET
display nat-policy statistics name INTERNET
clear nat-policy counters
display nat-policy sessions
clear nat-policy sessions
```

`display nat-policy sessions`不带参数时展示全部活动会话。也可以任意组合下列条件；多个条件采用AND语义，并由数据面按原始（转换前）五元组直接筛选：

```text
display nat-policy sessions [protocol { tcp | udp | icmp | sctp | 0..255 }]
 [source-ip IPV4] [destination-ip IPV4]
 [source-port PORT] [destination-port PORT]
 [worker INDEX] [core CPU-ID] [name POLICY] [rule RULE-ID]
 [action { no-nat | static-nat | snat-no-pat | snat-pat | dnat | twice-nat }]
 [hairpin { enable | disable }]
```

例如，查看`INTERNET`策略中由CPU 6处理、目的端口为443的TCP PAT会话：

```text
display nat-policy sessions protocol tcp destination-port 443 core 6 name INTERNET action snat-pat
```

会话按块显示。首行是协议、状态、worker、CPU核心、剩余时间和计数，第二行是接口、方向、FIB、policy/rule和动作，第三行显示原始五元组到转换后五元组。TCP、UDP和SCTP显示端口；ICMP显示identifier；GRE、ESP、AH、OSPF等无端口协议只显示地址，避免把内部零值误当成端口。

NAT回流默认关闭。需要先开启全局开关，再在包含DNAT、twice-NAT或静态NAT发布规则的policy中开启：

```text
nat-policy hairpin enable
nat-policy name INTERNET
 hairpin enable
commit
```

关闭时可撤销policy或全局开关：

```text
nat-policy name INTERNET
 undo hairpin enable
quit
undo nat-policy hairpin enable
commit
```

两个开关必须同时开启。显式NO_NAT和本接口的显式转换决定优先；回流只使用同一FIB中的唯一发布映射。开关不会强制清除已有会话。验证时应同时测试客户端到公网映射地址的正向连接、服务端回包恢复、同一端口多连接、会话清除后端口复用，以及关闭后已有会话不断、新会话不再回流。

新增、修改或删除规则后，只影响相关policy和接口绑定。已有会话继续按会话状态处理，新连接使用新的规则。

解除接口绑定后再删除policy和对象：

```text
interface Vlanif 100
 undo nat-policy INTERNET inbound
undo nat-policy name INTERNET
undo nat-policy port-set name WEB
undo nat-policy address-set name INSIDE
commit
```
