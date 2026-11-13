# IS-IS 邻接

**目标**：在两台直连路由器之间建立 Level-2 邻接。

**前提**：两端 Ethernet 1 为三层实验口，使用 192.0.2.1/30、192.0.2.2/30；链路与地址先验证可达。

## 配置

~~~text
system-view
isis 10
 network-entity 49.0001.0100.0000.0001.00
 is-level level-2
 cost-style wide
 quit
interface Ethernet 1
 isis enable 10
 isis circuit-type p2p
 isis circuit-level level-2
 quit
commit
~~~

对端使用相同的 Level 和链路类型，NET 改为 `49.0001.0100.0000.0002.00`，保证系统 ID 唯一。启用 IS-IS 会开始在这条链路上交换拓扑。参见 [IS-IS](../operator/isis.md)。

## 验证

用 `display isis 10 peer` 确认邻接 Up，用 `display isis 10 lsdb` 确认对端 LSP。只有对端发布了额外可达前缀时，才应在 `display isis 10 route` 中期待相应学习路由。

## 撤销

先在接口视图执行 `undo isis enable`，然后在系统视图执行 `undo isis 10` 并提交。该进程若在其他接口使用，不应删除整个进程。
