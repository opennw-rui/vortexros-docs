# 地址池 PAT

把多个连接转换到地址池地址及分配的端口，不依赖出口接口地址。公网池地址必须能从外部路由回到 P1。

## 前提与参数

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。池内地址由地址池对象定义，PAT 范围缺省 10000–65535；耗尽时新连接失败，不会自动使用范围外的端口。删除地址池前必须解除策略引用。

## 配置

P1 从用户视图开始；接口与基础路由由前置拓扑提供：

~~~text
system-view
~~~

配置清单：

~~~text
nat-policy address-pool name LAB-PUBLIC
 address 198.51.100.10/32
 pat-port-range 20000-20063
#
nat-policy name LAB-SNAT
 statistic enable
 rule 10
  source address 203.0.113.2/32
  action snat pat address-pool LAB-PUBLIC
#
interface Ethernet0
 nat-policy LAB-SNAT outbound
#
~~~

CLI 操作：

~~~text
commit
~~~

## 验证

P3 执行 `ping -a 203.0.113.2 -c 3 198.51.100.2`，然后在 P1 查询：

~~~text
display nat-policy name LAB-SNAT
display nat-policy statistics name LAB-SNAT
display nat-policy sessions action snat-pat
~~~

应能往返，且源地址变为 198.51.100.10，目的地址仍为 198.51.100.2。在会话中核对原始和转换后的地址；ICMP 使用标识符而非 TCP/UDP 端口。

Ping 成功只证明往返路径，应同时核对转换结果。查看状态要紧接探测执行，避免会话已老化。地址池耗尽和端口范围需要对应并发业务验证，不能从三次 Ping 推断。

## 撤销与保存

P1 系统视图：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet0
 undo nat-policy LAB-SNAT outbound
#
undo nat-policy name LAB-SNAT
undo nat-policy address-pool name LAB-PUBLIC
~~~

CLI 操作：

~~~text
commit
display nat-policy runtime
display nat-policy interfaces
~~~

解除绑定后再发起新连接，确认不再采用该策略。基础拓扑的普通路由仍在，撤销 NAT 不一定使业务断开，应比较转换结果而非只看 ping。需要重启保留配置时，在提交并验证后执行 `save`；撤销后也再次保存。

[功能说明](../../operator/nat/pool-pat.md) · [命令参数](../../operator/reference/nat.md)
