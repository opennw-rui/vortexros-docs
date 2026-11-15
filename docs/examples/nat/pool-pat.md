# 地址池 PAT

把多个连接转换到地址池地址及分配的端口，不依赖出口接口地址。公网池地址必须能从外部路由回到 P1。

## 前提与参数

先完成[基础拓扑](topology.md)。本例与其他 NAT 案例单独运行。池内地址由地址池对象定义，PAT 范围缺省 10000–65535；耗尽时新连接失败，不会自动使用范围外的端口。删除地址池前必须解除策略引用。

## 配置

P1 从用户视图开始；接口与基础路由由前置拓扑提供：

~~~text
system-view
nat-policy address-pool name LAB-PUBLIC
 address 198.19.81.1/32
 pat-port-range 20000-20063
quit
nat-policy name LAB-SNAT
 statistic enable
 rule 10
  source address 198.18.11.2/32
  action snat pat address-pool LAB-PUBLIC
 quit
quit
interface host-p1a12
 nat-policy LAB-SNAT outbound
quit
commit
~~~

## 验证与真实结果

在 P3 访问 http://198.19.80.2:8080/。随后在 P1 查询：

~~~text
display nat-policy sessions action snat-pat source-ip 198.18.11.2 destination-ip 198.19.80.2 destination-port 8080
~~~

已有隔离实验真实输出节选：

~~~text
host-p1a12/outbound  FIB:0 -> FIB:0  Policy:LAB-SNAT(4124874345)/10  Action:SNAT-PAT
198.18.11.2:44510 -> 198.19.80.2:8080  =>  198.19.81.1:20058 -> 198.19.80.2:8080
~~~

P3 到 P2 的 HTTP 返回 200；P2 日志看到 198.19.81.1。转换端口 20058 在配置的 20000–20063 内。端口不是固定分配值。 该记录证明本例路径，不是地址池耗尽、满表容量或吞吐测试。运行 ID、端口和时间会随连接变化。

## 撤销与保存

P1 系统视图：

~~~text
system-view
interface host-p1a12
 undo nat-policy LAB-SNAT outbound
quit
undo nat-policy name LAB-SNAT
undo nat-policy address-pool name LAB-PUBLIC
commit
display nat-policy runtime
display nat-policy interfaces
~~~

解除绑定后再发起新连接，确认不再采用该策略。基础拓扑的普通路由仍在，撤销 NAT 不一定使业务断开，应比较转换结果而非只看 ping。需要重启保留配置时，在提交并验证后执行 `save`；撤销后也再次保存。

[功能说明](../../operator/nat/pool-pat.md) · [命令参数](../../operator/reference/nat.md)
