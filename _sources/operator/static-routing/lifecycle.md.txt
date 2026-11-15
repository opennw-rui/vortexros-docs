# 收敛与精确撤销

同一次提交可以新增递归解析路由及其依赖路由。确认Installed、FIB实际路径与流量后再保存，不以route-zapi发送成功代替Zebra确认或实际转发。

下一跳暂时不可达时，配置意图与安装状态不同；恢复后应重建实际路径。相同前缀ECMP撤销一条路径时，仍可用的其他路径不应被整组删除。

~~~text
display ip routing-table 203.0.113.0 24 verbose
display ip fib
display ipv6 routing-table
display ipv6 fib
~~~

黑洞路由必须以同一前缀和NULL 0精确撤销；普通静态路由保留原VPN、前缀、下一跳与接口等定位参数加undo。跨表lookup-only路由的Lookup-Table显示实际查表号，普通路径显示-，默认VPP表0与Linux main254各有含义。

[完整配置、真实查询和撤销](../../examples/static-route.md) · [全部参数](../reference/static-routing.md)
