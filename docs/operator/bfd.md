# BFD

用独立会话或协议绑定快速检测路径故障。

[命令参考](reference/bfd.md) · [配置案例](../examples/bfd.md)

## 配置

BFD可建立独立会话，也可由OSPF、IS-IS、RIP和BGP邻居调用。静态和协议会话均默认发送间隔 1000 ms、接收间隔 1000 ms、检测次数 3。默认参数省略于保存配置。BGP 邻居覆盖对等体组的参数时，配置仍会显示有实际影响的覆盖项。

### 独立BFD会话

```text
bfd
bfd TO-P2 bind peer-ip 10.0.12.2 source-ip 10.0.12.1 interface Vlanif 12
 log-session-changes
```

多跳会话需要显式指定 `source-ip`，VPN场景可追加 `vpn-instance BLUE`。

### 路由协议调用BFD

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
