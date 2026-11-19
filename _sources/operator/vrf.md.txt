# VPN 实例

VPN-instance 缺省可用，不需要全局 enable 开关。默认实例对应 Linux main254、VPP表0；新表从1024找空闲号，可超过2048，跳过已占用表。

## 工作原理与业务隔离

VPN 实例为接口和路由提供独立的三层查找域，可用于不同租户复用地址以及隔离业务出口。它本身不是加密 VPN，也不自动允许不同实例之间互通。

接口绑定决定其地址和直连路由属于哪张表；普通路由在本实例解析，跨实例路由必须明确配置。设备显示名称与系统内部表号用途不同：默认实例使用 Linux main 254、VPP 表 0，不需要把它们改成相同数字。

变更已有接口的 VPN 归属会影响地址、邻居、协议及路由，应检查依赖和双向业务。RD/RT 用于 MPLS VPN 或 EVPN 的控制面标识和导入导出，不是普通本地 VRF 隔离所必需的开关。

~~~{toctree}
:maxdepth: 2

vrf/families
vrf/interfaces
~~~

[完整案例与示例输出](../examples/mpls-l3vpn.md) · [全部命令参数](reference/vrf.md)
