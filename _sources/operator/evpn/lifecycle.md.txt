# 变更与恢复

## ESI 撤销

在 Eth-Trunk 下配置 `esi 0000.0000.0000.0000.0010` 后，本次真实 FRR ES 清单为 local/up，BGP 显示对应 Type-4 路由，聚合链路 VLAN400 探测2/2。执行 `undo esi` 后，聚合端口应回到普通桥接成员，保留原来的管理状态和 VLAN 配置。

这项撤销曾实际失败：Linux 删除承载 ES 的 bond 时会关闭其原成员；同时未映射的旧 ES 索引被错误当作 LCP 索引回放，阻断恢复。现由控制层在删除自己的 bond 时保留成员原状态，并按真实 ES/LCP 生命周期清理失效工作。修复后真实撤销一次提交即成功，Linux/VPP 端口均 Up、FRR ES 清单为空、健康 ready。即刻探测为1/2，随后稳定探测为2/2；不声称无损切换或完整 All-Active 故障验证。


## 删除 VNI

`undo vni VNI` 删除选定 VNI 的整个 head-end 绑定，包括静态对端或 BGP 动态发现。指定 `head-end peer-list PEER` 仅删除该静态对端；指定 `head-end peer-list protocol bgp` 仅撤销动态发现。其他 VNI 保留。

真实 CLI 对 VNI10450 执行不带后缀的撤销、提交后，Nve 当前配置不再显示该 VNI，EVPN 路由清单为零；重新配置动态发现并提交后，恢复实际 Type-2/Type-3 路由。删除 BGP EVPN 地址族之前，应先撤销使用它的 NVE 绑定，依赖未解除时 Candidate 会拒绝。

## 保存和重启

配置按 Candidate → commit → Running → save → 启动 CFG 流转。核对邻居、路由和流量后再保存；不直接编辑 FRR、Linux 控制桥或内部 VPP 桥域作为持久配置。

恢复后分别检查 BGP 会话、Type-2/3/5、LCP 对象、VPP FIB 和租户流量。已有双栈 L3VPN 的重启证据见[案例](../../examples/evpn/l3vpn.md)，不外推为完整多归属冷重启已经通过。
