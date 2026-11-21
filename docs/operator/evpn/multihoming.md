# 多归属

All-Active 使用相同 ESI 将 CE 双接入两台 PE。远端 PE 根据 EVPN Type-1/Type-4 与 MAC 路由建立以太网段下一跳组；单播可以使用两个接入 PE。DF 选举控制发往该以太网段的广播与组播，split-horizon 防止业务返回原以太网段。

当前公开 CLI 支持 All-Active 接入及多 VNI 共用同一 ESI。不支持在 EVPN 地址族下配置 reflect-client，因此以下案例采用三台 PE 全互联，不要求额外 RR。

~~~{toctree}
:maxdepth: 1

../../examples/evpn/all-active
../../examples/evpn/all-active-multiple-vni
~~~

## 运行环境要求

Debug 8 请使用同一整包中的 FRR 和 VPP，先以 `display version` 确认设备实际版本。有些早期组件组合可以建立 EVPN 邻居和下一跳组，但远端业务 MAC 仍可能缺失。确认业务正常需要同时检查 Type-2、下一跳和实际业务流量。

## 核对与恢复 ESI

对接同一客户二层段的两个接入 PE 使用相同 ESI，并为二者配置一致的业务 VLAN 和 VNI。远端 PE 通过 ES 下一跳组抵达客户 MAC。计划维护前，先协调 CE 聚合与两端 PE，保留同段的另一条可用接入路径。

在指定接入 PE 的聚合视图执行 `undo esi` 和 `commit`，核对远端只保留仍参与该 ES 的成员。恢复时，在同一接口填回原 ESI，再次提交。在接入 PE 确认客户 MAC 指向本地聚合子接口，在远端检查对应 Type-2 和多成员下一跳组。已有客户 MAC 应自动恢复通告，无需手工清除 MAC。

~~~text
display current-configuration interface Eth-Trunk11
display eth-trunk 11
display bgp evpn all routing-table
display mac-address bridge-domain 460
~~~

先确认上述运行态恢复，再从 CE 侧分别发送 IPv4 与 IPv6 探测。多个 VNI 共用 ESI 时，按业务逐一核对。更新 ESI 期间业务可能重新选择链路，请按维护流程操作。完整命令见[ESI 配置变更](../../examples/evpn/esi.md)。

## 已验证的组合与限制

|组合|实际验证|
|---|---|
|ESI 配置与撤销|两端使用同一 ESI 时，远端 Type-4 路由和下一跳组均有两个成员；一端执行 `undo esi` 后缩为一个；恢复 ESI 后重建两成员，带 ESI 的客户 Type-2 恢复，IPv4、IPv6 各 3 发 3 收|
|双接入单播|远端 MAC 指向包含两台接入 PE 的 ES 下一跳组；单链路关闭后使用另一台 PE，链路恢复后重新可用|
|广播、组播|远端各发送5帧，DF侧各收到5帧，非DF侧为0；未观察到重复交付|
|接入故障后的广播|关闭原DF接入口后，另一侧成为DF，5帧广播全部交付|
|分割水平|CE发送5帧广播，远端收到5帧，未收到回到原CE段的反射副本|
|同一ESI、两个VNI|两个业务分别可达，撤销一个VNI后该业务不通，另一个仍可达|
|未知单播|EVPN业务桥域配置为UU-Flood drop，未学习目的MAC时不泛洪；先通过正常源MAC学习或控制面通告建立目的项|
|Single-Active、EVPN RR|当前公开CLI未提供，不支持|

本表是功能验证，不是负载分担比例、吞吐或所有厂商互通认证。多归属路由正常也不能替代实际业务报文检查。

[EVPN参数](../reference/evpn.md) · [完整All-Active案例](../../examples/evpn/all-active.md)
