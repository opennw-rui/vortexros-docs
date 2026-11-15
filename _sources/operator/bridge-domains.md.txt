# 桥域

用桥域关联 VLAN、VNI 和二层转发，使用 Vbdif 提供三层网关。

[命令参考](reference/bridge-domains.md)

## 配置与验证

```text
bridge-domain 11
 l2 binding vlan 100
 vxlan vni 1011
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

EVPN 的 Linux VLAN 端点与控制网桥应保持一致的 MTU。更改端口或重新应用相同配置不应短暂缩小已有端点。开发服务器已验证 9000/1500 混合成员、较大成员降至1500/Down、重复投影，以及携带既有 EVPN VNI 的真实 `reset service vpp`。最终网桥和 EVPN 端点均为9000；这些结果不构成满 MTU 吞吐保证。
