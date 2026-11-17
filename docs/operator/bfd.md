# BFD

用独立会话或协议绑定检测路径故障。


BFD可建立独立会话，也可由OSPF、IS-IS、RIP和BGP邻居调用。静态和协议会话均默认发送间隔 1000 ms、接收间隔 1000 ms、检测次数 3。默认参数省略于保存配置。BGP 邻居覆盖对等体组的参数时，配置仍会显示有实际影响的覆盖项。


~~~{toctree}
:maxdepth: 2

bfd/static
bfd/protocols
~~~

[完整双端案例](../examples/bfd.md) · [命令参数](reference/bfd.md)

## 默认计时器核对

协议动态会话与未覆盖计时器的静态会话默认接收、发送间隔均为1000ms，检测倍数3。一次OSPF联动验证的实际显示为：

```text
display bfd statistics
Peer             State       Detect(ms)  Rx(ms)  Tx(ms)  Multiplier
198.19.80.2      Up          3000        1000    1000    3
```

`display bfd configuration` 的Configured列中0表示未单独覆盖，由Effective列给出继承后的配置值；并非按0毫秒运行。动态会话不需手工创建静态会话名。先在系统视图启用BFD，再在接口或协议下绑定，否则配置会被拒绝。默认项不写入当前配置；已配置参数与协商运行状态应分别核对。
