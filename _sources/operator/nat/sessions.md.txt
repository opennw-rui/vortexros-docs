# 会话与统计

会话表示已建立的有状态转换，规则计数表示启用了统计的规则决策次数和对应字节数，worker 计数用于区分配额、容量、PAT 端口或哈希等失败。三者不能相互替代。

## 查看哪一层

| 命令 | 用途 |
|---|---|
| `display nat-policy all`、`name NAME` | 策略与规则 |
| `display nat-policy runtime` | 实际策略、引用数、会话配额、活动会话、统计和回流状态 |
| `display nat-policy objects`、`interfaces` | 实际对象与方向绑定 |
| `display nat-policy statistics [name NAME]` | 规则决策次数和对应字节数 |
| `display nat-policy sessions [FILTERS]` | 活跃有状态映射及原始/转换五元组 |
| `display nat-policy configuration` | 实际全局容量与超时 |
| `display nat-policy workers` | 每 worker 的会话、命中、丢弃及失败分类 |

## 筛选子命令

过滤条件可组合，使用 AND 语义，地址和端口匹配转换前五元组：

~~~text
display nat-policy sessions protocol tcp destination-port 443 name INTERNET action snat-pat
display nat-policy sessions source-ip 198.18.11.2 destination-ip 198.19.80.2 destination-port 8080
display nat-policy sessions hairpin enable
~~~

| 参数 | 含义 |
|---|---|
| `protocol` | tcp、udp、icmp、sctp 或 0–255 协议号 |
| `source-ip`、`destination-ip` | 原始 IPv4 主机地址 |
| `source-port`、`destination-port` | 原始端口，0–65535 |
| `worker` | VPP 线程索引 |
| `core` | 逻辑 CPU 编号，不能与 worker 索引混用 |
| `name`、`rule` | 策略名和规则 ID |
| `action` | no-nat、static-nat、snat-no-pat、snat-pat、dnat、twice-nat |
| `hairpin` | enable 只显示回流，disable 排除回流 |

TCP/UDP 显示传输层端口，ICMP 显示 identifier；SCTP 等其他协议当前按 IP 元组记录，端口列为 `0`，具体限制见下文。No-NAT、静态 NAT 不产生状态会话，所以会话数为零不代表未生效。

## 统计与会话

策略/规则 `statistic enable` 缺省关闭，显式开启后才能据此检查命中。接口 PAT 规则命中示例：

~~~text
Policy      Rule  Priority  Statistics  Packets  Bytes
-------------------------------------------------------------------------------
4124874345  10    10        policy      18       1248
~~~

Packets 与 Bytes 是规则决策计数，不是该规则所建立连接的完整转发流量。
有状态连接命中既有会话后直接使用已建立的转换，不再次进行规则决策。
例如 NUMPROTO 的 protocol17 规则实际转发了同一 UDP 五元组的三个124字节报文，
规则显示 Packets1、Bytes124；这表示一次规则决策建立了会话，不能据此判断丢了两个报文。
需要确认完整流量时，同时查看接口计数和实际收发结果。

逐会话包/字节统计是独立的后端开关，当前产品 CLI 不提供该开关；关闭时显示 `--`。不可用的逐会话计数不能解释为零流量。使用策略命中统计与实际往返联合检查。

配置 session-limit 2 时，已有两个有效会话后，新会话可能因配额失败。查询 worker 的 Quota 与 PAT fail/exhaust 区分配额和端口耗尽；放宽或撤销限制后用新连接检查。

## 清理与风险

~~~text
clear nat-policy counters
clear nat-policy sessions name LAB-SNAT rule 10
display nat-policy sessions name LAB-SNAT
~~~

清计数不删除会话；清会话会中断对应连接。不带名字的 `clear nat-policy sessions` 清除全部 NAT 会话。解除接口绑定再删除策略和对象，见[对象与规则](objects.md)。

[全部语法](../reference/nat.md)

## 按实际会话筛选

筛选条件按原始报文元组匹配，多个条件同时生效。例如：

```text
display nat-policy sessions protocol udp name LAB-SNAT
display nat-policy sessions hairpin enable
display nat-policy sessions action no-nat
display nat-policy sessions protocol sctp
display nat-policy sessions protocol 132
```

已建立的回流会话会同时显示 `Mode:hairpin`；只设置全局或策略的 hairpin 开关，不代表当前一定存在回流会话。实际筛选结果可为 `Total: 1`、`UDP:1`，并显示同一条记录的原始与转换后地址。

`action no-nat` 返回零会话是正常结果：no-NAT 和静态 NAT 使用无状态处理，不进入该会话表。应通过规则计数、原始地址是否保留和实际业务检查其效果，不能为得到非空表而制造会话。

SCTP 可按协议名 `sctp` 或数值 `132` 选择已有 IP 地址转换状态。当前这类记录以 IP 元组保存，端口列显示 `0`；这个数值不表示实际 SCTP 报文的源、目的端口被改为零。一个实际 SNAT-NO-PAT 记录显示 `SCTP:1`，原始 IP 为 198.18.30.99，转换后为 198.18.31.15，而报文中的端口仍为 42062 和 49000。这项显示能力不等于 SCTP 端口 PAT、基于端口的 SCTP 会话区分或完整关联握手验证。
