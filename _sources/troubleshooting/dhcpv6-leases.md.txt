# DHCPv6 租约查询

先区分客户端未获地址和管理端租约显示失败。先检查客户端状态、池范围和租约，再根据实际错误排查服务。

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

支持 IA_NA、IA_TA、IA_PD、正常空结果和多实例汇总，见[完整案例](../examples/dhcpv6.md)。
