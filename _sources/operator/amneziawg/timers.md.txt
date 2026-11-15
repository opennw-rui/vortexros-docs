# 计时与预共享密钥

## 定时范围和预共享密钥

Profile 支持 `timing rekey-after LOW HIGH`、`timing rekey-timeout LOW HIGH`、`timing reject-after LOW HIGH`、`timing keepalive LOW HIGH` 和 `timing max-handshakes LOW HIGH`。前四项是秒数范围，最后一项是尝试次数；`undo timing ...` 恢复插件默认，配置正文省略默认项。状态中的 0-0 是默认时序标记，不是零秒。

Peer 的 `presharedkey KEY` 增加额外预共享密钥，`undo presharedkey` 撤销；与本端 privatekey、对端 publickey 是不同对象。两端不一致会阻止新握手。完整的双端配置、实际签名出包、IPv4/IPv6、保存回放与默认恢复结果见[高级参数案例](../../examples/amneziawg.md#高级参数实测)。

[功能目录](../amneziawg.md) · [命令参数](../reference/amneziawg.md)
