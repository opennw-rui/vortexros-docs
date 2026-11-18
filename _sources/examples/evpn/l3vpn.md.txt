# EVPN 三层

## 拓扑和影响

两台 PE 使用 AS65000，通过 IPv4 underlay 建立 EVPN 邻居。P1 的 Ethernet0 为198.19.80.1/30，P2 的 Ethernet0 为198.19.80.2/30；它们还作为 VTEP 地址。租户 CLI-TYPE5 使用 L3VNI50081、RT65000:50081。P1/P2 的租户环回地址分别为198.18.196.1/32、198.18.196.2/32，以及2001:db8:196::1/128、::2/128。

该配置把租户直连前缀发布为 EVPN Type-5；路由隔离在租户 VRF 内，数据通过 VXLAN 转发。本例没有 VPNv4/VPNv6 传输邻居。请使用隔离示例接口，先确认 underlay 两端互通。

## P1

以下是完整业务配置。若接口原来已有地址，先按原配置撤销，避免保留其他业务地址。

```text
enable switch
evpn-overlay enable
interface Ethernet0
 ip address 198.19.80.1 255.255.255.252
#
ip vpn-instance CLI-TYPE5
 vxlan vni 50081
 ipv4-family
  route-distinguisher 65000:1801
  vpn-target 65000:50081 both
 #
 ipv6-family
  route-distinguisher 65000:1801
  vpn-target 65000:50081 both
#
interface LoopBack 181
 ipv6 enable
 ip binding vpn-instance CLI-TYPE5
 ip address 198.18.196.1 255.255.255.255
 ipv6 address 2001:db8:196::1 128
#
interface Nve 1
 source 198.19.80.1
#
bgp 65000
 router-id 1.1.1.1
 peer 198.19.80.2 as-number 65000
 l2vpn-family evpn
  peer 198.19.80.2 enable
 #
 ipv4-family vpn-instance CLI-TYPE5
  import-route direct
  advertise l2vpn evpn
 #
 ipv6-family vpn-instance CLI-TYPE5
  import-route direct
  advertise l2vpn evpn
#
```

CLI 操作：

```text
commit
```

## P2

```text
enable switch
evpn-overlay enable
interface Ethernet0
 ip address 198.19.80.2 255.255.255.252
#
ip vpn-instance CLI-TYPE5
 vxlan vni 50081
 ipv4-family
  route-distinguisher 65000:1802
  vpn-target 65000:50081 both
 #
 ipv6-family
  route-distinguisher 65000:1802
  vpn-target 65000:50081 both
#
interface LoopBack 182
 ipv6 enable
 ip binding vpn-instance CLI-TYPE5
 ip address 198.18.196.2 255.255.255.255
 ipv6 address 2001:db8:196::2 128
#
interface Nve 1
 source 198.19.80.2
#
bgp 65000
 router-id 2.2.2.2
 peer 198.19.80.1 as-number 65000
 l2vpn-family evpn
  peer 198.19.80.1 enable
 #
 ipv4-family vpn-instance CLI-TYPE5
  import-route direct
  advertise l2vpn evpn
 #
 ipv6-family vpn-instance CLI-TYPE5
  import-route direct
  advertise l2vpn evpn
#
```

CLI 操作：

```text
commit
```

## 验证

两端执行以下查询，P2 将目标地址替换为 P1 的地址。

```text
display bgp evpn all routing-table
display ip routing-table vpn-instance CLI-TYPE5 198.18.196.2 32
display ipv6 routing-table vpn-instance CLI-TYPE5 2001:db8:196::2 128
ping -vpn-instance CLI-TYPE5 -c 2 -a 198.18.196.1 198.18.196.2
ping ipv6 vpn-instance CLI-TYPE5 -c 2 -a 2001:db8:196::1 2001:db8:196::2
display health
```

两端应收到远端 Type-5 IPv4/IPv6 前缀，租户 VPN 的双向探测应成功。示例输出：

```text
2 packets transmitted, 2 received, 0% packet loss
```

路由存在不代表业务可用。两端在租户 VPN 内选择正确的源地址做双向探测，检查下一跳和 VXLAN 出口；数据面重建后再次核对恢复。

## 撤销

先在两端撤销通告并查询远端前缀：

```text
bgp 65000
 ipv4-family vpn-instance CLI-TYPE5
  undo advertise l2vpn evpn
 #
 ipv6-family vpn-instance CLI-TYPE5
  undo advertise l2vpn evpn
#
```

CLI 操作：

```text
commit
display bgp evpn all routing-table
display ip routing-table vpn-instance CLI-TYPE5 198.18.196.2 32
display ipv6 routing-table vpn-instance CLI-TYPE5 2001:db8:196::2 128
```

实际撤销提交成功，两端 IPv4/IPv6 的远端前缀查询均为0；原有 L2VNI 的路由保留。删除测试租户时先撤销 BGP 租户地址族，按提示逐项输入 Y，再删除环回接口和 VPN-instance：

```text
bgp 65000
 undo ipv4-family vpn-instance CLI-TYPE5
 Y
 undo ipv6-family vpn-instance CLI-TYPE5
 Y
#
undo interface LoopBack181
undo ip vpn-instance CLI-TYPE5
Y
```

CLI 操作：

```text
commit
```

P2 删除 LoopBack182。Nve、EVPN 邻居和 underlay 可能被其他业务共用，仅在确认无其他使用者时撤销；不要为删除单一租户而关闭整个 EVPN。
