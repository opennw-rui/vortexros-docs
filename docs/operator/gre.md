# GRE

使用 GRE 在 IP 网络上建立三层点到点隧道。

[命令参考](reference/gre.md) · [配置案例](../examples/gre.md)

## 配置与验证

```text
interface Tunnel 1
 description P1-P2-GRE
 tunnel-protocol gre
 source 192.0.2.1
 destination 192.0.2.2 vpn-instance default
 gre key 100
 mtu 1476
 ip address 10.0.12.1 255.255.255.252
```

source和destination必须按同一underlay VPN解析；GRE key可以与VPN绑定并存。修改/undo key后应重建所需参数且保持正确外层源地址，不能出现0.0.0.0。

```text
display interface Tunnel 1
```

提交后，Tunnel源地址必须能在指定underlay VPN中找到，目的地址也必须通过该VPN可达。隧道up后，Tunnel上的直连路由才应进入路由表。删除GRE隧道：

```text
undo interface Tunnel 1
commit
```
