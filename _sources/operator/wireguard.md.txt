# WireGuard

用密钥认证的三层隧道互连站点。

[命令参考](reference/wireguard.md) · [配置案例](../examples/wireguard.md)

~~~{toctree}
:maxdepth: 2

wireguard/profile
wireguard/lifecycle
wireguard/queries
~~~

## 激活条件

接口须未 shutdown，配置相应 tunnel-protocol，绑定含有效私钥的完整 profile，并已成功创建 Tunnel。显式 source 必须是对应底层 VPN 中的本机地址；自动 source 按每个 peer 的底层出口选择。Tunnel 上有有效 IP 地址后才能显示三层 Protocol Up。

接口状态与 peer 握手分别判断：未配置 peer、尚未握手或某个 peer 失联，不会直接使共享 Tunnel 整体 Down。实际通信还要求对端公钥、预共享密钥（如使用）、端点、允许前缀及业务路由正确，底层 UDP 能双向通过。先发起业务，再检查握手时间、peer 收发计数及双向探测。
