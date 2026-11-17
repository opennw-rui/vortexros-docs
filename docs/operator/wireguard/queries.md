# 握手与转发

接口绑定、配置端点和实际转发要分别检查。`display wireguard` 的 profile/peer 输出显示已提交参数，当前不提供握手时间；不要把存在配置条目当成已经握手。结合接口实际收发计数与双向业务探测判断是否生效。

## 验证

```text
display wireguard interface Tunnel 10
display interface Tunnel 10
display ip routing-table
ping -vpn-instance BLUE 10.255.0.2
```

除接口状态外，还应从对端确认握手、收发计数和业务路由。只有Tunnel地址可达而业务前缀没有路由时，WireGuard不会自动补充路由。

[功能目录](../wireguard.md) · [命令参数](../reference/wireguard.md)
