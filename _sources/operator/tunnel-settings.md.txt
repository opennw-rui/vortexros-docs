# Tunnel 接口

配置源地址、目的地址和封装前，先确认两端 underlay 可达。

[命令参考](reference/tunnels.md)

## 内层、底层与激活条件

Tunnel 接口代表封装后的业务链路，内层地址和业务路由决定哪些报文进入隧道；底层源、目的、VPN 和路由决定封装报文能否离开设备。接口激活检查是本地可用条件，不保证远端解封装或应用正常。

不同协议的封装开销、密钥/Key 语义及邻居验证能力不同，不能用相同的 Up 状态解释 GRE、IP-in-IP、WireGuard 和 VXLAN。改变协议或关键参数可能重建隧道并瞬时中断业务，具体条件见各协议页。

规划顺序为底层可达性、两端协议参数、MTU、内层地址与路由，最后检查实际双向业务。对同一接口同时应用 ACL、NAT、MQC 或 MSS 时，按内层/外层位置和[处理顺序](interface-processing.md)区分作用范围。

~~~{toctree}
:maxdepth: 2

tunnel-settings/endpoints
tunnel-settings/gre-key
tunnel-settings/lifecycle
~~~
