# IPv4 客户端

## DHCPv4客户端

```text
interface Ethernet 1
 ip address dhcp-alloc
```

CLI 操作：

```text
commit
display dhcp client
```

客户端只接收和维护IPv4地址、默认路由、classless route及租约生命周期。撤销：

```text
interface Ethernet 1
 undo ip address dhcp-alloc
```

CLI 操作：

```text
commit
```

接口使用 DHCP 时，业务报文仍通过该接口收发；不需要另外接管网卡或手工创建客户端进程。客户端可按配置安装默认路由和无类别静态路由。租约中的 DNS 选项不会修改设备的系统解析设置。

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
#
~~~

CLI 操作：

~~~text
commit
display dhcp client interface Ethernet0
display interface Ethernet0
display ip fib
~~~

撤销后检查默认路由和FIB，确认不再保留该DHCP客户端产生的默认路径。


[DHCP 功能与开关](../dhcp.md) · [逐条命令参数](../reference/dhcp.md)


## 无类别路由

```text
interface Ethernet0
 dhcp client classless-route enable
 dhcp client default-route enable
#
```

开启无类别路由接收后，客户端向服务器请求 DHCP Option 121，并按服务器回复安装路由。例如服务器通告 `203.0.113.0/24` 经 `198.19.229.1`，实际路由查询为：

```text
Destination/Mask   Proto    NextHop         Interface
203.0.113.0/24     Kernel   198.19.229.1     Ethernet0
```

客户端使用实际租约地址 `198.19.229.200` 探测该前缀内的服务器地址 `203.0.113.121`，实测 3 发 3 收。这里是客户端接收能力；服务器是否提供该选项取决于其配置，不能据此假定所有 DHCP 服务端都会通告无类别路由。

按 RFC 3442，收到 Option 121 时使用其中的路由，不再同时采用 Router Option 3。若 Option 121 没有默认路由，单独开启默认路由接收也不会把 Option 3 重新当成默认网关。服务器若需要提供默认路径，应在 Option 121 中同时提供 `0.0.0.0/0`。

`undo dhcp client classless-route enable` 撤销本接口已学习的无类别路由，重新按 Router Option 3 和默认路由开关处理；`undo dhcp client default-route enable` 只禁止默认路径，不删除正常租约地址。本次实际撤销验证中，前缀路由删除、Router Option 默认路由恢复；再关闭默认路由后，地址仍为 `198.19.229.200/24`，客户端安装的路由为空。

## 数据面重置后的恢复

重置数据面会中断该接口上的当前租约使用，客户端随后重新申请，地址可能改变。不要把重置前的动态地址作为永久管理地址或固定对端地址使用。

~~~text
display dhcp client
display ip interface brief
display ip routing-table
~~~

客户端服务运行但 Address 为 `-` 时，表示尚无已取得的地址；这与成功取得租约是不同状态。重置完成后，应核对新的地址、默认或无类别路由，并探测实际对端。不能只用服务运行状态判断已经恢复连通。

实测数据面重置后，IPv4 客户端重新取得地址和默认路由，对端探测3发3收。撤销 IPv4 客户端时，应同时移除其租约地址、临时地址及所安装路由；另行配置的 IPv6 自动配置意图仍保留，IPv6 地址是否已取得应独立查询。
