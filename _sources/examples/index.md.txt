# 配置案例

选择业务，再选择具体功能。每个末级案例分别列出拓扑、各端配置、实际影响、查询和流量结果，以及撤销顺序。标为增量操作的案例依赖明确列出的基础组网，不应单独粘贴执行。

所有网络设备角色均使用 VortexROS CLI；Ethernet 编号按每台设备分别规划。配置与查询输出用于说明操作和结果，接口、地址、计数及运行编号已按文档拓扑整理，标为示例输出；请以设备实际状态为准。外部监控平台、列表源和业务应用仅承担各自用途，不作为 Linux 路由设备配置。

~~~{toctree}
:maxdepth: 2

interfaces/index
routing/index
protocols/index
policy/index
nat/index
services/index
tunnels/index
evpn/index
mpls/index
~~~

[二层子接口完整案例](subinterfaces/l2.md) · [三层子接口完整案例](subinterfaces/l3.md) · [全部命令参数](../operator/reference/commands.md)
