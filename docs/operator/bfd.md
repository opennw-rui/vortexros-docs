# BFD

用独立会话或协议绑定检测路径故障。


BFD可建立独立会话，也可由OSPF、IS-IS、RIP和BGP邻居调用。静态和协议会话均默认发送间隔 1000 ms、接收间隔 1000 ms、检测次数 3。默认参数省略于保存配置。BGP 邻居覆盖对等体组的参数时，配置仍会显示有实际影响的覆盖项。


~~~{toctree}
:maxdepth: 2

bfd/static
bfd/protocols
~~~

[完整双端案例](../examples/bfd.md) · [命令参数](reference/bfd.md)
