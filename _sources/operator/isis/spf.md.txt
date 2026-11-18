# SPF 调度

在 IS-IS 进程视图用 `spf-delay-ietf init-delay 50 short-delay 200 long-delay 1000 holddown 5000 time-to-learn 500`
设置 SPF 退避参数，单位为毫秒。提交后查看 `display isis 10 spf-delay`，使用
`undo spf-delay-ietf` 并提交可关闭这组定时器。


[双端配置和路由查询](../../examples/isis.md) · [全部参数](../reference/isis.md)


## 查询示例

以下参数对应一次实际配置：Init 50 ms、Short 200 ms、Long 1000 ms、Holddown 5000 ms、TimeToLearn 2000 ms。display isis 1 spf-delay 显示相应值和 QUIET 等调度状态；撤销后显示 Using legacy backoff algo。

SPF 定时器调节路由计算的退避节奏，不直接改变报文的转发时延。修改前应考虑拓扑变化频率和收敛要求，不能把较小参数等同于任何规模下都收敛更快。
