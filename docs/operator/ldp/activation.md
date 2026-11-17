# 全局与接口

## 使用前提

1. 先为设备配置稳定的 IPv4 LSR ID，通常使用 LoopBack 地址。
2. 全局启用 MPLS 后，再启用 LDP。
3. 在参与 MPLS 转发的三层接口上分别启用 MPLS 和 LDP。
4. 底层 IPv4 IGP 必须先使各节点的 LSR ID 和 LDP transport address 可达。

MPLS 只能用于三层接口。配置了 `portswitch` 的二层接口不能启用 MPLS。


## 基本 LDP 配置

```text
system-view
```

配置清单：

```text
mpls lsr-id 10.0.0.1
mpls
#
mpls ldp

interface LoopBack 0
 ip address 10.0.0.1 255.255.255.255
#

#
interface Ethernet 1
 ip address 192.0.2.1 255.255.255.252
 mpls
 mpls ldp
#
```

CLI 操作：

```text
commit
save
```

`mpls` 打开接口 MPLS 转发能力；`mpls ldp` 使该接口参与 LDP 邻居发现。
两者是独立配置，系统不会根据 LDP 配置猜测接口转发身份。


[功能目录](../ldp.md) · [命令参数](../reference/mpls.md)
