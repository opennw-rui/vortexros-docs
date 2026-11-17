# 计时与预共享密钥

## 定时范围和预共享密钥

Profile 支持 `timing rekey-after LOW HIGH`、`timing rekey-timeout LOW HIGH`、`timing reject-after LOW HIGH`、`timing keepalive LOW HIGH` 和 `timing max-handshakes LOW HIGH`。前四项是秒数范围，最后一项是握手重试预算阈值；`undo timing ...` 恢复插件默认，配置正文省略默认项。状态中的 0-0 是默认时序标记，不是零秒。

Peer 的 `presharedkey KEY` 增加额外预共享密钥，`undo presharedkey` 撤销；与本端 privatekey、对端 publickey 是不同对象。两端不一致会阻止新握手。完整的双端配置、实际签名出包、IPv4/IPv6、保存回放与默认恢复结果见[高级参数案例](../../examples/amneziawg.md#高级参数配置)。

[功能目录](../amneziawg.md) · [命令参数](../reference/amneziawg.md)

## 重试预算的实际计数

该阈值沿用 WireGuard 的重传计数方式，不是线上 Init 报文的总数。一次没有对端回复、没有新的业务触发的握手序列中，阈值 N 可产生 N+2 次 Init，包括首次发送。实际将阈值固定为 3 后抓到了 5 次 Init，之后停止该序列；间隔还包含重试抖动。后续新的业务报文仍可重新触发握手，不代表前一序列没有停止。

该计数规则与[官方 AmneziaWG 计时实现](https://github.com/amnezia-vpn/amneziawg-go/blob/master/device/timers.go)一致。不要用阈值直接估算全设备的报文次数上限。

## Cookie Reply 控制

正常情况下不一定产生 Cookie Reply，不能仅凭普通 ping 成功判断开关已生效。真实对照使用同一组握手报文触发 Cookie 条件：保持默认发送行为时收到 25 个 Cookie Reply；配置 disable-cookies enable 后，相同输入没有 Cookie Reply。其余密钥协商、加密和访问限制仍需正常满足，关闭此机制不等于关闭认证。
