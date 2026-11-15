# NAT 回流

## 拓扑和前置配置

沿用[基础拓扑](topology.md)，先完成[Twice NAT](twice.md)案例，包括 P1 WAN 发布规则和 LAN 的 `LAB-LAN-PASS` 入方向状态处理。P3 既是内部客户端，也是监听 8081 的内网服务。P2 的外部访问应已成功。

本例只增加回流开关，不重新复制整份发布策略：

~~~text
system-view
nat-policy hairpin enable
nat-policy name LAB-DNAT
 hairpin enable
quit
commit
~~~

## 访问与验证

在 P3 的 Linux Bash 发起新连接：

~~~bash
curl --noproxy '*' --max-time 5 http://198.19.80.1:18080/
~~~

在 P1 查询：

~~~text
display nat-policy sessions hairpin enable
display nat-policy runtime
~~~

已有真实 CLI 输出节选：

~~~text
host-p1q13/inbound  FIB:0 -> FIB:0  Policy:LAB-DNAT(2572252004)/10  Action:TWICE-NAT  Mode:hairpin
198.18.11.2:57680 -> 198.19.80.1:18080  =>  198.18.11.1:57680 -> 198.18.11.2:8081
~~~

实际 HTTP 200，回包通过状态恢复为客户端访问的发布地址。只有看到会话不足以证明 HTTP 成功，两项证据需要一起判断。

## 关闭对照和撤销

~~~text
system-view
nat-policy name LAB-DNAT
 undo hairpin enable
quit
undo nat-policy hairpin enable
commit
~~~

再发起新的 HTTP 连接，原实验中新连接失败。已有连接可能继续工作，不能用它判断关闭无效。若要主动删除实验会话：

~~~text
clear nat-policy sessions name LAB-DNAT
display nat-policy sessions name LAB-DNAT
~~~

清会话会中断对应业务，不应用于生产故障的无差别试探。最后按 Twice NAT 案例解除接口绑定、删除两份策略；需要保留修改时执行 `save`。

[功能和范围](../../operator/nat/hairpin.md)
