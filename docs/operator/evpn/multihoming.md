# 多归属

All-Active 使用相同 ESI 将 CE 双接入两台 PE。远端 PE 根据 EVPN Type-1/Type-4 与 MAC 路由建立以太网段下一跳组；单播可以使用两个接入 PE。DF 选举控制发往该以太网段的广播与组播，split-horizon 防止业务返回原以太网段。

当前公开 CLI 支持 All-Active 接入及多 VNI 共用同一 ESI。不支持在 EVPN 地址族下配置 reflect-client，因此以下案例采用三台 PE 全互联，不要求额外 RR。

~~~{toctree}
:maxdepth: 1

../../examples/evpn/all-active
../../examples/evpn/all-active-multiple-vni
~~~

## 已验证的组合与限制

|组合|实际验证|
|---|---|
|双接入单播|远端 MAC 指向包含两台接入 PE 的 ES 下一跳组；单链路关闭后使用另一台 PE，链路恢复后重新可用|
|广播、组播|远端各发送5帧，DF侧各收到5帧，非DF侧为0；未观察到重复交付|
|接入故障后的广播|关闭原DF接入口后，另一侧成为DF，5帧广播全部交付|
|分割水平|CE发送5帧广播，远端收到5帧，未收到回到原CE段的反射副本|
|同一ESI、两个VNI|两个业务分别可达，撤销一个VNI后该业务不通，另一个仍可达|
|未知单播|EVPN业务桥域配置为UU-Flood drop，未学习目的MAC时不泛洪；先通过正常源MAC学习或控制面通告建立目的项|
|Single-Active、EVPN RR|当前公开CLI未提供，不支持|

本表是功能验证，不是负载分担比例、吞吐或所有厂商互通认证。多归属路由正常也不能替代实际业务报文检查。

[EVPN参数](../reference/evpn.md) · [完整All-Active案例](../../examples/evpn/all-active.md)
