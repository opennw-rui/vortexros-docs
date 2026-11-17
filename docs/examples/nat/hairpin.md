# Hairpin

## 用途与前提

内侧设备通过发布地址访问内侧服务，流量在 NAT 网关折返。先完成[基础拓扑](topology.md)及 [Twice NAT](twice.md)。Twice NAT 同时转换源地址，确保回包经过网关，不能只配置目的地址转换。

## 配置

P1 在系统视图启用全局及策略 hairpin，并给内侧绑定仅含默认放行行为的策略：

~~~text
nat-policy hairpin enable
nat-policy name D1-TWICE
 hairpin enable
#
nat-policy name D1-PASS
#
interface Ethernet1
 nat-policy D1-PASS inbound
#
~~~

CLI 操作：

~~~text
commit
~~~

外侧 D1-TWICE 保持发布，内侧 D1-PASS 不应有显式 No-NAT 规则覆盖目标。内侧报文未匹配显式规则时，全局和发布策略两个 hairpin 开关共同允许复用发布映射。直接把 Twice NAT 绑定到内侧属于显式转换，不能用来检查这两个自动折返开关。

## 验证

P3 执行 ping -a 203.0.113.2 -c 3 198.51.100.10，P1 执行：

~~~text
display nat-policy sessions action twice-nat
display nat-policy statistics name D1-TWICE
display nat-policy interfaces
~~~

核对目的从发布地址变为 203.0.113.2，源变为网关内侧地址，回包也经过 NAT。ICMP 仅验证折返地址转换；服务端口发布需按 DNAT 页另用相应业务检查。

## 撤销

先解除 Ethernet1 的 D1-PASS 入方向绑定，策略下执行 undo hairpin enable；不再有其他折返业务时执行全局 undo nat-policy hairpin enable。按 Twice NAT 页撤销其余对象并提交。需要保留的其他 NAT 业务不可随本例删除；最后按需 save。

## 实际检查结果

开启两个开关后，查询中可以看到自动折返标记及两次地址转换：

```text
Policy:D1-TWICE/10  Action:TWICE-NAT  Mode:hairpin
203.0.113.2 -> 198.51.100.10 => 203.0.113.1 -> 203.0.113.2
```

本例探测收到 3/3 回复。分别关闭全局或发布策略开关后，使用新标识符的探测均无回复；已有会话可能继续使用原映射，应使用新连接检查撤销效果。
