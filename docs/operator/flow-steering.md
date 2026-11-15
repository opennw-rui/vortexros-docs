# Flow Steering

将物理入口的流分配给 VPP 转发线程。

[命令参考](reference/interfaces.md)

## 配置与验证

当网卡不能按PPPoE、MPLS、L2TP、GRE、VXLAN或IP-in-IP内层流进行硬件RSS时，可以在物理入口启用flow steering。功能按接口生效，使用一套固定的产品参数，不创建或绑定profile，也不向用户暴露VPP内部调试开关：

```text
system-view
 interface Ethernet 1
  flow-steering enable
 commit
display flow-steering interface Ethernet 1
```

该功能只在VPP配置了两个或更多转发worker时激活；单worker设备保留配置但运行状态显示`inactive/single-worker`。解析最多检查256字节、4层封装、4个IPv6扩展头和8层MPLS标签，无法完整识别时使用稳定的外层会话散列，不丢包、不改变协议语义。它只决定入口worker，不替代Zebra、VPP FIB、ECMP或网卡本身已经提供的RSS。撤销接口绑定：

```text
interface Ethernet 1
 undo flow-steering enable
commit
```


## 开发服务器实测

两端 GRE Tunnel30，入口为 host-p2a12。P2 使用 main CPU2、worker CPU3-4。真实 CLI 启用后显示 active/inner-flow，健康 ready；P1 的 GRE 探测 4/4。原生累计 GRE 命中从 1 到 6，handoff/resume 从 1 到 2，handoff-drop 为 0。背景控制报文也在运行，不能将计数差全部归于四个探测包。

单 worker inactive 和双 worker active 是不同验收条件。完整配置与删除应同时检查 CLI 状态、实际流量和后端回读；不能把保留配置但未激活当作多 worker 已验证。


最终配套 26.10.6 包实际加载后，同一双 worker 拓扑启用及撤销均首次提交成功，启用前后探测各 2/2；撤销后原生与 CLI 一致为空，健康 ready、零告警。GET 回复的局部修复不改变 handoff 数据面算法。
