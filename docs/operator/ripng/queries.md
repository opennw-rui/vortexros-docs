# 查询与撤销

## 验证与撤销

```text
display ripng 2 interface
display ripng 2 route
```

执行 `undo ripng 2 vpn-instance BLUE` 并提交会删除该进程。

[完整双端案例](../../examples/ripng.md) · [参数参考](../reference/ripng.md)

## 核对实际选路

邻居统计按同一行显示 IPv6 邻居和计数：

```text
Gateway                                 BadPackets BadRoutes Distance Last Update
fe80::fe:54ff:fe56:cc86                          0         0      100 00:00:37
```

实际双设备验证的 `2001:db8:251::2/128` 路由由 RIPng 选中，Preference 为 100、Cost 为 2，下一跳为链路本地地址。使用 `display ipv6 routing-table 2001:db8:251::2 128` 核对协议、出接口和下载标志，再用 `ping ipv6 2001:db8:251::2` 检查连通性。一次连通性验证为 5/5，并在链路捕获到五组请求与回复。若实际有丢包，继续核对 IPv6 邻居、FIB 和链路状态，不能仅凭协议数据库宣布转发正常。

同一前缀若另由 IS-IS 学习，默认 Preference 15 的路由优先于 RIPng 的 100。此时 RIPng 数据库仍有记录，不能仅凭数据库判断 RIPng 已承担转发。

## 计时列

路由表的 TimeLeft 表示当前老化或垃圾回收计时器的剩余时间，格式为分:秒；本地条目显示 -。它不是路由已存在的时长。配置定时器后，用实际更新和路由变化核对，不能只依据当前配置判定旧条目的计时器已经重新开始。


## 等价路径与不可用候选

`maximum load-balancing 2` 允许同一前缀保留两条等价路径。IPv6 链路本地下一跳需要连同接口识别：两个独立链路上的地址即使相同，也是两个不同下一跳，不应合并为一条。

普通 IP 路由查询只列出可用路径。接口停止后，后端可能仍保留该接口的候选记录；使用 inactive 或 verbose 形式可以查看，不能把候选记录数当作可转发路径数。

~~~text
display ipv6 routing-table vpn-instance BLUE protocol ripng
display ipv6 routing-table vpn-instance BLUE protocol ripng inactive
display ipv6 routing-table vpn-instance BLUE protocol ripng verbose
display ipv6 fib vpn-instance BLUE
~~~

实测同一远端 /128 具有两个地址相同、接口不同的下一跳；停用聚合链路后仅保留独立链路转发，探测3发3收；恢复后回到两条可用路径。该条件不表示所有 IPv6 地址都可以在同一链路上重复使用，链路本地地址的作用域仍限定在各自链路。

实测两条链路都收到来自同一链路本地地址的通告后，路由表保留两个不同接口的下一跳。停止聚合接口时，协议表与内核仅使用另一接口，实际探测3发3收；恢复聚合后，两条路径重新可用，探测2发2收。查询 inactive 时仍可看到后端保留的不可用候选，它不计入普通活跃路径。
