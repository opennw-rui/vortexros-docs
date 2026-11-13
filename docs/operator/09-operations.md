# 诊断与恢复

按现象定位问题见[常见故障](../troubleshooting/index.md)。

## Ping、tracert与mtr

```text
ping 192.0.2.1
ping -vpn-instance BLUE 10.0.0.1
tracert 198.51.100.1
mtr -vpn-instance BLUE 10.0.0.1
```

普通和带VPN的命令都会边执行边显示结果。Ctrl+C只中止当前诊断命令，并尽量显示已经产生的统计信息，不会关闭SSH会话。错误消息保留诊断含义，但不会暴露系统中的程序路径。

`mtr`在CLI中保持交互式刷新和按键控制，但用户不能借此进入Linux shell。

## Display

推荐从摘要逐级深入：

```text
display service verbose
display health verbose
display alarm active
display interface brief
display ip routing-table
display current-configuration
```

`display version`按照NOS运行身份、硬件平台和后端组件分区显示信息，包括产品版本、作者、源码提交、构建时间、Debian包版本、系统名、系统时间、操作系统、内核、CPU、内存、控制面状态、VPP、DPDK和FRR。产品版本行只显示版本号，构建阶段和提交号使用独立字段。登录CLI时在等宽边框内居中显示NOS标题、纯版本号、版权和作者，不查询运行状态；完整信息以`display version`为准。

### `display version`

**功能**：显示设备软硬件版本、运行平台及转发/路由组件身份。
**命令格式**：`display version`
**视图**：所有视图。
**缺省情况**：无。
**输出说明**：`VortexROS`段用于确认产品版本、源码提交和构建时间；`System`段显示主机、内核、平台、序列号、CPU和内存；`VPP`、`DPDK`及`FRRouting`段来自当前运行组件。字段无法读取时显示`-`或`unavailable`，不以猜测值替代。
**使用建议**：升级、故障上报和兼容性核对时应保存完整输出；不要只根据登录横幅判断所有后端已经收敛。

命令错误只显示一次错误位置和原因，不重复回显整条命令，也不会附加与用户无关的内部读取错误。

自动化安装、升级和发布验收必须使用严格健康检查，而不是把 systemd
`READY=1` 或 `display health` 的可读输出当作已经收敛：

```text
health check --wait --timeout 2m --json
```

该命令仅在 Running/Actual generation一致、reconcile为`in-sync`、没有活动告警且所有必需VPP API组可用时返回0。`--timeout`会自动启用等待；超时或未收敛返回非零。`--json`只输出一次最终快照，适合作为安装程序的稳定接口。

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

### 清除 Running 并恢复已保存配置

`reset running-configuration` 经确认后立即清除 Running 中的业务配置。启用 VPP 时，设备重启 VPP 并按清除后的 Running 重建转发状态，业务会中断。VPP 启用状态、VPP 启动文件设置和已保存的启动 CFG 均保留。

清除前用 `display startup` 确认所选 CFG。清除后用 `display configuration storage` 核对 Running 与 Actual；如需恢复，执行 `apply config` 并确认，然后用 `health check --wait --timeout 2m --require-saved` 验证运行状态与已保存配置一致。需要清除已保存配置时使用独立的 `restore factory-configuration` 流程。通过 AF_PACKET 等内核接口启动 VPP 时，保存供重启加载的 CFG 前，须配置至少一个由 VPP 启动文件创建的物理接口。

## VPP恢复

```text
display vpp api compatibility verbose
display vpp interface-ownership verbose
display vpp takeover transaction
reset service vpp
```

VPP接管阶段只检查核心API、startup中的全部预期物理接口及对应LCP。该门槛未通过时会恢复全部Linux接口；门槛通过后，FRR、策略或隧道等后续收敛失败只进入degraded并重试，不再回绑驱动。

## 动态路由服务恢复

动态路由服务异常时，先检查具体协议的邻居和路由，再重启最小范围的服务。重启协议服务不会修改已保存配置，服务恢复后设备会重新应用已经提交的协议配置。

```text
display service verbose
display ip routing-table
display ospf peer brief
display bgp peer
display bfd
```

## 告警与日志

告警显示严重度、功能模块、错误码、受影响对象、首次/最近发生时间、累计次数以及当前是否已恢复。相同故障会合并计数，避免重复信息淹没有效日志。

```text
display alarm active
display alarm history last 100
journalctl -u vortexrosd -u vortexros-vpp -u vortexros-frr -u vortexros-route-zapi
```

## 故障处理顺序

1. 保住管理连接和当前会话；
2. 记录 `display health/service/alarm`；
3. 判断是配置错误、接口/路由依赖缺失，还是相关服务未就绪；
4. 先等待当前自动恢复动作完成；
5. 再执行最小范围reset；
6. 修复待提交配置后重新commit并检查状态；
7. 业务验证通过后save。

不要直接删除 `/var/lib/vortexros`、`/run/vortexros` 或服务运行目录来“清错”，否则可能破坏自动恢复所需的信息。无法恢复时先保存display和日志信息，再按安装手册中的恢复流程处理。
