# 配套 VPP

0.29-dev当前配套 **26.10.7+vortexros-vpp**，五个运行包使用相同版本。保留LCP、EVPN、MQC、NAT Policy、AmneziaWG等现有功能和Binary API/Go绑定。

## 本版纳入的底层修复

- LLDP软件/硬件索引分离；单速率policer桶减法边界；AF_PACKET错误和802.1ad处理。
- 接口移表的IPv6 link-local MFIB成员与未配对EVPN L3VNI的LCP本地接收。
- FDB删除暂时失败保留原桥端口/VLAN重试；同端口重学取消旧删除；目标或端口已消失时结束该条删除。新增错误仍报告。
- Flow Steering GET回复清零，撤销后实际状态与Binary API一致；不改变handoff算法。
- 本轮修正LCP最后MPLS标签路由消失时错误调用IP MFIB释放的崩溃：MPLS没有IP组播表，创建和释放仅对IP协议执行。未改通用MFIB或数据包快路径。

## 定向证据

LCP最后标签项的真实命名空间用例通过；隔离QEMU中原CLI撤销后同一VPP进程保持、健康ready。另以真实Linux标签900增删核对两种EOS项和LCP来源锁释放。具体配置和结果见[6PE](../examples/mpls/6pe.md)。

其余既有通过证据包括LLDP独立端口抓包、policer报文、EVPN双栈转发、FDB失败收敛及Flow Steering启用/撤销。未受影响的用例本轮没有重复运行，也没有新增硬件性能结论。最终包新验收见[验证记录](cli-validation.md)。

## 上游 26.10

- [跨 worker handoff](https://github.com/FDio/vpp/commit/a788d6c589) 改用固定槽位队列；配套 WireGuard、AmneziaWG、NAT Policy、L2 policer 和 flow steering 已适配。
- 更新配套 Binary API 与 Go 绑定；继续保留 VortexROS 自有的 LCP、EVPN、静态 FDB 回放和物理接口状态同步。

详细上游差异见 [FD.io 26.10 发布说明](https://raw.githubusercontent.com/FDio/vpp/v26.10/docs/aboutvpp/releasenotes/v26.10.rst)；测量结果见[性能测试](performance.md)。
