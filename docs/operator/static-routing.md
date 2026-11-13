# 静态路由

为指定前缀配置固定路径、黑洞路径或跨表查询。

[命令参考](reference/static-routing.md) · [配置案例](../examples/static-route.md)

## 配置

```text
ip route-static 203.0.113.0 255.255.255.0 192.0.2.1 preference 60 tag 100 description TO-WAN
ip route-static 198.51.100.0 255.255.255.0 NULL 0 preference 80 tag 900 description DISCARD
ip route-static vpn-instance BLUE 10.0.0.0 8 vpn-instance default 192.0.2.1 Tunnel 1
ip route-static vpn-instance BLUE 198.51.100.0 24 vpn-instance default
ipv6 route-static 2001:db8:100:: 64 2001:db8::1
ipv6 route-static vpn-instance BLUE 2001:db8:200:: 64 vpn-instance default
ipv6 route-static 2001:db8:dead:: 48 NULL 0 preference 80 tag 900 description DISCARD-V6
```

`NULL 0`明确创建黑洞路由，可同时携带`preference`、`tag`和`description`，但不能再指定下一跳、出接口或下一跳VPN。撤销时使用同一目的前缀和`NULL 0`，只删除该黑洞路径，不影响同前缀的普通静态路径。运行路由表中的接口名称仍显示为`NULL0`。

多条静态路由在配置中连续显示，不用无意义的`#`逐条分隔。跨VPN下一跳要同时显示目标VPN和下一跳VPN。

不指定下一跳和出接口、只指定不同下一跳VPN实例的形式表示“在目标VPP FIB中继续查表”。VPP仍是
这类路由唯一的数据面所有者，路由不会写入Linux路由表。控制层同时通过route-zapi向Zebra发布一条
不写内核的控制面影子，使BGP `network`、`redistribute static`、路由策略和递归下一跳能够观察该路由；
带下一跳、出接口或`NULL 0`的普通静态路由由统一静态路由后端发布，不再触发协议配置全树提交；
CLI、保存配置及显示语义保持不变。相同目的VPN和前缀不能同时配置继续查表路径与
普通路径，也不能配置多个查表目标。运行显示以精确VPP读回作为安装状态，不重复显示控制面影子，因此
少量此类路由不会触发对大型FIB的全表扫描。

[查询 RIB 与 FIB](routing-tables.md)。

## 验收场景

| 场景 | 配置 | 数据面效果 | 验证 |
|---|---|---|---|
| 直连下一跳 | 普通静态路由 | 安装到目标VRF | ping和routing-table |
| 递归下一跳 | 先建递归可达路由 | 解析成功后安装 | verbose中的NextHop/Interface |
| ECMP | 同前缀不同下一跳 | 多路径进入RIB/FIB | route verbose和流量 |
| 跨VPN | 目标VPN+下一跳VPN | 在目标表安装、去指定表解析下一跳 | 两个VPN路由表 |
| 默认路由 | `/0` | 无更长匹配时使用 | 特定目的ping/tracert |
| 精确undo | 完整路径参数 | 只删除一个所有者/路径 | 其他所有者仍保留 |
