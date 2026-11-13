# DHCPv6 有地址但查不到租约

Debug 5 配套 Kea 3.0.3 的服务端租约查询可能报错。先区分客户端拿不到地址和服务端显示失败。

~~~text
display dhcpv6 client interface host-p2b12
display ipv6 pool name LAB-V6 used
~~~

在客户端执行第一条，用现场接口名替换 `host-p2b12`。若显示已分配的 IPv6 地址，用该客户端 Ping 网关。第二条在服务端执行，用现场地址池名替换 `LAB-V6`。

- 客户端没有地址时，检查对应三层接口的链路、DHCPv6 服务绑定、地址池及服务状态。
- 客户端有地址、网关可达，而查询出现以下错误时，Debug 5 读取了 Kea 的租约回复，但无法解码字符串形式的 `IA_NA`。

~~~text
json: cannot unmarshal string into Go struct field keaLeaseArguments.leases.0.type of type uint8
~~~

此时保留服务和地址池配置，以客户端状态及连通性确认业务。升级至明确修复此问题的发布版后，重新执行服务端租约查询并和客户端地址对照。案例中的实际输出见[DHCPv6 地址分配](../examples/dhcpv6.md)。
