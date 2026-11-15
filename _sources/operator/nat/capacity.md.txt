# 容量与计时

## 缺省值

以下值来自 0.29-dev 配置模型和配套插件的真实 `display nat-policy configuration` 回读；默认项在配置中省略。这些是资源/老化参数，不是满表性能承诺。

| 参数 | 缺省 |
|---|---:|
| UDP timeout | 300 秒 |
| TCP established | 7440 秒 |
| TCP transitory | 240 秒 |
| ICMP timeout | 60 秒 |
| Other timeout | 120 秒 |
| TCP close | 5 秒 |
| Sessions per worker | 100000 |
| Interface PAT range | 10000–65535 |
| LRU refresh | 250 毫秒 |
| Expire check | 50 毫秒 |

会话配额在策略视图配置，缺省 unlimited；它与每 worker 的总容量不同。地址池有自己的 `pat-port-range`，不能通过修改接口 PAT 范围替代。

## 调整与影响

~~~text
system-view
nat-policy timeout udp 45
nat-policy timeout tcp-established 900
nat-policy timeout tcp-transitory 45
nat-policy timeout icmp 15
nat-policy timeout other 60
nat-policy timeout tcp-close 3
nat-policy sessions-per-worker 1024
nat-policy interface-pat-range 22000-22063
nat-policy x86-tune lru-refresh-ms 100
nat-policy x86-tune expire-check-ms 25
commit
display nat-policy configuration
display nat-policy workers
~~~

上述值在隔离真实 CLI 中已逐项回读。增大超时会延长空闲状态占用，缩小 PAT 范围或容量会使新建连接更早失败；维护间隔影响状态维护频率，不是业务限速。

有活动会话时，修改分配参数曾实际收到 `Instance in use`，Running 已接受意图而后端未完成。应先查询健康与会话，安排维护后清理所需会话，再确认实际值和健康恢复；不要把 commit 返回和实际生效混为一谈。

## 恢复默认

~~~text
system-view
undo nat-policy timeout udp
undo nat-policy timeout tcp-established
undo nat-policy timeout tcp-transitory
undo nat-policy timeout icmp
undo nat-policy timeout other
undo nat-policy timeout tcp-close
undo nat-policy sessions-per-worker
undo nat-policy interface-pat-range
undo nat-policy x86-tune lru-refresh-ms
undo nat-policy x86-tune expire-check-ms
commit
display nat-policy configuration
~~~

真实撤销回读节选：

~~~text
Hairpin NAT              disabled
UDP timeout              300s
TCP established timeout  7440s
TCP transitory timeout   240s
ICMP timeout             60s
Other timeout            120s
TCP close timeout        5s
Sessions per worker      100000
Interface PAT range      10000-65535
LRU refresh              250ms
Expire check             50ms
~~~

确认实际值后再 `save`。规则、会话配额和绑定不会随着全局超时撤销而自动删除。

[会话故障分类](sessions.md) · [命令参数](../reference/nat.md)
