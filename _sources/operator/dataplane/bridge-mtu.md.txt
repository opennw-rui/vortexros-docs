# 控制网桥 MTU


EVPN/L2 控制投影中的 Linux 网桥使用控制层明确设置的 MTU，不依赖内核按最小成员 MTU 自动缩小。创建、接管和更新交换投影时会固定该值；成员口 MTU 降低或链路断开，不应自行把已经固定的网桥 MTU 拉低。

Linux 对“再次写入当前相同 MTU”的操作可能不调用网桥的 MTU 修改入口。本轮在实际内核上复现这一点，采用与 NetworkManager 相同原则的强制实际变化后设置目标值，避免把同值写入成功误当成自动调整已经关闭。参考 [NetworkManager 网桥实现](https://github.com/NetworkManager/NetworkManager/blob/main/src/core/devices/nm-device-bridge.c)。

该网桥服务于 Linux/LCP 控制面同步，不代表普通业务必须通过 Linux bridge 转发。物理端口、VPP 接口和隧道仍有各自的 MTU 及封装开销限制；把控制网桥设大不会使较小物理端口能够发送超长报文。

本轮开发服务器实际内核验证覆盖：新增小 MTU 成员、同值接管、重复应用、全部成员降为 1500、关闭成员，以及实际 P2 成员 1500 → 1400 → 1500；网桥保持目标 9000。完整端口与隧道配置仍应按对应案例验证业务报文，不以网桥数值代替流量验收。


[数据面总览](../dataplane.md) · [逐条命令](../reference/dataplane.md)
