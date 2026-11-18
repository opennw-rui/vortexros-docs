# 进程与发布

## 配置


```text
ripng 2 vpn-instance BLUE
 network 2001:db8:100::/64
 import-route static
 default-route originate
```

RIPng视图中的`import-route ospf`表示导入OSPFv3路由，系统会映射到后端的IPv6协议名称。


[完整双端案例](../../examples/ripng.md) · [参数参考](../reference/ripng.md)

双栈 VPN 实例的完整两端配置、协议统计、路由、探测和撤销见[RIP VPN 案例](../../examples/rip.md#vpn-实例内的双栈发布)。RIPng 独立使用同样的实例绑定方式。

## 静默接口

RIPng 支持 `silent-interface Ethernet0` 和 `undo silent-interface Ethernet0`。`passive-interface default` 将全部接口置为静默，随后用 `undo silent-interface Ethernet0` 保留一个发送更新的接口；`undo passive-interface default` 清除全部静默项和活跃例外。此行为与 [RIP 的静默接口](../rip/configuration.md#全局静默与例外)相同。

```text
ripng 1
 passive-interface default
 undo silent-interface Ethernet0
#
commit
display ripng 1 interface
display ripng 1 route
```

停止更新后，对端已学习路由按原超时计时器老化。实际撤销静默后，接收端重新学到 Cost2 的主机路由，IPv6 探测2/2。恢复普通模式：

```text
ripng 1
 undo passive-interface default
#
commit
```
