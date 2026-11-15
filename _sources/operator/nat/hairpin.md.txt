# NAT 回流

让内部客户端通过对外发布的地址访问内部服务。回流复用同一 FIB 中唯一的 DNAT、Twice NAT 或静态发布映射；不会任意跨 VPN 寻找服务。

## 开关与影响

全局 `nat-policy hairpin enable` 和发布策略内的 `hairpin enable` 必须同时开启，缺省均关闭。显式 No-NAT 和本接口的显式转换决定优先。切换开关不会强制删除已有会话；关闭后应以新连接验证。

## 配置与真实显示

[回流完整案例](../../examples/nat/hairpin.md)从已验证的 Twice NAT 发布配置开始，包含内部客户端访问、显示与关闭对照。真实输出节选：

~~~text
host-p1q13/inbound  FIB:0 -> FIB:0  Policy:LAB-DNAT(2572252004)/10  Action:TWICE-NAT  Mode:hairpin
198.18.11.2:57680 -> 198.19.80.1:18080  =>  198.18.11.1:57680 -> 198.18.11.2:8081
~~~

端点实际 HTTP 200；双开关关闭后的新 HTTP 连接失败。该实验为同一内部端点访问自身发布服务，不外推为所有多客户端、端口耗尽或跨 VRF 组合均已验证。

## 撤销

在发布策略中执行 `undo hairpin enable`，退出到系统视图执行 `undo nat-policy hairpin enable`，然后提交。只撤销回流开关不会删除 DNAT/Twice NAT 发布规则。完整清理见案例。

[会话筛选](sessions.md) · [命令参数](../reference/nat.md)
