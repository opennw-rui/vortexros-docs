# 多归属

All-Active 使用相同 ESI 将 CE 双接入两台 PE。远端 PE 根据 EVPN Type-1/Type-4 与 MAC 路由建立以太网段下一跳组；单播可以使用两个接入 PE。DF 选举控制发往该以太网段的广播与组播，split-horizon 防止业务返回原以太网段。

当前公开 CLI 支持 All-Active 接入及多 VNI 共用同一 ESI。不支持在 EVPN 地址族下配置 reflect-client，因此以下案例采用三台 PE 全互联，不要求额外 RR。

~~~{toctree}
:maxdepth: 1

../../examples/evpn/all-active
../../examples/evpn/all-active-multiple-vni
~~~

## 运行环境要求

使用 Debug 9 整包中的配套 FRR 和 VPP。两台 PE 的 EVPN 邻居和下一跳组建立后，还需确认远端 MAC 已进入转发表，并用 CE 侧双栈流量验收。

## ESI 维护与回读

维护前协调 CE 聚合及两台接入 PE，确认同一业务 VLAN 和 VNI 并保留另一条可用链路。在一个接入 PE 的聚合视图执行 `undo esi` 并提交，远端下一跳组应保留仍参与该 ES 的成员。填回原 ESI 后再次提交。

~~~text
display eth-trunk 11
display bgp evpn all routing-table
display mac-address bridge-domain 460
~~~

示例使用聚合 11、桥域 460，实际按业务编号替换。在接入 PE 核对客户 MAC 指向本地聚合子接口，在远端核对客户 Type-2 和 ES 下一跳组。已有客户 MAC 会重新通告，无需清除 MAC。最后从 CE 分别验证 IPv4、IPv6 业务；多 VNI 逐项检查。详细步骤见 [ESI 案例](../../examples/evpn/esi.md)。

## 已验证的组合与限制

|组合|实际验证|
|---|---|
|ESI 配置与撤销|两端使用同一 ESI 时，远端 Type-4 路由和下一跳组均有两个成员；一端撤销 ESI 后下一跳组从两成员缩为一成员，恢复后 Type-2 和两成员自动恢复。接入静默且邻居已收敛的对照中，恢复后双栈各 3 发 3 收|
|双接入单播|远端 MAC 指向包含两台接入 PE 的 ES 下一跳组；单链路关闭后使用另一台 PE，链路恢复后重新可用|
|广播、组播|远端各发送5帧，DF侧各收到5帧，非DF侧为0；未观察到重复交付|
|接入故障后的广播|关闭原DF接入口后，另一侧成为DF，5帧广播全部交付|
|分割水平|CE发送5帧广播，远端收到5帧，未收到回到原CE段的反射副本|
|同一ESI、两个VNI|两个业务分别可达，撤销一个VNI后该业务不通，另一个仍可达|
|未知单播|EVPN业务桥域配置为UU-Flood drop，未学习目的MAC时不泛洪；先通过正常源MAC学习或控制面通告建立目的项|
|Single-Active、EVPN RR|当前公开CLI未提供，不支持|

本表是功能验证，不是负载分担比例、吞吐或所有厂商互通认证。多归属路由正常也不能替代实际业务报文检查。

[EVPN参数](../reference/evpn.md) · [完整All-Active案例](../../examples/evpn/all-active.md)

### 早期版本的兼容提示

All-Active 需要 Linux 正确接受引用下一跳组的远端 MAC 表项。部分内核包含提交 `98fc57d16744`，但尚未包含后续修复 `7308ef8b4a67`，会拒绝 FRR 的合法下发，报告 `A nexthop fdb cannot be dynamic`。此时 EVPN 路由和下一跳组可能正常，远端客户 MAC 却无法进入转发表，业务不能据邻居 Established 判定为正常。

部署前应使用未引入该回归、或已包含该修复的发行版内核。该问题不通过调整 VLAN、RT 或开启未知单播洪泛解决，也不应手工添加永久 MAC 作为长期配置。内核更新与重启按操作系统的维护流程执行。

参考：[Linux 上游修复](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=7308ef8b4a6779a39f68d053c19b53a5c584a663)。
