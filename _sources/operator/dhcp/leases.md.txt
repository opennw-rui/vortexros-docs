# 租约查询

## DHCP服务器租约查看

`display ip pool`同时列出全局IPv4地址池、接口地址池和仍在使用的Kea租约。接口定位既支持完整名称，也支持VRP风格的类型与编号分词；以下三条都能直接显示摘要和活动租约：

```text
display ip pool
display ip pool name OFFICE
display ip pool interface vlanif 20
```

默认视图和`used`都只显示仍有效的已分配地址；`all`显示Kea仍保留的全部租约状态，包括已过期或被拒绝的记录。`used`可以放在接口选择器之前或之后，例如`display ip pool used interface vlanif 20 verbose`。不存在`display ip pool use`命令。表格包含地址池或接口、客户端IP、MAC、Client-ID、剩余租期、状态、主机名和VPN实例。租约来自Kea控制Socket的权威运行态，不读取可能正在写入的CSV文件；读取失败会明确报错，不会把观察失败显示为零租约。

`verbose`把租约表切换成逐项详情，因此不必同时指定`used`。每条IPv4租约显示IP、MAC、网关、DNS、地址范围、域名、Client-ID、主机名、VPN实例、Kea服务实例、Subnet ID、状态、最近一次客户端事务时间、到期时间、有效租期和剩余租期。`used verbose`语义相同；`all verbose`还会展开已过期、declined及Kea保留的其他状态。没有由客户端提供的字段明确显示为`-`，不会根据MAC猜测厂商、操作系统或设备型号。

0.29-dev包含 DHCPv6 IA_NA/IA_TA/IA_PD 类型解码以及 Kea 正常空租约结果的修复。正常空库应显示零租约；同地址族的空实例不会阻断其他实例的租约或池名筛选。传输和服务错误仍报错。历史输出见[实测案例](../../examples/dhcpv6.md#空池查询)。

DHCPv6服务器使用相同的运行态语义：

```text
display dhcpv6 pool name V6-POOL used
display ipv6 pool name V6-POOL all
display ipv6 pool name V6-POOL verbose
```

IPv6输出区分IA_NA、IA_TA和IA_PD，并显示DUID、IAID、地址或委派前缀、Subnet ID、客户端事务时间、到期时间、剩余租期和状态。租约属于运行数据，不进入Candidate、CFG或SQLite配置投影。

Classless Static Route Option存在并启用解析时，按标准优先使用该选项，不再同时采用Router Option。无论默认路由来自哪个DHCP选项，`undo dhcp client default-route enable`都会阻止其中的`/0`，普通明细路由仍可安装。


[DHCP 功能与开关](../dhcp.md) · [逐条命令参数](../reference/dhcp.md)
