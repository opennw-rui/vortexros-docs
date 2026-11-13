# IS-IS

在同一 IS-IS 进程中运行 IPv4 和 IPv6。

[命令参考](reference/isis.md) · [配置案例](../examples/isis.md)

## 配置

进程号在设备内全局唯一。一个进程只能绑定一个VPN，一个VPN最多配置一个IS-IS进程；接口所属VPN必须与进程VPN一致。

```text
isis 10 vpn-instance BLUE
 network-entity 49.0001.0100.0000.0001.00
 is-level level-2
 cost-style wide
 log-adjacency-changes
interface Vlanif 100
 isis enable 10
 isis ipv6-enable 10
 isis circuit-type p2p
 isis circuit-level level-2
 isis cost 20
```

提交后，IPv4和IPv6在同一进程中运行。接口VPN不一致、同一接口引用另一个进程或同一VPN已存在其他进程时，命令会被拒绝。

`import-route`用于导入IPv4路由，`ipv6 import-route`用于导入IPv6路由：

```text
isis 10
 import-route static
 ipv6 import-route static
 ipv6 import-route ospfv3
```

系统根据进程的IS-IS level生成FRR要求的`level-1`或`level-2`重分发命令；默认level-1-2会同时下发两级，避免后端接受命令时因缺少level而拒绝配置。

```text
display isis 10 brief
display isis 10 peer
display isis 10 interface
display isis 10 lsdb
display isis 10 route
display isis 10 spf-delay
```

在 IS-IS 进程视图用 `spf-delay-ietf init-delay 50 short-delay 200 long-delay 1000 holddown 5000 time-to-learn 500`
设置 SPF 退避参数，单位为毫秒。提交后查看 `display isis 10 spf-delay`，使用
`undo spf-delay-ietf` 并提交可关闭这组定时器。

撤销示例：

```text
interface Vlanif 100
 undo isis ipv6-enable 10
 undo isis enable
undo isis 10
commit
```

如果需要把进程迁移到另一个VPN，应先删除进程，再使用新VPN重新创建。配套 FRR 的 IS-IS 路由缺省优先级为 115。
