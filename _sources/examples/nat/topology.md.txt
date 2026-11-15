# 基础拓扑

本组案例来自开发服务器隔离的 P1/P2/P3 真实 CLI 与 HTTP 端点实验。接口名 `host-p1q13` 等是该实验的 VPP/LCP 接口名；使用自己的实验口替换，不能直接套用到管理口。

~~~text
P3 客户端/内网服务       P1 NAT 网关                    P2 外网端点
198.18.11.2/24 ── host-p1q13 198.18.11.1/24
                        host-p1a12 198.19.80.1/30 ── 198.19.80.2/30
公网映射地址：198.19.81.1、198.19.81.2，P2 经 198.19.80.1 路由返回
~~~

## P1

两个承载接口已存在、处于三层模式，且由 VPP 管理：

~~~text
system-view
interface host-p1q13
 ip address 198.18.11.1 255.255.255.0
quit
interface host-p1a12
 ip address 198.19.80.1 255.255.255.252
quit
commit
display interface brief
~~~

## P2

~~~text
system-view
interface host-p2a12
 ip address 198.19.80.2 255.255.255.252
quit
ip route-static 198.19.81.0 255.255.255.0 198.19.80.1
ip route-static 198.18.11.0 255.255.255.0 198.19.80.1
commit
~~~

P3 的 Linux 测试端口配置 `198.18.11.2/24`，默认路由经 `198.18.11.1`。该默认路由保证内网服务回包重新经过 NAT 网关。P2 在 8080 监听 HTTP，P3 在 8081 监听 HTTP；可使用普通 HTTP 服务，例如 Linux Bash 中：

~~~bash
python3 -m http.server 8080 --bind 198.19.80.2
~~~

P3 对应使用 `python3 -m http.server 8081 --bind 198.18.11.2`。在各自端点直接访问监听地址，先确认服务自身正常。NAT 案例的 HTTP 状态码来自这些端点，不是产品 CLI 输出。

## 如何判定生效

SNAT：P3 访问 `http://198.19.80.2:8080/`，P2 的服务日志应看到转换后的源地址。DNAT：P2 访问 `http://198.19.80.1:18080/`，应到 P3 的 8081。用 `curl --noproxy '*' --max-time 5 URL` 发起新连接。

CLI 的会话显示证明映射，端点的 HTTP 200 和源地址日志证明真实往返。No-NAT、静态 NAT 没有状态会话，必须结合端点观测。

完成各案例撤销后再删除共用路由、接口地址和测试 HTTP 服务。P2 的两条实验静态路由分别以同样的前缀、掩码和下一跳加 `undo` 撤销，不能删除其他实验使用的共享基础设施。
