# VPP 更新

**当前配套版本：26.10.3+vortexros-vpp。** [完整发布说明](https://github.com/opennw-rui/VortexROS-VPP/releases/tag/v26.10.3%2Bvortexros-vpp)

相对 26.10.2，源码只修改 LCP 的 FDB 删除。Linux Netlink 拒绝删除时，保留原桥端口和 VLAN，供后续处理继续清理；同一 VPP 端口重新学到该 MAC 时，废弃旧删除。Binary API、Go 绑定和 FRR 版本未变。

发布版 VPP 与隔离 Linux 网桥验证了连续四次删除失败后的收敛，以及同端口重学后保留表项。EVPN 事件队列实测到达 1,024 条，3,600 条邻居新增和撤销均收敛，保留原批处理参数。

## 上游 26.10

- [跨 worker handoff](https://github.com/FDio/vpp/commit/a788d6c589) 改用固定槽位队列；配套 WireGuard、AmneziaWG、NAT Policy、L2 policer 和 flow steering 已适配。
- 更新配套 Binary API 与 Go 绑定；继续保留 VortexROS 自有的 LCP、EVPN、静态 FDB 回放和物理接口状态同步。

详细上游差异见 [FD.io 26.10 发布说明](https://raw.githubusercontent.com/FDio/vpp/v26.10/docs/aboutvpp/releasenotes/v26.10.rst)；测量结果见[性能测试](performance.md)。
