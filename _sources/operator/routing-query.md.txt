# 路由查询

查询规模较大时，先按 VPN、协议或前缀缩小范围。

## 协议查询

BGP、OSPF、OSPFv3、IS-IS、RIP、RIPng、LDP和MPLS控制面查询都直接读取对应
FRR daemon的VTY流，并在一次解析过程中生成VRP风格输出。路由表不会先完整读入内存，
也不会为排版再次请求后端。`display mpls forwarding-table`例外：它直接读取VPP实际
LFIB，用于确认数据面而不是重复显示FRR控制面。

常用大表入口如下：

```text
display bgp routing-table
display ospf 1 routing
display ospfv3 1 routing
display isis 1 route
display rip 1 route
display ripng 1 route
display mpls ldp binding
display mpls lsp
```

开发服务器使用十万条记录、输出到`io.Discard`的格式化基准结果如下。该测试只衡量
解析和排版，不包含FRR生成数据、终端传输或分页时间：

| 协议 | 十万条排版时间 |
|---|---:|
| BGP | 721.7 ms |
| OSPF | 669.6 ms |
| OSPFv3 | 382.3 ms |
| IS-IS | 220.6 ms |
| RIP | 215.7 ms |
| RIPng | 171.7 ms |
| LDP binding | 619.0 ms |
| MPLS LSP | 876.9 ms |

这些数字用于防止实现退回到“全量反序列化后再排版”的路径，不是设备转发性能承诺。


## 变更后检查

每次变更后至少执行：

```text
display this
commit
display current-configuration
display ip routing-table
display alarm active
```

随后使用本节对应的邻居、路由、BFD或VRRP命令检查运行状态。确认业务正常后再执行 `save`。删除配置时先解除引用或接口绑定，再删除协议进程和策略对象。
