# TCP MSS

降低 TCP SYN 的 MSS，适应有效 MTU 较小的链路。

[命令参考](reference/mss.md)

## 配置与验证

TCP MSS Clamp只处理包含MSS选项的TCP SYN报文。报文中的MSS大于出接口MTU允许的上限时才会被改小；原值已经足够小或报文不是SYN时不会修改。

自动模式随接口MTU变化重新计算上限：

```text
interface Tunnel 1
 tcp mss clamp
```

也可以指定固定MSS：

```text
interface Tunnel 1
 tcp mss 1360
```

接口MTU变化后，自动模式无需重新配置。使用 `display this` 和接口统计检查配置及报文变化。删除：

```text
interface Tunnel 1
 undo tcp mss
commit
```
