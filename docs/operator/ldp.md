# MPLS 与 LDP

使用 LDP 在 IPv4 核心网分发 MPLS 传输标签。

[命令参考](reference/mpls.md)

## 标签分发与转发前提

LDP（RFC 5036）为已知前缀分发标签，常配合 IGP 建立 MPLS 承载。IGP 负责下一跳可达性，LDP 提供相应标签绑定；LDP 邻居存在不代表所有目标前缀都有可用 LSP。

适合 MPLS 核心网的标签传输。接口 MPLS、LDP 激活、传输地址及底层路由要一致规划。检查邻居、绑定、LSP 和实际 MPLS 转发表，再验证上层 VPN 或 IPv6 业务。

标签 TTL、倒数第二跳弹出和显式空标签影响实际报文形态，详见 TTL 页面。删除前确认依赖该 LSP 的 L3VPN、6PE 等业务已迁移或允许中断。

~~~{toctree}
:maxdepth: 2

ldp/activation
ldp/ttl
ldp/operations
~~~
