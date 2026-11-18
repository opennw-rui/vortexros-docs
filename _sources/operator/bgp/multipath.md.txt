# 等价路径

BGP 默认要求参与等价转发的 AS_PATH 一致。BGP 视图中的 `load-balancing as-path-ignore` 放宽为允许长度相同、内容不同的 AS_PATH；它不忽略 AS_PATH 长度，也不跳过本地优先级、MED、下一跳可达性等其他选路条件。地址族中的 `maximum load-balancing` 另行控制最大路径数，单独启用放宽规则不会自动增加该数量。

## 配置

以下操作承接[双端 BGP 配置](../../examples/bgp.md)。接收端需已与两个路由源建立邻居，两条下一跳的 IGP 距离相同。示例中两条可达下一跳为198.19.80.1、198.19.80.2，IGP 距离均为20。

路由源 P1、P2 都用一个空闲的环回接口提供198.18.250.0/24。P1 为该网络指定 AS_PATH65111，P2 指定65112。以下为 P1 的增量配置；P2 将65111改为65112。若所选环回接口已有地址，应选择另一个空闲编号，避免替换已有业务地址。

```text
interface LoopBack 250
 ip address 198.18.250.1 255.255.255.0
#
route-policy MPATH permit node 10
 apply as-path 65111
#
bgp 65000
 ipv4-family unicast
  network 198.18.250.0 255.255.255.0 route-policy MPATH
#
commit
```

在接收端 P3 配置：

```text
bgp 65000
 load-balancing as-path-ignore
 ipv4-family unicast
  maximum load-balancing ibgp 2
#
commit
```

EBGP 对应使用 `maximum load-balancing ebgp N`。命令放在需要等价转发的地址族内；其他地址族的上限独立配置。

## 查询与影响

```text
display bgp routing-table 198.18.250.0 24
display ip routing-table 198.18.250.0 24
ping -c 2 198.18.250.1
```

实际路由查询包含以下两条路径，业务探测成功：

```text
Network            NextHop             MED     LocPrf Path/Ogn
198.18.250.0/24     198.19.80.1           0        100 65111 i
198.18.250.0/24     198.19.80.2           0        100 65112 i

Total Number of Routes: 2
2 packets transmitted, 2 received, 0% packet loss
```

两条已学习路径不一定都能参与等价转发；必须同时满足上限及其他选路条件。若两个 BGP 下一跳递归到同一个实际出接口、同一个下一跳，转发表会合并相同的实际出口，不能把两条 BGP 路径理解为两条独立物理链路或两倍带宽。

## 撤销

恢复相同 AS_PATH 约束：

```text
bgp 65000
 undo load-balancing as-path-ignore
 ipv4-family unicast
  undo maximum load-balancing ibgp
#
commit
```

实际撤销后，两条 BGP 路径仍然可见，但只保留一个最佳候选参与本例的转发选择。删除练习配置时，先撤销两端的网络声明，再删除未被引用的策略及本例新建的环回接口；保留原有接口上的其他地址。前缀在接收端消失后再保存，不要只删除策略而留下引用。
