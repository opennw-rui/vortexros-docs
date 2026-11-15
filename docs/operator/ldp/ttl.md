# TTL 模式

## TTL 模式

缺省使用 uniform 模式，IP TTL 会传播到 MPLS 标签栈：

```text
ttl propagate
```

如需隐藏 MPLS 核心跳数，可使用 pipe 模式：

```text
undo ttl propagate
```

Linux sysctl 是该模式的权威状态；LCP 将变化同步为 VPP 标签路径的 pipe 或
uniform 属性，不改变 FRR 的协议计算。


[功能目录](../ldp.md) · [命令参数](../reference/mpls.md)
