# 独立会话


```text
bfd
bfd TO-P2 bind peer-ip 10.0.12.2 source-ip 10.0.12.1 interface Vlanif 12
 log-session-changes
```

多跳会话需要显式指定 `source-ip`，VPN场景可追加 `vpn-instance BLUE`。


## 被动模式与重启

静态会话视图中的 `passive-mode` 让本端等待对端开始发送控制报文，不能将两端都设为被动后期待它们主动建立。撤销使用 `undo passive-mode`。重新进入已有静态会话时，使用原来的完整 `bfd NAME bind ...` 入口。

开发服务器实测，P1 `CLI-PASSIVE` 与 P2 `CLI-ACTIVE` 使用 198.19.80.1/2、对应 a12 接口直连：原生 FRR 确认 P1 的 `passive-mode`，两端真实 CLI 均显示 Up，有效参数 `1000/1000/3`、检测超时3000ms。通过真实 `reset service bfd` 确认重启，Running 回放与校验成功，会话恢复 Up。随后撤销被动模式，状态仍 Up；删除两端会话并提交后，成功的会话查询均为0。这是独立 BFD 的定向生命周期验证，不等同于所有协议共享会话或硬件故障收敛性能。

最终 RIP 进程保持运行时，再经真实 CLI 重启 VPP、重建全部 LCP 端点，RIP 的 LoopBack97/Tunnel30/e12 接口及两条实际更新源仍保留；没有用再次重启 RIP 来掩盖这次重建结果。该项是生命周期对照；0.29-dev 最终包另验证了组播成员释放和 Zebra 重连路由重放，见 [RIP](../rip.md)。

[默认计时](../bfd.md) · [双端案例](../../examples/bfd.md)
