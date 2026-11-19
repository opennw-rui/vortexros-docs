# WireGuard

用密钥认证的三层隧道互连站点。

[命令参考](reference/wireguard.md) · [配置案例](../examples/wireguard.md)

## 工作原理与组网规划

WireGuard 使用公钥认证对端，并以加密的 UDP 隧道承载三层报文。Peer 的 Allowed IPs 同时参与允许地址范围与对端选择；对端公钥、端点、允许前缀和路由必须相互配套。

适合站点互联或需要三层加密的点到点业务。它不是二层桥接，也不自动发布动态路由。相同目的前缀由哪个 Peer 承载应明确规划，避免把互相重叠的业务范围交给错误对端。

接口 Up 不证明已经握手或远端可达。核对最近握手、Peer 收发、业务路由和双向探测。改密钥或替换 Peer 会影响相应会话；MTU 还要扣除外层 IP、UDP 和加密开销。

~~~{toctree}
:maxdepth: 2

wireguard/profile
wireguard/lifecycle
wireguard/queries
~~~

## 激活条件

接口须未 shutdown，配置相应 tunnel-protocol，绑定含有效私钥的完整 profile，并已成功创建 Tunnel。显式 source 必须是对应底层 VPN 中的本机地址；自动 source 按每个 peer 的底层出口选择。Tunnel 上有有效 IP 地址后才能显示三层 Protocol Up。

接口状态与 peer 握手分别判断：未配置 peer、尚未握手或某个 peer 失联，不会直接使共享 Tunnel 整体 Down。实际通信还要求对端公钥、预共享密钥（如使用）、端点、允许前缀及业务路由正确，底层 UDP 能双向通过。先发起业务，再检查握手时间、peer 收发计数及双向探测。
