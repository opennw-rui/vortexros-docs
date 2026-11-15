# DHCPv6 中继

本例记录开发服务器真实隔离拓扑的接口形式中继：客户端请求被转发到服务器组 `ff05::1:3`。它与同链路 `ff02::1:2` 不同；强行替换成后者会让中继接收到自己的上行请求。

## 拓扑与前提

```text
客户端 cli-r4
  │ 客户端链路 2001:db8:11::/64
P1 host-p1q13 2001:db8:11::1
P1 host-p1e12 2001:db8:12::1 ─── P2 host-p2e12 2001:db8:12::2 / Kea
P1 host-p1a12 2001:db8:80::1 ─── P2 host-p2a12 2001:db8:80::2
                                     回程静态路由走此链路
```

这是 VPP/LCP 拓扑。P2 是路由器及 Linux Kea 测试服务器，后者是明确的互通对端，不是另一套 VortexROS 池配置。客户端使用真实 DHCPv6 请求。测试网关的既有策略必须允许这些地址的 DHCPv6、ICMPv6 和回程报文。

接口形式中继需要服务器实际加入并监听 `ff05::1:3`。本次配套 Kea 3.0.3 包包含上游 [b503d225](https://github.com/isc-projects/kea/commit/b503d22521864f19d72a851c58e08a1e1eba2030) 的完整修复，包括组成员和服务器监听 Socket 两部分。只加入组而未创建监听 Socket 不能接收请求。明确服务器地址的中继则不依赖该组播监听条件。

## P1 配置

```text
system-view
interface host-p1q13
 ipv6 address 2001:db8:11::1 64
 dhcpv6 relay interface host-p1e12
 quit
interface host-p1e12
 ipv6 address 2001:db8:12::1 64
 quit
interface host-p1a12
 ipv6 address 2001:db8:80::1 64
 quit
commit
display dhcpv6 relay
display dhcp service verbose
```

上行接口必须已存在且具备可用 IPv6 链路本地地址。中继无需启用全局 DHCP 服务端开关；它不为客户端自动安装默认网关，终端需要 RA 或明确路由。

## P2 与服务器

VortexROS 路由配置：

```text
system-view
interface host-p2e12
 ipv6 address 2001:db8:12::2 64
 quit
interface host-p2a12
 ipv6 address 2001:db8:80::2 64
 quit
ipv6 route-static 2001:db8:11:: 64 host-p2a12 2001:db8:80::1
commit
```

Linux Kea 对端使用以下配置，保存为 `/etc/kea/relay-lab6.json`。接口和地址必须与本机实际环境一致：

```json
{
  "Dhcp6": {
    "interfaces-config": {"interfaces": ["host-p2e12/2001:db8:12::2"]},
    "lease-database": {"type": "memfile", "persist": false},
    "valid-lifetime": 3600,
    "preferred-lifetime": 1800,
    "subnet6": [{
      "id": 1406,
      "subnet": "2001:db8:11::/64",
      "pools": [{"pool": "2001:db8:11::100 - 2001:db8:11::110"}],
      "option-data": [{"name": "dns-servers", "data": "2001:db8::53"}]
    }]
  }
}
```

在该网络命名空间启动服务器：

```sh
kea-dhcp6 -t /etc/kea/relay-lab6.json
kea-dhcp6 -c /etc/kea/relay-lab6.json
```

若在同一实验主机使用命名空间，在命令前添加实际的 `ip netns exec`。不要在已有托管 DHCPv6 服务的同一接口再启动第二个服务器；这里的独立进程仅是互通测试对端。

## 实际结果

本次客户端 MAC 为 `0200-0014-0401`，获得 `2001:db8:11::101`，有效期 3600 秒。抓包观察到：

```text
Relay-forward: P1 upstream -> ff05::1:3, Request
Relay-reply: P2 -> P1 upstream, Reply
Client address: 2001:db8:11::101
```

服务器存在 `ff05::1:3:547` 监听；没有嵌套自循环的 Relay-forward。为流量测试将客户端取得的地址应用到实验终端后，稳定拓扑的一次端到端探测为 1 sent、1 received。五个采集点记录了请求走 e12、回包走 a12 并送达客户端的完整路径。这证明该次租约及往返路径，不是吞吐或全部中继组合的保证。

早期拓扑重建期间的流量失败没有被算作通过；当前记录中的 DHCP 成功、组播监听与实际转发是分别取得的证据。

## 撤销与保存

在 P1：

```text
interface host-p1q13
 undo dhcpv6 relay interface host-p1e12
 quit
commit
display dhcpv6 relay
```

实际撤销后中继单元停止，新的客户端请求未取得租约。已取得地址的旧客户端可能继续使用剩余租期，因此仅看旧客户端保留地址不能判断撤销失败。测试结束后停止独立 Kea 服务器，删除不再使用的实验地址、路由；需要持久保留或撤销配置时执行 `save`。
