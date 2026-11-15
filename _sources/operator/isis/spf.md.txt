# SPF 调度

在 IS-IS 进程视图用 `spf-delay-ietf init-delay 50 short-delay 200 long-delay 1000 holddown 5000 time-to-learn 500`
设置 SPF 退避参数，单位为毫秒。提交后查看 `display isis 10 spf-delay`，使用
`undo spf-delay-ietf` 并提交可关闭这组定时器。


[双端配置和真实路由](../../examples/isis.md) · [全部参数](../reference/isis.md)
