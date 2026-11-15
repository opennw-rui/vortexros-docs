# Ping、tracert 与 mtr

## Ping、tracert与mtr

```text
ping 192.0.2.1
ping -vpn-instance BLUE 10.0.0.1
tracert 198.51.100.1
mtr -vpn-instance BLUE 10.0.0.1
```

普通和带VPN的命令都会边执行边显示结果。Ctrl+C只中止当前诊断命令，并尽量显示已经产生的统计信息，不会关闭SSH会话。错误消息保留诊断含义，但不会暴露系统中的程序路径。

`mtr`在CLI中保持交互式刷新和按键控制，但用户不能借此进入Linux shell。


[目录](../09-operations.md)
