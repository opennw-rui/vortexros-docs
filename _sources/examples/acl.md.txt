# 入站 ACL

**用途**。在实验 VLAN 的三层入口拒绝目的 TCP 端口 23，其余 IPv4 流量放行。

**前提**。使用具备 ACL 能力的 VPP 数据面。确认 Vlanif 100 承载测试流量，且没有需要保留的入方向 ACL 绑定。

## 配置

~~~text
system-view
acl name BLOCK-TELNET advance
 rule 10 deny tcp destination-port eq 23
 rule 100 permit ip
 quit
interface Vlanif 100
 traffic-filter inbound acl BLOCK-TELNET
 quit
commit
~~~

ACL 创建后只有绑定到接口才会影响流量。规则按编号从小到大匹配，首条命中决定结果。末尾 permit ip 保留其余 IPv4 流量；该规则不覆盖 IPv6。该绑定只处理进入这个三层接口的流量。

## 验证

使用 display acl name BLOCK-TELNET 核对规则。由测试客户端分别发起 TCP/23 和预期放行的连接，验证拒绝和放行两条路径。仅查看 ACL 对象不能证明策略已经作用于目标流量。

## 撤销

在 Vlanif 100 执行 undo traffic-filter inbound，然后提交并复测。确定 ACL 没有其他引用时，再删除 ACL 对象。
