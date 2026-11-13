# 硬件卸载

按接口查看和配置网卡驱动支持的收发卸载。

[命令参考](reference/interfaces.md)

## 查看与配置

设备直接读取物理接口实际支持的硬件卸载能力。除LRO外，支持的能力默认开启；使用 `undo hardware offload ...` 可以按接口关闭一个或多个能力。

```text
display interface hardware offload Ethernet 1
```

在接口视图使用 `undo hardware offload tso` 关闭 TSO。设备视图的驱动设置见[数据面](dataplane.md)。
