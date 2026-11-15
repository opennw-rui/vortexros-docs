# 地址、MTU 与统计

## 基本配置

用户视图和系统视图的接口选择帮助均按类型、编号两步显示。
例如先使用 `display interface ?` 查看 `Ethernet` 类型，再用
`display interface Ethernet ?` 查看可用编号。命令支持类型缩写，
例如 `display current-configuration interface ether 1`。

```text
interface Ethernet 1
 description uplink
 mtu 9000
 ip address 192.0.2.2 255.255.255.0
```

IPv4继续使用主地址与`sub`从地址语义；IPv6地址为累加列表，不使用`sub`：

```text
interface LoopBack 0
 ipv6 address 2001:db8:100::1 64
 ipv6 address 2001:db8:200::1 64
```

同一接口最多配置16个IPv6全局单播地址。同一VPN实例内，同一IPv6前缀只允许归属一个接口；
未指定、多播、链路本地、IPv4映射地址以及物理接口上的回环地址在进入Candidate时拒绝。前缀长度
小于127时，前缀本身的全零接口标识保留为子网路由器任播地址，不能作为普通接口地址。

| 步骤 | Candidate变化 | commit后效果 | 验证 |
|---|---|---|---|
| 创建/进入接口 | 无或创建配置对象 | 不一定创建数据面 | `display this` |
| 配置MTU/IP | 保存本会话修改 | 提交后更新接口MTU和地址 | `display interface Ethernet 1` |
| 关闭offload | 保存关闭项 | 提交后关闭硬件支持的指定能力 | `display interface hardware offload Ethernet 1` |
| 开启详细统计 | 保存`statistic enable` | 提交后采集物理口报文分类计数 | `display interface Ethernet 1`、标准IF-MIB |
| 精确undo | 删除对应叶 | 恢复默认/撤销地址 | display及转发验证 |



[功能目录](../ethernet.md) · [逐条参数](../reference/interfaces.md)
