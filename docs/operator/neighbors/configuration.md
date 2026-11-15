# 静态项与老化

## 配置与验证

IPv4 ARP和IPv6 ND邻居老化是VPP进程级参数，不依赖VLAN或bridge-domain。纯三层接口同样使用这些参数。默认值均为1200秒，并在VPP每次启动或重新连接后优先恢复，再下发接口、地址和业务配置。

```text
arp timeout 900
ipv6 nd stale-timeout 1800
ipv6 nd max-number 65536
ipv6 nd recycle enable
commit
```

恢复默认值：

```text
undo arp timeout
undo ipv6 nd stale-timeout
undo ipv6 nd max-number
undo ipv6 nd recycle
commit
```

`max-number`限制VPP IPv6邻居表容量；`recycle enable`在容量已满时回收最老的动态条目，静态邻居不参与动态回收。回收策略必须显式配置，`undo`恢复VPP启动时的默认策略。容量同步到 Linux ND 回收阈值。老化时间和回收开关作用于 VPP 邻居表。默认值不显示在配置中，非默认值通过 `display current-configuration` 和 `display ipv6 nd` 回读验证。

静态 IPv6 邻居绑定在三层数据面接口上。MAC 支持三段式和冒号分隔形式，保存时统一为冒号分隔形式。

```text
ipv6 neighbor 2001:db8:10::2 0211-2233-4455 interface Vlanif10
commit
display ipv6 neighbors static
undo ipv6 neighbor 2001:db8:10::2 02:11:22:33:44:55 interface Vlanif10
commit
```

多播、未指定IPv6地址，多播或全零MAC，以及二层或控制型接口都会在提交前被拒绝。提交后的静态项由Linux后端写入对应LCP接口，再由LCP同步至VPP；接口重建时按同一路径恢复，不再由VPP后端重复写入。动态邻居只属于运行态，不会写入配置。

静态ARP只接受可用IPv4单播地址和六字节单播MAC；全零、组播或广播映射会在提交前拒绝。


[功能目录](../neighbors.md) · [命令参数](../reference/neighbors.md)
