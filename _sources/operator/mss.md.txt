# TCP MSS

TCP MSS 只调整带 MSS 选项的 TCP SYN，包括建连请求和应答。它限制 TCP 单段数据长度，不改变接口 MTU，也不会解决 UDP 或其他非 TCP 报文的分片问题。只将过大的值调小，不会放大对端声明的 MSS。

[命令参考](reference/mss.md)

## 配置

在承载流量的接口上选择自动模式或固定值，两者互斥。自动模式根据接口 MTU 分别计算 IPv4、IPv6 的上限，接口 MTU 改变后会更新：

```text
system-view
interface host-p1q13
 tcp mss clamp
quit
commit
```

固定值适合已知路径上限：

```text
interface host-p1q13
 tcp mss 1200
quit
commit
```

`commit` 应用当前修改；确认后执行 `save` 才会写入启动配置。只影响新建立连接的握手，已有连接不会重新协商 MSS。

## 双栈实例与实际结果

本例在开发服务器的隔离 VPP 拓扑中完成。客户端通过 P1 的 `host-p1q13` 接入，HTTP 服务器位于 P2，P1 与 P2 已有双栈路由：

```text
客户端                           P1                        P2 HTTP 服务器
198.18.11.100/24 --- host-p1q13 198.18.11.1 --- 10.201.12.2:18080
2001:db8:11::105 ---            2001:db8:11::1 --- [2001:db8:12::2]:18081
```

HTTP 服务只提供本次测试的公共文件。测试客户端原始 SYN 的 MSS 为 IPv4 1460、IPv6 1440；在客户端和服务器同时抓取新连接的 SYN/SYN-ACK，区分原值与实际修改值。客户端使用：

```sh
curl -4 http://10.201.12.2:18080/probe.txt
curl -6 'http://[2001:db8:12::2]:18081/probe.txt'
```

两次请求均实际返回：

```text
VortexROS CLI MSS acceptance
```

实际验证结果如下，两个方向均检查握手，而不是仅凭配置存在判断生效：

| 配置 | 服务器收到的 IPv4 / IPv6 SYN MSS | 客户端收到的 IPv4 / IPv6 SYN-ACK MSS |
| --- | --- | --- |
| `tcp mss 1200` | 1200 / 1200 | 1200 / 1200 |
| `tcp mss clamp`，接口 MTU 1320 | 1280 / 1260 | 1280 / 1260 |
| 撤销 MSS 和 MTU 修改 | 1460 / 1440 | 1460 / 1440 |

固定模式验证后，先配置自动模式和 MTU 1400，再只将 MTU 改为 1320 并提交，抓包得到上表自动模式的值，证明无需重新输入 MSS 命令。上述请求都成功完成；该功能验证不代表吞吐性能测试。

查看已提交配置：

```text
display current-configuration interface host-p1q13
```

## 撤销与排查

```text
system-view
interface host-p1q13
 undo tcp mss
 undo mtu
quit
commit
```

`undo mtu` 只用于撤销本例额外的 MTU 修改；有实际业务 MTU 要求时保留原值。撤销后用新连接抓包，确认 MSS 恢复。若没有变化，检查连接是否新建、接口及流量路径是否正确，以及原始 MSS 是否已低于上限。不要用旧连接或仅有配置输出作为报文修改的证据。

[完整案例、实际查询与撤销](../examples/qos.md)
