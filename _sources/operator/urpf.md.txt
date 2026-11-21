# uRPF

在入口检查报文源地址是否有可用回程路由。

[命令参考](reference/urpf.md) · [配置案例](../examples/urpf.md)

## 工作原理与路由依赖

uRPF 对进入接口的报文源地址查反向路由，以识别不符合路由拓扑的源。严格模式要求返回路径与入接口匹配，宽松模式只要求源在路由中可达；可参照 RFC 3704 理解其适用场景。

严格模式适合回程明确的单出口接入，非对称路由、多出口或策略转发环境应先评估，否则正常业务也可能被丢弃。宽松模式不能阻止所有可路由的伪造源。默认路由是否参与匹配按本产品的命令说明核对，不套用其他 NOS 的行为。

验证必须同时准备合法源、应拒绝源及回程路由对照。变更路由本身也可能改变检查结果；撤销时只撤销目标地址族，不应误改另一地址族。

## 配置与验证

接口可以启用严格或宽松的反向路径检查：

```text
interface Vlanif 100
 ipv6 enable
 ip urpf strict
 ipv6 urpf strict
```

- `strict`：源地址的最佳返回路径必须从收到报文的接口到达；
- `loose`：源地址只需在路由表中可达；
- `disable`或对应的`undo ip urpf`、`undo ipv6 urpf`：关闭该地址族检查。

IPv4和IPv6 uRPF是两个独立配置对象，修改或撤销其中一个不会覆盖另一个。使用 `display urpf` 查看全部地址族，使用`display ipv6 urpf`只查看IPv6接口模式；通过`display ip routing-table ... verbose`或`display ipv6 routing-table ... verbose`检查作为判断依据的路由。

## 将接口加入聚合

接口启用了任一地址族的 uRPF 时，需要先撤销该接口上的检查再加入 Eth-Trunk。已有 IPv4、IPv6 检查分别使用 `undo ip urpf`、`undo ipv6 urpf`，提交后用 `display urpf` 核对。加入聚合后，通过 `display eth-trunk` 查看成员，再按业务验证双栈流量。第三轮验收中，启用 uRPF 的接口被正常拒绝，撤销后同一接口加入聚合并通过双栈探测。
