# 代理 ARP

在指定三层接口上为一个或一段 IPv4 地址回答 ARP。

[命令参考](reference/neighbors.md)

## 配置与撤销

静态ARP和单IP/范围代理ARP必须绑定一个真实、具备MAC且能发送ARP的L3接口；LoopBack和NVE不出现在补全中。

```text
arp proxy 10.10.10.12 10.10.10.14 interface Vlanif 100
display arp proxy
undo arp proxy 10.10.10.12 10.10.10.14 interface Vlanif 100
```

提交后，指定地址范围的ARP请求从所选三层接口代理响应。接口down/up或重新创建后，设备会自动恢复已经提交的代理配置。
