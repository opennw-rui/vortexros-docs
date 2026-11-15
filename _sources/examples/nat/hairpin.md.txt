# Hairpin

## 用途与前提

内侧设备通过发布地址访问内侧服务，流量在 NAT 网关折返。先完成[基础拓扑](topology.md)及 [Twice NAT](twice.md)。Twice NAT 同时转换源地址，确保回包经过网关，不能只配置目的地址转换。

## 配置

P1 在系统视图启用全局及策略 hairpin，并把策略绑定到内侧入方向：

~~~text
nat-policy hairpin enable
nat-policy name LAB-TWICE
 hairpin enable
quit
interface Ethernet1
 nat-policy LAB-TWICE inbound
quit
commit
~~~

若该方向已绑定 LAB-LAN-PASS，先解除原绑定。匹配条件应包括来自内侧、目的为 198.19.81.1 的报文；不要把规则源地址限定为外侧 P2。

## 验证

P3 执行 ping -a 198.18.11.2 -c 3 198.19.81.1，P1 执行：

~~~text
display nat-policy sessions action twice-nat
display nat-policy statistics name LAB-TWICE
display nat-policy interfaces
~~~

核对目的从发布地址变为 198.18.11.2，源变为网关内侧地址，回包也经过 NAT。ICMP 仅验证折返地址转换；服务端口发布需按 DNAT 页另用相应业务检查。

## 撤销

先解除 Ethernet1 的 LAB-TWICE 入方向绑定，策略下执行 undo hairpin enable；不再有其他折返业务时执行全局 undo nat-policy hairpin enable。按 Twice NAT 页撤销其余对象并提交。需要保留的其他 NAT 业务不可随本例删除；最后按需 save。
