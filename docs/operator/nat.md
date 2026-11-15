# NAT

NAT 策略按接口和方向匹配 IPv4 流量，可执行源地址转换、目的地址转换、双向转换或明确不转换。规则、地址集和地址池只定义意图，绑定接口并提交后才参与转发。NAT 需要 VPP 数据面。

先按转换方式选择子页；共享对象、回流、会话和容量分别维护。各子页给出适用条件、配置、示例输出结果和撤销步骤。

| 需求 | 功能 |
|---|---|
| 多个内部连接共享出口地址 | 接口 PAT、地址池 PAT |
| 保留源端口 | NO-PAT |
| 固定前缀的一对一转换 | 静态 NAT |
| 发布内网服务 | DNAT |
| 同时改变源、目的地址 | Twice NAT |
| 指定流量不做转换 | No-NAT |
| 内网访问发布地址 | NAT 回流 |

接口地址作为 SNAT 来源时，只能绑定 **outbound**；地址池 SNAT 的方向按业务路径选择。带端口转换的 DNAT 使用直接的目的端口匹配，不能以 port-set 替代。

配置改变主要影响新流；已有状态会话继续使用已建立的映射。验证新规则时使用新的连接，不将旧会话仍存在误判为下发失败。

~~~{toctree}
:maxdepth: 2

nat/objects
nat/interface-pat
nat/pool-pat
nat/no-pat
nat/static
nat/dnat
nat/twice
nat/no-nat
nat/hairpin
nat/sessions
nat/capacity
~~~

[逐条命令参考](reference/nat.md) · [NAT 案例目录](../examples/nat/index.md)
