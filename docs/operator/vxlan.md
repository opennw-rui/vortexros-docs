# VXLAN

使用静态 VTEP 列表在三层网络上延伸二层桥域。

[命令参考](reference/vxlan.md)

## 配置与验证

NVE用于集中保存VXLAN源地址和远端VTEP信息，不承载普通三层转发。因此NVE可以进入配置视图、display和undo，但不会出现在路由、BFD、VRRP或ACL等需要真实转发接口的命令补全中。

```text
interface Nve 1
 source 192.0.2.1
 vni 1011 head-end peer-list 192.0.2.2
```

BD、VNI 和 Vbdif 见[桥域](bridge-domains.md)。验证：

```text
display vxlan tunnel
display vxlan statistics
display bridge-domain 11
display mac-address
```

underlay变化导致VXLAN暂时不可用时，应撤销相关数据面接口/路由并在恢复后自动重建。

使用BGP自动发现远端VTEP和MAC时，将静态peer命令替换为
`vni VNI head-end peer-list protocol bgp`，并配置bridge-domain EVPN RD/RT和BGP
EVPN地址族。完整步骤、限制及Type-2/Type-3验证见[VXLAN EVPN](11-vxlan-evpn.md)。

NVE是控制层逻辑对象，没有独立的VPP收发计数器和MTU，因此`display interface brief`中的利用率显示`0.0%`、MTU显示`--`。实际VXLAN成员的原始计数使用`display vxlan statistics`查看，避免把父接口、子接口和多个VXLAN成员重复相加。创建、管理状态、MTU、桥域绑定及删除属于同一VPP会话事务；VPP在中途重启时本次操作失败关闭，由下一轮权威收敛重建，不会继续使用旧接口索引。

删除远端或整个NVE配置：

```text
interface Nve 1
 undo vni 1011 head-end peer-list 192.0.2.2
undo interface Nve 1
commit
```
