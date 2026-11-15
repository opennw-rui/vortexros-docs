# IPv4 客户端

## DHCPv4客户端

```text
interface Ethernet 1
 ip address dhcp-alloc
commit
display dhcp client
```

客户端只接收和维护IPv4地址、默认路由、classless route及租约生命周期。撤销：

```text
interface Ethernet 1
 undo ip address dhcp-alloc
commit
```

VPP启用时，DHCP客户端运行在VPP为业务接口建立的LCP host接口上。报文仍通过对应VPP物理接口收发，客户端不会重新绑定、独占或接管物理网卡。这样IPv4与IPv6租约采用同一套生命周期、VRF、撤销和重启恢复逻辑，并且可以完整处理默认路由和classless route。租约中的DNS选项不写入Linux系统解析配置。

接口`shutdown`只暂停对应的DHCP client、relay和PD运行单元，配置意图仍保留。子接口还继承父接口的有效管理状态：父接口关闭时子接口单元同时暂停；父接口恢复后，只有自身未配置`shutdown`的子接口才按原配置恢复。该行为不删除租约配置，也不会把显式关闭的子接口强制拉起。

默认会安装 DHCP 学习到的默认路由，默认优先级为 60。该值用于与其他协议路由比较；数值越小越优先，不是路由的 Cost。可以调整优先级，或显式禁止默认路由：

```text
interface Ethernet 1
 dhcp client default-route preference 80
 # 如不需要上游默认路由：
 undo dhcp client default-route enable
```


## 路由与撤销验证

例如设置`default-route preference 80`后，可在路由摘要检查Pre是否为80；DHCP缺省路由的显示协议为Kernel。
加入同前缀的静态默认路由时，优先级 90 保留 DHCP 选路，优先级 60 改选静态路由；
撤销静态路由后恢复 DHCP。验证时应同时查看路由表、实际 FIB 和连通性，不能只看配置。

~~~text
display dhcp client interface Ethernet0
display ip routing-table 0.0.0.0
display ip fib | include 0.0.0.0/0
~~~

接口名请替换为实际客户端接口。撤销客户端后，原租约地址、客户端安装的路由和 FIB 投影均应清除；
保留接口本身和其他来源的静态地址。租约记录在资源清理失败时保留以便继续清理，错误会返回给提交方。
不应把进程已经停止当作地址和路由都已撤销。

~~~text
interface Ethernet0
 undo ip address dhcp-alloc
 quit
commit
display dhcp client interface Ethernet0
display interface Ethernet0
display ip fib
~~~

撤销后检查默认路由和FIB，确认不再保留该DHCP客户端产生的默认路径。


[DHCP 功能与开关](../dhcp.md) · [逐条命令参数](../reference/dhcp.md)
