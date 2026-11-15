# NAT 回流

让内部客户端通过对外发布的地址访问内部服务。回流复用同一 FIB 中唯一的 DNAT、Twice NAT 或静态发布映射；不会任意跨 VPN 寻找服务。

## 开关与影响

全局 `nat-policy hairpin enable` 和发布策略内的 `hairpin enable` 必须同时开启，缺省均关闭。显式 No-NAT 和本接口的显式转换决定优先。切换开关不会强制删除已有会话；关闭后应以新连接验证。

## 配置与检查

按[回流案例](../../examples/nat/hairpin.md)配置发布规则及内侧绑定。内侧客户端访问发布地址后，查询会话中的 Mode:hairpin、原始地址与转换后地址，并验证回复。Twice NAT 可将源同时改为网关内侧地址，避免服务端绕过 NAT 直接回包。

关闭开关后使用新连接检查；已有会话不一定立即消失。此功能不会自动创建路由、服务监听或防火墙放行。

## 撤销

在发布策略中执行 `undo hairpin enable`，退出到系统视图执行 `undo nat-policy hairpin enable`，然后提交。只撤销回流开关不会删除 DNAT/Twice NAT 发布规则。完整清理见案例。

[会话筛选](sessions.md) · [命令参数](../reference/nat.md)
