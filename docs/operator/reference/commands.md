# 命令参考

本参考列出当前版本实际提供的CLI。每条命令路径只出现一次；同一命令在不同视图中的合法写法会合并展示。配置命令先写入本会话 Candidate，提交后才影响 Running；即时运维命令可直接改变运行状态。

原冻结基线为 **844** 条规范命令路径；本开发候选新增 `rewrite pop` 和 `undo rewrite pop` 后为 **846** 条。路径数量不表示全部参数、视图和组合已验收通过，实际范围以本轮独立台账为准。

按功能选择章节。共用命令保留一份定义，从各功能页链接过去。完整流程见[配置案例](../../examples/index.md)。

~~~{toctree}
:maxdepth: 1

reading
cli
aaa
system
operations
interfaces
dataplane
link-aggregation
vlan
bridge-domains
neighbors
vrf
static-routing
route-groups
ip-routing
icmp
urpf
prefix-lists
route-policy
ospf
ospfv3
bgp
isis
rip
ripng
bfd
vrrp
dynamic-routing
mpls
acl
nat
qos
mqc
mss
policy
tunnels
gre
vxlan
evpn
wireguard
amneziawg
dhcp
ipv6-autoconfig
lldp
snmp
~~~
