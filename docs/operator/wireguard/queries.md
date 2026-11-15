# 握手与转发

## 验证

```text
display wireguard interface Tunnel 10
display interface Tunnel 10
display ip routing-table
ping -vpn-instance BLUE 10.255.0.2
```

除接口状态外，还应从对端确认握手、收发计数和业务路由。只有Tunnel地址可达而业务前缀没有路由时，WireGuard不会自动补充路由。

[功能目录](../wireguard.md) · [命令参数](../reference/wireguard.md)
