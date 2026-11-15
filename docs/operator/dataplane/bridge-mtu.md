# 网桥与 MTU

VortexROS管理的控制网桥不会因另一个成员接口MTU较小、链路Down或重复提交而自动压低已配置的目标MTU。EVPN端点应与其业务承载要求保持一致。

这不表示小MTU出口能够转发更大的报文。实际业务仍受出口接口、隧道封装开销和路径MTU限制；配置较大MTU前应同时检查两端及中间链路。

先用`display interface`核对各业务接口的运行MTU，再通过带实际业务长度的探测检查端到端路径。网桥自身的MTU数值不能代替业务验证。

[接口参数](../ethernet/settings.md) · [桥域](../bridge-domains.md)
