# 进程重置


开发服务器 Linux 数据面只配置 OSPF1，router-id 198.51.100.9、area0 和 198.51.100.0/24 接口。真实终端执行 reset ospf 1 process 并确认后返回：

~~~text
Info: ospf process 1 reset; runtime state matches the running configuration.
~~~

随后 display ospf 1 brief 显示 Router ID 198.51.100.9，接口到虚拟对端的探测 2/2；删除进程与临时地址后提交，恢复原配置。本项证明单进程重置入口及运行回读，不把单路由器结果写成额外双邻居故障切换验证。

[OSPF 总览](../ospf.md) · [完整案例](../../examples/ospf.md) · [命令参数](../reference/ospf.md)
