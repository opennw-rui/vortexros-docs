# 桥域

用桥域关联 VLAN、VNI 和二层转发，使用 Vbdif 提供三层网关。

[命令参考](reference/bridge-domains.md)

## 配置与验证

```text
bridge-domain 11
 l2 binding vlan 100
 vxlan vni 1011
#
interface Vbdif 11
 ip address 10.11.0.1 255.255.255.0
```

验证BD、VNI、MAC学习和L3网关：

```text
display bridge-domain 11
display mac-address
display interface Vbdif 11
```

删除前先解除Vbdif、VNI和VLAN绑定，避免业务仍在引用BD。


## 控制网桥 MTU

Linux 控制网桥用于 LCP/FRR 的二层状态投影，普通业务仍由 VPP 转发。网桥 MTU 按受管端口所需的最大值设置，不因另一个成员使用较小 MTU 或变为 Down 而自动压低；这不表示小 MTU 端口能够转发超过自身能力的报文。实际业务仍受出口 MTU、封装开销与路径 MTU 限制。

为EVPN业务规划MTU时，应同时考虑接入口、底层接口和VXLAN封装开销。控制网桥不会因较小成员的状态变化而自动压低目标MTU，但报文仍受实际出口和路径MTU限制。


桥域摘要的 `Flood` 表示实际广播/组播泛洪开关，不是统计计数开关；`State` 表示桥域是否已建立。需要判断业务端口是否工作时，继续查看桥域明细、成员接口、MAC表与实际流量。未知单播泛洪由明细中的 `uu-flood` 单独表示。

## Vbdif 激活条件

Vbdif 未 shutdown、相应业务桥域已建立，且至少有一个非网关成员处于管理 Up 和链路 Up 时，PHY 才能 Up；有效接口 IP 地址决定三层 Protocol 是否 Up。成员可以是本地接入口或可用的 VXLAN 业务成员。只有 Vbdif 自身、所有成员均 Down 或业务映射尚未建立时，网关不能激活。成员恢复后自动恢复；显式 shutdown 的网关需先执行 undo shutdown。
