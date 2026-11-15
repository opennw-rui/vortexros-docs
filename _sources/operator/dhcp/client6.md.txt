# IPv6 客户端与 PD

地址请求和前缀委派是不同用途。IA_NA 为本接口取得地址，IA_PD 为下游取得可分配前缀；二者可同时存在，但不是互相替代。

有状态地址、前缀委派以及立即续租的示例：

```text
interface Ethernet 1
 ipv6 address auto dhcp
 dhcpv6 client pd CPE-PREFIX
commit
display dhcpv6 client interface Ethernet 1
display dhcpv6 client prefix name CPE-PREFIX
# 在接口视图立即请求续租：
interface Ethernet 1
 dhcpv6 client renew
```

`display dhcpv6 client`分别显示IA_NA地址和IA_PD委派前缀，不会用其中一个字段遮盖另一个字段。`dhcpv6 client renew`是立即执行的运行命令，不进入Candidate或保存配置。

IPv6 默认网关来自 [RA 与 SLAAC](../ipv6-autoconfig.md)。


## 实际效果与撤销

[完整双端案例](../../examples/dhcpv6.md)有真实地址/委派前缀和续租结果。只需要 DNS 等信息时选择[Information-Request](information.md)，不应期待它分配地址。

在接口下 `undo ipv6 address auto dhcp` 撤销地址客户端；委派客户端用 `undo dhcpv6 client pd` 撤销，不需要追加前缀名。两者的配置及清理分别核对；接口手工静态地址不应被当作租约一起删除。提交并确认运行单元、租约地址和路由清理后保存。

[DHCPv6 总览](ipv6.md) · [RA 与 SLAAC](../ipv6-autoconfig.md)
