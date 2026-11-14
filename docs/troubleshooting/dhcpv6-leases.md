# DHCPv6 租约查询

先区分客户端未获地址和管理端租约显示失败。Debug 9 已继承 DHCPv6 类型解码及正常空租约汇总的修复。

~~~text
display dhcp service verbose
display dhcpv6 client interface Ethernet 1
display ipv6 pool name LAB-V6 used
display ipv6 pool name LAB-V6 verbose
~~~

客户端命令在客户端执行，池查询在服务端执行；替换为现场接口和池名。

- 客户端没有地址：检查链路、服务绑定、地址池和服务状态。
- 正常空租约数据库：查询成功并显示零租约。Kea 列表查询的结果码 3 表示正常空结果。
- 同地址族多实例：一个实例为空时，其他实例的租约及池名筛选仍应正常。
- socket、服务命令或回复格式错误：保留错误并检查服务日志，不能按零租约处理。

Debug 5 的 `IA_NA` 字符串解码错误已在 Debug 6 修复；正常空结果及多实例汇总在 Debug 7 修复。原始错误和流量结果保留在[历史实测案例](../examples/dhcpv6.md)，不代表 Debug 9 仍有该限制，也不表示本轮重新运行了 DHCPv6 拓扑。
