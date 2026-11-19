# AmneziaWG

配置独立的 AmneziaWG 隧道及两端的协议参数。

[命令参考](reference/amneziawg.md) · [配置案例](../examples/amneziawg.md)

## 工作原理与版本选择

AmneziaWG 在 WireGuard 式密钥隧道之外加入版本相关的报文外观及填充参数。两端必须选用本产品支持的相同协议版本，并按该版本配置一致参数；不能把不同版本示例中的字段任意拼接。

它适合需要对应协议互通的加密三层连接，不是只要接口 Up 就完成了对端认证。密钥、端点、允许前缀与业务路由仍需正确配置。额外填充会增加报文开销，MTU 和带宽规划应预留空间。

支持版本、字段关系与完整配置分别见下列页面。修改协议参数后检查实际握手和双向业务，使用对端普通 WireGuard 能连通的结果不能替代 AmneziaWG 的版本互通验证。

~~~{toctree}
:maxdepth: 2

amneziawg/versions
amneziawg/profile
amneziawg/timers
~~~

## 激活条件

接口须未 shutdown，配置相应 tunnel-protocol，绑定含有效私钥的完整 profile，并已成功创建 Tunnel。显式 source 必须是对应底层 VPN 中的本机地址；自动 source 按每个 peer 的底层出口选择。Tunnel 上有有效 IP 地址后才能显示三层 Protocol Up。

接口状态与 peer 握手分别判断：未配置 peer、尚未握手或某个 peer 失联，不会直接使共享 Tunnel 整体 Down。实际通信还要求对端公钥、预共享密钥（如使用）、两端混淆参数、端点、允许前缀及业务路由正确，底层 UDP 能双向通过。先发起业务，再检查握手时间、peer 收发计数及双向探测。

协议参数与客户端兼容范围见[版本与参数](amneziawg/versions.md)。
