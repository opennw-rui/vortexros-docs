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
