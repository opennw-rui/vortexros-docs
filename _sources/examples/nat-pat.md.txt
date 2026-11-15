# 接口 PAT

## 拓扑与作用

使用 [NAT 基础拓扑](nat/topology.md)，三台均为 VortexROS。P1 把内侧 P3 的源地址转换成出口 Ethernet0 的 198.19.80.1，并为有状态流量分配转换标识。出口地址变化时无需改地址池。

## P1 配置

~~~text
system-view
nat-policy name CLI-PAT
 statistic enable
 rule 10
  source address 198.18.11.2/32
  action snat pat interface
 quit
quit
interface Ethernet0
 nat-policy CLI-PAT outbound
quit
commit
~~~

## 验证

P3 执行 ping -a 198.18.11.2 -c 3 198.19.80.2，然后在 P1 查询：

~~~text
display nat-policy name CLI-PAT
display nat-policy sessions action snat-pat
display nat-policy statistics name CLI-PAT
~~~

回包应可达；会话应显示源地址 198.18.11.2 转换为 198.19.80.1。ICMP 标识符与 TCP/UDP 端口不是同一字段，此检查不代替端口集合匹配或会话上限验证。地址集合、端口集合和容量参数见[对象](../operator/nat/objects.md)与[容量](../operator/nat/capacity.md)。

## 撤销

~~~text
system-view
interface Ethernet0
 undo nat-policy CLI-PAT outbound
quit
undo nat-policy name CLI-PAT
commit
display nat-policy interfaces
~~~

未配置其他转换时，P3 到 P2 将按原始源地址普通路由转发。核对不再应用该策略，再按基础拓扑说明清理专用地址和路由；创建和撤销结果均可用 save 持久化。
