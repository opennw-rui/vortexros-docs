# 协议绑定


```text
interface Vlanif 12
 ospf bfd enable
```

```text
bgp 64512
 peer 10.0.0.2 bfd enable
```

IS-IS和RIP使用同样的接口形式，将命令前缀替换为 `isis bfd` 或 `rip bfd`。

```text
display bfd configuration
display bfd session all
display bfd statistics
```

BFD 会话摘要显示 Local、Remote 鉴别值、出接口、单跳或多跳和状态。
`display bfd session <名称>` 还显示源地址、配置与运行定时器、检测超时和诊断。
尚未在后端建立的会话显示 Pending。

若配置过非默认计时，使用以下前三条 undo 恢复；需要删除时使用最后一条 undo：

```text
bfd TO-P2 bind peer-ip 10.0.12.2 source-ip 10.0.12.1 interface Vlanif 12
 undo min-tx-interval
 undo min-rx-interval
 undo detect-multiplier
 #
undo bfd TO-P2
```

CLI 操作：

```text
commit
```


## 共享和计时归属

在接口下启用 BFD 不会自动启用相应的路由协议。IS-IS 接口尚未启用时，设备保存 BFD 预配置；创建该电路后才向后端注册，不会伪造已建立的会话。检查 `display bfd session all` 中实际会话，而不是只看 `display bfd configuration` 的 Enabled。

同一个 bfdd 会话可以被多个协议引用，它们必须使用相同的有效计时器；但 IPv4 与 IPv6 是不同的会话，允许不同计时器。当前 FRR 在双地址族 IS-IS 电路上优先使用 IPv6 BFD，不能把同端口的所有协议都无条件看成同一会话。

协议缺省使用 1000ms 发送、1000ms 接收、检测 3 次。需要非默认参数时，两端及共享同一会话的协议引用应协调一致，并在 display bfd session 中核对有效值。

配置非默认计时应先写计时器，再启用对应绑定，避免在同一会话上保留不一致的中间配置。例如：

```text
interface Ethernet 1
 ipv6 enable
 ospf bfd min-tx-interval 500 min-rx-interval 500 detect-multiplier 4
 ospf bfd enable
 ospfv3 bfd min-tx-interval 600 min-rx-interval 600 detect-multiplier 5
 ospfv3 bfd enable
#
```

CLI 操作：

```text
commit
```

修改已经共享同一会话的计时器时，应先停用相关绑定，统一参数后再启用。撤销参数使用：

```text
interface Ethernet 1
 undo ospf bfd enable
 undo ospf bfd min-tx-interval min-rx-interval detect-multiplier
 undo ospfv3 bfd enable
 undo ospfv3 bfd min-tx-interval min-rx-interval detect-multiplier
#
```

CLI 操作：

```text
commit
```

提交后应检查会话引用是否撤销，配置中默认参数是否省略。动态协议会话直接使用上述计时参数，无需另外创建 BFD profile。


[默认计时](../bfd.md) · [命令参数](../reference/bfd.md)


## RIP 撤路与等价路径

RIP 的 BFD 检测到邻居故障后，撤销该邻居贡献的转发路径。只有一条路径时，该前缀不应继续出现在活跃 IP 路由表中；协议表可能暂时保留 metric 16 的不可达记录，等待正常回收。存在等价路径时，仅撤销故障邻居，其他路径继续转发。

检查时同时使用以下命令：

~~~text
display bfd session all
display bfd statistics
display rip 96 route
display ip routing-table vpn-instance BLUE protocol rip
~~~

动态会话与 RIP 邻居生命周期联动；邻居被删除时，对应的动态 BFD 会话也可能消失。不要把会话不再列出误当成仍处于 Up。解除故障后，重新收到路由通告并建立会话，才能确认恢复。


## 故障检测与重新建邻

当前协议联动不提供 BFD strict-mode。BFD 从 Up 转为 Down 会通知使用它的路由协议，但若协议 Hello 仍能到达，邻接随后可能重新建立，而 BFD 会话尚未恢复。因此，不能将单独屏蔽 BFD 报文的实验理解为“只要 BFD 显示 Down，协议路由就永久禁止安装”。需要同时查询邻居、路由及实际业务流量。关于 OSPF strict-mode 对建邻条件的额外要求，参见 [RFC 9355](https://www.rfc-editor.org/rfc/rfc9355.html)。

一组同接口 OSPFv3 与双栈 IS-IS 的运行结果中，共享会话使用 IPv6 链路本地地址，配置发送 200 ms、接收 300 ms、检测倍数 4，正常为 Up。单独丢弃该链路的 BFD 控制报文后，会话 Down，IS-IS 两族目标路由一度撤销；由于 IS-IS Hello 仍正常，邻接和路由随后恢复。解除屏蔽后，BFD 恢复 Up。该行为与接口物理断链或业务路径整体中断应区分。

共享会话的本端配置恢复 1000/1000/3 后，对端仍使用检测倍数 4 时，运行显示的检测超时可以为 4000 ms。配置值与协商结果不是同一项，不能仅用本端的 1000×3 推断所有显示值。
