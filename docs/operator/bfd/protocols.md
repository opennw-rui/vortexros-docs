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
 quit
undo bfd TO-P2
commit
```



## 共享和计时归属

在接口下启用 BFD 不会自动启用相应的路由协议。IS-IS 接口尚未启用时，设备保存 BFD 预配置；创建该电路后才向后端注册，不会伪造已建立的会话。检查 `display bfd session all` 中实际会话，而不是只看 `display bfd configuration` 的 Enabled。

同一个 bfdd 会话可以被多个协议引用，它们必须使用相同的有效计时器；但 IPv4 与 IPv6 是不同的会话，允许不同计时器。当前 FRR 在双地址族 IS-IS 电路上优先使用 IPv6 BFD，不能把同端口的所有协议都无条件看成同一会话。

本轮开发服务器的真实结果：

| 协议与链路 | 实际对端族 | 有效 Tx/Rx/次数 | 状态 |
| --- | --- | --- | --- |
| OSPF，CLI-UNDER b12 | IPv4 | 500/500/4 | Up |
| OSPFv3，同一 b12 | IPv6 | 600/600/5 | Up |
| IS-IS，a12/e12 双族电路 | IPv6 | 500/500/4 | Up |
| RIP，e12 | IPv4 | 700/700/5 | Up |

这些是特意配置的非默认对照；缺省仍为1000/1000/3。RIP 表格中的运行证据来自重启回放后的实际会话，不把重启前未激活接口的状态算作通过。最终包另做了定向复核：重启 RIP 后接口和实际更新源正常，接口 Down/Up 后继续正常，双端 RIP-BFD Up、原生 700/700/5；撤销后为零。0.29-dev 后续已用保留的异常进程与重复端点重建查清组播成员泄漏；修复、最终包结果及历史样本的证据边界见 [RIP 恢复](../rip.md)。

配置非默认计时应先写计时器，再启用对应绑定，避免在同一会话上保留不一致的中间配置。例如：

```text
interface Ethernet 1
 ospf bfd min-tx-interval 500 min-rx-interval 500 detect-multiplier 4
 ospf bfd enable
 ospfv3 bfd min-tx-interval 600 min-rx-interval 600 detect-multiplier 5
 ospfv3 bfd enable
 quit
commit
```

修改已经共享同一会话的计时器时，应先停用相关绑定，统一参数后再启用。撤销参数使用：

```text
interface Ethernet 1
 undo ospf bfd enable
 undo ospf bfd min-tx-interval min-rx-interval detect-multiplier
 undo ospfv3 bfd enable
 undo ospfv3 bfd min-tx-interval min-rx-interval detect-multiplier
 quit
commit
```

提交后应检查会话引用是否撤销，配置中默认参数是否省略。后端内部生成的 `auto-bfd-*` profile 用于落实产品计时，不需要用户在 CLI 单独创建 profile。


[默认计时](../bfd.md) · [命令参数](../reference/bfd.md)
