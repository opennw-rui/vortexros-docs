# 三层子接口

用 802.1Q 或 QinQ 标签将物理链路划分成多个三层接口。

[命令参考](reference/interfaces.md)

## 配置与验证

```text
interface Ethernet 1.100
 encapsulation dot1q vid 100
 ip address 10.100.0.1 255.255.255.0
```

QinQ示例：

```text
interface Ethernet 1.200
 encapsulation qinq vid 200 ce-vid 20
 ip address 10.200.20.1 255.255.255.0
```

提交后，只有标签匹配的报文进入对应子接口。父接口down时子接口随之down；父接口恢复后自动恢复。使用以下命令验证：

```text
display interface Ethernet 1.100
display ip interface brief
display ip routing-table protocol direct
```
