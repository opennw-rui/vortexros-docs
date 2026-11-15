# 运行配置重置

## Clear与Reset

- `clear`清理计数或当前Candidate；
- `reset`清理动态ARP/MAC表项，或执行服务重启、远端列表刷新和协议会话重置；
- 二者都是即时运维命令，不进入配置；
- 对外部连接、路由邻居或转发有影响的操作需要管理员权限和明确确认。

示例：

```text
reset ip arp
reset ip arp interface Vlanif 20 ip 192.0.2.10
reset mac-address
reset mac-address interface Ethernet 1 mac-address 00-11-22-33-44-55
clear interface Ethernet 1 counter
clear nat-policy counters
reset service vpp
reset service bgp
reset route-static group name CDN
```

`reset ip arp`只删除Linux LCP接口上的动态IPv4邻居，可按三层接口、IPv4地址或两者同时过滤；不指定接口时使用当前VPP LCP清单，覆盖自动物理LCP和配置型LCP。删除事件由LCP同步至VPP，在二层接口上执行会明确报错。`reset mac-address`由switchd删除Linux控制FDB中的动态外部学习项，再由LCP同步至VPP；可按二层接口、MAC地址或两者同时过滤，在三层接口上执行会明确报错。两条命令都保留静态配置，并由vortexrosd与commit串行执行。

`clear interface <接口> counter`为指定接口建立新的VortexROS可见计数基线。接口详情、300秒速率窗口和标准SNMP接口计数统一从零重新累计；可读取的CRC/FCS也按同一基线显示。该操作不清NIC/VPP原始计数，不改变接口配置、管理状态或转发表。基线保存在当前vortexrosd的进程内SQLite运行态中；VPP或vortexrosd重启时进入新的计数不连续代次，旧基线不再使用。


## 清除 Running 并恢复已保存配置

`reset running-configuration` 经确认后立即清除 Running 中的业务配置。启用 VPP 时，设备重启 VPP 并按清除后的 Running 重建转发状态，业务会中断。VPP 启用状态、VPP 启动文件设置和已保存的启动 CFG 均保留。

清除前用 `display startup` 确认所选 CFG。清除后用 `display configuration storage` 核对 Running 与 Actual；如需恢复，执行 `apply config` 并确认，然后用 `health check --wait --timeout 2m --require-saved` 验证运行状态与已保存配置一致。需要清除已保存配置时使用独立的 `restore factory-configuration` 流程。通过 AF_PACKET 等内核接口启动 VPP 时，保存供重启加载的 CFG 前，须配置至少一个由 VPP 启动文件创建的物理接口。


[目录](../09-operations.md)
