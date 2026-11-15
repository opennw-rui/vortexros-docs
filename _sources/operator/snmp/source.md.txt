# 监听与通知来源

不固定监听接口时无需配置source-interface；下面两种显式写法语义相同，都会用
一个listener接收public和全部VPN实例的请求，而不是为每个IP地址启动一个进程：

```text
snmp-agent protocol source-interface all-interface
snmp-agent protocol source-status all-interface
```

若只允许从某一VPN实例中的接口接收查询，VPN和source-interface在同一条命令中
指定；该接口和trap source必须属于同一VPN。master和listener使用该接口主IPv4
建立VRF内的内部通道，不要求VPN中另行配置loopback路由：

```text
snmp-agent protocol source-interface vpn-instance INT Tunnel1
commit
# 恢复public及全部VPN实例的全接口监听
undo snmp-agent protocol source-interface
commit
```


trap发往NMS UDP162，设备自己不监听162。配置trap source后使用该接口主IPv4为源；标准linkUp/linkDown的实际记录见[计数与通知](notifications.md)。

[参数](../reference/snmp.md) · [实际案例](../../examples/snmp.md)
