# IPv6 网关

## IPv6示例

```text
interface Vlanif 100
 ipv6 address 2001:db8:100::1 64
 vrrp6 vrid 20 virtual-ip 2001:db8:100::fe
 vrrp6 vrid 20 priority 120
 vrrp6 vrid 20 timer advertise 1
```

IPv6组使用 `vrrp6`，无需单独输入IPv4的版本命令。


[功能目录](../vrrp.md) · [命令参数](../reference/vrrp.md)
