# ICMP 发送控制

在三层接口上禁止设备从该接口发送指定的 IPv4 ICMP 报文。配置对 VPP 和 Linux 统一生效，用户无需选择报文生成者。

规则只限制设备本机生成的 ICMP，不是转发 ACL。经过设备转发的 TCP、UDP 和 ICMP 报文不匹配这些规则。TTL 已耗尽的原始报文仍按原有逻辑丢弃；禁止的是随后生成的超时回复。

## 默认行为与接口含义

默认没有禁止规则，ICMP 按各协议原有的发送条件和限速工作，默认项不显示在配置中。禁止规则仅抑制匹配的本机 ICMP 消息，不会启用原本不支持的 ICMP 类型。

接口指 ICMP 回复自身经路由选择后的发送接口，不是原始报文的入接口。设备用对应路由域的路由返回发送者；非对称路由下，两者可能不同。源地址的选择和出接口的选择不能混为一谈。

## 配置

在接口视图禁止消息，提交后生效：

进入系统视图后，配置：

```text
interface Ethernet 0
 undo icmp name ttl-exceeded
 undo icmp name echo-reply
#
```

返回系统视图提交，再保存：

```text
commit
save
```

数值规则支持 Type 0–255；Code 可以省略，或指定 0–255：

```text
[~VortexROS-Ethernet0] undo icmp type 11
[*VortexROS-Ethernet0] undo icmp type 3 code 4
```

`type 11` 禁止这一 Type 的全部 Code；`name ttl-exceeded` 等价于 `type 11 code 0`。同一规则用名称或数值输入不会产生两个条目。

整类规则与精确规则分别保存，任意一条匹配即禁止。例如同时配置 `type 11` 和 `type 11 code 0`，撤销后者仍然禁止 11/0。没有用“允许”覆盖禁止规则的优先级机制。

## 名称

| 名称 | Type | Code |
| --- | ---: | ---: |
| echo | 8 | 0 |
| echo-reply | 0 | 0 |
| ttl-exceeded | 11 | 0 |
| reassembly-timeout | 11 | 1 |
| net-unreachable | 3 | 0 |
| host-unreachable | 3 | 1 |
| protocol-unreachable | 3 | 2 |
| port-unreachable | 3 | 3 |
| fragmentneed-dfset | 3 | 4 |
| source-route-failed | 3 | 5 |
| parameter-problem | 12 | 0 |
| redirect | 5 | 全部 |
| net-redirect | 5 | 0 |
| host-redirect | 5 | 1 |
| net-tos-redirect | 5 | 2 |
| host-tos-redirect | 5 | 3 |
| source-quench | 4 | 0 |
| timestamp-request | 13 | 0 |
| timestamp-reply | 14 | 0 |
| information-request | 15 | 0 |
| information-reply | 16 | 0 |

## 验证与影响

用 `display this` 查看接口配置，用 `display icmp interface Ethernet 0` 对照已配置规则和 VPP、Linux 的实际回读结果。

禁止 Echo Reply 后，发往设备自身接口地址的 ping 可以超时；经过设备去访问其他主机的 ping 应继续正常。禁止 TTL Exceeded 会使 traceroute 对应跳不再回复，但不会让已经耗尽 TTL 的原始报文继续转发。

禁止 `fragmentneed-dfset` 或整个 Type 3 会抑制路径 MTU 发现需要的反馈，可能间接导致较大业务报文无法通信。禁止规则的含义是抑制反馈，不是保证所有上层协议行为完全不受影响。

只有支持 IPv4 三层处理的接口才能配置此功能。ICMPv6 不属于本命令范围。

ICMP 回复可以沿普通 IPv4 回程，也可以沿 MPLS 标签回程发送；规则均按最终邻接的出接口匹配。禁止的是本机新生成的 ICMP。已经由其他设备生成、经过本设备转发的 ICMP，即使需要压入 MPLS 标签，也不会被本规则过滤。

## 查询示例与发送效果

以下输出按本例的 `Ethernet0` 名称整理，字段来自实际规则回读：

```text
<VortexROS> display icmp interface Ethernet 0
Interface: Ethernet0
IPv4 ICMP send policy: egress, locally generated only
Scope: locally generated IPv4 ICMP, including MPLS return paths, and Linux local output.
Rule                               Configured   VPP          Linux
name ttl-exceeded                  deny         installed    installed
```

`Configured` 是已提交意图；`VPP`、`Linux` 的 `installed` 表示这一条精确规则已从对应后端读回。`-` 表示没有这条规则，不代表报文一定允许：另一个整类 Type 规则仍可能禁止它。Linux 数据面没有 VPP 投影时，VPP 列显示 `not applicable`。先用 `display health` 确认配置已经收敛，再判断效果。

实际验证覆盖：

| 场景 | 观察结果 |
| --- | --- |
| 仅在原始报文的入接口禁止 TTL 超时，回复从另一接口发送 | 回复仍发出 |
| 在实际发送接口禁止 TTL 超时 | 不再捕获到对应回复 |
| 禁止本机 Echo、Echo Reply 和 TTL 超时 | 本机请求及回复被禁止；穿越设备的 ping 仍为 2/2 |
| 普通 TCP、UDP 及转发的 ICMP 差错报文 | 仍可转发；TCP 完成 4096 字节内容校验 |
| 出接口 MTU 1200、转发带 DF 的 1400 字节 IPv4 报文 | 正常返回携带 MTU 1200 的 3/4 消息；禁止后不返回，撤销后恢复 |
| 完整 Type 11 与精确 11/0 重叠 | 撤销精确项后，整类禁止仍生效 |
| 保存并重新启动数据面 | 已保存规则恢复，VPP 与 Linux 均显示已安装 |
| MPLS 双标签回程 | TTL 超时和 Echo Reply 在允许时发出，禁止后不发出；同时转发的 UDP 和 ICMP 差错报文仍正常压入标签发送 |
| 21 个名称及数值边界规则 | 均可配置、回读和撤销；不表示系统会生成所有历史 ICMP 类型 |

设备从被禁止的接口主动发送消息时，Linux 工具可能直接报告 `Operation not permitted`，也可能表现为没有回复。应结合规则回读与对端接收结果判断，不能仅把工具退出码当成转发故障。批量数据和硬件吞吐不属于上述功能结果。

## 撤销与保存恢复

使用正向命令撤销同一条禁止规则，随后提交：

```text
interface Ethernet 0
 icmp name ttl-exceeded
 icmp name echo-reply
 icmp type 11
 icmp type 3 code 4
#
```

返回系统视图提交、保存：

```text
commit
save
```

`save` 记录已提交配置。重启和数据面重新接管后按保存配置恢复规则。接口删除时移除相应规则，避免接口索引被重新使用后套用旧规则。

## 运维检查

- 禁止反馈消息前，确认受影响的是设备自身消息，还是业务所依赖的错误反馈。
- 修改规则后，同时检查当前配置、实际安装状态以及必要的端到端业务。
- 撤销全部规则后，当前配置不再出现 ICMP 禁止项，查询显示 `No ICMP send suppression configured or installed.`。
- 地址、路由、接口或数据面重建时，规则仍属于原接口配置；用保存恢复流程管理它们，不在后端手工维护另一份规则。

## 协议依据

ICMP 类型、差错消息和回复约束由 [RFC 792](https://www.rfc-editor.org/rfc/rfc792.html) 与 [RFC 1812](https://www.rfc-editor.org/rfc/rfc1812.html) 定义。这些规范不定义厂商 CLI，也不构成与某个 VRP 版本全部行为一致的认证。

