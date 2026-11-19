# MQC

classifier 分类、behavior 动作和 policy 绑定组成一条处理链，未绑定的对象不处理流量。

## 分类、行为和绑定

MQC 将“匹配哪些报文”“对匹配报文做什么”“在哪个接口方向使用”分为 classifier、behavior 和 policy。三个对象组成一条完整配置链；只创建 classifier 不会对业务生效。

| 对象 | 作用 |
| --- | --- |
| Classifier | 按支持的地址、协议、标记等条件识别流量 |
| Behavior | 执行限速、重标记、重定向等已配置动作 |
| Policy | 将分类与行为关联 |
| 接口绑定 | 选择处理位置及 inbound / outbound 方向 |

适合按业务分类管理带宽或改变服务标记。DSCP 是 IP 头中的服务类别标记（RFC 2474），修改标记本身不保证后续网络给予优先服务。重定向会改变选路，应先检查目标下一跳与回程。

多项策略叠加时按[接口处理顺序](interface-processing.md)核对匹配时的地址、端口及标记。变更后检查命中、实际收发与对照流量；撤销先解除接口引用，再删除策略及共享对象。

~~~{toctree}
:maxdepth: 2

mqc/classification
mqc/actions
mqc/attachment
~~~

[完整案例与示例输出](../examples/mqc.md) · [全部命令参数](reference/mqc.md)
